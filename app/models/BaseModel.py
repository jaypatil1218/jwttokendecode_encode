import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, func, Uuid
from app.configs.Database import Engine

# Base Entity Model Schema
EntityMeta = declarative_base()


class BaseModel(EntityMeta):
    __abstract__ = True

    id = Column(
        Uuid(as_uuid=True),
        primary_key=True,
        unique=True,
        nullable=False,
        default=uuid.uuid4,
    )
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


def init():
    EntityMeta.metadata.create_all(bind=Engine)
