from abc import ABC, abstractmethod

from api.models import Sale


class ISaleRepository(ABC):

    @abstractmethod
    def add_sale(self, sale: Sale):
        pass

    @abstractmethod
    def get_sale(self, sale_id: int):
        pass

    @abstractmethod
    def get_sales(self):
        pass

    @abstractmethod
    def update_sale(self, sale_id: int, sale: Sale):
        pass

    @abstractmethod
    def delete_sale(self, sale_id: int):
        pass

class SaleController:
    def __init__(self, sale_repository: ISaleRepository):
        self.sale_repository = sale_repository

    def add_sale(self, sale):
        new_sale = Sale(
            SaleID=None,
            ProductID=sale['ProductID'],
            CustomerID=sale['CustomerID'],
            Quantity=sale['Quantity'],
            Amount=sale['Amount'],
            PromotionID=sale['PromotionID'],
            Date=sale['Date']
        )
        return self.sale_repository.add_sale(new_sale)

    def get_sale(self, sale_id: int):
        return self.sale_repository.get_sale(sale_id)

    def get_sales(self):
        return self.sale_repository.get_sales()

    def update_sale(self, sale_id: int, sale):
        new_sale = Sale(
            SaleID=None,
            ProductID=sale['ProductID'],
            CustomerID=sale['CustomerID'],
            Quantity=sale['Quantity'],
            Amount=sale['Amount'],
            PromotionID=sale['PromotionID'],
            Date=sale['Date']
        )
        return self.sale_repository.update_sale(sale_id, new_sale)

    def delete_sale(self, sale_id: int):
        return self.sale_repository.delete_sale(sale_id)

