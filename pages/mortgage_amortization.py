import streamlit as st
from finraz.mortgage import Mortgage

# Streamlit UI
st.title("Mortgage and Refinance Calculator")

# Mortgage Inputs
principal = st.number_input("Loan Principal ($)", value=250000.0, step=1000.0)
interest_rate = st.number_input("Annual Interest Rate (%)", value=3.5, step=0.1)
term_years = st.number_input("Loan Term (years)", value=30, step=1)
start_date = st.date_input("Start Date (YYYY-MM-DD)", value="today", format="YYYY-MM-DD")
extra_payment = st.number_input("Extra Principal Payment ($)", value=0.0, step=50.0)

mortgage = Mortgage(principal, interest_rate, term_years, str(start_date), extra_payment)
st.write("### Monthly Payment:", round(mortgage.monthly_payment, 2))


# Amortization Schedule
if st.button("Show Amortization Schedule"):
    schedule_df = mortgage.generate_amortization_schedule().to_pandas()
    st.dataframe(schedule_df)

if st.button("Show Principal Only Impact"):
    new_term,time_saved,schedule_df = mortgage.calculate_principal_only_payment()
    st.write("New Term:", new_term)
    st.write("Time Saved:", time_saved)
    st.dataframe(schedule_df)
