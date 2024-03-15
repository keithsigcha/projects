-- Create database
CREATE DATABASE IF NOT EXISTS walmartSales;

-- Create table
CREATE TABLE IF NOT EXISTS sales(
	invoice_id VARCHAR(30) NOT NULL PRIMARY KEY,
    branch VARCHAR(5) NOT NULL,
    city VARCHAR(30) NOT NULL,
    customer_type VARCHAR(30) NOT NULL,
    gender VARCHAR(30) NOT NULL,
    product_line VARCHAR(100) NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL,
    tax_pct FLOAT(6,4) NOT NULL,
    total DECIMAL(12, 4) NOT NULL,
    date DATETIME NOT NULL,
    time TIME NOT NULL,
    payment VARCHAR(15) NOT NULL,
    cogs DECIMAL(10,2) NOT NULL,
    gross_margin_pct FLOAT(11,9),
    gross_income DECIMAL(12, 4),
    rating FLOAT(2, 1)
);

SELECT * FROM sales;

#how many cities are included in the dataset

SELECT DISTINCT(CITY) FROM sales;

# what is the average price of the products Walmart offers to its customers 

SELECT avg(unit_price) FROM sales AS avgunitprice;

#what is the total quantity Walmart have sold from each product line?

SELECT product_line, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product_line
ORDER BY total_quantity ASC;

#Which product line is most sold in quanity among the men demographic population?\

SELECT product_line, SUM(quantity) AS total_quantity
FROM sales
WHERE gender= "Male"
GROUP BY product_line;

#LIST the product lines for each city that sold more than 300 units 
SELECT city,product_line,SUM(quantity) AS total_quantity 
FROM sales
GROUP BY city, product_line
HAVING total_quantity > 300;

#Which city had the most revenue?
SELECT city, SUM(total) AS revenue 
FROM sales
GROUP BY city
ORDER BY revenue DESC;

# What is the average money a Normal customer would spend on each  product lines offered by Walmart?
SELECT customer_type, product_line, AVG(total) AS avgmoney_spent
FROM sales 
WHERE customer_type= "Normal"
GROUP BY product_line
ORDER BY avgmoney_spent;

# What is the total money spent by Member customers on each product line only for the city,Yangon?
SELECT city , customer_type , product_line, SUM(total) AS total 
FROM sales
WHERE city = "Yangon" AND customer_type= "Member"
GROUP BY product_line
ORDER BY total DESC;

#Label each product line as either outperforming ,underperforming, or normal for their average ratings. If average rate is below 4 the product line
# is underperfroming. If the rate is 4 , then the product line is performing normal. If rate >4, product is outperforming.

SELECT product_line,
CASE
WHEN AVG(rating) > 7.0 THEN "outperforming" 
WHEN AVG(rating) < 4.0 THEN "underperforming"
ELSE "underperforming"
END AS "performance"
FROM sales
GROUP BY product_line;

#How much do Normal members who are male spend on Sports and Travel across Walmart? GROUP By city
SELECT city, customer_type,product_line, SUM(total) AS Total
FROM sales
WHERE customer_type="Normal" AND product_line="Sports and travel" AND gender="male"
GROUP BY city
ORDER BY Total;

#What is the most common payment method?
SELECT payment,
COUNT(*) as count
FROM sales
GROUP BY payment
ORDER BY count ASC;

#What is the most common payment method among men?
SELECT gender,payment ,COUNT(payment) AS count
FROM sales
WHERE gender="male"
GROUP BY payment
ORDER BY count DESC;

#What is the most common payment method among women?
SELECT gender,payment,COUNT(payment) AS count
FROM sales
WHERE gender="female"
GROUP BY payment
ORDER BY COUNT DESC;

#What is the most common payment method among Normal female customers?
SELECT gender, customer_type,payment,COUNT(payment) AS count
FROM sales
WHERE customer_type="Normal" AND gender="female"
GROUP BY payment, gender
ORDER BY count DESC;

#What is the most common payment method among Member customers?
SELECT customer_type,payment,COUNT(payment) AS count
FROM sales
WHERE customer_type="Member"
GROUP BY payment 
ORDER BY count DESC;

#What date had the highest total money spent by customers at Walmart?
SELECT  MAX(Total_money) AS highest_sales
FROM (SELECT date, SUM(total) AS Total_money
FROM sales
GROUP BY date) sales_by_date
