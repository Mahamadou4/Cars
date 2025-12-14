# 🚗 Car Management System

A comprehensive car management system with a Streamlit web interface for managing car inventory, tracking service history, and analyzing car data.

## Features

- **Car Class**: Complete car object with properties like make, model, year, color, price, and mileage
- **Car Manager**: Inventory management system with search, filter, and sort capabilities
- **Streamlit Web App**: Interactive web interface with multiple pages:
  - 📊 Dashboard: Overview of inventory statistics
  - 🚙 Inventory: View and sort all cars
  - ➕ Add Car: Add new cars to inventory
  - 🔍 Search: Search cars by various criteria
  - 📋 Car Details: Detailed view with service history
  - 📈 Analytics: Visual analytics with charts and graphs

## Installation

1. Make sure you have Python 3.8+ installed

2. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/Cars.git
cd Cars
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Deployment to Streamlit Cloud

### Option 1: Quick Deploy from GitHub

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io/)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository, branch (main), and main file (app.py)
   - Click "Deploy"

3. **Your app will be live** at: `https://YOUR_USERNAME-YOUR_REPO_NAME.streamlit.app`

### Option 2: Deploy with Streamlit Cloud Dashboard

1. Visit [share.streamlit.io](https://share.streamlit.io/)
2. Connect your GitHub account
3. Select the repository containing this project
4. Set the main file path to `app.py`
5. Click "Deploy"

The app will automatically install dependencies from `requirements.txt` and start running!

## Usage

### Running the Streamlit App

```bash
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`

### Using the Car Class

```python
from car import Car

# Create a new car
my_car = Car("Toyota", "Camry", 2020, "Silver", 25000, 35000)

# Get car information
print(my_car)  # 2020 Toyota Camry (Silver)
print(f"Age: {my_car.get_age()} years")
print(f"Current value: ${my_car.get_depreciation():.2f}")

# Add service record
my_car.add_service_record("Oil Change", 50.00, "Regular maintenance")

# Update mileage
my_car.update_mileage(40000)
```

### Using the Car Manager

```python
from car_manager import CarManager
from car import Car

# Create manager
manager = CarManager()

# Add cars
car1 = Car("Honda", "Civic", 2021, "Blue", 22000, 25000)
car2 = Car("Ford", "Mustang", 2019, "Red", 35000, 45000)
manager.add_car(car1)
manager.add_car(car2)

# Search and filter
toyota_cars = manager.search_by_make("Toyota")
recent_cars = manager.search_by_year_range(2020, 2025)
affordable_cars = manager.search_by_price_range(0, 30000)

# Get statistics
stats = manager.get_statistics()
print(f"Total cars: {stats['total_cars']}")
print(f"Average price: ${stats['average_price']:.2f}")

# Export data
manager.export_to_json("inventory.json")
```

## Project Structure

```
Cars/
├── car.py              # Car class definition
├── car_manager.py      # Car inventory management
├── app.py             # Streamlit web application
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Features in Detail

### Car Class Features
- Automatic age calculation
- Depreciation estimation based on age and mileage
- Service history tracking
- Owner management
- Mileage updates with validation

### Car Manager Features
- Add/remove cars from inventory
- Search by make, model, year range, or price range
- Sort by price, year, or mileage
- Calculate inventory statistics
- Export data to JSON

### Streamlit App Features
- Interactive dashboard with key metrics
- Sortable inventory table
- Advanced search functionality
- Detailed car information view
- Service history management
- Visual analytics with charts:
  - Price distribution histogram
  - Cars by manufacturer (pie chart)
  - Cars by year (bar chart)
  - Price vs age scatter plot
  - Depreciation comparison

## Sample Data

The app comes pre-loaded with 8 sample cars for demonstration purposes:
- Toyota Camry 2020
- Honda Civic 2021
- Ford Mustang 2019
- Tesla Model 3 2022
- BMW X5 2020
- Chevrolet Silverado 2018
- Mercedes-Benz C-Class 2021
- Audi A4 2022

## Technologies Used

- **Python 3.8+**
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations

## Future Enhancements

- Database integration (SQLite/PostgreSQL)
- User authentication and authorization
- Car image uploads
- Advanced filtering options
- Export to Excel/CSV
- Email notifications for service reminders
- Mobile responsive design improvements

## License

This project is open source and available for educational purposes.

## Author

Created as a demonstration of Python OOP and Streamlit integration.

