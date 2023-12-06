from sqlalchemy.orm import sessionmaker
from api.controller.product import IProductRepository
from api.models import *
from dbconnection import create_connection

engine = create_connection()


class ProductRepository(IProductRepository):

    def get_product(self, product_id: int):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        products = session.query(Product).all()
        session.close()

        return products

    def get_products(self):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        res_products = session.query(Product).all()
        session.close()

        print(f"HERE {res_products}")

        return res_products


    def add_product(self, product):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()
        new_product = Product(
            Name=product['Name'],
            CategoryID=product['CategoryID'],
            Price=product['Price'],
            ProducerID=product['ProducerID']
        )
        session.add(new_product)
        session.commit()
        print(f"Product '{product['Name']}' created successfully!")
        session.close()

    def update_product(self, product_id: int, updated_product: Product):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()
        product = session.query(Product).filter_by(ProductID=product_id).first()
        if product:
            product.Name = updated_product.Name
            product.Price = updated_product.Price
            product.ProducerID = updated_product.ProducerID
            product.CategoryID = updated_product.CategoryID
            session.commit()
            print(f"Product with ID {product_id} updated successfully!")
        else:
            print(f"Product with ID {product_id} not found.")

        session.commit()
        session.close()

    def delete_product(self, product_id: int):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()
        product = session.query(Product).filter_by(ProductID=product_id).first()
        if product:
            session.delete(product)
            session.commit()
            print(f"Product with ID {product_id} deleted successfully!")
        else:
            print(f"Product with ID {product_id} not found.")

        session.commit()
        session.close()
