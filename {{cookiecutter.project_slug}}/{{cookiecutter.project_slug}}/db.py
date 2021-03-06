from sqlalchemy import Column, BigInteger, DateTime
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import CreateColumn
from sqlalchemy.sql import expression
from sqlalchemy.types import DateTime as DatetimeType

Base = declarative_base()


class utcnow(expression.FunctionElement):
    type = DatetimeType()


@compiles(utcnow, "postgresql")
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


@compiles(CreateColumn, 'postgresql')
def use_identity(element, compiler, **kw):
    text = compiler.visit_create_column(element, **kw)
    text = text.replace("SERIAL", "INT GENERATED BY DEFAULT AS IDENTITY")
    return text


class DBMixin:
    id = Column(BigInteger, primary_key=True)
    created_date = Column(DateTime(timezone=True), server_default=utcnow())
    modified_date = Column(
        DateTime(timezone=True), server_default=utcnow(), onupdate=utcnow()
    )
