from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP
from datetime import datetime

metadata = MetaData()

task = Table(
    "task",
    metadata, 
    Column("id", Integer, primary_key=True),
    Column("head", String),
    Column("body", String),
    Column("created_at", TIMESTAMP, default=datetime.utcnow)
)