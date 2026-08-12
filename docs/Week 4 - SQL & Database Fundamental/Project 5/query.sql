-- Project 05 - SQL JOIN


-- Quiz 1 - INNER JOIN
-- Menggabungkan orders dan orderdetails
-- menggunakan orderNumber sebagai key column.

SELECT
    orders.orderNumber,
    orders.customerNumber,
    orderdetails.productCode,
    orderdetails.quantityOrdered,
    orderdetails.priceEach
FROM orders
INNER JOIN orderdetails
    ON orders.orderNumber = orderdetails.orderNumber;


-- Quiz 1 - Alternative Query
-- Menghasilkan hasil JOIN yang sama
-- menggunakan WHERE.

SELECT
    orders.orderNumber,
    orders.customerNumber,
    orderdetails.productCode,
    orderdetails.quantityOrdered,
    orderdetails.priceEach
FROM orders, orderdetails
WHERE orders.orderNumber = orderdetails.orderNumber;


-- Quiz 2 - JOIN + Calculated Column
-- Total = quantityOrdered × priceEach

SELECT
    orders.orderNumber,
    orders.customerNumber,
    orderdetails.productCode,
    orderdetails.priceEach,
    orderdetails.quantityOrdered,
    orderdetails.priceEach * orderdetails.quantityOrdered AS total
FROM orders
INNER JOIN orderdetails
    ON orders.orderNumber = orderdetails.orderNumber;
