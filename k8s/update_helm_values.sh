#!/usr/bin/env bash

HELM_CHART=$1
TARGET_CHART_VERSION=$2
CURRENT_CHART_VERSION=$(cat helm/CHART_VERSION)

# INPUT VALIDATION
# Validation 1: semantic versioning (and effectively that they're not empty)
SEMVER_REGEX="^[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?(\+[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?$"
if [[ $TARGET_CHART_VERSION =~ $SEMVER_REGEX ]] && [[ $CURRENT_CHART_VERSION =~ $SEMVER_REGEX ]]; then
    echo "$TARGET_CHART_VERSION and $CURRENT_CHART_VERSION are valid semantic versions."
else
    echo "one of the provided chart versions is NOT in valid semantic version (or empty):"
    echo "  TARGET_CHART_VERSION: \"$TARGET_CHART_VERSION\""
    echo "  CURRENT_CHART_VERSION: \"$CURRENT_CHART_VERSION\""
    exit 1
fi

# Validation 2: target chart version exists
EXISTS=`helm search repo $HELM_CHART --version $TARGET_CHART_VERSION -o json | jq 'length'`
if [[ $EXISTS -eq 1 ]]; then 
    echo "chart version exists"
elif [[ $EXISTS -eq 0 ]]; then 
    echo "chart version, $TARGET_CHART_VERSION, does NOT exist"
    exit 1
else
    echo "$TARGET_CHART_VERSION appears in the version of multiple charts"
    exit 1
fi

# get curr commit sha of helm/default.yaml
CURR_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`
echo "CURR_SHA: "$CURR_SHA

# update helm/default.yaml with changes from next chart version and commit
cp -rp helm/default.yaml helm/default.yaml.bak
helm show values $HELM_CHART --version ${TARGET_CHART_VERSION} > helm/default.yaml
if [[ diff helm/default.yaml helm/default.yaml.bak == "" ]]; then
    echo "no diff in default values.yaml in upgraded chart version"
    echo "setting CHART_VERSION to target version"
    echo $TARGET_CHART_VERSION > helm/CHART_VERSION
    exit 0
fi

git add helm/default.yaml
git commit -m "updating $HELM_CHART helm/default.yaml"
RET=$?
if [[ $RET -ne 0 ]]; then
    echo "git commit failed"
    exit 1
fi

# get new commit sha of helm/default.yaml
NEW_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`
echo "NEW_SHA: "$CURR_SHA

# get diff between helm/default.yaml versions + patch helm/values.yaml
git diff --relative $CURR_SHA $NEW_SHA helm/default.yaml > /tmp/values.diff
patch helm/values.yaml /tmp/values.diff
echo $TARGET_CHART_VERSION > helm/CHART_VERSION

# cleanup
rm -rf helm/default.yaml.bak helm/values.yaml.* 
