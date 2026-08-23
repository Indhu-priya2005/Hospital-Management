import streamlit as st
import requests
import pandas as pd

API = "https://hospital-management-system-2-kk0u.onrender.com"

st.set_page_config(
    page_title="Patients",
    layout="wide"
)

st.title("Patient Management System")

operation = st.selectbox(
    "Choose Operation",
    (
        "View Patients",
        "Add Patient",
        "Update Patient",
        "Delete Patient"
    )
)

st.divider()

# ==================================================
# VIEW PATIENTS
# ==================================================

if operation == "View Patients":

    st.subheader("Patient List")

    try:

        response = requests.get(f"{API}/patients", timeout=10)

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

                st.warning("No Patients Found")

        else:

            st.error("Unable to Fetch Patients")

    except Exception as e:

        st.error(f"Connection Error: {e}")

# ==================================================
# ADD PATIENT
# ==================================================

elif operation == "Add Patient":

    st.subheader("Add New Patient")

    patient_id = st.number_input(
        "Patient ID",
        min_value=1,
        step=1
    )

    name = st.text_input("Patient Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    disease = st.text_input("Disease")

    if st.button("Add Patient"):

        patient = {
            "id": patient_id,
            "name": name,
            "age": age,
            "gender": gender,
            "disease": disease
        }

        try:

            response = requests.post(
                f"{API}/patients",
                json=patient,
                timeout=10
            )

            if response.status_code == 200:

                st.success("Patient Added Successfully")

                

            else:

                st.error("Unable to Add Patient")

        except Exception as e:

            st.error(f"Connection Error: {e}")

# ==================================================
# UPDATE PATIENT
# ==================================================

elif operation == "Update Patient":

    st.subheader("Update Patient")

    patient_id = st.number_input(
        "Patient ID",
        min_value=1,
        step=1
    )

    name = st.text_input("New Name")

    age = st.number_input(
        "New Age",
        min_value=1,
        max_value=120
    )

    gender = st.selectbox(
        "New Gender",
        ["Male", "Female", "Other"]
    )

    disease = st.text_input("New Disease")

    if st.button("Update Patient"):

        patient = {
            "id": patient_id,
            "name": name,
            "age": age,
            "gender": gender,
            "disease": disease
        }

        try:

            response = requests.put(
                f"{API}/patients/{patient_id}",
                json=patient,
                timeout=10
            )

            if response.status_code == 200:

                st.success("Patient Updated Successfully")

                

            else:

                st.error("Unable to Update Patient")

        except Exception as e:

            st.error(f"Connection Error: {e}")

# ==================================================
# DELETE PATIENT
# ==================================================

elif operation == "Delete Patient":

    st.subheader("Delete Patient")

    patient_id = st.number_input(
        "Patient ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Patient"):

        try:

            response = requests.delete(
                f"{API}/patients/{patient_id}",
                timeout=10
            )

            if response.status_code == 200:

                st.success("Patient Deleted Successfully")

                

            else:

                st.error("Unable to Delete Patient")

        except Exception as e:

            st.error(f"Connection Error: {e}")