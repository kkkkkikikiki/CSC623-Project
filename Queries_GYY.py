import sqlite3
import pandas as pd
from tabulate import tabulate

db_connect = sqlite3.connect('SuperMaids.db')

cursor = db_connect.cursor()

def table_print(table_name):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    column_names = [row[0] for row in cursor.description]
    table_data = cursor.fetchall()
    df = pd.DataFrame(table_data, columns=column_names)
    print(table_name)
    print(df)

#table_print('Employee')
#table_print('Requirement')
#table_print('Client')
#table_print('Equipment')
#table_print('Perform')
#table_print('Need')

### Query 1: List the total workhours in April and May ###
query_1 = '''
    SELECT SUM(duration) AS hoursTotal
    FROM Requirement     
    WHERE strftime('%m', startDate) IN ('04', '05')
'''
cursor = db_connect.cursor()
cursor.execute(query_1)
results = cursor.fetchall()
columns = [description[0] for description in cursor.description]
print("\nThe total workhours in April and May:")
print(tabulate(results, headers=columns, tablefmt='psql'))



### Query 2: List all the comments of clients who had cleaning service in January ###
query_2 = '''
    SELECT c.clientNo, c.clientName, r.comments, r.startDate
    FROM Client c
    JOIN Requirement r ON c.clientNo = r.clientNo
    WHERE strftime('%m', r.startDate) = '01'
'''
cursor = db_connect.cursor()
cursor.execute(query_2)
results = cursor.fetchall()
columns = [description[0] for description in cursor.description]
print("\nThe comments of clients who had cleaning service in January:")
print(tabulate(results, headers=columns, tablefmt='psql'))



### Query 3: List the phone number of the employee who used Steam Power Wash ###
query_3 = '''
    SELECT e.staffNo, e.fName, e.lName, e.telNo, q.equipmentID, q.description
    FROM Employee e
    JOIN Perform p ON e.staffNo = p.staffNo
    JOIN Need n ON p.requirementID = n.requirementID
    JOIN Equipment q ON n.equipmentID = q.equipmentID
    WHERE description= 'Steam Power Wash'
'''
cursor = db_connect.cursor()
cursor.execute(query_3)
results = cursor.fetchall()
columns = [description[0] for description in cursor.description]
print("\nThe phone number of the employee who used Steam Power Wash:")
print(tabulate(results, headers=columns, tablefmt='psql'))



### Query 4: List all the employees who use equipment that costs more than $300 ###
query_4 = '''
    SELECT e.staffNo, e.fName, e.lName, q.equipmentID, q.description, q.cost
    FROM Employee e
    JOIN Perform p ON e.staffNo = p.staffNo
    JOIN Need n ON p.requirementID = n.requirementID
    JOIN Equipment q ON n.equipmentID = q.equipmentID
    WHERE q.cost > 300
'''
cursor = db_connect.cursor()
cursor.execute(query_4)
results = cursor.fetchall()
columns = [description[0] for description in cursor.description]
print("\nThe employees who use equipment that costs more than $300:")
print(tabulate(results, headers=columns, tablefmt='psql'))


### Query 5: List the employees and their equipments in descending order of worktime ###
query_5 = '''
    SELECT e.staffNo, e.fName, e.lName, q.equipmentID, q.description, p.worktime
    FROM Employee e     
    JOIN Perform p ON e.staffNo = p.staffNo
    JOIN Need n ON p.requirementID = n.requirementID
    JOIN Equipment q ON n.equipmentID = q.equipmentID
    ORDER BY worktime DESC
'''
cursor = db_connect.cursor()
cursor.execute(query_5)
results = cursor.fetchall()
columns = [description[0] for description in cursor.description]
print("\nThe employees and their equipments in descending order of worktime:")
print(tabulate(results, headers=columns, tablefmt='psql'))



db_connect.close()