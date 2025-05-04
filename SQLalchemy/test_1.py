from sqlalchemy import MetaData, create_engine, Table, Select

metadata = MetaData(schema='sql_test')
engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/sqlalchemy_test")

# cookies = Table('cookies', metadata, autoload_with=engine)
# print(cookies.c.keys())

# s = Select(cookies)

# connection = engine.connect()
# results = connection.execute(s)

# print(results.fetchall())

metadata.reflect(bind=engine)

print(metadata.tables.keys())