from sqlalchemy import UUID, DateTime, String, Table, Column, MetaData

metaData = MetaData()

#Таблица задач 
tickets = Table (
    "tickets",
    metaData,
    Column("id", UUID, primary_key=True),
    Column("source_system", String, nullable=False),
    Column("name", String, nullable=False),
    Column("status", String, nullable=False), 
    Column("timeCreate", DateTime, nullable=False),
    Column("timeToResolve", DateTime, nullable=False)
)

