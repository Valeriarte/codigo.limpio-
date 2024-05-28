-- Crear tabla de hipotecas
CREATE TABLE hipotecas (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER NOT NULL,
    monto_total FLOAT NOT NULL,
    fecha_inicio DATE NOT NULL,
    cuota_mensual INTEGER NOT NULL,
    UNIQUE (usuario_id, monto_total, fecha_inicio),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
