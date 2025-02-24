import streamlit as st

st.title("Car Repair or Replace")

# Input fields
current_car_value = st.number_input("Current Car Value ($)", min_value=0.0, step=1000.0)
repair_cost = st.number_input("Repair Cost ($)", min_value=0.0, step=100.0)
yearly_mileage = st.number_input("Yearly Mileage (miles)", min_value=0, step=1000)
car_mileage = st.number_input("Current Car Mileage (miles)", min_value=0, step=1000)
expected_total_mileage = st.number_input("Expected Total Mileage (miles)", min_value=0, step=1000)
monthly_carrying_cost = st.number_input("Monthly Carrying Cost ($)", min_value=0.0, step=50.0)

# Calculate remaining life of the car
remaining_mileage = expected_total_mileage - car_mileage
remaining_years = remaining_mileage / yearly_mileage if yearly_mileage > 0 else 0
remaining_months = remaining_years * 12

# Decision logic
if remaining_mileage <= 0:
    decision = "The car has reached its expected total mileage. Consider replacing it."
elif repair_cost >= current_car_value:
    decision = "The repair cost exceeds the current car value. Consider replacing it."
else:
    decision = f"The car has approximately {remaining_years:.1f} years ({remaining_months:.1f} months) of life left. Repairing it may be worth it if the monthly repair cost are less than a car payment would be."

# Calculate and display the carrying cost
total_carrying_cost = remaining_months * monthly_carrying_cost
monthly_repair_cost = repair_cost / remaining_months if remaining_months > 0 else 0

st.write(decision)
st.write(f"The estimated total carrying cost over the remaining life of the car is ${total_carrying_cost:.2f}.")
st.write(f"The estimated monthly repair cost is ${monthly_repair_cost:.2f}.")