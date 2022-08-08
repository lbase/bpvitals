import sys
from icecream import ic
from sqlalchemy.orm import sessionmaker
from PyQt5.QtCore import QSettings
from sqlalchemy.pool import StaticPool
from dataclasses import dataclass
from dataclasses import field
from typing import List
from sqlalchemy import column
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

mapper_reg = registry()


@mapper_reg.mapped
@dataclass
class foodnotes:
    __table__ = Table(
        "foodnotes",
        column("bpid"),
        column("bpsys"),
        column("bpdate"),
        column("bpdia"),
        column("bphr"),
        column("bpsugar"),
        column("bpoxy"),
        column("bpcomment"),
    )


@mapper_reg.mapped
@dataclass
class fastnotes:
    __table__ = Table(
        "fastnotes",
        column("bpid"),
        column("bpsys"),
        column("bpdate"),
        column("bpdia"),
        column("bphr"),
        column("bpsugar"),
        column("bpoxy"),
        column("bpcomment"),
    )
