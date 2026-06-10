# Arquitectura

## Diagrama General

```mermaid
flowchart LR

A[Administrador]
T[Técnico]

A --> F
T --> F

F[React Frontend]

F --> API[FastAPI Backend]

API --> DB[(PostgreSQL)]
API --> FS[Almacenamiento de Fotos]
```

## 🏗️ Ficha Técnica

### Herramientas

<table align="center">
  <tr>
    <td align="center">
      <img src="./assets/icons/fastapi_logo.webp" height="35px" width="35px" alt="FastApi"/>
      <br/>FastApi
      <br/>(Backend)
    </td>
    <td align="center">
      <img src="./assets/icons/React_logo.webp" height="35px" width="40px" alt="React"/>
      <br/>React
      <br/>(Frontend)
    </td>
    <td align="center">
      <img src="./assets/icons/postgresql_logo.png" height="40px" width="40px" alt="PostgreSQL"/>
      <br/>PostgreSQL
      <br/>(Database)
    </td>
  </tr>
</table>

### Lenguajes

<table align="center">
  <tr>
    <td align="center">
      <img src="./assets/icons/Typescript_logo.webp" height="40px" width="40px" alt="Typescript"/>
      <br/>Typescript
      <br/>(Interfaz)
    </td>
    <td align="center">
      <img src="./assets/icons/Python_logo.webp" height="40px" width="40px" alt="Python"/>
      <br/>Python
      <br/>(Servidor)
    </td>
  </tr>
</table>

### Librerías

#### Backend (Python)

##### Base
- FastAPI
	- Backend
- Uvicorn
	- Servidor Web
- Psycopg
	- Adaptador PostgreSQL
- Sqlalchemy
	- Para interactuar con el SQL
- Pydantic
	- Validación de información entre front y back
- Python-dotnenv
	- Leer .env

##### Autenticación
- Passlib
	- Hashing de contraseña
- Python-JOSE
	- Para manejar tokens de autenticación

##### Imágenes
- Pillow
	- Manipulación de imagenes
- Python-multipart
	- Recibir archivos desde React

##### Facturas y PDFs
- Jinja2
	- Plantillas para HTML
- Weasyprint
	- Convertir HTML a PDF

## 🗃️ Base de Datos

### Diagrama
![Diagrama de Base de Datos en PostgreSQL](./assets/diagrams/SIJR-db.svg)

