BEGIN;
SET CONSTRAINTS ALL DEFERRED;

INSERT INTO orden_rubro (nombre)
VALUES
  ('Albañilería'),
  ('Pintura'),
  ('Plomería'),
  ('Electricidad'),
  ('Refrigeración'),
  ('Impermeabilización'),
  ('Campanas'),
  ('Mantenimiento General');

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

SET CONSTRAINTS ALL IMMEDIATE;
COMMIT;