from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Category(Base):
    __tablename__ = 'Categories'
    CategoryID = Column(Integer, primary_key=True)
    CategoryName = Column(String(255))

db_uri = "mysql+pymysql://your_username:your_password@your_host/your_database"
engine = create_engine(db_uri)

Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()

def create_category(name):
    new_category = Category(CategoryName=name)
    session.add(new_category)
    session.commit()
    print(f"Category '{name}' added with ID: {new_category.CategoryID}")

def get_category_by_id(category_id):
    category = session.query(Category).filter_by(CategoryID=category_id).first()
    if category:
        print(f"Category ID: {category.CategoryID}, Name: {category.CategoryName}")
    else:
        print(f"No category found with ID: {category_id}")

def update_category(category_id, new_name):
    category = session.query(Category).filter_by(CategoryID=category_id).first()
    if category:
        category.CategoryName = new_name
        session.commit()
        print(f"Category ID: {category_id} updated with new name: {new_name}")
    else:
        print(f"No category found with ID: {category_id}")

def delete_category(category_id):
    category = session.query(Category).filter_by(CategoryID=category_id).first()
    if category:
        session.delete(category)
        session.commit()
        print(f"Category ID: {category_id} deleted")
    else:
        print(f"No category found with ID: {category_id}")
