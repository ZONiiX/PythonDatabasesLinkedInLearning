import sqlite3

connection = sqlite3.connect('users.db')

cursor = connection.cursor()

insertThese = [(1, 'Tron', 'Schell', 'tron.schell@icloud.com'), (2, 'Emma', 'Agostino', 'ega1609@rit.edu'), (3, 'Judith', 'Wansor', 'judy.wansor@gmail.com'), (4, 'Chris', 'Bubnick', 'ctb@gmail.com'), (4, 'Sawako', 'Schell', 'sch305ny@gmail.com')]

'''
cursor.execute("""CREATE TABLE users(
    User_Id INT, First VARCHAR(10), Last VARCHAR(10), EmailAddress VARCHAR(40)
) """)


cursor.executemany("""INSERT INTO users(User_Id, First, Last, EmailAddress) VALUES(?,?,?,?)
""", insertThese)
'''
'''
cursor.execute("SELECT * FROM users")

print(cursor.fetchall())
'''

cursor.execute("SELECT EmailAddress FROM users")
print(cursor.fetchall())

connection.commit()
connection.close