import pandas as pd 

AmazonSales = pd.DataFrame({
    "order_id":[1,2,3,4,5],
    "product": ["iPhone", "MacBook Pro", "AirPods", "Leather Case", "iPad"],
    "quantity":[12,34,13,54,10],
    "price": [120000, 220000, 30000,27000, 50000],
    "city": ["Mumbai", "Chennai", "Nagpur", "Pune", "Hyderabad"]
})

AmazonSales["revenue"] = AmazonSales["quantity"] * AmazonSales["price"]

print(AmazonSales["revenue"].sum())

# top selling order by revenue 

print(AmazonSales.sort_values("revenue" , ascending=False).head(3))