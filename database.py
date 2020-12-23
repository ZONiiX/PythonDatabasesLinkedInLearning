import sqlalchemy as db

engine = db.create_engine('sqlite:///items.db')

connection = engine.connect()

metadata = db.MetaData()

items = db.Table('items', metadata, autoload=True, autoload_with=engine)

query = db.select([items])

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

# print(result_set[:3])

query = db.select([items]).where(items.columns.price <= 80.00)

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

print(result_set)

query = items.insert().values(name="TestInsert", price=30.21, URL="www.kjhfakldhf.com")

connection.execute(query)

result_proxy = connection.execute(db.select([items]))

result_set = result_proxy.fetchall()

print(result_set)