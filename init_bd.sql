

-- Створення БД
CREATE DATABASE CarSalesAccounting;

-- Підключення до БД
\c CarSalesAccounting;

-- Таблиця працівників
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    position VARCHAR,
    phone VARCHAR,
    email VARCHAR
);

-- Таблиця авто
CREATE TABLE car (
    id SERIAL PRIMARY KEY,
    manufacturer VARCHAR,
    model VARCHAR,
    year INTEGER,
    cost_price NUMERIC,
    selling_price NUMERIC,
    status VARCHAR DEFAULT 'available'
);

-- Таблиця продажів
CREATE TABLE sale (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employee(id),
    car_id INTEGER REFERENCES car(id),
    sale_date DATE,
    sold_price NUMERIC
);