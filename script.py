import csv
import sqlite3

db_name = "shipment_database.db"
product_table_name = "product"
shipment_table_name = "shipment"
con = sqlite3.connect(db_name)
cur = con.cursor()
print("Success to connect "+db_name+"\n")

with open('data/shipping_data_0.csv', 'r')as csv_file_0:
    csv_reader_0 = csv.reader(csv_file_0)
    next(csv_reader_0)
    product_id = 0
    product_name = ''
    quantity = ''
    origin = ''
    destination = ''

    for row in csv_reader_0:
        product_name = row[2]
        quantity = row[4]
        origin = row[0]
        destination = row[1]

        insertQuery_product = f"INSERT OR IGNORE INTO {product_table_name} VALUES ('{product_id}','{product_name}')"
        #insertQuery_shipment = f"INSERT INTO shipment VALUES ('{}', '{product_id}', '{quantity}', '{origin}', '{destination}')"
        
        cur.execute(insertQuery_product)
        con.commit()
        product_id += 1
cur.close()
con.close()
print("Success to transfer data\n")
