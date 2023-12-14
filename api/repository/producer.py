from sqlalchemy.orm import sessionmaker
from api.controller.producer import IProducerRepository
from api.models import *
from dbconnection import create_connection

engine = create_connection()


class ProducerRepository(IProducerRepository):

    def add_producer(self, producer):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        new_producer = Producer(
            ProducerName=producer['Name'],
            ProducerLocation=producer['Location']
        )
        session.add(new_producer)
        session.commit()
        session.refresh(new_producer)
        session.close()

        print(f"Product '{producer['Name']}' created successfully!")

        return new_producer

    def get_producer(self, producer_id: int):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        producer = session.query(Producer).get(producer_id)

        session.close()

        return producer

    def get_producers(self):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        res_producers = session.query(Producer).all()
        session.close()

        return res_producers

    def update_producer(self, producer_id: int, new_producer):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        producer = session.query(Producer).get(producer_id)
        if producer:
            producer.ProducerName = new_producer['Name']
            producer.ProducerLocation = new_producer['Location']
            session.commit()
            session.refresh(producer)

        session.close()
        return producer

    def delete_producer(self, producer_id: int):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        producer = session.query(Producer).get(producer_id)
        if producer:
            session.delete(producer)
            session.commit()
            session.refresh(producer)

        session.close()
        return producer
