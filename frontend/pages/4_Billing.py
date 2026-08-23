import streamlit as st
import requests
import pandas as pd

API = "https://hospital-management-system-2-kk0u.onrender.com"

st.set_page_config(
    page_title="Billing",
    layout="wide"
)

st.title("Billing Management System")

operation = st.selectbox(
    "Choose Operation",
    (
        "View Bills",
        "Add Bill",
        "Update Bill",
        "Delete Bill"
    )
)

st.divider()

# ==================================================
# VIEW BILLS
# ==================================================

if operation == "View Bills":

    st.subheader("Bill List")

    try:

        response = requests.get(f"{API}/bills", timeout=10)

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

                st.warning("No Bills Found")

        else:

            st.error("Unable to Fetch Bills")

    except Exception as e:

        st.error(f"Connection Error: {e}")

# ==================================================
# ADD BILL
# ==================================================

elif operation == "Add Bill":

    st.subheader("Add New Bill")

    bill_id = st.number_input(
        "Bill ID",
        min_value=1,
        step=1
    )

    patient_name = st.text_input("Patient Name")

    amount = st.number_input(
    "Amount",
    min_value=0.0,
    value=0.0,
    step=100.0,
    format="%.2f"
)

    payment_status = st.selectbox(
        "Payment Status",
        ["Paid", "Pending"]
    )

    if st.button("Add Bill"):

        bill = {
            "id": bill_id,
            "patient_name": patient_name,
            "amount": amount,
            "payment_status": payment_status
        }

        try:

            response = requests.post(
                f"{API}/bills",
                json=bill,
                timeout=10
            )

            if response.status_code == 200:

                st.success("Bill Added Successfully")

                

            else:

                st.error("Unable to Add Bill")

        except Exception as e:

            st.error(f"Connection Error: {e}")

# ==================================================
# UPDATE BILL
# ==================================================

elif operation == "Update Bill":

    st.subheader("Update Bill")

    bill_id = st.number_input(
        "Bill ID",
        min_value=1,
        step=1
    )

    patient_name = st.text_input("Patient Name")

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    payment_status = st.selectbox(
        "Payment Status",
        ["Paid", "Pending"]
    )

    if st.button("Update Bill"):

        bill = {
            "id": bill_id,
            "patient_name": patient_name,
            "amount": amount,
            "payment_status": payment_status
        }

        try:

            response = requests.put(
                f"{API}/bills/{bill_id}",
                json=bill,
                timeout=10
            )

            if response.status_code == 200:

                st.success("Bill Updated Successfully")

                

            else:

                st.error("Unable to Update Bill")

        except Exception as e:

            st.error(f"Connection Error: {e}")

# ==================================================
# DELETE BILL
# ==================================================

elif operation == "Delete Bill":

    st.subheader("Delete Bill")

    bill_id = st.number_input(
        "Bill ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Bill"):

        try:

            response = requests.delete(
                f"{API}/bills/{bill_id}",
                timeout=10
            )

            if response.status_code == 200:

                st.success("Bill Deleted Successfully")

                

            else:

                st.error("Unable to Delete Bill")

        except Exception as e:

            st.error(f"Connection Error: {e}")