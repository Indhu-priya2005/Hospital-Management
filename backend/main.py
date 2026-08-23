from fastapi import FastAPI, Request

app = FastAPI(
    title="Hospital Management System",
    version="1.0"
)

# ==========================================
# Sample Patient Data (Python List)
# ==========================================

patients = [
    {
        "id": 1,
        "name": "Rahul",
        "age": 24,
        "gender": "Male",
        "disease": "Fever"
    },
    {
        "id": 2,
        "name": "Priya",
        "age": 21,
        "gender": "Female",
        "disease": "Cold"
    }
]

# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():
    return {
        "message": "Hospital Management System API"
    }

# ==========================================
# GET ALL PATIENTS
# ==========================================

@app.get("/patients")
def get_patients():
    return patients

# ==========================================
# GET SINGLE PATIENT
# ==========================================

@app.get("/patients/{patient_id}")
def get_patient(patient_id: int):

    for patient in patients:

        if patient["id"] == patient_id:
            return patient

    return {"message": "Patient Not Found"}

# ==========================================
# ADD PATIENT
# ==========================================

@app.post("/patients")
async def add_patient(request: Request):

    patient = await request.json()

    patients.append(patient)

    return {
        "message": "Patient Added Successfully",
        "patient": patient
    }

# ==========================================
# UPDATE PATIENT
# ==========================================

@app.put("/patients/{patient_id}")
async def update_patient(patient_id: int, request: Request):

    updated_patient = await request.json()

    for index, patient in enumerate(patients):

        if patient["id"] == patient_id:

            patients[index] = updated_patient

            return {
                "message": "Patient Updated Successfully"
            }

    return {
        "message": "Patient Not Found"
    }

# ==========================================
# DELETE PATIENT
# ==========================================

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):

    for patient in patients:

        if patient["id"] == patient_id:

            patients.remove(patient)

            return {
                "message": "Patient Deleted Successfully"
            }

    return {
        "message": "Patient Not Found"
    }
# ==========================================
# Sample Doctor Data
# ==========================================

doctors = [
    {
        "id": 1,
        "name": "Dr. Ramesh",
        "specialization": "Cardiologist",
        "experience": 10
    },
    {
        "id": 2,
        "name": "Dr. Priya",
        "specialization": "Dermatologist",
        "experience": 6
    }
]

# ==========================================
# GET ALL DOCTORS
# ==========================================

@app.get("/doctors")
def get_doctors():
    return doctors


# ==========================================
# GET SINGLE DOCTOR
# ==========================================

@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):

    for doctor in doctors:

        if doctor["id"] == doctor_id:
            return doctor

    return {"message": "Doctor Not Found"}


# ==========================================
# ADD DOCTOR
# ==========================================

@app.post("/doctors")
async def add_doctor(request: Request):

    doctor = await request.json()

    doctors.append(doctor)

    return {
        "message": "Doctor Added Successfully",
        "doctor": doctor
    }


# ==========================================
# UPDATE DOCTOR
# ==========================================

@app.put("/doctors/{doctor_id}")
async def update_doctor(doctor_id: int, request: Request):

    updated_doctor = await request.json()

    for index, doctor in enumerate(doctors):

        if doctor["id"] == doctor_id:

            doctors[index] = updated_doctor

            return {
                "message": "Doctor Updated Successfully"
            }

    return {"message": "Doctor Not Found"}


# ==========================================
# DELETE DOCTOR
# ==========================================

@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int):

    for doctor in doctors:

        if doctor["id"] == doctor_id:

            doctors.remove(doctor)

            return {
                "message": "Doctor Deleted Successfully"
            }

    return {"message": "Doctor Not Found"}
# ==========================================
# Sample Appointment Data
# ==========================================

appointments = [
    {
        "id": 1,
        "patient_name": "Rahul",
        "doctor_name": "Dr. Ramesh",
        "date": "2026-08-05",
        "time": "10:00 AM"
    },
    {
        "id": 2,
        "patient_name": "Priya",
        "doctor_name": "Dr. Priya",
        "date": "2026-08-06",
        "time": "11:30 AM"
    }
]

# ==========================================
# GET ALL APPOINTMENTS
# ==========================================

@app.get("/appointments")
def get_appointments():
    return appointments


# ==========================================
# GET SINGLE APPOINTMENT
# ==========================================

@app.get("/appointments/{appointment_id}")
def get_appointment(appointment_id: int):

    for appointment in appointments:

        if appointment["id"] == appointment_id:
            return appointment

    return {"message": "Appointment Not Found"}


# ==========================================
# ADD APPOINTMENT
# ==========================================

@app.post("/appointments")
async def add_appointment(request: Request):

    appointment = await request.json()

    appointments.append(appointment)

    return {
        "message": "Appointment Added Successfully",
        "appointment": appointment
    }


# ==========================================
# UPDATE APPOINTMENT
# ==========================================

@app.put("/appointments/{appointment_id}")
async def update_appointment(appointment_id: int, request: Request):

    updated_appointment = await request.json()

    for index, appointment in enumerate(appointments):

        if appointment["id"] == appointment_id:

            appointments[index] = updated_appointment

            return {
                "message": "Appointment Updated Successfully"
            }

    return {"message": "Appointment Not Found"}


# ==========================================
# DELETE APPOINTMENT
# ==========================================

@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int):

    for appointment in appointments:

        if appointment["id"] == appointment_id:

            appointments.remove(appointment)

            return {
                "message": "Appointment Deleted Successfully"
            }

    return {"message": "Appointment Not Found"}
# ==========================================
# Sample Billing Data
# ==========================================

bills = [
    {
        "id": 1,
        "patient_name": "Rahul",
        "amount": 2500,
        "payment_status": "Paid"
    },
    {
        "id": 2,
        "patient_name": "Priya",
        "amount": 1800,
        "payment_status": "Pending"
    }
]

# ==========================================
# GET ALL BILLS
# ==========================================

@app.get("/bills")
def get_bills():
    return bills


# ==========================================
# GET SINGLE BILL
# ==========================================

@app.get("/bills/{bill_id}")
def get_bill(bill_id: int):

    for bill in bills:

        if bill["id"] == bill_id:
            return bill

    return {
        "message": "Bill Not Found"
    }


# ==========================================
# ADD BILL
# ==========================================

@app.post("/bills")
async def add_bill(request: Request):

    bill = await request.json()

    bills.append(bill)

    return {
        "message": "Bill Added Successfully",
        "bill": bill
    }


# ==========================================
# UPDATE BILL
# ==========================================

@app.put("/bills/{bill_id}")
async def update_bill(bill_id: int, request: Request):

    updated_bill = await request.json()

    for index, bill in enumerate(bills):

        if bill["id"] == bill_id:

            bills[index] = updated_bill

            return {
                "message": "Bill Updated Successfully"
            }

    return {
        "message": "Bill Not Found"
    }


# ==========================================
# DELETE BILL
# ==========================================

@app.delete("/bills/{bill_id}")
def delete_bill(bill_id: int):

    for bill in bills:

        if bill["id"] == bill_id:

            bills.remove(bill)

            return {
                "message": "Bill Deleted Successfully"
            }

    return {
        "message": "Bill Not Found"
    }