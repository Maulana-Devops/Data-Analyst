-- =========================================
-- PROJECT 05
-- GROUP BY, AGGREGATE FUNCTION & CASE WHEN
-- =========================================


-- =========================================
-- QUIZ 1
-- SUM() + CASE WHEN
-- =========================================

SELECT
    orderNumber,
    SUM(quantityOrdered * priceEach) AS total,
    CASE
        WHEN SUM(quantityOrdered * priceEach) >= 50000
            THEN 'Target Achieved'
        WHEN SUM(quantityOrdered * priceEach) <= 20000
            THEN 'Less performed'
        ELSE 'Follow Up'
    END AS remark
FROM orderdetails
GROUP BY orderNumber;


-- =========================================
-- QUIZ 2
-- 1. Total seluruh revenue
-- =========================================

SELECT
    SUM(quantityOrdered * priceEach) AS total_revenue
FROM orderdetails;


-- =========================================
-- QUIZ 2
-- 2. Total quantity seluruh produk
-- =========================================

SELECT
    SUM(quantityOrdered) AS total_quantity
FROM orderdetails;


-- =========================================
-- QUIZ 2
-- 3. Total quantity dan revenue setiap produk
-- =========================================

SELECT
    productCode,
    SUM(quantityOrdered) AS total_quantity,
    SUM(quantityOrdered * priceEach) AS total_revenue
FROM orderdetails
GROUP BY productCode;


-- =========================================
-- QUIZ 2
-- 4. Rata-rata total belanja per customer
-- =========================================

SELECT
    orders.customerNumber,
    AVG(orderdetails.quantityOrdered * orderdetails.priceEach)
        AS average_order_value
FROM orders
INNER JOIN orderdetails
    ON orders.orderNumber = orderdetails.orderNumber
GROUP BY orders.customerNumber;


-- =========================================
-- QUIZ 2
-- 5. Kategori revenue setiap order
-- =========================================

SELECT
    orderNumber,
    SUM(quantityOrdered * priceEach) AS total_revenue,
    CASE
        WHEN SUM(quantityOrdered * priceEach) > 300000
            THEN 'High'
        WHEN SUM(quantityOrdered * priceEach) >= 100000
            THEN 'Medium'
        ELSE 'Low'
    END AS kategori
FROM orderdetails
GROUP BY orderNumber;
