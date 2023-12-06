from abc import ABC, abstractmethod


class IProductRepository(ABC):
    @abstractmethod
    def get_product(self, product_id: int):
        pass

    @abstractmethod
    def add_product(self, product):
        pass

    @abstractmethod
    def update_product(self, product_id: int, updated_product):
        pass

    @abstractmethod
    def delete_product(self, product_id: int):
        pass


class ProductController:
    def __init__(self, product_repository: IProductRepository):
        self.product_repository = product_repository

    def add_product(self, product):
        return self.product_repository.add_product(product)

    def get_product(self, product_id: int):
        return self.product_repository.get_product(product_id)

    def update_product(self, product_id, updated_product):
        return self.product_repository.update_product(product_id, updated_product)

    def delete_product(self, product_id):
        return self.product_repository.delete_product(product_id)
