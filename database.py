from sqlalchemy import create_engine

DB_PATH = "data/db.sqlite"
engine = create_engine(f"sqlite:///{DB_PATH}")
