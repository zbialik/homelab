# kargo

## Updating git credentials sealed secret

```
# generate plaintext secret
cat <<EOF > /tmp/secret.yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: kargo-gitops-repo-creds
  namespace: kargo
  labels:
    kargo.akuity.io/secret-type: repository
stringData:
  type: git
  project: default
  url: https://github.com/zbialik/homelab.git
  username: zbialik
  password: ${GITHUB_PAT}
EOF

# seal the secret
kubeseal -f /tmp/secret.yaml -w sealed-secret.yaml
```
