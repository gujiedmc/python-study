import pymysql

# db = pymysql.connect(host= 'bit.local', user='root', password='esIzNwS2D03z8A', database='bit')
db = pymysql.connect(host= 'localhost', user='root', password='Aa123456', database='bit', port=3306)

cursor = db.cursor()

tables = [
    'test_table'
]

sql_file = open(file="create_table.sql",mode='w')

for table_name in tables:
    cursor.execute("SHOW CREATE TABLE " + table_name)
    sql = cursor.fetchone()
    print(sql[1])
    sql_file.write("DROP TABLE IF EXISTS " + table_name + ";\n")
    sql_file.write(sql[1])
    sql_file.write(";\n\n")
db.close()

sql_file.close()