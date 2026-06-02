-- Увеличить цену на 10% для всех товаров, 
-- у которых текущая цена меньше 1000.
UPDATE prices
SET price = price * 1.1
WHERE price < 1000;