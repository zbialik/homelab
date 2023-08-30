# Generating initial root CA Secret for cert-manager


Generate root CA public/private key pair in `tmp` directory:
```
mkdir tmp
cd tmp
openssl genrsa -out rootCAKey.pem 2048
openssl req -x509 -sha256 -new -nodes -key rootCAKey.pem -days 3650 -out rootCACert.pem
```

Then, use kustomize to generate `Secret` from those files. Add `kustomization.yaml` in the `tmp` directory with contents:
```
kind: Kustomization
namespace: cert-manager-zbialik

secretGenerator:
- name: zbialik-root-cert
  files:
  - tls.crt=rootCACert.pem
  - tls.key=rootCAKey.pem
  literals:
  - privateKey.algorithm=RSA
  type: "kubernetes.io/tls"
  options:
    disableNameSuffixHash: true
```

Finally, deploy the initial root CA Secret:
```
kubectl apply -k ./tmp
```