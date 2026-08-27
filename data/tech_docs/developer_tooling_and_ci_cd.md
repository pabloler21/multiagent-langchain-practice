# Herramientas de Desarrollo, CI/CD y Repositorios GitHub

## 1. Flujo de Trabajo en GitHub Enterprise
- Todas las contribuciones deben realizarse mediante Pull Request (PR).
- Requisitos minimos para mergear a rama principal (main):
  - Al menos 1 aprobacion (Code Review) de un miembro del equipo.
  - Pipeline de CI en verde (Tests unitarios, linter y analisis de vulnerabilidades con Snyk).
  - Commits firmados criptograficamente.

## 2. Despliegue Continuo (CD) y Ambientes
- Staging: Despliegue automatico tras merge a main.
- Produccion: Despliegue mediante GitHub Actions con aprobacion manual del Tech Lead o release manager.