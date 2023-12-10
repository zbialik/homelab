# Updating Metallb manifests

```
helm repo add metallb https://metallb.github.io/metallb
helm repo update
helm template metallb metallb/metallb -f helm/values.yaml -n metallb-system > generated.yaml
```

You'll also need to grab the CRD's separately, which I got from [here](https://doc.traefik.io/traefik/reference/dynamic-configuration/kubernetes-crd/)

## Notes on Setup

I use a pretty basic Archer C7 router at home. In order to use MetalLB, I had to update the router's configuration to do the following:
- allow for a wider IP range for my LAN (e.g. `192.168.0.1/16`)
- update the DHCP IP range to be a slice of that LAN IP range (e.g. `192.168.0.100-192.168.0.254`)

Then, I can let MetalLB handle IPs in the ranges the DHCP aren't handled by my router (e.g. `192.168.1.100-192.168.1.249`)
- see this [config](./confs.yaml)

## Update `helm/values.yaml` with changes from chart upgrade

```bash
# get curr commit sha of helm/default.yaml
CURR_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# update helm/default.yaml with changes from next chart version and commit
helm show values metallb/metallb > helm/default.yaml
git add .
git commit -m "updating metallb helm/default.yaml"

# get new commit sha of helm/default.yaml
NEW_SHA=`git --no-pager log -n 1 --pretty=format:%H -- helm/default.yaml`

# get diff between helm/default.yaml versions + patch helm/values.yaml
git diff --relative $CURR_SHA $NEW_SHA helm/default.yaml > /tmp/values.diff
patch helm/values.yaml /tmp/values.diff && rm -rf helm/values.yaml.*

# solve all the conflicts
```
