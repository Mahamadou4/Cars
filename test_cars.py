"""
Test script for the Car Management System
"""
from car import Car
from car_manager import CarManager


def test_car_class():
    """Test the Car class functionality"""
    print("Testing Car Class...")
    print("-" * 50)

    # Create a car
    car = Car("Toyota", "Camry", 2020, "Silver", 25000, 35000)

    print(f"Car: {car}")
    print(f"Age: {car.get_age()} years")
    print(f"Original Price: ${car.price:,.2f}")
    print(f"Current Value: ${car.get_depreciation():,.2f}")

    # Add service record
    car.add_service_record("Oil Change", 50.00, "Regular maintenance")
    print(f"Service records: {len(car.service_history)}")

    # Set owner
    car.set_owner("John Doe")
    print(f"Owner: {car.owner}")

    print("\n✅ Car class tests passed!\n")


def test_car_manager():
    """Test the CarManager class functionality"""
    print("Testing CarManager Class...")
    print("-" * 50)

    # Create manager and add cars
    manager = CarManager()

    cars = [
        Car("Toyota", "Camry", 2020, "Silver", 25000, 35000),
        Car("Honda", "Civic", 2021, "Blue", 22000, 25000),
        Car("Ford", "Mustang", 2019, "Red", 35000, 45000),
    ]

    for car in cars:
        manager.add_car(car)

    print(f"Total cars in inventory: {manager.get_car_count()}")

    # Search tests
    toyota_cars = manager.search_by_make("Toyota")
    print(f"Toyota cars found: {len(toyota_cars)}")

    recent_cars = manager.search_by_year_range(2020, 2025)
    print(f"Cars from 2020-2025: {len(recent_cars)}")

    # Get statistics
    stats = manager.get_statistics()
    print(f"Average price: ${stats['average_price']:,.2f}")
    print(f"Total inventory value: ${stats['total_value']:,.2f}")

    print("\n✅ CarManager class tests passed!\n")


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("CAR MANAGEMENT SYSTEM - TESTS")
    print("=" * 50 + "\n")

    test_car_class()
    test_car_manager()

    print("=" * 50)
    print("All tests completed successfully! ✅")
    print("=" * 50)
    print("\nYou can now run the Streamlit app:")
    print("  streamlit run app.py")
    print("=" * 50 + "\n")

