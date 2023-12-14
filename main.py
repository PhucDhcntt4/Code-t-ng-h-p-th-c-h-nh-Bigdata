# main.py
from base import SessionLocal, engine
from customer import Customer, Base

# Create tables (this should be done only once)
Base.metadata.create_all(bind=engine)

# Create a session
session = SessionLocal()

customers_to_add = [
    Customer(id=1,name='Alice', age=25, email='alice@example.com'),
    Customer(id=2,name='Bob', age=30, email='bob@example.com'),
    Customer(id=3,name='Charlie', age=22, email='charlie@example.com'),
]

session.add_all(customers_to_add)
session.commit()

# Query and print all customers
all_customers = session.query(Customer).all()
print("Tất cả khách hàng:")
for customer in all_customers:
    print("Thông tin:", f"ID: {customer.id}, Name: {customer.name}, Age: {customer.age}, Email: {customer.email}")

# Close the session
session.close()