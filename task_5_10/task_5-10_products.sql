-- Файл: task_5-10_products.sql

-- 1. Выведите все товары из таблицы products
SELECT * FROM products;

-- 2. Выведите только название (name) и категорию (category) всех товаров
SELECT name, category FROM products;

-- 3. Выведите список всех уникальных категорий товаров
SELECT DISTINCT category FROM products;

-- 4. Выведите все товары, отсортированные по названию в алфавитном порядке
SELECT * FROM products ORDER BY name ASC;

-- 5. Выведите все товары, отсортированные по названию в обратном алфавитном порядке
SELECT * FROM products ORDER BY name DESC;

-- 6. Выведите первые 10 товаров из таблицы products
SELECT * FROM products LIMIT 10;

-- 7. Выведите 10 товаров из таблицы products, начиная с 11-й записи
SELECT * FROM products LIMIT 10 OFFSET 10;

-- 8. Выведите 5 случайных товаров (ORDER BY RANDOM() и LIMIT)
SELECT * FROM products ORDER BY RANDOM() LIMIT 5;

-- 9. Выведите все категории товаров (без DISTINCT), отсортированные по алфавиту (ASC)
SELECT category FROM products ORDER BY category ASC;

-- 10. Выведите все товары, отсортированные сначала по категории, затем по названию
SELECT * FROM products ORDER BY category, name;