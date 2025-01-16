from sqlalchemy.orm import Session
from typing import List, Optional
from models import Address, City

class AddressRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_address_by_id(self, address_id: int) -> Optional[Address]:
        """
        Fetch an address by its ID.
        """
        return self.session.query(Address).filter(Address.id_address == address_id).one_or_none()

    def get_addresses_by_city(self, city_name: str) -> List[Address]:
        """
        Fetch all addresses in a specific city by the city's name.
        """
        return (
            self.session.query(Address)
            .join(City)
            .filter(City.name == city_name)
            .all()
        )

    def add_address(self, address: Address) -> Address:
        """
        Add a new address to the database.
        """
        self.session.add(address)
        self.session.commit()
        return address

    def update_address(self, address: Address) -> Address:
        """
        Update an existing address in the database.
        """
        self.session.merge(address)
        self.session.commit()
        return address

    def delete_address(self, address_id: int) -> bool:
        """
        Delete an address by its ID.
        """
        address = self.get_address_by_id(address_id)
        if address:
            self.session.delete(address)
            self.session.commit()
            return True
        return False

    def get_addresses_by_postal_code(self, postal_code: str) -> List[Address]:
        """
        Fetch all addresses with a specific postal code.
        """
        return self.session.query(Address).filter(Address.postal_code == postal_code).all()

    def get_users_by_address(self, address_id: int) -> List:
        """
        Fetch all users associated with a specific address.
        """
        address = self.get_address_by_id(address_id)
        return address.users if address else []