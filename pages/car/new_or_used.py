import json
import streamlit as st
from finraz.car import new_or_used



st.title("Car Cost Comparison Tool")

st.header("Enter New Car Details")
new_car_price = st.number_input("New Car Price ($)", min_value=0.0)
new_car_downpayment = st.number_input("New Car Downpayment ($)", min_value=0.0)
new_car_interest_rate = st.number_input("New Car Interest Rate (%)", min_value=0.0, max_value=100.0) / 100
new_car_loan_term_years = st.number_input("New Car Loan Term (Years)", min_value=1, max_value=30)

st.header("Enter Used Car Details")
used_car_price = st.number_input("Used Car Price ($)", min_value=0.0)
used_car_interest_rate = st.number_input("Used Car Interest Rate (%)", min_value=0.0, max_value=100.0) / 100
used_car_loan_term_years = st.number_input("Used Car Loan Term (Years)", min_value=1, max_value=30)
used_car_mileage = st.number_input("Used Car Mileage (miles)", min_value=0)
used_car_msrp = st.number_input("Used Car MSRP ($)", min_value=0.0)

annual_mileage = st.number_input("Annual Mileage (miles)", value=12000)
total_lifespan_miles = st.number_input("Total Lifespan Miles (miles)", value=180000)

used_car_downpayment = st.number_input("Used Car Downpayment ($)", min_value=0.0)

if st.button("Compare Cars"):
    results = new_or_used(
        new_car_price,
        new_car_interest_rate,
        new_car_loan_term_years,
        used_car_price,
        used_car_interest_rate,
        used_car_loan_term_years,
        used_car_mileage,
        used_car_msrp,
        annual_mileage,
        total_lifespan_miles,
        new_car_downpayment,
        used_car_downpayment
    )

    st.subheader("Comparison Results")
    st.write(results)

    # Convert results to JSON
    results_json = json.dumps(results, indent=4)
    
    # Create a download button
    st.download_button(
        label="Download Comparison as JSON",
        data=results_json,
        file_name="car_comparison_results.json",
        mime="application/json"
    )

