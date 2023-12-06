from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Promotion(Base):
    __tablename__ = 'Promotions'
    PromotionID = Column(Integer, primary_key=True)
    PromotionName = Column(String(255))
    DiscountPercentage = Column(Float)
    StartDate = Column(Date)
    EndDate = Column(Date)

# Replace 'your_username', 'your_password', 'your_host', and 'your_database' with your actual credentials
db_uri = "mysql+pymysql://your_username:your_password@your_host/your_database"
engine = create_engine(db_uri)

# Bind the engine to the base class
Base.metadata.bind = engine

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

def create_promotion(name, discount_percentage, start_date, end_date):
    new_promotion = Promotion(
        PromotionName=name,
        DiscountPercentage=discount_percentage,
        StartDate=start_date,
        EndDate=end_date
    )
    session.add(new_promotion)
    session.commit()
    return new_promotion

def get_promotion(promotion_id):
    return session.query(Promotion).filter_by(PromotionID=promotion_id).first()

def update_promotion(promotion_id, name=None, discount_percentage=None, start_date=None, end_date=None):
    promotion = get_promotion(promotion_id)
    if promotion:
        if name is not None:
            promotion.PromotionName = name
        if discount_percentage is not None:
            promotion.DiscountPercentage = discount_percentage
        if start_date is not None:
            promotion.StartDate = start_date
        if end_date is not None:
            promotion.EndDate = end_date
        session.commit()
        return promotion
    return None

def delete_promotion(promotion_id):
    promotion = get_promotion(promotion_id)
    if promotion:
        session.delete(promotion)
        session.commit()
        return True
    return False

# Example usage
# Create a new promotion
new_promotion = create_promotion("Holiday Sale", 15.0, "2023-12-01", "2023-12-31")
print(f"Created Promotion: {new_promotion.PromotionName}")

# Retrieve a promotion by ID
retrieved_promotion = get_promotion(new_promotion.PromotionID)
print(f"Retrieved Promotion: {retrieved_promotion.PromotionName}")

# Update a promotion
updated_promotion = update_promotion(new_promotion.PromotionID, discount_percentage=20.0)
print(f"Updated Promotion Discount Percentage: {updated_promotion.DiscountPercentage}%")

# Delete a promotion
delete_result = delete_promotion(new_promotion.PromotionID)
print(f"Promotion Deleted: {delete_result}")
