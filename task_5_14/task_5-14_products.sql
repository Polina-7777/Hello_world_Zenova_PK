-- Выведите список товаров из таблицы products, переименовав столбцы:
-- name → «Название товара»
-- category → «Категория»
SELECT 
    name AS "Название товара", 
    category AS "Категория"
FROM products;