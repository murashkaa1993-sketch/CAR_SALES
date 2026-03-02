

-- Створення БД
CREATE DATABASE CarSalesAccounting;

-- Підключення до БД
\c CarSalesAccounting;

-- Таблиця працівників
CREATE TABLE employee (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    position VARCHAR(50),
    phone VARCHAR(20),
    email VARCHAR(50)
);

-- Таблиця авто
CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    manufacturer VARCHAR(50),
    model VARCHAR(50),
    year INT,
    cost_price NUMERIC,
    selling_price NUMERIC,
    status VARCHAR(20) DEFAULT 'available'
);

-- Таблиця продажів
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES employee(id),
    car_id INT REFERENCES cars(id),
    sale_date DATE,
    sold_price NUMERIC
);