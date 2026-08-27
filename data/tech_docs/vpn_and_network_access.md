# Guia de Acceso a Red, VPN Corporativa y Credenciales

## 1. Arquitectura de Acceso Seguro y VPN
Para acceder a entornos de staging, bases de datos de desarrollo y dashboards internos, es obligatorio utilizar la red privada virtual corporativa.

### 1.1 Configuracion de VPN (GlobalProtect y WireGuard)
- Servidor Principal (US-East): vpn.company.internal (Puerto 443 TCP/UDP).
- Servidor Secundario (EU-Central): vpn-eu.company.internal.
- Protocolo recomendado para ingenieria: WireGuard con certificados cliente renovables cada 90 dias.
- Portal de autogestion: Acceder a https://vpn-portal.company.internal con credenciales SSO corporativas.

### 1.2 Configuracion por Sistema Operativo
- macOS: Descargar GlobalProtect desde Jamf Self Service. Ingresar vpn.company.internal y autenticar mediante Okta Verify.
- Windows 11: Abrir la aplicacion GlobalProtect preinstalada, ingresar cuenta @company.internal y confirmar notificacion push MFA.
- Linux (Ubuntu/Debian):
  Instalar openconnect o wireguard:
  sudo apt-get install openconnect
  sudo openconnect --protocol=gp vpn.company.internal
  Importar certificados ubicados en /etc/ssl/company-certs/ca.crt.

---

## 2. Autenticacion Multifactor (MFA / 2FA)
- Obligatoria para el 100% de los servicios corporativos (Google Workspace, GitHub, Slack, AWS Console).
- Metodos aceptados: Llaves fisicas FIDO2 (YubiKey 5 Series) o Notificaciones Push con verificacion de numero en Okta Verify / 1Password.
- Prohibido el uso de SMS o llamadas no cifradas como segundo factor por riesgo de SIM swapping.

### 2.1 Perdida de Dispositivo o Reseteo de MFA
- Notificar inmediatamente en el canal de Slack #it-urgent o abrir ticket en el portal de Helpdesk.
- Se requiere llamada de validacion de identidad con Helpdesk antes del reseteo de claves de recuperacion.