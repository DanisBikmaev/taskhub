from datetime import datetime
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, JSON, Boolean, ForeignKey
from uuid import UUID

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column("email", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False,  nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)
