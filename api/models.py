from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'Customers'
    CustomerID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Email = Column(String(255))
    Phone = Column(String(20))


class Producer(Base):
    __tablename__ = 'Producers'
    ProducerID = Column(Integer, primary_key=True)
    ProducerName = Column(String(255))
    ProducerLocation = Column(String(255))


class Sale(Base):
    __tablename__ = 'Sales'
    SaleID = Column(Integer, primary_key=True)
    ProductID = Column(Integer, ForeignKey('Products.ProductID'))
    CustomerID = Column(Integer, ForeignKey('Customers.CustomerID'))
    Quantity = Column(Integer)
    Amount = Column(Float)
    PromotionID = Column(Integer, ForeignKey('Promotions.PromotionID'))
    Date = Column(Date)


class Category(Base):
    __tablename__ = 'Categories'
    CategoryID = Column(Integer, primary_key=True)
    CategoryName = Column(String(255))


@dataclass
class Product(Base):
    __tablename__ = 'Products'
    ProductID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    CategoryID = Column(Integer, ForeignKey('Categories.CategoryID'))
    Price = Column(Float)
    ProducerID = Column(Integer, ForeignKey('Producers.ProducerID'))


class Promotion(Base):
    __tablename__ = 'Promotions'
    PromotionID = Column(Integer, primary_key=True)
    PromotionName = Column(String(255))
    DiscountPercentage = Column(Float)
    StartDate = Column(Date)
    EndDate = Column(Date)

# Producer.products = relationship("Product", order_by=Product.ProductID, back_populates="producer")
# Producer = relationship("Producer", back_populates="products")
