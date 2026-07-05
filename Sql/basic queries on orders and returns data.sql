USE bootcamp;

SELECT * FROM orders_data
LIMIT 10;

-- top 5 rows with highest sales values
select * from orders_data
order by sales desc
limit 5;

SELECT * from orders_data
where sales in (select sales from(
 select distinct sales
 from orders_data
 order by sales desc
 limit 5) as top_sales
 )
 ORDER BY sales desc;
 
--  ratio
select *, profit/sales as ratio
from orders_data 
order by ratio;

select * from orders_data
where quantity in(3,5)
order by quantity;

select * from orders_data
where customer_name like 'A%';

SELECT *
FROM orders_data
WHERE customer_name LIKE '_a%'
   OR customer_name LIKE '_e%';

select category, sum(sales) as total_sales, sum(profit) as total_profit
from orders_data
group by category;

select city, sum(sales) as total_sales
from orders_data
where region = 'West'
group by city
having total_sales > 500;

select * from returns_data;

select * from orders_data as od  
inner join returns_data as rd
on od.order_id = rd.order_id
where return_reason = 'Wrong Items' and city = 'Los Angeles';

select * ,
CASE when profit < 0 then 'loss'
when profit between 50 and 99 then 'high profit'
when profit between 0 and 49 then 'low profit'
else 'very high profit'
end as  profit_bucket
from orders_data;

select *, length(customer_name) as cust_length,
left(order_id,2) as left_value
from orders_data;

SELECT order_id,order_date,
    DATE_FORMAT(order_date, '%M') AS order_month,
    year(order_date) as order_year,
    month(order_date) as order_month_num,
    datediff(ship_date, order_date) as lead_days
FROM orders_data;