-- 1. Выведите количество (COUNT) записей в таблице prices 
-- для каждого товара (product_id).
SELECT product_id, COUNT(*) AS count_records
FROM prices
GROUP BY product_id;

-- 2. Выведите среднюю цену товаров (AVG(price)) 
-- для каждого product_id из таблицы prices.
SELECT product_id, AVG(price) AS average_price
FROM prices
GROUP BY product_id;

-- 3. Выведите минимальную (MIN) цену 
-- для каждого товара (product_id) из таблицы prices.
SELECT product_id, MIN(price) AS min_price
FROM prices
GROUP BY product_id;

-- 4. Выведите максимальную (MAX) цену 
-- для каждого товара (product_id) из таблицы prices.
SELECT product_id, MAX(price) AS max_price
FROM prices
GROUP BY product_id;