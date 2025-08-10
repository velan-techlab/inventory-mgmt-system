insert INTO inventory (item_id, item_name, quantity, price) VALUES
(1, 'Widget A', 100, 19.99),
(2, 'Widget B', 200, 29.99),
(3, 'Widget C', 150, 39.99);


INSERT INTO sales_order (order_id, item_id, order_date, quantity) VALUES
(1, 1, '2023-10-01', 2),
(2, 2, '2023-10-02', 5),
(3, 3, '2023-10-03', 1);

INSERT INTO purchase_order (purchase_id, item_id, purchase_date, quantity) VALUES
(1, 1, '2023-10-04', 10),
(2, 2, '2023-10-05', 20),
(3, 3, '2023-10-06', 15);


select * from inventory;
select * from purchase_order;
select * from sales_order;