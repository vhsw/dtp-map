import json
from datetime import datetime

from sqlalchemy.orm import sessionmaker
from tqdm import tqdm

from database import engine
from bindings import Base, DTP

if input("Drop existing DB? [y/N] ").lower() == "y":
    Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def parse_float(data: str):
    try:
        return float(data)
    except ValueError:
        return float("NaN")


def create_db():
    with open("data/dtp.json") as fp:
        for line in tqdm(fp, total=678269):  # TODO aprox size
            line = line.rstrip(",\n")
            if line in "[]":
                continue
            data = json.loads(line)
            dt_string = data["date"] + " " + data["Time"]
            date_time = datetime.strptime(dt_string, r"%d.%m.%Y %H:%M")

            dtp = DTP(
                kart_id=data["KartId"],
                date_time=date_time,
                description=data["DTP_V"],
                latitude=parse_float(data["infoDtp"]["COORD_W"]),
                longitude=parse_float(data["infoDtp"]["COORD_L"]),
                area_name=data["area_name"],
                parent_region_name=data["parent_region_name"],
                parent_region_code=data["parent_region_code"],
                oktmo_code=data["oktmo_code"],
                city=data["infoDtp"]["n_p"],
            )
            session.add(dtp)
        session.commit()


if __name__ == "__main__":
    create_db()
