"""
CityRepository

Handles database operations related to the `City` model.

Responsibilities:
- Managing city-related data.
- Fetching city records by ID or name.
- Querying cities based on specific criteria.
- Creating, updating, or deleting city records.

Usage:
- Initialize with a session factory:
    repo = CityRepository(get_session)
- Use the provided methods to interact with the database for city-related operations.
"""

from sqlalchemy.orm import Session
from typing import List, Optional
from src.core.models import City, Address

class CityRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_city_by_id(self, city_id: int) -> Optional[City]:
        """
        Fetch a city by its ID.
        """
        return self.session.query(City).filter(City.id_city == city_id).one_or_none()

    def get_city_by_name(self, name: str) -> Optional[City]:
        """
        Fetch a city by its name (case insensitive).
        """
        return self.session.query(City).filter(City.name.ilike(f"%{name}%")).one_or_none()

    def get_all_cities(self) -> List[City]:
        """
        Fetch all cities in the database.
        """
        return self.session.query(City).all()

    def get_addresses_in_city(self, city_id: int) -> List[Address]:
        """
        Fetch all addresses associated with a specific city.
        """
        city = self.get_city_by_id(city_id)
        return city.addresses if city else []

    def add_city(self, city: City) -> City:
        """
        Add a new city to the database.
        """
        self.session.add(city)
        self.session.commit()
        return city

    def update_city(self, city: City) -> City:
        """
        Update an existing city's details.
        """
        self.session.merge(city)
        self.session.commit()
        return city

    def delete_city(self, city_id: int) -> bool:
        """
        Delete a city by its ID.
        """
        city = self.get_city_by_id(city_id)
        if city:
            self.session.delete(city)
            self.session.commit()
            return True
        return False
