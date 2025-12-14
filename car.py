"""
Car class module for managing car objects
"""
from datetime import datetime
from typing import Optional


class Car:
    """Class representing a car with various attributes and methods"""

    def __init__(self, make: str, model: str, year: int, color: str,
                 price: float, mileage: float = 0.0):
        """
        Initialize a Car object

        Args:
            make: Car manufacturer (e.g., 'Toyota', 'Honda')
            model: Car model (e.g., 'Camry', 'Civic')
            year: Year of manufacture
            color: Car color
            price: Car price in dollars
            mileage: Current mileage in miles (default: 0.0)
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.mileage = mileage
        self.owner: Optional[str] = None
        self.service_history = []

    def __str__(self) -> str:
        """String representation of the car"""
        return f"{self.year} {self.make} {self.model} ({self.color})"

    def __repr__(self) -> str:
        """Detailed representation of the car"""
        return (f"Car(make='{self.make}', model='{self.model}', year={self.year}, "
                f"color='{self.color}', price={self.price}, mileage={self.mileage})")

    def get_age(self) -> int:
        """Calculate the age of the car"""
        current_year = datetime.now().year
        return current_year - self.year

    def update_mileage(self, new_mileage: float) -> None:
        """
        Update the car's mileage

        Args:
            new_mileage: New mileage value

        Raises:
            ValueError: If new mileage is less than current mileage
        """
        if new_mileage < self.mileage:
            raise ValueError("New mileage cannot be less than current mileage")
        self.mileage = new_mileage

    def add_service_record(self, service_type: str, cost: float,
                          description: str = "") -> None:
        """
        Add a service record to the car's history

        Args:
            service_type: Type of service (e.g., 'Oil Change', 'Tire Rotation')
            cost: Cost of the service
            description: Optional description of the service
        """
        service_record = {
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'type': service_type,
            'cost': cost,
            'description': description,
            'mileage': self.mileage
        }
        self.service_history.append(service_record)

    def set_owner(self, owner_name: str) -> None:
        """Set the owner of the car"""
        self.owner = owner_name

    def get_depreciation(self) -> float:
        """
        Calculate depreciation based on age and mileage
        Rough estimate: 15% per year + 0.05% per 1000 miles
        """
        age_depreciation = self.get_age() * 0.15
        mileage_depreciation = (self.mileage / 1000) * 0.0005
        total_depreciation = min(age_depreciation + mileage_depreciation, 0.9)
        return self.price * (1 - total_depreciation)

    def to_dict(self) -> dict:
        """Convert car object to dictionary"""
        return {
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'color': self.color,
            'price': self.price,
            'mileage': self.mileage,
            'owner': self.owner,
            'age': self.get_age(),
            'current_value': round(self.get_depreciation(), 2),
            'service_history': self.service_history
        }

