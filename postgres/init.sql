
DROP TABLE IF EXISTS estudiante CASCADE;
DROP TABLE IF EXISTS carrera CASCADE;
DROP TABLE IF EXISTS facultad CASCADE;

-- TABLA: facultad
CREATE TABLE IF NOT EXISTS facultad (
  id      SERIAL PRIMARY KEY,
  nombre  VARCHAR(255) NOT NULL
);

-- TABLA: carrera (pertenece a facultad)
CREATE TABLE IF NOT EXISTS carrera (
  id           SERIAL PRIMARY KEY,
  nombre       VARCHAR(255) NOT NULL,
  facultad_id  INTEGER NOT NULL,
  CONSTRAINT fk_carrera_facultad
    FOREIGN KEY (facultad_id)
    REFERENCES facultad (id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS ix_carrera_facultad_id ON carrera(facultad_id);

-- TABLA: estudiante (pertenece a carrera)
CREATE TABLE IF NOT EXISTS estudiante (
  id          SERIAL PRIMARY KEY,
  nombre      VARCHAR(255) NOT NULL,
  email       VARCHAR(255),
  carrera_id  INTEGER NOT NULL,
  CONSTRAINT fk_estudiante_carrera
    FOREIGN KEY (carrera_id)
    REFERENCES carrera (id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS ix_estudiante_carrera_id ON estudiante(carrera_id);

-- ======== Seed mínimo (opcional, puedes editarlo) ========
INSERT INTO facultad (nombre) VALUES ('Facultad de Ingeniería'), ('Facultad de Ciencias Económicas');

INSERT INTO carrera (nombre, facultad_id) VALUES
  ('Ingeniería de Sistemas', (SELECT id FROM facultad WHERE nombre='Facultad de Ingeniería')),
  ('Ingeniería Civil',       (SELECT id FROM facultad WHERE nombre='Facultad de Ingeniería')),
  ('Administración',         (SELECT id FROM facultad WHERE nombre='Facultad de Ciencias Económicas'));

INSERT INTO estudiante (nombre, email, carrera_id) VALUES
  ('Juan Pérez',  'juan.perez@example.com',  (SELECT id FROM carrera WHERE nombre='Ingeniería de Sistemas')),
  ('María López', 'maria.lopez@example.com', (SELECT id FROM carrera WHERE nombre='Administración'));
