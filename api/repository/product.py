from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Producer(Base):
    __tablename__ = 'Producers'
    ProducerID = Column(Integer, primary_key=True)
    ProducerName = Column(String(255))
    ProducerLocation = Column(String(255))
    products = relationship("Product", back_populates="producer")

class Category(Base):
    __tablename__ = 'Categories'
    CategoryID = Column(Integer, primary_key=True)
    CategoryName = Column(String(255))

class Product(Base):
    __tablename__ = 'Products'
    ProductID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    CategoryID = Column(Integer, ForeignKey('Categories.CategoryID'))
    Price = Column(Float)
    ProducerID = Column(Integer, ForeignKey('Producers.ProducerID'))
    Producer = relationship("Producer", back_populates="products")

# Replace 'your_username', 'your_password', 'your_host', and 'your_database' with your actual credentials
db_uri = "mysql+pymysql://your_username:your_password@your_host/your_database"
engine = create_engine(db_uri)

# Bind the engine to the base class
Base.metadata.bind = engine

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Example: Create a new product
def create_product(name, category_id, price, producer_id):
    new_product = Product(Name=name, CategoryID=category_id, Price=price, ProducerID=producer_id)
    session.add(new_product)
    session.commit()
    print(f"Product '{name}' created successfully!")

# Example: Read (Retrieve) products
def get_all_products():
    products = session.query(Product).all()
    return products

# Example: Update a product
def update_product(product_id, new_price):
    product = session.query(Product).filter_by(ProductID=product_id).first()
    if product:
        product.Price = new_price
        session.commit()
        print(f"Product with ID {product_id} updated successfully!")
    else:
        print(f"Product with ID {product_id} not found.")

# Example: Delete a product
def delete_product(product_id):
    product = session.query(Product).filter_by(ProductID=product_id).first()
    if product:
        session.delete(product)
        session.commit()
        print(f"Product with ID {product_id} deleted successfully!")
    else:
        print(f"Product with ID {product_id} not found.")

# Example usage
create_product("Laptop", category_id=1, price=999.99, producer_id=1)
create_product("Smartphone", category_id=2, price=599.99, producer_id=2)

all_products = get_all_products()
print("All Products:")
for product in all_products:
    print(f"ID: {product.ProductID}, Name: {product.Name}, Price: {product.Price}")

update_product(product_id=1, new_price=1099.99)

delete_product(product_id=2)

# Don't forget to close the session when you're done
session.close()
