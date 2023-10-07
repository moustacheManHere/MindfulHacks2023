import streamlit as st

# Title of the app
st.title('Mental Health App')

# Introduction
st.write("Welcome to the Mental Health App. This is a safe space where you can find resources, take self-assessments, and learn more about mental health.")

# Navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "Resources", "Self-Assessment"])

if page == "Home":
    st.header("Home")
    st.write("This is the home page.")
elif page == "Resources":
    st.header("Resources")
    st.write("This is the resources page.")
elif page == "Self-Assessment":
    st.header("Self-Assessment")
    st.write("This is the self-assessment page.")
    
