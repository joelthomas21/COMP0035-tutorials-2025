from sqlmodel import SQLModel, create_engine
from models import *  # this MUST stay so metadata sees your models

engine = create_engine("sqlite:///paralympics_sqlmodel.db", echo=True)


def create_db_and_tables() -> None:
    # Debug: print what tables SQLModel thinks exist in metadata
    print("Metadata tables BEFORE create_all:", SQLModel.metadata.tables.keys())
    SQLModel.metadata.create_all(engine)
    print("Metadata tables AFTER create_all:", SQLModel.metadata.tables.keys())
