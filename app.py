import streamlit as st


pages = {  
    "Home":[
        st.Page("pages/home.py", title="Home", icon="🏠"),
    ],

    "Car ": [
        st.Page("pages/car/new_or_used.py", title="New Or Used", icon="🚗"),
        st.Page("pages/car/repair_or_replace.py", title="Repair or Replace", icon="🔧"),  # New module added here
    ],

    "Real Estate": [
    ],
}


pg = st.navigation(pages)
pg.run()



