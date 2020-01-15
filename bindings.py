from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DTP(Base):
    __tablename__ = "DTP"
    kart_id = Column(Integer, primary_key=True)
    date_time = Column(DateTime)
    latitude = Column(Float)
    longitude = Column(Float)
    description = Column(String)
    weather_cond = Column(Integer)
    parent_region_name = Column(String)
    parent_region_code = Column(String)
    area_name = Column(String)
    oktmo_code = Column(String)
    city = Column(String)

    num_cars = Column(Integer)
    num_participants = Column(Integer)
    street = Column(String)
    house = Column(String)
    dor = Column(String)
    km = Column(String)
    m = Column(String)
    k_ul = Column(String)
    dor_k = Column(String)
    dor_z = Column(String)
    s_pch = Column(String)
    osv = Column(String)
    change_org_motion = Column(String)
    s_dtp = Column(String)

    def __repr__(self):
        return f"DTP({self.kart_id}, {self.district}, {self.date_time})"
