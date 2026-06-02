-- Обновить цены товаров: увеличить на 5% для записей,
-- где product_id меньше или равен 5 и цена меньше 10000.
UPDATE prices
SET price = price * 1.05
WHERE product_id <= 5 
  AND price < 10000;