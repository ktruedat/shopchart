from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

from api.controller.producer import IProducerRepository
from dbconnection import create_connection

engine = create_connection()

class ProducerRepository(IProducerRepository):

    def add_producer(self, producer):
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

