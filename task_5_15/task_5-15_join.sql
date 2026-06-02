-- Выведите список цен товаров, используя алиасы таблиц: 
-- products → p, prices → pr. 
-- Вывод: "название товара" и "цена"
SELECT 
    p.name AS "Название товара", 
    pr.price AS "Цена"
FROM products p
JOIN prices pr ON p.id = pr.product_id;