## Getting Cookie

```bash
LEAGUE_ID=o90qdw15mc719reh
TEAM_ID=jassfpe6mc719rep

python bootstrap_cookie.py --league-id ${LEAGUE_ID} --team-id ${TEAM_ID} --wait 10 -o /tmp/fantraxloggedin.cookie

kubectl create secret generic fantrax-cookie \
  --from-file=/tmp/fantraxloggedin.cookie \
  --namespace=fantrax-pl-team-manager \
  --dry-run=client -o yaml > /tmp/secret.yaml

kubeseal -f /tmp/secret.yaml -w sealed-fantrax-cookie.yaml
```
s