import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="Akhil@63057",database="Inventoty_Management")
cur=mydb.cursor()
cur.execute("use Inventoty_Management")

manufacture="create table manufacture(manufacture_id int primary key,item_name VARCHAR(30),company_name varchar(30),color_of_item VARCHAR(30),no_0f_items int,defective_items int)"
#cur.execute(manufacture)

goods="create table goods(goods_id int PRIMARY KEY, manufacture_id int,manufacture_date date,FOREIGN KEY(manufacture_id) REFERENCES manufacture(manufacture_id))"
#cur.execute(goods)

purchase="create table purchase(purchase_id int PRIMARY KEY,store_name varchar(30),purchase_amount FLOAT,purchase_date date)"
#cur.execute(purchase)

sale="create table sale(sale_id int PRIMARY KEY,store_name VARCHAR(30),sale_date DATE,goods_id int, profit_margin FLOAT,FOREIGN KEY(goods_id) REFERENCES goods(goods_id))"
#cur.execute(sale)

m="insert into manufacture values(%s,%s,%s,%s,%s,%s)"
v= (4, "pens","cello" ,"blue",200, 0), (1, "wooden tables","SS EXPORT" "brown", 100, 1),(6, "red toy","N TOYS","red", 50, 1),(4,"shirt","high lander","white",300,1),(5,"shoes","nike","black",30,1)
cur.executemany(m,v)
mydb.commit()

g="insert into goods values (%s,%s,%s,)"
v = ((3, 1, "2023-01-22"),(4, 1, "2023-03-22"),(1, 2, "2023-03-22"),(2, 3, "2023-07-22"))
cur.executemany(g,v)
mydb.commit()

p="insert into purchase values(%s,%s,%s,%s)"
v= ((3, "DIMS", 100, "2023-04-21"), (2, "ORay", 150, "2023-04-22"),(3, "ORIYO",175,"2023-04-23"))
cur.executemany(p,v)
mydb.commit()

s="INSERT INTO sale(sale_id ,store_name ,sale_date,goods_id , profit_margin )values(%s,%s,%s,%s,%s)"
v= ((1, "MyCare", "2023-07-22", 1, 100),(2, "ORay", "2023-07-22", 2, 50),(3, "DIMS", "2023-01-22", 3, 75),(4, "ORIYO", "2023-04-22", 4, 80))
cur.executemany(s,v)
mydb.commit()