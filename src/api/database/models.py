from database.config import Base
from sqlalchemy import TIMESTAMP, Column, INT, String, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(INT, primary_key=True, unique=True, nullable=False)
    username = Column(String,  nullable=False)
    full_name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    modified_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
