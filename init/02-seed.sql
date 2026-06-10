BEGIN;
SET CONSTRAINTS ALL DEFERRED;

INSERT INTO orden_rubro (id,nombre)
VALUES
  (1,'Albañilería'),
  (2,'Pintura'),
  (3,'Plomería'),
  (4,'Electricidad'),
  (5,'Refrigeración'),
  (6,'Impermeabilización'),
  (7,'Campanas'),
  (8,'Mantenimiento General');

INSERT INTO orden_estado (nombre)
VALUES
  ('Pendiente'),
  ('Asignado'),
  ('En Curso'),
  ('Finalizado'),
  ('Observado');

INSERT INTO orden_prioridad (nombre)
VALUES
  ('Normal'),
  ('Alta'),
  ('Urgente');

INSERT INTO fotos_proceso (nombre)
VALUES
  ('Antes'),
  ('Durante'),
  ('Después');

INSERT INTO tipo_cliente (nombre)
VALUES
  ('Particular'),
  ('Consorcio'),
  ('Comercio'),
  ('Empresa'),
  ('Local'),
  ('Gastronómico'),
  ('Oficina'),
  ('Otro');

INSERT INTO checklist_estado (nombre)
VALUES
  ('Pendiente'),
  ('Asignado'),
  ('En Curso'),
  ('Finalizado'),
  ('Observado');

INSERT INTO checklist_prioridad (nombre)
VALUES
  ('Normal'),
  ('Alta'),
  ('Urgente');

INSERT INTO usuario_rol (nombre)
VALUES
  ('Admin'),
  ('Tecnico'),
  ('Cliente');

INSERT INTO checklist_plantilla (id, rubro_id, nombre)
VALUES
  (1,8,'Mantenimiento general plantilla'),
  (2,5,'Aire acondicionado plantilla'),
  (3,6,'Impermeabilización plantilla'),
  (4,7,'Revisar campanas plantilla');

INSERT INTO checklist_plantilla_item (plantilla_id, orden_visual, nombre)
VALUES
  (1,0,'Revisar sector indicado'),
  (1,1,'Registrar fotos iniciales'),
  (1,2,'Verificar estado general'),
  (1,3,'Realizar tareas acordadas'),
  (1,4,'Informar daños o adicionales'),
  (1,5,'Limpiar sector intervenido'),
  (1,6,'Cargar observaciones finales'),
  (1,7,'Registrar fotos finales'),
  (2,0,'Verificar encendido'),
  (2,1,'Revisar filtros'),
  (2,2,'Revisar desagüe'),
  (2,3,'Revisar unidad interior'),
  (2,4,'Revisar unidad exterior'),
  (2,5,'Controlar funcionamiento general'),
  (2,6,'Cargar recomendación'),
  (3,0,'Revisar grietas'),
  (3,1,'Revisar encuentros con paredes'),
  (3,2,'Revisar embudos/desagües'),
  (3,3,'Registrar humedad o filtración'),
  (3,4,'Cargar fotos'),
  (3,5,'Indicar producto utilizado'),
  (3,6,'Cargar recomendación final'),
  (4,0,'Revisar campana'),
  (4,1,'Revisar filtros'),
  (4,2,'Revisar ductos visibles'),
  (4,3,'Revisar extractor'),
  (4,4,'Registrar estado de grasa'),
  (4,5,'Cargar fotos'),
  (4,6,'Indicar si requiere limpieza profunda');

SET CONSTRAINTS ALL IMMEDIATE;
COMMIT;