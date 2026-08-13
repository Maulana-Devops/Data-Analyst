-- =========================================
-- PROJECT 10
-- SQL HAVING
-- =========================================


-- =========================================
-- QUIZ 1
-- Menampilkan orderNumber, itemscount
-- dan total sales
-- =========================================

SELECT
    orderNumber,
    SUM(quantityOrdered) AS itemscount,
    SUM(quantityOrdered * priceEach) AS total
FROM orderdetails
GROUP BY orderNumber;


-- =========================================
-- QUIZ 1
-- Total sales lebih besar dari 1000
-- =========================================

SELECT
    orderNumber,
    SUM(quantityOrdered) AS itemscount,
    SUM(quantityOrdered * priceEach) AS total
FROM orderdetails
GROUP BY orderNumber
HAVING SUM(quantityOrdered * priceEach) > 1000;


-- =========================================
-- QUIZ 1
-- Total sales > 1000
-- dan itemscount > 600
-- =========================================

SELECT
    orderNumber,
    SUM(quantityOrdered) AS itemscount,
    SUM(quantityOrdered * priceEach) AS total
FROM orderdetails
GROUP BY orderNumber
HAVING
    SUM(quantityOrdered * priceEach) > 1000
    AND SUM(quantityOrdered) > 600;


-- =========================================
-- QUIZ 2
-- JOIN orders dan orderdetails
-- Status Shipped
-- Total sales > 1500
-- =========================================

SELECT
    o.orderNumber,
    o.status,
    SUM(od.quantityOrdered) AS itemscount,
    SUM(od.quantityOrdered * od.priceEach) AS total
FROM orders AS o
INNER JOIN orderdetails AS od
    ON o.orderNumber = od.orderNumber
WHERE o.status = 'Shipped'
GROUP BY
    o.orderNumber,
    o.status
HAVING SUM(od.quantityOrdered * od.priceEach) > 1500;
