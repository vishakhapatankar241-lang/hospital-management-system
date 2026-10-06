import mysql.connector


# ==========================================
# DATABASE CONNECTION
# ==========================================

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vishu",
    database="hospitaldb"
)

cursor = db.cursor()

print("Connection Done...!")


# ==========================================
# PARENT CLASS
# ==========================================

class User:

    def __init__(self, username, role):
        self.username = username
        self.role = role

    def show_role(self):
        print("Role:", self.role)


# ==========================================
# CHILD CLASS - DOCTOR
# ==========================================

class Doctor(User):

    def doctor_details(self):
        print("Doctor can manage appointments..!")


# ==========================================
# CHILD CLASS - PATIENT
# ==========================================

class Patient(User):

    def patient_details(self):
        print("Patient can view details..!")


# ==========================================
# CHILD CLASS - CHEMIST
# ==========================================

class Chemist(User):

    def chemist_details(self):
        print("Chemist can manage medicines..!")


# ==========================================
# LOGIN FUNCTION
# ==========================================

def login():

    username = input("Enter username: ")
    password = input("Enter password: ")

    query = """
    SELECT username, role
    FROM users
    WHERE username=%s AND passwod=%s
    """

    cursor.execute(query, (username, password))

    result = cursor.fetchone()

    if result:

        print("\nLogin Successful..!")
        print("Welcome:", result[0])
        print("Role:", result[1])

        return result[0], result[1]

    else:

        print("\nInvalid Username Or Password")

        return None, None


# ==========================================
# CREATE - ADD PATIENT
# ==========================================

def add_patient():

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")

    query = """
    INSERT INTO patient(name, age, gender, disease)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (name, age, gender, disease))

    db.commit()

    print("\nPatient Added Successfully..!")


# ==========================================
# READ - VIEW PATIENTS
# ==========================================

def view_patients():

    query = "SELECT * FROM patient"

    cursor.execute(query)

    results = cursor.fetchall()

    print("\n========== Patient Records ==========")

    if results:

        for row in results:

            print(
                "Patient ID:", row[0],
                "| Name:", row[1],
                "| Age:", row[2],
                "| Gender:", row[3],
                "| Disease:", row[4]
            )

    else:

        print("No Patient Records Found.")


# ==========================================
# UPDATE - UPDATE PATIENT
# ==========================================

def update_patient():

    patient_id = int(input("Enter Patient ID to Update: "))

    new_disease = input("Enter Updated Disease: ")

    query = """
    UPDATE patient
    SET disease=%s
    WHERE patient_id=%s
    """

    cursor.execute(query, (new_disease, patient_id))

    db.commit()

    if cursor.rowcount > 0:

        print("\nPatient Updated Successfully..!")

    else:

        print("\nPatient ID Not Found.")


# ==========================================
# DELETE - DELETE PATIENT
# ==========================================

def delete_patient():

    patient_id = int(input("Enter Patient ID to Delete: "))

    query = """
    DELETE FROM patient
    WHERE patient_id=%s
    """

    cursor.execute(query, (patient_id,))

    db.commit()

    if cursor.rowcount > 0:

        print("\nPatient Deleted Successfully..!")

    else:

        print("\nPatient ID Not Found.")


# ==========================================
# PATIENT MANAGEMENT MENU
# ==========================================

def patient_menu():

    while True:

        print("\n")
        print("====================================")
        print("     PATIENT MANAGEMENT SYSTEM")
        print("====================================")

        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            add_patient()

        elif choice == 2:

            view_patients()

        elif choice == 3:

            update_patient()

        elif choice == 4:

            delete_patient()

        elif choice == 5:

            print("Thank You..!")
            break

        else:

            print("Invalid Choice!")


# ==========================================
# MAIN PROGRAM
# ==========================================

username, role = login()


# ==========================================
# ROLE CHECK
# ==========================================

if role == "Admin":

    print("\n========== ADMIN DASHBOARD ==========")

    print("Admin can manage patients.")

    patient_menu()


elif role == "Doctor":

    print("\n========== DOCTOR DASHBOARD ==========")

    doctor = Doctor(username, role)

    doctor.show_role()

    doctor.doctor_details()


elif role == "Patient":

    print("\n========== PATIENT DASHBOARD ==========")

    patient = Patient(username, role)

    patient.show_role()

    patient.patient_details()


elif role == "Chemist":

    print("\n========== CHEMIST DASHBOARD ==========")

    chemist = Chemist(username, role)

    chemist.show_role()

    chemist.chemist_details()


else:

    print("\nAccess Denied..!")


# ==========================================
# CLOSE DATABASE CONNECTION
# ==========================================

cursor.close()
db.close()

