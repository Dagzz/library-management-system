# =========================================================
# Association tables (many-to-many) without own attributes
# =========================================================

from sqlalchemy import Table, Column, Integer, ForeignKey
from .base import Base

writes_table = Table(
    'writes',
    Base.metadata,
    Column('id_author', Integer, ForeignKey('author.id_author'), primary_key=True),
    Column('id_book', Integer, ForeignKey('book.id_book'), primary_key=True)
)

genre_book_table = Table(
    'genre_book',
    Base.metadata,
    Column('id_genre', Integer, ForeignKey('genre.id_genre'), primary_key=True),
    Column('id_book', Integer, ForeignKey('book.id_book'), primary_key=True)
)

user_role_table = Table(
    'user_role',
    Base.metadata,
    Column('id_user', Integer, ForeignKey('user.id_user'), primary_key=True),
    Column('id_role', Integer, ForeignKey('role.id_role'), primary_key=True)
)
