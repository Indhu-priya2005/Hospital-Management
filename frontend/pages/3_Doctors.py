import streamlit as st
import requests
import pandas as pd

API = "https://hospital-management-system-2-kk0u.onrender.com"

st.set_page_config(
    page_title="Doctors",
    layout="wide"
)

st.title("Doctor Management System")

operation = st.selectbox(
    "Choose Operation",
    (
        "View Doctors",
        "Add Doctor",
        "Update Doctor",
        "Delete Doctor"
    )
)

st.divider()

# ==================================================
# VIEW DOCTORS
# ==================================================

if operation == "View Doctors":

    st.subheader("Doctor List")

    try:

        response = requests.get(f"{API}/doctors", timeout=10)

        if response.status_code == 200:

            data = response.json()

            if len(data) > 0:

                df = pd.DataFrame(data)

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

            else:

                st.warning("No Doctors Found")

        else:

            st.error("Unable to Fetch Doctors")

    except Exception as e:

        st.error(f"Connection Error: {e}")

# ==================================================
# ADD DOCTOR
# ==================================================

elif operation == "Add Doctor":

    st.subheader("Add New Doctor")

    doctor_id = st.number_input(
        "Doctor ID",
        min_value=1,
        step=1
    )

    name = st.text_input("Doctor Name")

    specialization = st.text_input("Specialization")

    experience = st.number_input(
        "Experience (Years)",
        min_value=0,
        max_value=50
    )

    if st.button("Add Doctor"):

        doctor = {
            "id": doctor_id,
            "name": name,
            "specialization": specialization,
            "experience": experience
        }

        try:

            response = requests.post(
                f"{API}/doctors",
                json=doctor,
                timeout=10
            )

            if response.status_code == 200:

                st.success("Doctor Added Successfully")

                

            else:

                st.error("Unable to Add Doctor")

        except Exception as e:

            st.error(f"Connection Error: {e}")

# ==================================================
# UPDATE DOCTOR
# ==================================================

elif operation == "Update Doctor":

    st.subheader("Update Doctor")

    doctor_id = st.number_input(
        "Doctor ID",
        min_value=1,
        step=1
    )

    name = st.text_input("New Doctor Name")

    specialization = st.text_input("New Specialization")

    experience = st.number_input(
        "New Experience",
        min_value=0,
        max_value=50
    )

    if st.button("Update Doctor"):

        doctor = {
            "id": doctor_id,
            "name": name,
            "specialization": specialization,
            "experience": experience
        }

        try:

            response = requests.put(
                f"{API}/doctors/{doctor_id}",
                json=doctor,
                timeout=10
            )

            if response.status_code == 200:

                st.success("Doctor Updated Successfully")

                

            else:

                st.error("Unable to Update Doctor")

        except Exception as e:

            st.error(f"Connection Error: {e}")

# ==================================================
# DELETE DOCTOR
# ==================================================

elif operation == "Delete Doctor":

    st.subheader("Delete Doctor")

    doctor_id = st.number_input(
        "Doctor ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Doctor"):

        try:

            response = requests.delete(
                f"{API}/doctors/{doctor_id}",
                timeout=10
            )

            if response.status_code == 200:

                st.success("Doctor Deleted Successfully")

                

            else:

                st.error("Unable to Delete Doctor")

        except Exception as e:

            st.error(f"Connection Error: {e}")