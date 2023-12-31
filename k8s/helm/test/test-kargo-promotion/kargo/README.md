## Updating git credentials sealed secret

NOTE: As of right now, I've created this sealed-secret in each respective kargo project namespace manually. This is because the global sharing of repository creds doesn't appear to be working ([see here](https://github.com/akuity/kargo/pull/1041)).

```
# generate plaintext secret
cat <<EOF > /tmp/secret.yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: kargo-gitops-repo-creds
  namespace: kargo-test-kargo-promotion
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
