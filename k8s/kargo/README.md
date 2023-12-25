# Notes

Requires creation of Secret to read/write to GitOps repo:
```
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: kargo-homelab-repo
  namespace: kargo-homelab
  labels:
    kargo.akuity.io/secret-type: repository
stringData:
  type: git
  project: default
  url: ${GITOPS_REPO_URL}
  username: ${GITHUB_USERNAME}
  password: ${GITHUB_PAT}
EOF
```
