import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "ind_pjc_owner_info"
)

mycursor = mydb.cursor()
    
def collect_data():
    accepted = accept_var.get()
    dt = d_b_entry.get()
    mt = m_b_entry.get()
    yr = y_b_entry.get()
    today = date.today()
    birthdate = date(int(yr), int(mt), int(dt))
    age = today.year - birthdate.year #((today.month, today.day) < (birthdate.month, birthdate.day))

    output_age = tk.Label(cat_owner_frame, text=f"{age} Year",fg="white", bg="#836953")
    output_age.grid(row=4, column=1) 

    if accepted == "Accepted":
        name = owner_name_entry.get()
        dbirth = d_b_entry.get()
        mbirth = m_b_entry.get()
        ybirth = y_b_entry.get()
        address = owner_address_entry.get()
        phone = owner_phone_entry.get()
        email = owner_email_address_entry.get()

        if name and address and phone and email:  
            cat = cat_name_entry.get()
            cat_age = cat_age_spinbox.get()
            cat_breed = cat_breed_combobox.get()

            print("Name: ", name)
            print("Birth Date:", dbirth, "/", mbirth, "/", ybirth)
            print("Age:", age,"Year")
            print("Address:", address)
            print("Contact No:", phone)
            print("Email:", email)
            print(".............")
            print("Cat Name:", cat)
            print("Age:", cat_age)
            print("Breed:", cat_breed)
            print("---------------------------------------------------------------")
        else:
            tk.messagebox.showwarning(title= "Error", message= "There are items that require your attention!")
    else:
        tk.messagebox.showwarning(title= "Error", message= "You have not accepted the terms!")  
 
    sql = "INSERT INTO registration (NAME, AGE, ADDRESS, PHONE_NO, EMAIL, CAT_NAME, CAT_AGE, CAT_BREED) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (name,age, address, phone, email, cat, cat_age, cat_breed)
    mycursor.execute(sql, val)
    mydb.commit()

root = tk.Tk()
root.geometry("520x365")
root['background'] = '#836953'
root.title("Cat Owner Registration")

label = tk.Label(root, text = "Customer Registration", font = ('Comic Sans MS bold', 18), fg="white", bg="#836953")
label.pack(padx=20, pady=1)

frame = tk.Frame(root, bg="#836953")
frame.pack()

#owner
cat_owner_frame = tk.LabelFrame(frame, text = "Personal Detail", fg="white", bg="#836953")
cat_owner_frame.grid(row= 0, column=0, sticky="News", padx=1, pady=1)

owner_name_label = tk.Label(cat_owner_frame, text="Name :", fg="white", bg="#836953")
owner_name_label.grid(row=0, column=0)
owner_name_entry = tk.Entry(cat_owner_frame)
owner_name_entry.grid(row=0, column=1)

owner_birth_date = tk.Label(cat_owner_frame, text="Birth Date :", fg="white", bg="#836953")
owner_birth_date.grid(row=1, column=0)

d_b_entry = ttk.Combobox(cat_owner_frame, values=["1","2","3","4","5","6","7","8","9","10",
                                                  "11","12","13","14","15","16","17","18","19","20",
                                                  "21","22","23","24","25","26","27","28","29","30","31"]) 
d_b_entry.grid(row=1, column=1)
d_b_entry.set("Select day")
d_b_entry["state"] = 'readonly'

m_b_entry = ttk.Combobox(cat_owner_frame, values=["01","02","03","04","05","06",
                                                  "07","08","09","10","11","12"]) 
m_b_entry.grid(row=2, column=1)
m_b_entry.set("Select month")
m_b_entry["state"] = 'readonly'

y_b_entry = ttk.Combobox(cat_owner_frame, values=list(range(1960, 2200)))
y_b_entry.grid(row=3, column=1)
y_b_entry.set("select year")
y_b_entry["state"] = 'readonly'

owner_age_label = tk.Label(cat_owner_frame, text="Age :", fg="white", bg="#836953")
owner_age_label.grid(row=4, column=0)

owner_address_label = tk.Label(cat_owner_frame, text="Address :", fg="white", bg="#836953")
owner_address_label.grid(row=5, column=0)
owner_address_entry = tk.Entry(cat_owner_frame)
owner_address_entry.grid(row=5, column=1)

owner_phone_label = tk.Label(cat_owner_frame, text="Contact No :", fg="white", bg="#836953")
owner_phone_label.grid(row=6, column=0)
owner_phone_entry = tk.Entry(cat_owner_frame)
owner_phone_entry.grid(row=6, column=1)

owner_email_address_label = tk.Label(cat_owner_frame, text="Email Address :", fg="white", bg="#836953")
owner_email_address_label.grid(row=7, column=0)
owner_email_address_entry = tk.Entry(cat_owner_frame)
owner_email_address_entry.grid(row=7, column=1)

for widget in cat_owner_frame.winfo_children():
    widget.grid_configure(padx= 10, pady=5)

#cat
cat_frame = tk.LabelFrame(frame, text="Cat Details", fg="white", bg="#836953")
cat_frame.grid(row=0, column=1, sticky="News", padx=1, pady=1)

cat_name_label = tk.Label(cat_frame, text="Name :", fg="white", bg="#836953")
cat_name_label.grid(row=0, column=0)
cat_name_entry = tk.Entry(cat_frame)
cat_name_entry.grid(row=0, column=1)

cat_age_label = tk.Label(cat_frame, text="Age :", fg="white", bg="#836953")
cat_age_label.grid(row=1, column=0)
cat_age_spinbox = ttk.Combobox(cat_frame, values=["Kitten(0-1)", "Young Adult(1-6)", "Mature Adult(7-10)", "Senior(>10)"])
cat_age_spinbox.grid(row=1, column=1)
cat_age_spinbox.set("Choose age")
cat_age_spinbox["state"] = 'readonly'

cat_breed_label = tk.Label(cat_frame, text="Breed :", fg="white", bg="#836953")
cat_breed_label.grid(row=2, column=0)
cat_breed_combobox = ttk.Combobox(cat_frame, values=["Domestic", "American", "Siamese", "Maine Coon", "Ragdoll", 
                                                     "Russian Blue", "Bengal", "Bombay", "Persian"])
cat_breed_combobox.grid(row=2, column=1)
cat_breed_combobox.set("Choose breed")
cat_breed_combobox["state"] = 'readonly'

for widget in cat_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#terms
terms_frame = tk.LabelFrame(frame, text="Terms & Condition", fg="white", bg="#836953")
terms_frame.grid(row=2, column=0, sticky="News", padx=1, pady=1)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame, text="I accept the terms and condition.", fg="#3d251e",
                             variable=accept_var, onvalue="Accepted", offvalue="Not Accepted", bg="#836953")
terms_check.grid(row=0, column=0)

#enter button
enter_button = tk.Button(frame, text="Enter", bg="white", command= collect_data)
enter_button.place(x=325, y=283, width=90, height=30)

close_button = tk.Button(frame, text="Close", bg="white", command=root.destroy)
close_button.place(x=416, y=283, width=90, height=30)

root.mainloop()