# Updating Metallb manifests

## Notes on Setup

I use a pretty basic Archer C7 router at home. In order to use MetalLB, I had to update the router's configuration to do the following:
- allow for a wider IP range for my LAN (e.g. `192.168.0.1/16`)
- update the DHCP IP range to be a slice of that LAN IP range (e.g. `192.168.0.100-192.168.0.254`)

Then, I can let MetalLB handle IPs in the ranges the DHCP aren't handled by my router (e.g. `192.168.1.100-192.168.1.249`)
- see this [config](./confs.yaml)

## Install

```
helm repo add metallb https://metallb.github.io/metallb
helm repo update
```

## Upgrades

```bash
# identify chart version
helm search repo metallb/metallb -l

# update version
METALLB_VERSION=0.15.3
helm show values metallb/metallb --version $METALLB_VERSION > helm/default.yaml
helm template metallb metallb/metallb -f helm/values.yaml -n metallb-system --version $METALLB_VERSION > generated.yaml
```