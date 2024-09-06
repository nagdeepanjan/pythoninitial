import mysql.connector

mydb = mysql.connector.connect(host="mysql-deepanjan-deepanjannag-giraffe.a.aivencloud.com", user="avnadmin", port="22903", database="")

mycursor = mydb.cursor()

mycursor.execute("select * from employees")
print('showing all records in employees table')
print('This is a test print')
for i in mycursor:
    print(i)