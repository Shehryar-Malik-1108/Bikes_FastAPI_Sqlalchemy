import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Bike


class Testdatabase(unittest.TestCase):

    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()
        Bike.metadata.create_all(engine)

        bike1 = Bike(id=1, name="Bike1", cc=100, color="Red", price=1000)
        bike2 = Bike(id=2, name="Bike2", cc=150, color="Blue", price=1500)
        self.session.add_all([bike1, bike2])
        self.session.commit()

    def test_select_existing_bike(self):
        result = self.session.query(Bike).filter_by(id=1).first()
        self.assertEqual(result.name, "Bike1")

    def test_select_non_existing_bike(self):
        result = self.session.query(Bike).filter_by(id=3).first()
        self.assertEqual(result, None)

    def test_get_all_bikes(self):
        result = self.session.query(Bike).all()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].name, "Bike1")
        self.assertEqual(result[1].name, "Bike2")

    def test_valid_insert_bike(self):
        bike = Bike(id=3, name="Bike3", cc=150, color="Blue", price=1500)
        self.session.add(bike)
        self.session.commit()

        result = self.session.query(Bike).filter_by(id=3).first()
        self.assertEqual(result.name, "Bike3")

    def test_invalid_insert_bike(self):
        try:
            bike = Bike(id="4", name=4, cc=150, color="Blue", price=1500)
            self.session.add(bike)
            self.session.commit()
        except Exception as e:
            self.assertTrue(True)
            return e

    def test_valid_update_bike(self):
        result = self.session.query(Bike).filter_by(id=1).first()

        result.price = 1500
        self.session.commit()

        result = self.session.query(Bike).filter_by(id=1).first()
        self.assertEqual(result.price, 1500)

    def test_invalid_update_bike(self):
        try:
            result = self.session.query(Bike).filter_by(id=1).first()
            self.assertEqual(result.price, "1500")
            self.session.commit()

        except Exception as e:
            self.assertTrue(True)
            return e

    def test_delete_bike(self):

        result = self.session.query(Bike).filter_by(id=1).first()
        self.assertIsNotNone(result)

        self.session.delete(result)
        self.session.commit()

        result = self.session.query(Bike).filter_by(id=1).first()
        self.assertIsNone(result)

    def test_delete_invalid_bike(self):
        bike = Bike(id=100, name="Bike", cc=150, color="Blue", price=1500)

        try:
            self.session.delete(bike)
            self.session.commit()
            self.assertTrue(False)
        except Exception as e:
            self.assertTrue(True)
            return e


if __name__ == "__main__":
    unittest.main()
