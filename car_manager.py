"""
Car Manager module for managing a collection of cars
"""
import json
from typing import List
from car import Car


class CarManager:
    """Class for managing a collection of cars"""

    def __init__(self):
        """Initialize CarManager with an empty inventory"""
        self.inventory: List[Car] = []

    def add_car(self, car: Car) -> None:
        """
        Add a car to the inventory

        Args:
            car: Car object to add
        """
        self.inventory.append(car)

    def remove_car(self, make: str, model: str, year: int) -> bool:
        """
        Remove a car from the inventory

        Args:
            make: Car manufacturer
            model: Car model
            year: Year of manufacture

        Returns:
            True if car was removed, False otherwise
        """
        for i, car in enumerate(self.inventory):
            if car.make == make and car.model == model and car.year == year:
                self.inventory.pop(i)
                return True
        return False

    def get_all_cars(self) -> List[Car]:
        """Get all cars in the inventory"""
        return self.inventory

    def search_by_make(self, make: str) -> List[Car]:
        """Search cars by manufacturer"""
        return [car for car in self.inventory if car.make.lower() == make.lower()]

    def search_by_model(self, model: str) -> List[Car]:
        """Search cars by model"""
        return [car for car in self.inventory if car.model.lower() == model.lower()]

    def search_by_year_range(self, min_year: int, max_year: int) -> List[Car]:
        """Search cars within a year range"""
        return [car for car in self.inventory if min_year <= car.year <= max_year]

    def search_by_price_range(self, min_price: float, max_price: float) -> List[Car]:
        """Search cars within a price range"""
        return [car for car in self.inventory if min_price <= car.price <= max_price]

    def get_total_inventory_value(self) -> float:
        """Calculate total value of all cars in inventory"""
        return sum(car.price for car in self.inventory)

    def get_average_price(self) -> float:
        """Calculate average price of cars in inventory"""
        if not self.inventory:
            return 0.0
        return self.get_total_inventory_value() / len(self.inventory)

    def get_statistics(self) -> dict:
        """Get statistics about the car inventory"""
        if not self.inventory:
            return {
                'total_cars': 0,
                'total_value': 0.0,
                'average_price': 0.0,
                'average_age': 0.0,
                'average_mileage': 0.0
            }

        return {
            'total_cars': len(self.inventory),
            'total_value': round(self.get_total_inventory_value(), 2),
            'average_price': round(self.get_average_price(), 2),
            'average_age': round(sum(car.get_age() for car in self.inventory) / len(self.inventory), 1),
            'average_mileage': round(sum(car.mileage for car in self.inventory) / len(self.inventory), 1),
            'makes': list(set(car.make for car in self.inventory)),
            'colors': list(set(car.color for car in self.inventory))
        }

    def sort_by_price(self, ascending: bool = True) -> List[Car]:
        """Sort cars by price"""
        return sorted(self.inventory, key=lambda car: car.price, reverse=not ascending)

    def sort_by_year(self, ascending: bool = True) -> List[Car]:
        """Sort cars by year"""
        return sorted(self.inventory, key=lambda car: car.year, reverse=not ascending)

    def sort_by_mileage(self, ascending: bool = True) -> List[Car]:
        """Sort cars by mileage"""
        return sorted(self.inventory, key=lambda car: car.mileage, reverse=not ascending)

    def export_to_json(self, filename: str) -> None:
        """
        Export inventory to JSON file

        Args:
            filename: Name of the file to export to
        """
        data = [car.to_dict() for car in self.inventory]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def get_car_count(self) -> int:
        """Get the total number of cars in inventory"""
        return len(self.inventory)

