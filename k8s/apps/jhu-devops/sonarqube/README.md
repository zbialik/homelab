# Helm Generation

```bash
helm repo add sonarqube https://SonarSource.github.io/helm-chart-sonarqube
helm repo update
helm template -n sonarqube sonarqube sonarqube/sonarqube -f helm/values.yaml > generated.yaml
```
