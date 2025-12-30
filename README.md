# Personal Kubernetes Homelab

IaC repository for managing my home kubespray cluster made up of Raspberry Pi's

## Infrastructure + Cluster Maintenance

See [this doc](docs/INFRA_MAINTENANCE.md).

## Ingress/DNS

### DuckDNS

I DuckDNS as a free service to host my DNS records under the following subdomain: zeb17.duckdns.org

I must update the subdomain IP every 30 days, and can automate that with curl commands.

#### Internal DNS

1. DuckDNS hosts subdomain `zeb17-int.duckdns.org` which targets ingress-controller's internal IP (`192.168.1.100`).

Update record like so:

```
curl -g "https://www.duckdns.org/update/zeb17-int/${DUCKDNS_TOKEN}/192.168.1.100"
```

#### External DNS

I've since disabled external access, but if I were to set this up again, I'd start with something like:

1. DuckDNS hosts subdomain `zeb17-ext.duckdns.org` which targets ingress-controller's internal IP (`192.168.1.200`).
1. Setup Port Forwarding (in NAT forwarding section in my Archer C7 router) to route `443` --> `443` on ingress-controller's internal IP (`192.168.1.200`).

Update record like so:

```
curl -g "https://www.duckdns.org/update/zeb17-ext/${DUCKDNS_TOKEN}/"
```

NOTE: I would want to do some network segmentation here ideally. Maybe using a separate set of ingress controllers for the externally reachable records and hosting these on isolated hosts.
