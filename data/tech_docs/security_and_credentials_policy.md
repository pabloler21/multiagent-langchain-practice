# Politicas de Ciberseguridad, Gestion de Secretos y Llaves SSH

## 1. Politica de Contrasenas y Bovedas de 1Password
- Longitud minima de 16 caracteres compuesta por combinacion de palabras aleatorias, digitos y caracteres especiales.
- Prohibida la reutilizacion de contrasenas corporativas en servicios personales o de terceros.
- Acceso a bovedas compartidas de infraestructura de produccion asignado bajo estricto principio de menor privilegio (Least Privilege).

---

## 2. Llaves Criptograficas SSH y Firma de Commits
- Algoritmo unico admitido para nuevas llaves SSH: Ed25519 (ssh-keygen -t ed25519).
- Las llaves privadas deben estar cifradas con passphrase y registradas en el agente SSH del sistema operativo.
- Es obligatorio firmar todos los commits de Git enviados a GitHub Enterprise mediante GPG o SSH Signing Keys con verificacion habilitada.

---

## 3. Reporte de Phishing e Incidentes de Seguridad
- Ante cualquier correo sospechoso, hacer clic en el boton corporativo Report Phishing en Gmail.
- Ante llamadas o mensajes en Slack solicitando transferencias o claves haciendose pasar por ejecutivos (CEO Fraud), reportar en #security-incidents.
- Dispositivo extraviado o robado: Notificar antes de 2 horas a security-ops@company.internal para ejecutar el bloqueo y borrado remoto preventivo (Remote Wipe).
## 3. Politica de Uso Aceptable de Dispositivos y Criptografia
- Cifrado en reposo (BitLocker / FileVault / LUKS) obligatorio con recovery key custodiada en Jamf Pro / Microsoft Intune.
- Bloqueo automatico de pantalla configurado a los 5 minutos de inactividad con solicitud de contrasena o TouchID.
- Desactivacion estricta de puertos USB para almacenamiento masivo externo no encriptado por politicas DLP (Data Loss Prevention).
- Todo software no homologado instalado en equipos de ingenieria disparara una alerta de auditoria en el dashboard de CrowdStrike Falcon.
- Auditorias semestrales de puertos abiertos y servicios locales (Docker daemon, bases de datos locales no protegidas).
- Guia de configuracion de terminal zsh/bash segura con plugins corporativos auditados.
