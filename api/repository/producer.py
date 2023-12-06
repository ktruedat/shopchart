from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Producer(Base):
    __tablename__ = 'Producers'
    ProducerID = Column(Integer, primary_key=True)
    ProducerName = Column(String(255))
    ProducerLocation = Column(String(255))

# Replace 'your_username', 'your_password', 'your_host', and 'your_database' with your actual credentials
db_uri = "mysql+pymysql://your_username:your_password@your_host/your_database"
engine = create_engine(db_uri)

# Bind the engine to the base class
Base.metadata.bind = engine

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

def create_producer(producer_name, producer_location):
    new_producer = Producer(ProducerName=producer_name, ProducerLocation=producer_location)
    session.add(new_producer)
    session.commit()
    return new_producer

def read_producer(producer_id):
    return session.query(Producer).get(producer_id)

def update_producer(producer_id, new_name, new_location):
    producer = session.query(Producer).get(producer_id)
    if producer:
        producer.ProducerName = new_name
        producer.ProducerLocation = new_location
        session.commit()
    return producer

def delete_producer(producer_id):
    producer = session.query(Producer).get(producer_id)
    if producer:
        session.delete(producer)
        session.commit()
    return producer

# Example usage:
# Create a new producer
created_producer = create_producer("New Producer", "Location XYZ")
print("Created Producer:", created_producer.__dict__)

# Read an existing producer
read_producer_result = read_producer(1)
print("Read Producer:", read_producer_result.__dict__)

# Update an existing producer
updated_producer = update_producer(1, "Updated Producer", "New Location")
print("Updated Producer:", updated_producer.__dict__)

# Delete an existing producer
deleted_producer = delete_producer(1)
print("Deleted Producer:", deleted_producer.__dict__)

# Don't forget to close the session when you're done
session.close()
