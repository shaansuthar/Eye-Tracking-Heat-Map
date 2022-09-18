import numpy as np
from sqlalchemy import ARRAY, Column, Integer, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Recordings(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'recordings'
    id = Column(UUID(as_uuid=True), primary_key=True)
    recording = Column(JSON)
