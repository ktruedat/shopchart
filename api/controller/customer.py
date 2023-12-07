from abc import ABC, abstractmethod


class ICustomerRepository(ABC):

    @abstractmethod
    def add_customer(self, customer):
        pass

    @abstractmethod
    def get_customer(self, customer_id):
        pass

    @abstractmethod
    def get_customers(self):
        pass

    @abstractmethod
    def update_customer(self, customer_id: int, updated_customer):
        pass

    @abstractmethod
    def delete_customer(self, customer_id: int):
        pass


class CustomerController:
    def __init__(self, customer_repository: ICustomerRepository):
        self.customer_repository = customer_repository

    def add_customer(self, customer):
        return self.customer_repository.add_customer(customer)

    def get_customer(self, customer_id: int):
        return self.customer_repository.get_customer(customer_id)

    def get_customers(self):
        return self.customer_repository.get_customers()

    def update_customer(self, customer_id: int, updated_customer):
        return self.customer_repository.update_customer(customer_id, updated_customer)

    def delete_customer(self, customer_id: int):
        return self.customer_repository.delete_customer(customer_id)
