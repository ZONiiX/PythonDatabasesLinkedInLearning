import sqlite3

conn = sqlite3.connect('items.db')

c = conn.cursor()


#item_list = [('1TB NVME SSD', 139.99, 'https://www.amazon.com/Samsung-970-EVO-1TB-MZ-V7E1T0BW/dp/B07BN217QG'), ('500GB NVME SSD', 59.99, 'https://www.amazon.com/Samsung-970-EVO-1TB-MZ-V7E1T0BW/dp/B07BN4NJ2J/'), ('250GB NVME SSD', 34.99, 'https://www.amazon.com/Inland-Professional-Internal-Express-Compatible/dp/B08KZS8N8Y/')]
c.execute("SELECT * FROM items")
items = c.fetchall()

for item in items:
    print(str(item[0])+" " +item[1] + " "+str(item[2]) + " " + item[3])

conn.commit()
c.close()
