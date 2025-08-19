import tkinter as tk
from Admin import Admin
from Doctor import Doctor
from Patient import Patient
from tkinter import ttk

class GUI():
    def __init__(self):
        self.admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
        self.doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
        self.patients = [Patient('Sara','Smith', 20, '07012345678','B1 234','Headache'), Patient('Mike','Jones', 37,'07555551234','L2 2AB','Headache'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC','Common Cold')]
        self.discharged_patients = []
        self.admin_login_GUI()

    def admin_login_GUI(self):
        self.root = tk.Tk()
        self.root.title("Hospital Management-Login Admin")
        self.root.geometry("500x500")
        self.root.configure(bg="#E5E1DA")

# Heading Label
        label_heading = tk.Label(self.root, text="Admin", font=("Arial", 20, "bold"), bg="#F1E4C3", fg="black")
        label_heading.pack(pady=15)

# Username Label and Entry
        label_username = tk.Label(self.root, text="Username:", font=("Arial", 12), bg="#F1E4C3", fg="black")
        label_username.pack(pady=5)
        self.entry_username = tk.Entry(self.root, font=("Arial", 12),bd=0)
        self.entry_username.pack()
        
# Password Label and Entry
        label_password = tk.Label(self.root, text="Password:", font=("Arial", 12), bg="#F1E4C3", fg="black")
        label_password.pack(pady=6)
        self.entry_password = tk.Entry(self.root, show="*", font=("Arial", 12),bd=0)
        self.entry_password.pack()

# Login Button
        btn_login = tk.Button(self.root, text="Login", command=self.login, font=("Arial", 12),bd=0, bg="#000000", fg="white", width=10)
        btn_login.pack(pady=20)

        self.label_result = tk.Label(self.root, text="", font=("Arial", 20), fg="white")
        self.root.mainloop()

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        self.label_result.pack()
        if(self.admin.login(username,password)):
            self.label_result.config(text="Login Successful", fg="green",bg="#FFFFFF",padx=2)
            self.main_menu()
        else:
            self.label_result.config(text="Login Failed", fg="red")
    
    def main_menu(self):
        root = tk.Tk()
        root.title("Main Panel")

# Define the options
        options = [
            (" 1- Register/view/update/delete doctor", self.option1_method),
            (" 2- Discharge patients", self.option2_method),
            (" 3- View discharged patient", self.option3_method),
            (" 4- Assign doctor to a patient", self.option4_method),
            (" 5- Update admin details", self.option5_method),
            (" 6- Generate Management Report", self.option6_method),
            (" 7- View all the patients", self.option7_method),
            (" 8- View all the patients with same surname", self.option8_method),
            ("Quit", self.option9_method)]



# Customize front-end design
        root.configure(bg="#B4B4B8")  # Set background color
        root.geometry("500x600")


        label_font = ("Arial", 18, "bold")  # Set label font
        button_font = ("Arial", 12, "bold")  # Set button font

# Create label
        label = tk.Label(root, text="Choose an operation", font=label_font, bg="#F2EFE5")
        label.pack(pady=20)

# Create buttons for each option
        for option, method in options:
            button = tk.Button(root, text=option, font=button_font, bg="#F7F7F7", fg="black", padx=10, pady=5, command=method,width=40,bd=0)
            button.pack(pady=5)
        root.mainloop()
    
    def option1_method(self):
        # self.doctor_main_panel()
        self.admin.doctor_management(self.doctors)

    def option2_method(self):
        patients=self.admin.read_patientRecords()
        self.discharge_patients(patients)
       
    def option3_method(self):
        self.view_everything(self.discharged_patients)

    def option4_method(self,):
        Admin.assign_doctor_to_patient(self.patients,self.doctors)
        self.look_terminal()

    def option5_method(self):
        self.update_admin_details()

    def option6_method(self):
        Admin.get_report(self.doctors,self.patients)
        self.look_terminal()
    def option7_method(self):
        file=self.admin.read_patientRecords()
        self.view_everything(file)

    def option8_method(self):
        self.group_patients(self.patients)

    def option9_method():
        quit()


g=GUI()