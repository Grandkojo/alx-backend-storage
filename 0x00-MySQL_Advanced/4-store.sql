DELIMITER $$
USE holberton
$$
CREATE TRIGGER decrease_quantity AFTER INSERT on holberton.items
FOR EACH ROW
BEGIN
UPDATE holberton.items SET quantity = quantity - holberton.orders.number WHERE holberton.items.name = holberton.orders.name;
END$$