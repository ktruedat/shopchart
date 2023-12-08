from abc import ABC, abstractmethod
from api.models import Promotion


class IPromotionRepository(ABC):

    @abstractmethod
    def add_promotion(self, promotion: Promotion):
        pass

    @abstractmethod
    def get_promotion(self, promotion_id: int):
        pass

    @abstractmethod
    def get_promotions(self):
        pass

    @abstractmethod
    def update_promotion(self, promotion_id: int, new_promotion: Promotion):
        pass

    @abstractmethod
    def delete_promotion(self, promotion_id: int):
        pass


class PromotionController:
    def __init__(self, promotion_repository: IPromotionRepository):
        self.promotion_repository = promotion_repository

    def add_promotion(self, promotion):
        new_promotion = Promotion(

        )
