from abc import ABC, abstractmethod


class IProducerRepository(ABC):

    @abstractmethod
    def add_producer(self, producer):
        pass

    @abstractmethod
    def get_producer(self, producer_id: int):
        pass

    def get_producers(self):
        pass

    @abstractmethod
    def update_producer(self, producer_id: int, new_producer):
        pass

    @abstractmethod
    def delete_producer(self, producer_id: int):
        pass


class ProducerController:
    def __init__(self, producer_repository: IProducerRepository):
        self.producer_repository = producer_repository

    def add_producer(self, producer):
        return self.producer_repository.add_producer(producer)

    def get_producer(self, producer_id: int):
        return self.producer_repository.get_producer(producer_id)

    def get_producers(self):
        return self.producer_repository.get_producers()

    def update_producer(self, producer_id: int, new_producer):
        return self.producer_repository.update_producer(producer_id, new_producer)

    def delete_producer(self, producer_id: int):
        return self.producer_repository.delete_producer(producer_id)