

use grocery;
desc inventory_management;
ALTER TABLE inventory_management;

select * from inventory_management;
CREATE TABLE IF NOT EXISTS sales_transactions (
    customer_id INT,
    item VARCHAR(50),
    quantity DECIMAL(10, 2),
    price_per_unit DECIMAL(10, 2),
    total_price DECIMAL(10, 2),
    FOREIGN KEY (item) REFERENCES inventory_management(item)
);


CREATE TABLE if not exists customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_mobile_number VARCHAR(15) NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL);
select * from customers;
desc customers;
select * from sales_transactions;

create table profit_data(item varchar(100),quantity varchar(100),quantity_purchased int,profit_per_unit int,total_profit int);
-- Alter table to add AUTO_INCREMENT
ALTER TABLE customers
MODIFY customer_id INT AUTO_INCREMENT PRIMARY KEY;
desc customers;
alter table customers drop primary key;
select * from profit_data;
ALTER TABLE customers AUTO_INCREMENT = 1;

truncate sales_transactions;
desc inventory_management;
select * from inventory_management;

ALTER TABLE customers AUTO_INCREMENT = 1;
ALTER TABLE sales_transactions AUTO_INCREMENT = 1;
desc customers;

select * from customers;
select * from sales_transactions;
desc sales_transactions;
select * from profit_data;
alter table sales_transactions modify column customer_id int AUTO_INCREMENT primary key;
desc profit_data;
truncate profit_data;
truncate sales_transactions;
truncate customers;

alter table profit_data add constraint primary key(item);
alter table profit_data add constraint fk foreign key(item) references inventory_management(item);
desc profit_data;
select * from customers;
select * from sales_transactions;
select * from profit_data;
