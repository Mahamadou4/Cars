# Streamlit Car Management System - Quick Start Guide

## Overview
Your project already includes a fully functional Streamlit application (`app.py`) for managing a car inventory system.

## Installation

1. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. The application will automatically open in your default web browser (typically at `http://localhost:8501`)

## Features

### 📊 Dashboard
- View key statistics (total cars, total value, average price, average age)
- See available makes and colors in inventory
- Quick overview of your entire car collection

### 🚙 Inventory
- View all cars in a sortable table
- Sort by year, price, or mileage
- Export inventory to JSON format
- See depreciation values

### ➕ Add Car
- Add new cars to the inventory
- Enter make, model, year, color, price, mileage
- Optional owner assignment
- Form validation

### 🔍 Search Cars
- Search by make
- Search by model
- Search by year range
- Search by price range
- Detailed results with car information

### 📋 Car Details
- View detailed information for any car
- See financial info (original price, current value, depreciation)
- View and add service records
- Track maintenance history

### 📈 Analytics
- Price distribution histogram
- Cars by manufacturer (pie chart)
- Cars by year (bar chart)
- Price vs Age scatter plot
- Original price vs current value comparison

## Sample Data
The app comes pre-loaded with 8 sample cars including:
- Toyota Camry (2020)
- Honda Civic (2021)
- Ford Mustang (2019)
- Tesla Model 3 (2022)
- BMW X5 (2020)
- Chevrolet Silverado (2018)
- Mercedes-Benz C-Class (2021)
- Audi A4 (2022)

## Project Structure
```
Cars/
├── app.py              # Streamlit application (main file)
├── car.py              # Car class definition
├── car_manager.py      # CarManager class for inventory management
├── test_cars.py        # Unit tests
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Technologies Used
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and display
- **Plotly**: Interactive visualizations and charts

## Tips
- The app uses Streamlit's session state to persist data during your session
- Data is not saved to disk unless you use the "Export to JSON" feature
- All charts are interactive - you can zoom, pan, and hover for details
- Use the sidebar navigation to switch between different pages

## Troubleshooting

### Port already in use
If port 8501 is already in use, run:
```bash
streamlit run app.py --server.port 8502
```

### Missing dependencies
Make sure all packages are installed:
```bash
pip install streamlit pandas plotly
```

## Next Steps
- Customize the sample data
- Add more car attributes if needed
- Implement data persistence (database or file storage)
- Add authentication for multi-user support
- Deploy to Streamlit Cloud for public access

