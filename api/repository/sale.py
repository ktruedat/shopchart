from sqlalchemy import create_engine, Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship
from datetime import date

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'Customers'
    CustomerID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Email = Column(String(255))
    Phone = Column(String(20))
    sales = relationship("Sale", back_populates="customer")

class Product(Base):
    __tablename__ = 'Products'
    ProductID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    sales = relationship("Sale", back_populates="product")

class Promotion(Base):
    __tablename__ = 'Promotions'
    PromotionID = Column(Integer, primary_key=True)
    PromotionName = Column(String(255))
    DiscountPercentage = Column(Float)
    StartDate = Column(Date)
    EndDate = Column(Date)
    sales = relationship("Sale", back_populates="promotion")

class Sale(Base):
    __tablename__ = 'Sales'
    SaleID = Column(Integer, primary_key=True)
    ProductID = Column(Integer, ForeignKey('Products.ProductID'))
    CustomerID = Column(Integer, ForeignKey('Customers.CustomerID'))
    Quantity = Column(Integer)
    Amount = Column(Float)
    PromotionID = Column(Integer, ForeignKey('Promotions.PromotionID'))
    Date = Column(Date)

    # Relationships
    product = relationship("Product", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")
    promotion = relationship("Promotion", back_populates="sales")

# Replace 'your_username', 'your_password', 'your_host', and 'your_database' with your actual credentials
db_uri = "mysql+pymysql://your_username:your_password@your_host/your_database"
engine = create_engine(db_uri)

# Bind the engine to the base class
Base.metadata.bind = engine

# Create tables if they don't exist
Base.metadata.create_all()

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# CRUD Operations

# Create a new sale
new_sale = Sale(
    ProductID=1,
    CustomerID=1,
    Quantity=5,
    Amount=100.0,
    PromotionID=1,
    Date=date.today()
)

session.add(new_sale)
session.commit()

# Read all sales
all_sales = session.query(Sale).all()
for sale in all_sales:
    print(f"SaleID: {sale.SaleID}, Product: {sale.product.Name}, Customer: {sale.customer.Name}, Quantity: {sale.Quantity}, Amount: {sale.Amount}, Date: {sale.Date}")

# Update a sale
sale_to_update = session.query(Sale).filter_by(SaleID=1).first()
sale_to_update.Amount = 120.0
session.commit()

# Delete a sale
sale_to_delete = session.query(Sale).filter_by(SaleID=1).first()
session.delete(sale_to_delete)
session.commit()

# Don't forget to close the session when you're done
session.close()
