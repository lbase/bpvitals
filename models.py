## rfile add Thursday, May 16, 2024 12:41:04 PM EDT
## https://realpython.com/python-sqlite-sqlalchemy/#working-with-sqlalchemy-and-python-objects
## 5-20-24 added sqlmodel
from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa


class qt_sugar(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

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
