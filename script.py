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
    product_name = ''
    quantity = ''
    origin = ''
    destination = ''

    for row in csv_reader_0:
        product_name = row[2]

        insertQuery_product = f"INSERT OR IGNORE INTO {product_table_name} VALUES (NULL,'{product_name}')"
        cur.execute(insertQuery_product)
    print(f"Success to transfer data to {product_table_name} table\n")

    csv_file_0.seek(0)
    csv_reader_0 = csv.reader(csv_file_0)
    next(csv_reader_0)
    for row in csv_reader_0:
        product_name = row[2]
        quantity = row[4]
        origin = row[0]
        destination = row[1]

        selectQuery_product = f"SELECT id FROM {product_table_name} WHERE name = '{product_name}'"
        cur.execute(selectQuery_product)
        res = cur.fetchone()

        insertQuery_shipment = f"INSERT INTO {shipment_table_name} VALUES (NULL, '{res[0]}', '{quantity}', '{origin}', '{destination}')"
        cur.execute(insertQuery_shipment)
    print(f"Success to transfer data to {shipment_table_name} table\n")
    con.commit()
cur.close()
con.close()
