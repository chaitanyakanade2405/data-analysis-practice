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