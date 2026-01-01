#!/usr/bin/env python3
"""
Bootstrap script for extracting Fantrax authentication cookies.

This script opens a Chrome browser window, navigates to Fantrax login,
and captures the authentication cookies after login.
"""

import pickle
import time
import argparse
import os
import sys
from pathlib import Path
from typing import List, Optional

import logging
import os
import pickle
from pathlib import Path
from typing import Optional, Union, List, Dict
from requests import Session
from json.decoder import JSONDecodeError
from requests.exceptions import RequestException

# Add src directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

try:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError as e:
    print(f"❌ Missing required dependency: {e}")
    print("Please install selenium and webdriver-manager:")
    print("  pip install selenium webdriver-manager")
    sys.exit(1)

def bootstrap_cookies(
    output_path: Optional[str] = None,
    wait_time: int = 30,
    headless: bool = False
) -> str:
    """
    Bootstrap Fantrax authentication cookies.
        
    Returns:
        Path to the saved cookie file
        
    Raises:
        Exception: If cookie extraction fails
    """
    
    print("🚀 Starting Fantrax cookie bootstrap...")
    print("=" * 50)
    
    try:
        # Set up Chrome driver
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--window-size=1920,1600")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        # A user-agent is suggested in the wrapper docs
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
        )
        
        if headless:
            options.add_argument("--headless")
        
        print("🌐 Opening Chrome browser...")
        with webdriver.Chrome(service=service, options=options) as driver:
            driver.get("https://www.fantrax.com/login")
            print("✅ Browser opened and navigated to Fantrax login")
            print(f"⏳ Please log in to Fantrax. I'll capture cookies in {wait_time} seconds...")
            print("   (Make sure you're logged in before the time expires)")
            
            # Wait for user to log in
            time.sleep(wait_time)
            
            # Check if user is logged in by looking for specific cookies
            cookies = driver.get_cookies()
            
            # Save cookies
            output_file = Path(output_path)
            with open(output_file, "wb") as f:
                pickle.dump(cookies, f)
            
            print(f"✅ Saved {len(cookies)} cookies to {output_file.absolute()}")
            print("🎉 Cookie bootstrap complete!")
            
            return str(output_file.absolute())
            
    except Exception as e:
        print(f"❌ Error during cookie bootstrap: {e}")
        raise


def _request(session, league_id, method, **kwargs):
    data = {"leagueId": league_id}
    for key, value in kwargs.items():
        data[key] = value
    json_data = {"msgs": [{"method": method, "data": data}]}

    try:
        response = session.post("https://www.fantrax.com/fxpa/req", params={"leagueId": league_id}, json=json_data)
        response_json = response.json()
    except (RequestException, JSONDecodeError) as e:
        raise Exception(f"Failed to Connect to {method}: {e}\nData: {data}")
    if response.status_code >= 400:
        raise Exception(f"({response.status_code} [{response.reason}]) {response_json}")
    if "pageError" in response_json:
        if "code" in response_json["pageError"]:
            if response_json["pageError"]["code"] == "WARNING_NOT_LOGGED_IN":
                raise Exception("Unauthorized: Not Logged in")
        raise Exception(f"Error: {response_json}")
    return response_json["responses"][0]["data"]            


def main():
    """Main entry point for the bootstrap script."""
    
    parser = argparse.ArgumentParser(
        description="Bootstrap Fantrax authentication cookies",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  python -m utils.bootstrap_cookie --league-id <LEAGUE_ID> --team-id <TEAM_ID>
  python -m utils.bootstrap_cookie --wait 15 --league-id <LEAGUE_ID> --team-id <TEAM_ID>
  python -m utils.bootstrap_cookie -o deploy/fantraxloggedin.cookie --league-id <LEAGUE_ID> --team-id <TEAM_ID>
        """
    )
    
    parser.add_argument(
        "--output", "-o",
        help="Output file path for cookies (default: deploy/fantraxloggedin.cookie)",
        default="deploy/fantraxloggedin.cookie"
    )
    
    parser.add_argument(
        "--wait", "-w",
        type=int,
        default=30,
        help="Time to wait for login in seconds (default: 30)"
    )
    
    parser.add_argument(
        "--league-id",
        type=str,
        required=True,
        default=os.getenv('LEAGUE_ID'),
        help="Fantrax League ID"
    )
    
    parser.add_argument(
        "--team-id",
        type=str,
        required=True,
        default=os.getenv('TEAM_ID'),
        help="Fantrax Team ID"
    )
    
    args = parser.parse_args()
    
    try:
        cookie_file = bootstrap_cookies(
            output_path=args.output,
            wait_time=args.wait
        )
        
        if cookie_file:
            # Test the cookie file by initializing FantraxClient and checking roster
            print(f"\n🔍 Testing cookie file...")
            _session = Session()
            if not os.path.exists(cookie_file):
                raise FileNotFoundError(f"Cookie file not found: {cookie_file}")
            else:
                cookie_file = Path(cookie_file)
                
                if not cookie_file.exists():
                    raise FileNotFoundError(f"Cookie file not found: {cookie_file}")
                
                with open(cookie_file, "rb") as f:
                    cookies = pickle.load(f)
                    for cookie in cookies:
                        _session.cookies.set(cookie["name"], cookie["value"])
            data = _request(_session, args.league_id, "getTeamRosterInfo", teamId=args.team_id)
            player_rows_data= []
            try:
                for table in data.get("tables", []):
                    for row_item in table.get("rows", []):
                        if "scorer" in row_item:
                            player_rows_data.append(row_item)
                print(f"✅ Cookie file verified successfully!")
                print(f"   Team ID: ({args.team_id})")
                print(f"   FantraxPlayers found: {len(player_rows_data)}")
                print(f"   Cookie file save to path:: {cookie_file}")
            except Exception as e:
                print(f"❌ Unexpected error testing cookie: {e}")
                print(f"   Cookie file saved, but verification failed")            
    except KeyboardInterrupt:
        print("\n❌ Bootstrap cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Bootstrap failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

