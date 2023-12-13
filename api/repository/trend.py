from sqlalchemy import func, distinct, and_, exists
from sqlalchemy.orm import sessionmaker
from api.models import *
from api.controller.trend import ITrendsRepository
from dbconnection import create_connection
# from api.controller.entity import EntityController

engine = create_connection()


class TrendsRepository(ITrendsRepository):

    def get_total_sales(self, start_date, end_date):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        total_sales = (
            session.query(Sale.Date, func.sum(Sale.Amount).label("TotalSales"))
            .filter(and_(Sale.Date.between(start_date, end_date)))
            .group_by(Sale.Date)
            .all()
        )

        session.close()

        return total_sales

    def get_total_quantity_sold(self, start_date, end_date):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        total_quantity_sold = (
            session.query(Sale.Date, func.sum(Sale.Quantity).label("TotalQuantitySold"))
            .filter(and_(Sale.Date.between(start_date, end_date)))
            .group_by(Sale.Date)
            .all()
        )

        session.close()

        return total_quantity_sold

    def get_total_customers(self, start_date, end_date):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        total_customers = (
            session.query(Sale.Date, func.count(distinct(Sale.CustomerID)).label("TotalCustomers"))
            .filter(and_(Sale.Date.between(start_date, end_date)))
            .group_by(Sale.Date)
            .all()
        )

        session.close()

        return total_customers

    def get_total_new_customers(self, start_date, end_date):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        total_new_customers = (
            session.query(Sale.Date, func.count(distinct(Sale.CustomerID)).label("TotalNewCustomers"))
            .filter(and_(Sale.Date.between(start_date, end_date), ~exists().where(Sale.Date < start_date)))
            .group_by(Sale.Date)
            .all()
        )

        session.close()

        return total_new_customers

    def get_total_repeat_customers(self, start_date, end_date):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        total_repeat_customers = (
            session.query(Sale.Date, func.count(distinct(Sale.CustomerID)).label("TotalRepeatCustomers"))
            .filter(and_(Sale.Date.between(start_date, end_date), exists().where(Sale.Date < start_date)))
            .group_by(Sale.Date)
            .all()
        )

        session.close()

        return total_repeat_customers

    def get_product_popularity(self, start_date, end_date):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        product_popularity = (
            session.query(Sale.Date, Product.Name, func.sum(Sale.Quantity).label("TotalQuantitySold"))
            .join(Product, Sale.ProductID == Product.ProductID)
            .filter(Sale.Date.between(start_date, end_date))
            .group_by(Sale.Date, Product.ProductID)
            .all()
        )

        session.close()

        return product_popularity

    def get_category_popularity(self, start_date, end_date):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        category_popularity = (
            session.query(Sale.Date, Category.CategoryName, func.sum(Sale.Quantity).label("TotalQuantitySold"))
            .join(Product, Product.CategoryID == Category.CategoryID)
            .join(Sale, Sale.ProductID == Product.ProductID)
            .filter(Sale.Date.between(start_date, end_date))
            .group_by(Sale.Date, Category.CategoryID)
            .all()
        )

        session.close()

        return category_popularity

    def get_sales_growth_percentage(self, start_date, end_date):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()
        total_sales_start = (
            session.query(func.sum(Sale.Amount))
            .filter(Sale.Date == start_date)
            .scalar()
        )
        total_sales_end = (
            session.query(func.sum(Sale.Amount))
            .filter(Sale.Date == end_date)
            .scalar()
        )

        session.close()

        if total_sales_start is not None and total_sales_end is not None and total_sales_start != 0:
            sales_growth_percentage = ((total_sales_end - total_sales_start) / total_sales_start) * 100
        else:
            sales_growth_percentage = 0

        return sales_growth_percentage

    def get_average_purchase_frequency(self, start_date, end_date):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()
        total_purchases = (
            session.query(func.count(Sale.SaleID))
            .filter(Sale.Date.between(start_date, end_date))
            .scalar()
        )
        total_customers = (
            session.query(func.count(distinct(Sale.CustomerID)))
            .join(Customer, Sale.CustomerID == Customer.CustomerID)
            .filter(Sale.Date.between(start_date, end_date))
            .scalar()
        )

        # Assuming you have a date for which you are calculating average purchase frequency
        date = start_date  # You may need to replace this with the actual date

        session.close()

        average_purchase_frequency_data = {'Date': date, 'AveragePurchaseFrequency': total_purchases / total_customers if total_customers > 0 else 0}
        return average_purchase_frequency_data

    def get_customer_retention_rate(self, start_date, end_date):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()
        retained_customers = (
            session.query(func.count(distinct(Sale.CustomerID)))
            .filter(Sale.Date.between(start_date, end_date))
            .scalar()
        )
        total_customers_previous_period = (
            session.query(func.count(distinct(Sale.CustomerID)))
            .filter(Sale.Date < start_date)
            .scalar()
        )
        session.close()

        customer_retention_rate = (retained_customers / total_customers_previous_period) * 100 if total_customers_previous_period != 0 else 0
        return customer_retention_rate

    def get_seasonal_trends(self, start_date, end_date):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        seasonal_trends = (
            session.query(func.extract("month", Sale.Date).label("Month"), func.sum(Sale.Amount).label("TotalSales"))
            .filter(Sale.Date.between(start_date, end_date))
            .group_by(func.extract("month", Sale.Date))
            .all()
        )
        session.close()

        return seasonal_trends

    def get_promotion_effectiveness(self, promotion_id):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        promotion_effectiveness = (
            session.query(func.sum(Sale.Amount).label("TotalSales"))
            .filter(Sale.PromotionID == promotion_id)
            .scalar()
        )
        session.close()

        return promotion_effectiveness if promotion_effectiveness is not None else 0


