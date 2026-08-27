# Politica de Respaldo de Datos, Backups y Recuperacion ante Desastres

## 1. Frecuencia y Retencion de Backups
- Bases de datos PostgreSQL y MySQL: Snapshots diarios automatizados con retencion de 30 dias y Point-in-Time Recovery (PITR) de 7 dias.
- Respaldos inmutables en almacenamiento secundario S3 con bloqueo de objetos (Object Lock).
- Simulacros de Disaster Recovery (DR) realizados semestralmente con RPO objetivo < 1 hora y RTO < 4 horas.