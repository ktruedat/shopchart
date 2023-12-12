from api.controller.customer import CustomerController
from api.controller.producer import ProducerController
from api.controller.sale import SaleController
from api.controller.promotion import PromotionController
from api.controller.product import ProductController


class EntityController:
    def __init__(self, customer_controller: CustomerController, producer_controller: ProducerController, sale_controller: SaleController, promotion_controller: PromotionController, product_controller: ProductController):
        self.customer_controller = customer_controller
        self.producer_controller = producer_controller
        self.sale_controller = sale_controller
        self.promotion_controller = promotion_controller
        self.product_controller = product_controller
