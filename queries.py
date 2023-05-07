
import mysql.connector
mydb=mysql.connector.connect(host="localhost",username="root",password="Akhil@63057",database="Inventoty_Management")
cur=mydb.cursor()

cur.execute('DELETE FROM purchase WHERE item_name = "shirt" AND purchase_date = "2023-04-22" AND store_name = "ORay"')
mydb.commit()

cur.execute('UPDATE manufacture SET quantity = 100 WHERE item_color = "red" AND manufacture_id IN (SELECT manufacture_id FROM goods WHERE goods_id IN (SELECT goods_id FROM sale WHERE store_name = "dims")')
mydb.commit()

cur.execute('SELECT * FROM  goods JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id WHERE item_name = "wooden chair" AND manufacture_date< "2023-05-22"')
rows=cur.fetchall()
for i in rows:
    print(i)
mydb.commit()

cur.execute('SELECT sale.profit_margin FROM sale JOIN goods ON sale.goods_id = goods.goods_id JOIN manufacture ON goods.manufacture_id = manufacture.manufacture_id JOIN purchase ON goods.purchase_id = purchase.purchase_id WHERE item_name = "wooden table" AND store_name = "MyCare",company = "SS Export"')
row = cur.fetchone()
print(row[0])
mydb.commit()