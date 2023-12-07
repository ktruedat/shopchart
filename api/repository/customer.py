from sqlalchemy.orm import sessionmaker
from api.controller.customer import ICustomerRepository
from api.models import *
from dbconnection import create_connection

engine = create_connection()


class CustomerRepository(ICustomerRepository):
    def add_customer(self, customer):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()
        new_customer = Customer(
            Name=customer['Name'],
            Email=customer['Email'],
            Phone=customer['Phone'],
        )
        session.add(new_customer)
        session.commit()
        session.close()
        print("Customer created successfully!")

    def get_customer(self, customer_id):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        customer = session.query(Customer).filter_by(CustomerID=customer_id).first()
        if customer:
            print(
                f"Customer ID: {customer.CustomerID}, Name: {customer.Name}, Email: {customer.Email}, Phone: {customer.Phone}")
        else:
            print("Customer not found.")

    def get_customers(self):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()
        res_customers = session.query(Customer).all()
        session.close()

        print(f"{res_customers}")

        return res_customers

    def update_customer(self, customer_id: int, updated_customer):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        new_customer = Customer(
            Name=updated_customer['Name'],
            Email=updated_customer['Email'],
            Phone=updated_customer['Phone'],
        )

        customer = session.query(Customer).filter_by(CustomerID=customer_id).first()
        if customer:
            customer.Name = new_customer.Name
            customer.Email = new_customer.Email
            customer.Phone = new_customer.Phone
            session.commit()
            print("Customer updated successfully!")
        else:
            print("Customer not found.")
        session.close()

    def delete_customer(self, customer_id: int):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()
        customer = session.query(Customer).filter_by(CustomerID=customer_id).first()
        if customer:
            session.delete(customer)
            session.commit()
            print("Customer deleted successfully!")
        else:
            print("Customer not found.")
        session.close()
