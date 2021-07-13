DROP TABLE IF EXISTS vehicles;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
   id SERIAL PRIMARY KEY,
   name VARCHAR(255)
);

CREATE TABLE vehicles (
   id SERIAL PRIMARY KEY,
   description VARCHAR(255),
   engine FLOAT,
   gearbox VARCHAR(255),
   colour VARCHAR(255),
   price FLOAT,
   year INT,
   quantity INT,
   for_sale BOOLEAN,
   make VARCHAR(255),
   model VARCHAR(255),
   image TEXT,
   manufacturer_id INT REFERENCES manufacturers(id)
);


