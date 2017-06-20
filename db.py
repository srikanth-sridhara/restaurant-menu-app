from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    """ Restaurant Table """
    __tablename__ = 'restaurant'
    name = Column(String(80), nullable = False)
    address = Column(String(200))
    category = Column(String(50))

    id = Column(Integer, primary_key = True)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'address': self.address,
            'id': self.id,
            'category': self.category,
        }

class MenuItem(Base):
    """ Menu Item Table """
    __tablename__ = 'menu_item'
    name = Column(String(80), nullable = False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))

    id = Column(Integer, primary_key = True)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
