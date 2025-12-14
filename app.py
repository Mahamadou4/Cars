"""
Streamlit application for Car Management System
"""
import streamlit as st
import pandas as pd
from car import Car
from car_manager import CarManager
import plotly.express as px
import plotly.graph_objects as go


# Initialize session state
if 'car_manager' not in st.session_state:
    st.session_state.car_manager = CarManager()
    # Add some sample data
    sample_cars = [
        Car("Toyota", "Camry", 2020, "Silver", 25000, 35000),
        Car("Honda", "Civic", 2021, "Blue", 22000, 25000),
        Car("Ford", "Mustang", 2019, "Red", 35000, 45000),
        Car("Tesla", "Model 3", 2022, "White", 45000, 15000),
        Car("BMW", "X5", 2020, "Black", 55000, 40000),
        Car("Chevrolet", "Silverado", 2018, "Gray", 32000, 65000),
        Car("Mercedes-Benz", "C-Class", 2021, "Silver", 48000, 22000),
        Car("Audi", "A4", 2022, "Blue", 42000, 12000),
    ]
    for car in sample_cars:
        st.session_state.car_manager.add_car(car)


def main():
    """Main application function"""
    st.set_page_config(page_title="Car Management System", page_icon="🚗", layout="wide")

    st.title("🚗 Car Management System")
    st.markdown("---")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["Dashboard", "Inventory", "Add Car", "Search Cars", "Car Details", "Analytics"]
    )

    if page == "Dashboard":
        show_dashboard()
    elif page == "Inventory":
        show_inventory()
    elif page == "Add Car":
        show_add_car()
    elif page == "Search Cars":
        show_search()
    elif page == "Car Details":
        show_car_details()
    elif page == "Analytics":
        show_analytics()


def show_dashboard():
    """Display dashboard with statistics"""
    st.header("📊 Dashboard")

    stats = st.session_state.car_manager.get_statistics()

    # Display metrics in columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Cars", stats['total_cars'])
    with col2:
        st.metric("Total Value", f"${stats['total_value']:,.2f}")
    with col3:
        st.metric("Average Price", f"${stats['average_price']:,.2f}")
    with col4:
        st.metric("Average Age", f"{stats['average_age']} years")

    st.markdown("---")

    # Additional info
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Available Makes")
        if stats['makes']:
            for make in sorted(stats['makes']):
                st.write(f"• {make}")
        else:
            st.write("No cars in inventory")

    with col2:
        st.subheader("Available Colors")
        if stats['colors']:
            for color in sorted(stats['colors']):
                st.write(f"• {color}")
        else:
            st.write("No cars in inventory")


