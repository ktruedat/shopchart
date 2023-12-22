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

        print(f"{res_products}")

        return res_products

    def add_product(self, product):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()
        new_product = Product(
            ProductID=None,
            Name=product['Name'],
            CategoryID=product['CategoryID'],
            Price=product['Price'],
            ProducerID=product['ProducerID']
        )
        session.add(new_product)
        session.commit()
        print(f"Product '{product['Name']}' created successfully!")
        session.close()

    def update_product(self, product_id: int, updated_product):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        new_product = Product(
            Name=updated_product['Name'],
            CategoryID=updated_product['CategoryID'],
            Price=updated_product['Price'],
            ProducerID=updated_product['ProducerID']
        )
        product = session.query(Product).filter_by(ProductID=product_id).first()
        if product:
            product.Name = new_product.Name
            product.Price = new_product.Price
            product.ProducerID = new_product.ProducerID
            product.CategoryID = new_product.CategoryID
            session.refresh(product)
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
            session.refresh(product)
            session.commit()
            print(f"Product with ID {product_id} deleted successfully!")
        else:
            print(f"Product with ID {product_id} not found.")

        session.close()
