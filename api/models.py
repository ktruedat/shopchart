from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


@dataclass
class Customer(Base):
    __tablename__ = 'Customers'
    CustomerID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Email = Column(String(255))
    Phone = Column(String(20))

    def __init__(self, CustomerID, Name, Email, Phone):
        self.CustomerID = CustomerID
        self.Name = Name
        self.Email = Email
        self.Phone = Phone

    def __repr__(self):
        return f"Customer(CustomerID={self.CustomerID}, Name='{self.Name}', Email={self.Email}, Phone={self.Phone})"


@dataclass
class Producer(Base):
    __tablename__ = 'Producers'
    ProducerID = Column(Integer, primary_key=True)
    ProducerName = Column(String(255))
    ProducerLocation = Column(String(255))

    def __init__(self, ProducerID, ProducerName, ProducerLocation):
        self.ProducerID = ProducerID
        self.ProducerName = ProducerName
        self.ProducerLocation = ProducerLocation

    def __repr__(self):
        return f"Producer(ProducerID={self.ProducerID}, ProducerName='{self.ProducerName}', ProducerLocation={self.ProducerLocation})"


@dataclass
class Sale(Base):
    __tablename__ = 'Sales'
    SaleID = Column(Integer, primary_key=True)
    ProductID = Column(Integer, ForeignKey('Products.ProductID'))
    CustomerID = Column(Integer, ForeignKey('Customers.CustomerID'))
    Quantity = Column(Integer)
    Amount = Column(Float)
    PromotionID = Column(Integer, ForeignKey('Promotions.PromotionID'))
    Date = Column(Date)

    def __init__(self, SaleID, ProductID, CustomerID, Quantity, Amount, PromotionID, Date):
        self.SaleID = SaleID
        self.ProductID = ProductID
        self.CustomerID = CustomerID
        self.Quantity = Quantity
        self.Amount = Amount
        self.PromotionID = PromotionID
        self.Date = Date

    def __repr__(self):
        return f"Sale(SaleID={self.SaleID}, ProductID='{self.ProductID}', CustomerID={self.CustomerID}, Quantity={self.Quantity}, Amount={self.Amount}, PromotionID={self.PromotionID}, Date={self.Date})"


class Category(Base):
    __tablename__ = 'Categories'
    CategoryID = Column(Integer, primary_key=True)
    CategoryName = Column(String(255))

    def __init__(self, CategoryID, CategoryName):
        self.CategoryID = CategoryID
        self.CategoryName = CategoryName

    def __repr__(self):
        return f"Category(CategoryID={self.CategoryID}, CategoryName='{self.CategoryName}')"


@dataclass
class Product(Base):
    __tablename__ = 'Products'
    ProductID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    CategoryID = Column(Integer, ForeignKey('Categories.CategoryID'))
    Price = Column(Float)
    ProducerID = Column(Integer, ForeignKey('Producers.ProducerID'))

    def __init__(self, ProductID, Name, CategoryID, Price, ProducerID):
        self.ProductID = ProductID
        self.Name = Name
        self.CategoryID = CategoryID
        self.Price = Price
        self.ProducerID = ProducerID

    def __repr__(self):
        return f"Product(ProductID={self.ProductID}, Name='{self.Name}', CategoryID={self.CategoryID}, Price={self.Price}, ProducerID={self.ProducerID})"


@dataclass
class Promotion(Base):
    __tablename__ = 'Promotions'
    PromotionID = Column(Integer, primary_key=True)
    PromotionName = Column(String(255))
    DiscountPercentage = Column(Float)
    StartDate = Column(Date)
    EndDate = Column(Date)

    def __init__(self, PromotionID, PromotionName, DiscountPercentage, StartDate, EndDate):
        self.PromotionID = PromotionID
        self.PromotionName = PromotionName
        self.DiscountPercentage = DiscountPercentage
        self.StartDate = StartDate
        self.EndDate = EndDate

    def __repr__(self):
        return f"Promotion(PromotionID={self.PromotionID}, PromotionName='{self.PromotionName}', DiscountPercentage={self.DiscountPercentage}, StartDate={self.StartDate}, EndDate={self.EndDate})"


# @dataclass
# class SalesTrend(Base):
#     __tablename__ = 'SalesTrend'
#     SalesTrendID: int = Column(Integer, primary_key=True, autoincrement=True)
#     Date: Date = Column(Date, unique=True, nullable=True)
#     TotalSales: Float = Column(Float, nullable=True)
#     TotalQuantitySold: int = Column(Integer, nullable=True)
#     AverageSaleAmount: Float = Column(Float, nullable=True)
#     TotalCustomers: int = Column(Integer, nullable=True)
#     NewCustomers: int = Column(Integer, nullable=True)
#     RepeatCustomers: int = Column(Integer, nullable=True)
#     ProductPopularity: String = Column(String(255), nullable=True)
#     CategoryPopularity: String = Column(String(255), nullable=True)
#     SalesGrowthPercentage: Float = Column(Float, nullable=True)
#     AveragePurchaseFrequency: Float = Column(Float, nullable=True)
#     CustomerRetentionRate: Float = Column(Float, nullable=True)
#     SeasonalTrends: String = Column(String(255), nullable=True)
#     PromotionEffectiveness: String = Column(String(255), nullable=True)
#
#     def __repr__(self):
#         return f"SalesTrend(SalesTrendID={self.SalesTrendID}, Date={self.Date}, TotalSales={self.TotalSales}, " \
#                f"TotalQuantitySold={self.TotalQuantitySold}, AverageSaleAmount={self.AverageSaleAmount}, " \
#                f"TotalCustomers={self.TotalCustomers}, NewCustomers={self.NewCustomers}, " \
#                f"RepeatCustomers={self.RepeatCustomers}, ProductPopularity={self.ProductPopularity}, " \
#                f"CategoryPopularity={self.CategoryPopularity}, SalesGrowthPercentage={self.SalesGrowthPercentage}, " \
#                f"AveragePurchaseFrequency={self.AveragePurchaseFrequency}, CustomerRetentionRate={self.CustomerRetentionRate}, " \
#                f"SeasonalTrends={self.SeasonalTrends}, PromotionEffectiveness={self.PromotionEffectiveness})"


# Producer.products = relationship("Product", order_by=Product.ProductID, back_populates="producer")
# Producer = relationship("Producer", back_populates="products")
