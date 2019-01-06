import mysql.connector

database_user = 'root'
database_password ='root'
database = 'db_carledwinti'
host = 'localhost'
connection = mysql.connector.connect(user=database_user, 
                                     password=database_password, 
                                     host=host, 
                                     database=database)

cursor = connection.cursor()

query = ('show databases')

cursor.execute(query)

print('\n**** query 1 cursor ****** \n\n')

for database in cursor:
    print('database: ' + str(database[0]))

query_2 = ("select * from tb_task")

cursor.execute(query_2)

result = cursor.fetchall()

print('\n\n**** query 2 result fetchall ****** \n\n')
for task in result:
    print('ID: ' + str(task[0]) + ' Name: ' + str(task[1]))

cursor.close()
connection.close()



