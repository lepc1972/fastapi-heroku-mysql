from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine


users = Table("users", meta, Column(
    "id", Integer, primary_key=True), Column(
        "name", String(256)), Column("email", String(255)), Column(
            "password", String(256)))

meta.create_all(engine)
