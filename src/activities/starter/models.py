from datetime import date

from sqlmodel import Field, SQLModel


class Games(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str = Field()
    year: int
    start: date
    end: date
    countries: int
    events: int
    sports: int
    participants_m: int
    participants_f: int
    participants: int
    highlights: str
    URL: str

class Country(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    country: str = Field(index=True)


class Disability(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str


class Team(SQLModel, table=True):
    code: str = Field(primary_key=True)
    name: str
    region: str
    sub_region: str
    member_type: str
    notes: str | None = None
    country_id: int | None = Field(default=None, foreign_key="country.id")


