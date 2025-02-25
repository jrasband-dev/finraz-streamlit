import streamlit as st
from finraz.mortgage import Mortgage, RefinanceOption

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

# Refinance Inputs
st.subheader("Refinance Options")
new_loan_amount = st.number_input("New Loan Amount ($)", value=250000.0, step=1000.0)
new_interest_rate = st.number_input("New Annual Interest Rate (%)", value=2.5, step=0.1)
new_term_years = st.number_input("New Loan Term (years)", value=30, step=1)
associated_costs = st.number_input("Refinancing Costs ($)", value=5000.0, step=500.0)
break_even_point = st.number_input("Break Even Point (months, optional)", value=36, step=1)

if st.button("Assess Refinance Option"):
    refinance_option = RefinanceOption(new_loan_amount, new_interest_rate, new_term_years, associated_costs)
    results = mortgage.refinance_assessment(refinance_option, break_even_threshold=break_even_point)
    st.write(results)

