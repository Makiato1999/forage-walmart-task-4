import csv, sqlite3

con = sqlite3.connect("shipment_database.db")
cur = con.cursor()

with open('data/shipping_data_0.csv', 'r')as csv_file:
    csv_reader_0 = csv.reader(csv_file)
    header = next(csv_reader_0)
    no_record = 0
    id = ''
    product_id = ''
    quantity = ''
    origin = ''
    destination = ''

    for row in csv_reader_0:
        id = no_record
        quantity = row[4]
        origin = row[0]
        destination = row[1]

        insertQuery = f"INSERT INTO shipment VALUES ('{id}', '{id}', '{quantity}', '{origin}', '{destination}')"
        cur.execute(insertQuery)
        no_record += 1
        con.commit()
con.close()
print("Success to transfer data\n")

