DROP TABLE IF EXISTS vehicles;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
   id SERIAL PRIMARY KEY,
   make VARCHAR(255),
   model VARCHAR(255)
);

CREATE TABLE vehicles (
   id SERIAL PRIMARY KEY,
   description VARCHAR(255),
   engine FLOAT,
   gearbox VARCHAR(255),
   colour VARCHAR(255),
   year INT,
   quantity INT,
   vehicle_id INT REFERENCES vehicles(id)
);


