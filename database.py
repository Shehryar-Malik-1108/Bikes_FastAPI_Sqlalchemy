from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Bike(Base):
    __tablename__ = "bikes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cc = Column(Integer, nullable=False)
    color = Column(String, nullable=False)
    price = Column(Integer, nullable=False)


class MyDatabase:
    def __init__(self):
        self.engine = create_engine("sqlite:///my_db.db")
        Base.metadata.create_all(bind=self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def select_bike(self, id: int):
        bike = self.session.query(Bike).filter_by(id=id).first()
        if bike:
            return {
                "id": bike.id,
                "name": bike.name,
                "cc": bike.cc,
                "color": bike.color,
                "price": bike.price
            }
        else:
            return None

    def get_all_bikes(self):
        bikes = self.session.query(Bike).all()
        return {"bikes": [{"id": bike.id, "name": bike.name, "cc": bike.cc, "color": bike.color, "price": bike.price}
                          for bike in bikes]}

    def insert_bike(self, id: int, name: str, cc: int, color: str, price: int):
        bike = Bike(id=id, name=name, cc=cc, color=color, price=price)
        self.session.add(bike)
        self.session.commit()
        return f"Bike {name} created successfully"

    def update_bike(self, id: int, price: int):
        bike = self.session.query(Bike).filter_by(id=id).first()
        if bike:
            bike.price = price
            self.session.commit()
            return f"id {id} updated."
        else:
            return f"Error occurred while updating {id}."

    def delete_bike(self, id: int):
        bike = self.session.query(Bike).filter_by(id=id).first()
        if bike:
            self.session.delete(bike)
            self.session.commit()
            return f"id {id} deleted."
        else:
            return "Error occurred while deleting bike."


if __name__ == "__main__":
    pass
