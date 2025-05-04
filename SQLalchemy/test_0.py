from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Numeric, DateTime, ForeignKey, Boolean, Update, Select
from sqlalchemy.sql import func

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/sqlalchemy_test", echo=True)
connection = engine.connect()

metadata = MetaData(schema='sql_test')
cookies = Table(
    'cookies',
    metadata,
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unit_cost', Numeric(12, 2))
)

users = Table('users', metadata,
              Column('user_id', Integer(), primary_key=True),
              Column('username', String(15), nullable=False, unique=True),
              Column('email_address', String(255), nullable=False),
              Column('phone', String(20), nullable=False),
              Column('password', String(25), nullable=False),
              Column('created_on', DateTime(), default=datetime.now),
              Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
              )

orders = Table('orders', metadata,
               Column('order_id', Integer(), primary_key=True),
               Column('user_id', ForeignKey('users.user_id')),
               Column('shipped', Boolean(), default=False)
               )
line_items = Table('line_items', metadata,
                   Column('line_items_id', Integer(), primary_key=True),
                   Column('order_id', ForeignKey('orders.order_id')),
                   Column('cookie_id', ForeignKey('cookies.cookie_id')),
                   Column('quantity', Integer()),
                   Column('extended_cost', Numeric(12, 2))
                   )

inventory_list = [
    {
        'cookie_name': 'peanut butter',
        'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
        'cookie_sku': 'PB01',
        'quantity': '24',
        'unit_cost': '0.25'
    },
    {
        'cookie_name': 'oatmeal raisin',
        'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
        'cookie_sku': 'EWW01',
        'quantity': '100',
        'unit_cost': '1.00'
    }
]
# ins = cookies.insert()
#
# result = connection.execute(ins, inventory_list)
#
# connection.commit()

ins = Update(cookies)
ins = ins.values(quantity=(cookies.c.quantity + 120))
results = connection.execute(ins)
print(results.rowcount)

ins = Select(cookies)
results = connection.execute(ins)
print(results.fetchall())
# for record in results:
#     print(record)

# metadata.create_all(engine)
