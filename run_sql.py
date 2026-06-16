import sqlite3
import pandas as pd

conn = sqlite3.connect("gophle.db")

query = """
SELECT
    Item,
    SUM(Quantity) AS Total_Sold,
    SUM(Quantity * Price) AS Revenue
FROM sales
GROUP BY Item
ORDER BY Revenue DESC;
"""

result = pd.read_sql_query(query, conn)

print(result)

conn.close()