from sqlalchemy.orm import sessionmaker
from api.controller.sale import ISaleRepository
from api.models import *
from dbconnection import create_connection

engine = create_connection()


class SaleRepository(ISaleRepository):

    def add_sale(self, sale: Sale):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(sale)
        session.commit()
        session.close()

        print(f"Product '{sale.SaleID}' created successfully!")

        return sale

    def get_sale(self, sale_id: int):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        sale = session.query(Sale).get(sale_id)

        session.close()

        return sale

    def get_sales(self):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        res_sales = session.query(Sale).all()

        session.close()

        return res_sales

    def update_sale(self, sale_id: int, sale: Sale):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        updated_sale = session.query(Sale).get(sale_id)
        if updated_sale:
            updated_sale.SaleID = None
            updated_sale.ProductID = sale.ProductID
            updated_sale.CustomerID = sale.CustomerID
            updated_sale.Quantity = sale.Quantity
            updated_sale.Amount = sale.Amount
            updated_sale.PromotionID = sale.PromotionID
            updated_sale.Date = sale.Date
            session.commit()

        session.close()
        return updated_sale

    def delete_sale(self, sale_id: int):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        sale = session.query(Sale).get(sale_id)
        if sale:
            session.delete(sale)
            session.commit()

        session.close()
        return sale


