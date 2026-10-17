--write a merge commands

merge into taget_customer as t 
using source_customer as s 
on t.customer_id=s.customer_id 

when matched
		and s.updated_at > t.updated_at
		then update set *
		
when not matched
then insert *;
-------------------------------------------------
--order table order _id 1 folder order 2 folder order 3 

df=spark.table("orders")

df=df.withcolumn("folder_id",.when(col("order-id")%3 == 1,1)
							.when(col("order-id")%3 == 2,2)
							.otherwise(3)
						)
						
for i in range(1,4):
		df.filter(col("folder_id")== i) \
		.drop("folder_id")\
		.write.format("delta")\
		.mode("overwrite")\
		.save("/output/order/folder_{i}")
		
		
Find customers who have not placed an order in the last 6 months.



six_month_ago=.add_month(current_date(),-6),

recent_orders=order.filter(col("order_date")>six_month_ago)
.select ("customer_id").distinct() 

result=customers.join(recent_orders,customers.customer_id== recent_orders.customer_id,"left")
.select ("customer_id","customer_name")

result.show()

----sql 


select c.customer_id,c.customer_name from customer C

left join order O
on c.customer_id=o.customer_id
and o.orderdate>=date_sub(curdate(),interval 6 month)

where o.order_id is null;

------------------------------------------------