def show_inventory():
    """Display full inventory"""
    st.header("🚙 Car Inventory")

    cars = st.session_state.car_manager.get_all_cars()

    if not cars:
        st.info("No cars in inventory. Add some cars to get started!")
        return

    # Sorting options
    col1, col2 = st.columns([3, 1])
    with col1:
        sort_by = st.selectbox("Sort by", ["Year (Newest)", "Year (Oldest)", "Price (High to Low)",
                                           "Price (Low to High)", "Mileage (Low to High)",
                                           "Mileage (High to Low)"])

    # Sort cars based on selection
    if sort_by == "Year (Newest)":
        cars = st.session_state.car_manager.sort_by_year(ascending=False)
    elif sort_by == "Year (Oldest)":
        cars = st.session_state.car_manager.sort_by_year(ascending=True)
    elif sort_by == "Price (High to Low)":
        cars = st.session_state.car_manager.sort_by_price(ascending=False)
    elif sort_by == "Price (Low to High)":
        cars = st.session_state.car_manager.sort_by_price(ascending=True)
    elif sort_by == "Mileage (Low to High)":
        cars = st.session_state.car_manager.sort_by_mileage(ascending=True)
    elif sort_by == "Mileage (High to Low)":
        cars = st.session_state.car_manager.sort_by_mileage(ascending=False)

    # Convert to DataFrame for display
    car_data = []
    for car in cars:
        car_data.append({
            'Make': car.make,
            'Model': car.model,
            'Year': car.year,
            'Color': car.color,
            'Price': f"${car.price:,.2f}",
            'Mileage': f"{car.mileage:,.0f} mi",
            'Age': f"{car.get_age()} years",
            'Current Value': f"${car.get_depreciation():,.2f}"
        })

    df = pd.DataFrame(car_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

    # Export option
    if st.button("📥 Export to JSON"):
        st.session_state.car_manager.export_to_json("car_inventory.json")
        st.success("Inventory exported to car_inventory.json!")


def show_add_car():
    """Add a new car to inventory"""
    st.header("➕ Add New Car")

    with st.form("add_car_form"):
        col1, col2 = st.columns(2)

        with col1:
            make = st.text_input("Make*", placeholder="e.g., Toyota")
            model = st.text_input("Model*", placeholder="e.g., Camry")
            year = st.number_input("Year*", min_value=1900, max_value=2025, value=2022)

        with col2:
            color = st.text_input("Color*", placeholder="e.g., Silver")
            price = st.number_input("Price ($)*", min_value=0.0, value=25000.0, step=1000.0)
            mileage = st.number_input("Mileage (miles)", min_value=0.0, value=0.0, step=1000.0)

        owner = st.text_input("Owner (optional)", placeholder="Owner name")

        submitted = st.form_submit_button("Add Car")

        if submitted:
            if not all([make, model, color]):
                st.error("Please fill in all required fields (marked with *)")
            else:
                new_car = Car(make, model, year, color, price, mileage)
                if owner:
                    new_car.set_owner(owner)
                st.session_state.car_manager.add_car(new_car)
                st.success(f"✅ Successfully added {year} {make} {model}!")
                st.balloons()


def show_search():
    """Search for cars"""
    st.header("🔍 Search Cars")

    search_type = st.selectbox("Search by", ["Make", "Model", "Year Range", "Price Range"])

    results = []

    if search_type == "Make":
        make = st.text_input("Enter make", placeholder="e.g., Toyota")
        if st.button("Search") and make:
            results = st.session_state.car_manager.search_by_make(make)

    elif search_type == "Model":
        model = st.text_input("Enter model", placeholder="e.g., Camry")
        if st.button("Search") and model:
            results = st.session_state.car_manager.search_by_model(model)

    elif search_type == "Year Range":
        col1, col2 = st.columns(2)
        with col1:
            min_year = st.number_input("From year", min_value=1900, max_value=2025, value=2018)
        with col2:
            max_year = st.number_input("To year", min_value=1900, max_value=2025, value=2025)

        if st.button("Search"):
            results = st.session_state.car_manager.search_by_year_range(min_year, max_year)

    elif search_type == "Price Range":
        col1, col2 = st.columns(2)
        with col1:
            min_price = st.number_input("Min price ($)", min_value=0.0, value=0.0, step=5000.0)
        with col2:
            max_price = st.number_input("Max price ($)", min_value=0.0, value=100000.0, step=5000.0)

        if st.button("Search"):
            results = st.session_state.car_manager.search_by_price_range(min_price, max_price)

    # Display results
    if results:
        st.success(f"Found {len(results)} car(s)")
        for car in results:
            with st.expander(f"{car} - ${car.price:,.2f}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Make:** {car.make}")
                    st.write(f"**Model:** {car.model}")
                    st.write(f"**Year:** {car.year}")
                    st.write(f"**Color:** {car.color}")
                with col2:
                    st.write(f"**Price:** ${car.price:,.2f}")
                    st.write(f"**Mileage:** {car.mileage:,.0f} miles")
                    st.write(f"**Age:** {car.get_age()} years")
                    st.write(f"**Current Value:** ${car.get_depreciation():,.2f}")
    elif results is not None and len(results) == 0:
        st.warning("No cars found matching your search criteria.")


def show_car_details():
    """Show detailed information about a specific car"""
    st.header("📋 Car Details")

    cars = st.session_state.car_manager.get_all_cars()

    if not cars:
        st.info("No cars in inventory.")
        return

    car_options = [f"{car.year} {car.make} {car.model} ({car.color})" for car in cars]
    selected = st.selectbox("Select a car", car_options)

    if selected:
        index = car_options.index(selected)
        car = cars[index]

        st.markdown("---")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Basic Information")
            st.write(f"**Make:** {car.make}")
            st.write(f"**Model:** {car.model}")
            st.write(f"**Year:** {car.year}")
            st.write(f"**Color:** {car.color}")
            st.write(f"**Owner:** {car.owner if car.owner else 'Not assigned'}")

        with col2:
            st.subheader("Financial Information")
            st.write(f"**Original Price:** ${car.price:,.2f}")
            st.write(f"**Current Value:** ${car.get_depreciation():,.2f}")
            depreciation_pct = (1 - car.get_depreciation() / car.price) * 100
            st.write(f"**Depreciation:** {depreciation_pct:.1f}%")

        with col3:
            st.subheader("Usage Information")
            st.write(f"**Mileage:** {car.mileage:,.0f} miles")
            st.write(f"**Age:** {car.get_age()} years")
            st.write(f"**Service Records:** {len(car.service_history)}")

        st.markdown("---")

        # Service history section
        st.subheader("Service History")

        with st.expander("Add Service Record"):
            with st.form("service_form"):
                service_type = st.text_input("Service Type", placeholder="e.g., Oil Change")
                cost = st.number_input("Cost ($)", min_value=0.0, value=50.0)
                description = st.text_area("Description", placeholder="Additional details...")

                if st.form_submit_button("Add Service Record"):
                    if service_type:
                        car.add_service_record(service_type, cost, description)
                        st.success("Service record added!")
                    else:
                        st.error("Please enter a service type")

        if car.service_history:
            for record in car.service_history:
                with st.expander(f"{record['type']} - {record['date']}"):
                    st.write(f"**Cost:** ${record['cost']:.2f}")
                    st.write(f"**Mileage:** {record['mileage']:,.0f} miles")
                    if record['description']:
                        st.write(f"**Description:** {record['description']}")
        else:
            st.info("No service records yet.")


def show_analytics():
    """Show analytics and visualizations"""
    st.header("📈 Analytics")

    cars = st.session_state.car_manager.get_all_cars()

    if not cars:
        st.info("No cars in inventory. Add some cars to see analytics!")
        return

    # Prepare data
    car_data = [car.to_dict() for car in cars]
    df = pd.DataFrame(car_data)

    # Price distribution
    st.subheader("Price Distribution")
    fig_price = px.histogram(df, x='price', nbins=10, title="Car Price Distribution",
                             labels={'price': 'Price ($)', 'count': 'Number of Cars'})
    st.plotly_chart(fig_price, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        # Cars by make
        st.subheader("Cars by Make")
        make_counts = df['make'].value_counts()
        fig_make = px.pie(values=make_counts.values, names=make_counts.index,
                         title="Distribution by Manufacturer")
        st.plotly_chart(fig_make, use_container_width=True)

    with col2:
        # Cars by year
        st.subheader("Cars by Year")
        year_counts = df['year'].value_counts().sort_index()
        fig_year = px.bar(x=year_counts.index, y=year_counts.values,
                         title="Cars by Year",
                         labels={'x': 'Year', 'y': 'Number of Cars'})
        st.plotly_chart(fig_year, use_container_width=True)

    # Price vs Age
    st.subheader("Price vs Age Analysis")
    fig_scatter = px.scatter(df, x='age', y='price', color='make', size='mileage',
                            hover_data=['model', 'color'],
                            title="Price vs Age (bubble size = mileage)",
                            labels={'age': 'Age (years)', 'price': 'Price ($)'})
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Depreciation comparison
    st.subheader("Original Price vs Current Value")
    df_comparison = pd.DataFrame({
        'Car': df['make'] + ' ' + df['model'],
        'Original Price': df['price'],
        'Current Value': df['current_value']
    })

    fig_comparison = go.Figure(data=[
        go.Bar(name='Original Price', x=df_comparison['Car'], y=df_comparison['Original Price']),
        go.Bar(name='Current Value', x=df_comparison['Car'], y=df_comparison['Current Value'])
    ])
    fig_comparison.update_layout(barmode='group', title="Price Depreciation Comparison")
    st.plotly_chart(fig_comparison, use_container_width=True)


if __name__ == "__main__":
    main()

