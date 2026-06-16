-- Total revenue
SELECT 
    SUM(Quantity * Price) AS Total_Revenue
FROM sales;

-- Total profit
SELECT 
    SUM(Quantity * (Price - Cost)) AS Total_Profit
FROM sales;

-- Revenue by menu item
SELECT 
    Item,
    SUM(Quantity * Price) AS Revenue
FROM sales
GROUP BY Item
ORDER BY Revenue DESC;

-- Profit by menu item
SELECT 
    Item,
    SUM(Quantity * (Price - Cost)) AS Profit
FROM sales
GROUP BY Item
ORDER BY Profit DESC;

-- Best-selling items
SELECT 
    Item,
    SUM(Quantity) AS Total_Quantity_Sold
FROM sales
GROUP BY Item
ORDER BY Total_Quantity_Sold DESC;

-- Revenue by customer type
SELECT 
    Customer_Type,
    SUM(Quantity * Price) AS Revenue
FROM sales
GROUP BY Customer_Type;

-- Competitor ranking
SELECT 
    Restaurant,
    Rating,
    Reviews,
    Avg_Price
FROM competitors
ORDER BY Rating DESC;