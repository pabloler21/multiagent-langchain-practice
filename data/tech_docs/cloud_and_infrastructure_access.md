# Acceso a Infraestructura Cloud, AWS, GCP y Kubernetes

## 1. Politica de Acceso a Entornos Productivos
- El acceso a consolas de AWS y GCP de produccion se rige por el principio de Zero Trust.
- No existen credenciales permanentes (Long-Lived Access Keys) para usuarios individuales.
- El acceso se realiza mediante AWS IAM Identity Center (SSO) con sesion temporal maxima de 4 horas y aprobacion Just-In-Time (JIT) via Slack bot #access-requests.

## 2. Clusters de Kubernetes (EKS / GKE)
- Acceso a clusters mediante comando 	eleport o ws eks update-kubeconfig.
- Prohibido ejecutar comandos kubectl delete o kubectl exec directos en produccion sin ticket de cambio aprobado (RFC).