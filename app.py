import streamlit as st


pages = {  
    "Home":[
        st.Page("pages/home.py", title="Home", icon="🏠"),
    ],

    "Car ": [
        st.Page("pages/new_or_used.py", title="New Or Used", icon="🚗"),
        st.Page("pages/repair_or_replace.py", title="Repair or Replace", icon="🔧"),
    ],

    "Real Estate": [
    ],
}


pg = st.navigation(pages)
pg.run()



