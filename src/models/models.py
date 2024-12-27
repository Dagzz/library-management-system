from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Text,
    Enum,
    Table,
    UniqueConstraint
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# =========================================================
# Association tables (many-to-many) without own attributes
# =========================================================

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


# ============================================
# Table: city
# ============================================
class City(Base):
    __tablename__ = 'city'

    id_city = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

    # Relation with Address
    addresses = relationship("Address", back_populates="city")

    def __repr__(self):
        return f"<City(id_city={self.id_city}, name='{self.name}')>"


# ============================================
# Table: address
# ============================================
class Address(Base):
    __tablename__ = 'address'

    id_address = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(10), nullable=False)
    street = Column(String(50), nullable=False)
    postal_code = Column(String(15), nullable=False)
    id_city = Column(Integer, ForeignKey('city.id_city'), nullable=False)

    # Relation with City
    city = relationship("City", back_populates="addresses")

    # Reverse relation with User
    users = relationship("User", back_populates="address")

    def __repr__(self):
        return (
            f"<Address(id_address={self.id_address}, number='{self.number}', "
            f"street='{self.street}', postal_code='{self.postal_code}')>"
        )


# ============================================
# Table: user
# ============================================
class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        UniqueConstraint('login', name='user_AK'),
        # Index('user_Idx', 'last_name', 'mail'),  # Optional
    )

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    phone = Column(String(15), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    last_connection_date = Column(DateTime, nullable=False)
    is_active = Column(Boolean, nullable=False)
    login = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    mail = Column(String(254), nullable=False)
    id_address = Column(Integer, ForeignKey('address.id_address'))

    # Relation with Address
    address = relationship("Address", back_populates="users")

    # Relations many-to-many avec Role (via user_role_table)
    roles = relationship(
        "Role",
        secondary=user_role_table,
        back_populates="users"
    )

    # Relation one-to-many with Loan
    loans = relationship("Loan", back_populates="user")

    # Relation one-to-many with Reservation
    reservations = relationship("Reservation", back_populates="user")

    # Relation one-to-many with Modification
    modifications = relationship("Modification", back_populates="user")

    def __repr__(self):
        return f"<User(id_user={self.id_user}, login='{self.login}')>"


# ============================================
# Table: role
# ============================================
class Role(Base):
    __tablename__ = 'role'
    __table_args__ = (
        UniqueConstraint('role_name', name='role_AK'),
    )

    id_role = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text, nullable=False)
    role_name = Column(String(50), nullable=False)

    # Relation many-to-many with User
    users = relationship(
        "User",
        secondary=user_role_table,
        back_populates="roles"
    )

    def __repr__(self):
        return f"<Role(id_role={self.id_role}, role_name='{self.role_name}')>"


# ============================================
# Table: language
# ============================================
class Language(Base):
    __tablename__ = 'language'

    id_language = Column(Integer, primary_key=True, autoincrement=True)
    language_name = Column(String(50), nullable=False)

    # Relation one-to-many with Book
    books = relationship("Book", back_populates="language")

    def __repr__(self):
        return f"<Language(id_language={self.id_language}, language_name='{self.language_name}')>"


# ============================================
# Table: collection
# ============================================
class Collection(Base):
    __tablename__ = 'collection'
    __table_args__ = (
        UniqueConstraint('collection_name', name='collection_AK'),
    )

    id_collection = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text, nullable=False)
    collection_name = Column(String(50), nullable=False)

    # Relation one-to-many with Book
    books = relationship("Book", back_populates="collection")

    def __repr__(self):
        return f"<Collection(id_collection={self.id_collection}, collection_name='{self.collection_name}')>"


# ============================================
# Table: author
# ============================================
class Author(Base):
    __tablename__ = 'author'

    id_author = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    bio = Column(Text, nullable=False)

    # Relation many-to-many with Book (via writes_table)
    books = relationship("Book", secondary=writes_table, back_populates="authors")

    def __repr__(self):
        return f"<Author(id_author={self.id_author}, name='{self.first_name} {self.last_name}')>"


