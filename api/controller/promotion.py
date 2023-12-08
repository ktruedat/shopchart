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
            PromotionID=None,
            PromotionName=promotion['PromotionName'],
            DiscountPercentage=promotion['DiscountPercentage'],
            StartDate=promotion['StartDate'],
            EndDate=promotion['EndDate'],
        )
        return self.promotion_repository.add_promotion(new_promotion)

    def get_promotion(self, promotion_id: int):
        return self.promotion_repository.get_promotion(promotion_id)

    def get_promotions(self):
        return self.promotion_repository.get_promotions()

    def update_promotion(self, promotion_id: int, promotion):
        new_promotion = Promotion(
            PromotionID=None,
            PromotionName=promotion['PromotionName'],
            DiscountPercentage=promotion['DiscountPercentage'],
            StartDate=promotion['StartDate'],
            EndDate=promotion['EndDate'],
        )
        return self.promotion_repository.update_promotion(promotion_id, new_promotion)

    def delete_promotion(self, promotion_id: int):
        return self.promotion_repository.delete_promotion(promotion_id)
