# Gestion de Incidentes de IT, Niveles de Servicio (SLA) y Helpdesk

## 1. Canales Oficiales de Soporte Tecnico
- Portal de Tickets: https://helpdesk.company.internal
- Canal de Slack general: #it-helpdesk (Atencion con bot inteligente y agentes de soporte).
- Canal de Slack para emergencias: #it-urgent (Para bloqueos totales o incidentes de produccion).
- Correo: servicedesk@company.internal

---

## 2. Niveles de Severidad y Tiempos de Respuesta (SLA)
- P1 (Blocker / Emergencia): Caida total de red, falla masiva de SSO o sospecha de brecha de seguridad.
  - Primera respuesta: Menor a 15 minutos. Resolucion objetivo: Menor a 2 horas.
- P2 (Alta / Critica): Bloqueo total de acceso para un usuario individual sin workaround.
  - Primera respuesta: Menor a 1 hora. Resolucion objetivo: Menor a 6 horas.
- P3 (Media / Estandar): Solicitudes de licencias de software, configuraciones de VPN o dudas tecnicas.
  - Primera respuesta: Menor a 4 horas habiles. Resolucion: Menor a 24 horas habiles.
- P4 (Baja / Planificada): Consultas de hardware futuro o cambios cosmeticos.
  - Primera respuesta: Menor a 8 horas habiles. Resolucion: Menor a 48 horas habiles.

---

## 3. Esquema de Guardia (On-Call) y Postmortems
- Rotaciones semanales de On-Call gestionadas a traves de PagerDuty con compensacion adicional por disponibilidad.
- Analisis de Causa Raiz (RCA) obligatorio para incidentes P1 y P2 dentro de las 72 horas habiles posteriores a la resolucion.