# ============================================
# Table: genre
# ============================================
class Genre(Base):
    __tablename__ = 'genre'
    __table_args__ = (
        UniqueConstraint('name_genre', name='genre_AK'),
    )

    id_genre = Column(Integer, primary_key=True, autoincrement=True)
    name_genre = Column(String(100), nullable=False)

    # Relation many-to-many with Book (via genre_book_table)
    books = relationship("Book", secondary=genre_book_table, back_populates="genres")

    def __repr__(self):
        return f"<Genre(id_genre={self.id_genre}, name_genre='{self.name_genre}')>"


# ============================================
# Table: book
# ============================================
class Book(Base):
    __tablename__ = 'book'

    id_book = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    publication_date = Column(DateTime)
    status = Column(
        Enum("available", "borrowed", "reserved", name="status_enum"),
        nullable=False
    )
    aspect = Column(
        Enum("new", "good", "damaged", name="aspect_enum"),
        nullable=False
    )
    isbn = Column(String(17), nullable=False)
    page_number = Column(Integer, nullable=False)
    editor = Column(String(255), nullable=False)
    resume = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime)
    id_collection = Column(Integer, ForeignKey('collection.id_collection'), nullable=False)
    id_language = Column(Integer, ForeignKey('language.id_language'), nullable=False)

    # Relation many-to-many with Author
    authors = relationship("Author", secondary=writes_table, back_populates="books")

    # Relation many-to-many with Genre
    genres = relationship("Genre", secondary=genre_book_table, back_populates="books")

    # Relation with Collection
    collection = relationship("Collection", back_populates="books")

    # Relation with Language
    language = relationship("Language", back_populates="books")

    # Reverse Relation (loans, reservations, modifications)
    loans = relationship("Loan", back_populates="book")
    reservations = relationship("Reservation", back_populates="book")
    modifications = relationship("Modification", back_populates="book")

    def __repr__(self):
        return f"<Book(id_book={self.id_book}, title='{self.title}')>"


# ============================================
# Table: loan
# ============================================
class Loan(Base):
    __tablename__ = 'loan'

    id_loan = Column(Integer, primary_key=True, autoincrement=True)
    date_loan = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    id_book = Column(Integer, ForeignKey('book.id_book'), nullable=False)

    # Relations
    user = relationship("User", back_populates="loans")
    book = relationship("Book", back_populates="loans")

    def __repr__(self):
        return f"<Loan(id_loan={self.id_loan}, date_loan={self.date_loan}, return_date={self.return_date})>"


# ============================================
# Table: reservation
# ============================================
class Reservation(Base):
    __tablename__ = 'reservation'
    __table_args__ = (
        # Unique constraints
        UniqueConstraint('id_user', name='reservation_user_AK'),
    )

    id_reservation = Column(Integer, primary_key=True, autoincrement=True)
    reservation_date = Column(DateTime, nullable=False)
    is_confirmed = Column(Boolean, nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    id_book = Column(Integer, ForeignKey('book.id_book'), nullable=False)

    # Relations
    user = relationship("User", back_populates="reservations")
    book = relationship("Book", back_populates="reservations")

    def __repr__(self):
        return f"<Reservation(id_reservation={self.id_reservation}, is_confirmed={self.is_confirmed})>"


# ============================================
# Table: modification
# ============================================
class Modification(Base):
    __tablename__ = 'modification'

    id_modif = Column(Integer, primary_key=True, autoincrement=True)
    date_modification = Column(DateTime, nullable=False)
    id_book = Column(Integer, ForeignKey('book.id_book'), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)

    # Relations
    book = relationship("Book", back_populates="modifications")
    user = relationship("User", back_populates="modifications")

    def __repr__(self):
        return f"<Modification(id_modif={self.id_modif}, date_modification={self.date_modification})>"
