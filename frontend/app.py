import streamlit as st

st.set_page_config(
    page_title="Hospital Management System",
    page_icon="🏥",
    layout="wide"
)

st.title("Hospital Management System")

st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.info("Patients")
    st.metric("Module", "Patient Management")

with col2:
    st.info("Doctors")
    st.metric("Module", "Doctor Management")

col3, col4 = st.columns(2)

with col3:
    st.info("Appointments")
    st.metric("Module", "Appointment Management")

with col4:
    st.info("Billing")
    st.metric("Module", "Billing Management")

st.write("---")

st.subheader("Project Modules")

st.write("""
Use the left sidebar to navigate between modules.

Available Modules:

• Patient Management

• Doctor Management

• Appointment Management

• Billing Management

Each module supports complete CRUD Operations:

• View

• Add

• Update

• Delete
""")

st.write("---")

st.success("Hospital Management System is Running Successfully")