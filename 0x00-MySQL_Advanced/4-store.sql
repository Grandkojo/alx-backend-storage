-- a trigger to the store
DELIMITER //
CREATE TRIGGER decrease_quantity
AFTER INSERT on orders
FOR EACH ROW
	BEGIN
		UPDATE items 
		SET quantity = quantity - NEW.number 
		WHERE name = NEW.item_name;
	END;//
DELIMITER;
