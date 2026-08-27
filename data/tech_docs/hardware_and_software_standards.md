# Estandares de Hardware, Software y Entornos de Desarrollo

## 1. Asignacion y Especificaciones de Hardware
- Perfil Engineering / Data Science:
  - Apple MacBook Pro 14 o 16 pulgadas con chip M3 Pro/Max, 36GB RAM, 1TB SSD.
  - Dell XPS 15 (Core i9, 64GB RAM, 1TB SSD, Ubuntu Linux certificado).
- Perfil General (Sales, HR, Finance, Operations):
  - Apple MacBook Air 15 pulgadas (Chip M3, 16GB RAM, 512GB SSD) o Dell Latitude 7440.

### 1.1 Ciclo de Renovacion de Equipos (Hardware Refresh)
- Renovacion programada cada 3 anos calendario.
- Opcion de compra del equipo anterior por el 10% del valor residual al completarse el periodo de 36 meses.
- Equipamiento adicional: 1 monitor Dell UltraSharp 27 4K, teclado ergonomico Logitech MX Keys y raton MX Master 3S provistos sin costo.

---

## 2. Catalogo de Software Homologado y Licencias
- Gestion de Contrasenas: 1Password Business (Obligatorio).
- Suites de Desarrollo: JetBrains All Products (IntelliJ, PyCharm, WebStorm), Docker Desktop Enterprise, Postman Pro, Cursor Enterprise.
- Seguridad en Endpoint: CrowdStrike Falcon EDR preinstalado y monitoreado 24/7. Prohibida su desactivacion.
- Solicitud de nuevo software de pago: Abrir ticket en Jira Service Desk (Cola IT-Software-Approval) con justificacion tecnica y aprobacion del Engineering Lead.

---

## 3. Seguridad en el Entorno Local de Desarrollo
- Cifrado total de disco obligatorio: FileVault en macOS y BitLocker en Windows.
- Prohibido clonar repositorios corporativos en computadoras o servidores personales.
- Secretos y variables de entorno: Nunca commitear archivos .env con contraseñas o tokens. Utilizar siempre 1Password CLI (op run) o AWS Secrets Manager.