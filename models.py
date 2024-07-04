## rfile add Thursday, May 16, 2024 12:41:04 PM EDT
## https://realpython.com/python-sqlite-sqlalchemy/#working-with-sqlalchemy-and-python-objects
## 5-20-24 added sqlmodel
from typing import Optional
from decimal import Decimal
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa


class SugarTable(SQLModel, table=True):
    bsid: Optional[int] = Field(default=None, primary_key=True)
    bsdate: str
    bsugar: int
    ketone: Decimal = Field(default=0.01, max_digits=5, decimal_places=2)
    comment : str
class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    money: Decimal = Field(default=0, max_digits=5, decimal_places=3)
        

Base = declarative_base()


def qtsugar_table(self):
    metadata = sa.MetaData
    qtsugar = sa.Table(
        'qtsugar',
        Base.metadata,
        sa.Column('bsid', sa.Integer, autoincrement=True, primary_key=True),
        sa.Column('bsdate', sa.String),
        sa.Column('bsugar', sa.Integer),
        sa.Column('ketone', sa.Numeric, default=0.01),
        sa.Column('comment', sa.String),

    )
author_publisher = Table(
    "author_publisher",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("author.author_id")),
    Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),
)

book_publisher = Table(
    "book_publisher",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("book.book_id")),
    Column("publisher_id", Integer, ForeignKey("publisher.publisher_id")),
)
