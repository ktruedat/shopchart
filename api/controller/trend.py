from abc import ABC, abstractmethod


class ITrendsRepository(ABC):

    @abstractmethod
    def get_total_sales(self, start_date, end_date):
        pass


class TrendController:
    def __init__(self, trend_repository: ITrendsRepository):
        self.trend_repository = trend_repository

    def generate_trends(self):
        self.trend_repository.generate_trends()
