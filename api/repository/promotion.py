from sqlalchemy.orm import sessionmaker
from api.controller.promotion import IPromotionRepository
from api.models import *
from dbconnection import create_connection

engine = create_connection()


class PromotionRepository(IPromotionRepository):

    def add_promotion(self, promotion: Promotion):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        session.add(promotion)
        session.commit()
        session.refresh(promotion)
        session.close()

        print(f"Product '{promotion.PromotionName}' created successfully!")

        return promotion

    def get_promotion(self, promotion_id: int):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        promotion = session.query(Promotion).get(promotion_id)

        session.close()

        return promotion

    def get_promotions(self):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        res_promotions = session.query(Promotion).all()

        session.close()

        return res_promotions

    def update_promotion(self, promotion_id: int, new_promotion: Promotion):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        promotion = session.query(Promotion).get(promotion_id)
        if promotion:
            promotion.PromotionName = new_promotion.PromotionName
            promotion.DiscountPercentage = new_promotion.DiscountPercentage
            promotion.StartDate = new_promotion.StartDate
            promotion.EndDate = new_promotion.EndDate
            session.refresh(promotion)
            session.commit()

        session.close()
        return promotion

    def delete_promotion(self, promotion_id: int):
        Base.metadata.bind = engine
        Session = sessionmaker(bind=engine)
        session = Session()

        promotion = session.query(Promotion).get(promotion_id)
        if promotion:
            session.delete(promotion)
            session.refresh(promotion)
            session.commit()

        session.close()
        return promotion

