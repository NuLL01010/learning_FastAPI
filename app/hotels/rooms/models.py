from sqlalchemy import JSON, Column, ForeignKey, Integer, String

from sqlalchemy.orm import relationship
from app.database import Base


class Rooms(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, nullable=False)
    hotel_id = Column(Integer, ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=False)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)


    hotel = relationship("Hotels", back_populates="room")
    booking = relationship("Bookings", back_populates="room")



    def __str__(self) -> str:
        return f"Room {self.name}"
