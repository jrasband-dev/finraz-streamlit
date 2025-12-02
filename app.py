import streamlit as st


pages = {  
    "Home":[
        st.Page("pages/home.py", title="About", icon="🏠"),
    ],

    "Car": [
        st.Page("pages/new_or_used.py", title="New or Used", icon="🚗"),
        st.Page("pages/repair_or_replace.py", title="Repair or Replace", icon="🔧"),
    ],

    "Mortgage": [
        st.Page("pages/mortgage_amortization.py", title="Amortization", icon="🏠"),
        st.Page("pages/mortgage_refinance.py", title="Refinance", icon="🏠"),
        st.Page("pages/rent_or_buy.py", title="Rent Or Buy", icon="🏠"),
    ],
}


pg = st.navigation(pages)
pg.run()



