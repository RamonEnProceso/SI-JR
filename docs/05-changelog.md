# Changelog

## v0.0.4 - 2026-06-15
- Creación de estructuras Pydantic para el envío y recibo de datos
    - Cliente
    - Orden
    - Usuario
- Creación de CRUDs usando SQLAlchemy
    - Cliente
        - CreateCliente
        - GetCliente
        - GetClientes
        - UpdateCliente
        - DeleteCliente


## v0.0.3 — 2026-06-12
- Terminar Modelado (de la base de datos) en SQLAlchemy
    - Creación de modelos:
		- OrdenObservacion
		- OrdenFoto
            - FotoProceso
		- OrdenChecklist
			- ChecklistPlantilla
			- ChecklistPlantillaItem
			- ChecklistItem
			- ChecklistEstado
			- ChecklistPrioridad
- Cargar modelos en `/models/__init__` para evitar redundancias
- Actualizar CRUD para cargar desde `/models/__init__`
- Actualizar diagrama SQL
				

## v0.0.2 — 2026-06-11
- Inicio de Modelado (de la base de datos) en SQLAlchemy
    - Creación de Base, Engine, Session y GetDB
    - Creación de modelos:
        - Usuario
            - UsuarioRol
        - Cliente
            - TipoCliente
        - Orden
            - OrdenEstado
            - OrdenPrioridad
            - OrdenRubro
            - OrdenTecnico
- Creación del router ```/roles```
    - Lee los roles en el Docker PostgreSQL
- Creación de una nueva tabla SQL "Orden_Tecnico"
    - Permite asignar varios técnicos a una orden

## v0.0.1 — 2026-06-10
- Inicio de documentación
- Inicio del servidor en FastAPI
- Creación de Base de Datos en PostgreSQL
    - Creación de tablas
    - Asignación de "Estados" y "Prioridades"
    - Creación de plantillas base para ordenes
    - Asignación de "Tipos de usuarios"