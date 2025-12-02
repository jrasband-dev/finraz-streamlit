import streamlit as st
from finraz.mortgage import rent_or_buy, income_multiplier




st.title("Rent? or Buy?")

st.header("Initial Assessment")
income = st.number_input("What is your annual Income?",min_value=0)
desired_home_price = st.number_input("About how much do you want to pay for your home?",min_value=0)
down_payment = st.number_input("How Much can you put down? ")

if income > 0:
    multiplier = income_multiplier( income, desired_home_price)
else:
    multiplier = 0

if down_payment > 0:
    percent_down = down_payment/desired_home_price
else:
    percent_down = 0
    

st.write("Income Multiple")
st.write(multiplier)
st.write("A good rule of thumb is to keep your income multiplier between 2.5 and 3.5. This multiplier is an indicator of your income's ability to cover the cost of your home.")

st.write("Down Payment")
st.write(percent_down)
st.write("If don't have more than 20% down you will most likely have to pay mortgage insurance. In some cases, mortgage insurance may be worth the price if the housing market is in a boom.")

st.header("Rental Info")
deposit = st.number_input("Deposit",min_value=0.0)
rent = st.number_input("Rent",min_value=0.0)
utilities = st.number_input("Utilities",help="Utility expenses not included in rent",min_value=0.0)

st.header("Home Purchase Info")
monthly_payment = st.number_input("Monthly Payment", min_value=0.0)
home_insurance = st.number_input("Home Insurance", min_value=0.0)
utilities = st.number_input("Utilities",min_value=0.0)
property_taxes = st.number_input("Property Taxes",min_value=0.0)
maintenance = st.number_input("Maintenance & Up-Keep",min_value=0) 



