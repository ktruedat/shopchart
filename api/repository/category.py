from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Category(Base):
    __tablename__ = 'Categories'
    CategoryID = Column(Integer, primary_key=True)
    CategoryName = Column(String(255))

# Replace 'your_username', 'your_password', 'your_host', and 'your_database' with your actual credentials
db_uri = "mysql+pymysql://your_username:your_password@your_host/your_database"
engine = create_engine(db_uri)

# Bind the engine to the base class
Base.metadata.bind = engine

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create Operation
def create_category(name):
    new_category = Category(CategoryName=name)
    session.add(new_category)
    session.commit()
    print(f"Category '{name}' added with ID: {new_category.CategoryID}")

# Read Operation
def get_category_by_id(category_id):
    category = session.query(Category).filter_by(CategoryID=category_id).first()
    if category:
        print(f"Category ID: {category.CategoryID}, Name: {category.CategoryName}")
    else:
        print(f"No category found with ID: {category_id}")

# Update Operation
def update_category(category_id, new_name):
    category = session.query(Category).filter_by(CategoryID=category_id).first()
    if category:
        category.CategoryName = new_name
        session.commit()
        print(f"Category ID: {category_id} updated with new name: {new_name}")
    else:
        print(f"No category found with ID: {category_id}")

# Delete Operation
def delete_category(category_id):
    category = session.query(Category).filter_by(CategoryID=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        print(f"Category ID: {category_id} deleted")
    else:
        print(f"No category found with ID: {category_id}")

# Example usage
create_category("Electronics")
get_category_by_id(1)
update_category(1, "Gadgets")
delete_category(1)

# Don't forget to close the session when you're done
session.close()
