from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Replace 'your_username', 'your_password', 'your_host', and 'your_database' with your actual credentials
db_uri = "mysql+pymysql://your_username:your_password@your_host/your_database"
engine = create_engine(db_uri)

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'Customers'
    CustomerID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Email = Column(String(255))
    Phone = Column(String(20))

# Bind the engine to the base class
Base.metadata.bind = engine

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create (Insert) Operation
def create_customer(name, email, phone):
    new_customer = Customer(Name=name, Email=email, Phone=phone)
    session.add(new_customer)
    session.commit()
    print("Customer created successfully!")

# Read (Retrieve) Operation
def get_customer_by_id(customer_id):
    customer = session.query(Customer).filter_by(CustomerID=customer_id).first()
    if customer:
        print(f"Customer ID: {customer.CustomerID}, Name: {customer.Name}, Email: {customer.Email}, Phone: {customer.Phone}")
    else:
        print("Customer not found.")

# Update Operation
def update_customer_email(customer_id, new_email):
    customer = session.query(Customer).filter_by(CustomerID=customer_id).first()
    if customer:
        customer.Email = new_email
        session.commit()
        print("Customer email updated successfully!")
    else:
        print("Customer not found.")

# Delete Operation
def delete_customer(customer_id):
    customer = session.query(Customer).filter_by(CustomerID=customer_id).first()
    if customer:
        session.delete(customer)
        session.commit()
        print("Customer deleted successfully!")
    else:
        print("Customer not found.")

# Example Usage:
create_customer("John Doe", "john@example.com", "123-456-7890")
get_customer_by_id(1)
update_customer_email(1, "john.doe@example.com")
delete_customer(1)

# Don't forget to close the session when you're done
session.close()
