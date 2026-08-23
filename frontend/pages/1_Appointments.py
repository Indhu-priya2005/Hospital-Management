import streamlit as st
import requests
import pandas as pd

API = "https://hospital-management-system-2-kk0u.onrender.com"

st.set_page_config(page_title="Appointments", layout="wide")

st.title("Appointment Management System")

operation = st.selectbox(
    "Choose Operation",
    (
        "View Appointments",
        "Add Appointment",
        "Update Appointment",
        "Delete Appointment"
    )
)

st.divider()

# ==================================================
# VIEW APPOINTMENTS
# ==================================================

if operation == "View Appointments":

    st.subheader("Appointment List")

    try:

        response = requests.get(f"{API}/appointments", timeout=10)

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

                st.warning("No Appointments Found")

        else:

            st.error("Unable to Fetch Appointments")

    except Exception as e:

        st.error(f"Connection Error: {e}")

# ==================================================
# ADD APPOINTMENT
# ==================================================

elif operation == "Add Appointment":

    st.subheader("Add Appointment")

    appointment_id = st.number_input(
        "Appointment ID",
        min_value=1,
        step=1
    )

    patient_name = st.text_input("Patient Name")

    doctor_name = st.text_input("Doctor Name")

    appointment_date = st.date_input("Appointment Date")

    appointment_time = st.text_input("Appointment Time")

    if st.button("Add Appointment"):

        appointment = {

            "id": appointment_id,
            "patient_name": patient_name,
            "doctor_name": doctor_name,
            "date": str(appointment_date),
            "time": appointment_time

        }

        try:

            response = requests.post(
                f"{API}/appointments",
                json=appointment,
                timeout=10
            )

            if response.status_code == 200:

                st.success("Appointment Added Successfully")

                

            else:

                st.error("Unable to Add Appointment")

        except Exception as e:

            st.error(f"Connection Error: {e}")

# ==================================================
# UPDATE APPOINTMENT
# ==================================================

elif operation == "Update Appointment":

    st.subheader("Update Appointment")

    appointment_id = st.number_input(
        "Appointment ID",
        min_value=1,
        step=1
    )

    patient_name = st.text_input("Patient Name")

    doctor_name = st.text_input("Doctor Name")

    appointment_date = st.date_input("Appointment Date")

    appointment_time = st.text_input("Appointment Time")

    if st.button("Update Appointment"):

        appointment = {

            "id": appointment_id,
            "patient_name": patient_name,
            "doctor_name": doctor_name,
            "date": str(appointment_date),
            "time": appointment_time

        }

        try:

            response = requests.put(
                f"{API}/appointments/{appointment_id}",
                json=appointment,
                timeout=10
            )

            if response.status_code == 200:

                st.success("Appointment Updated Successfully")

                

            else:

                st.error("Unable to Update Appointment")

        except Exception as e:

            st.error(f"Connection Error: {e}")

# ==================================================
# DELETE APPOINTMENT
# ==================================================

elif operation == "Delete Appointment":

    st.subheader("Delete Appointment")

    appointment_id = st.number_input(
        "Appointment ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Appointment"):

        try:

            response = requests.delete(
                f"{API}/appointments/{appointment_id}",
                timeout=10
            )

            if response.status_code == 200:

                st.success("Appointment Deleted Successfully")

                

            else:

                st.error("Unable to Delete Appointment")

        except Exception as e:

            st.error(f"Connection Error: {e}")