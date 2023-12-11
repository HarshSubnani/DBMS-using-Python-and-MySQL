import mysql.connector as ms
import sys
#NOTE - First enter the required details below to establish connection to your MySQL server
mycon = ms.connect(host='', user='', password='', database='')
cursor = mycon.cursor()

#Patient Database

def print_pheader():
    print('_'*152)
    print('Patient ID      |','First Name    |',"Last Name     |",'Mobile Number |','Email ID              |','Admission reason       |','Admission date|','Discharge date|','Department    |')
    print('_'*152)
    
def view_pData():
    print_pheader()
    cursor.execute("select * from patient_info")
    mydata = cursor.fetchall()
    for j in mydata:
        for i in j:
            print("%11s"%i, end="\t|")
        print()
        
def delete_pData():
    p_id = int(input('\nEnter the Patient ID of the Patient to be deleted:'))
    query = 'select * from patient_info where p_id={}'.format(p_id)
    cursor.execute(query)
    data = cursor.fetchone()
    if data!=None:
        confirm = input('Are you sure to delete Patient Information(y/n)?  ')
        if (confirm.lower()=='y'):
            delete_query = 'delete from patient_info where p_id={}'.format(p_id)
            cursor.execute(delete_query)
            mycon.commit()
            print("\n\tPatient Information Succesfully Deleted!")
    else:
        print('\nPatient Not Found!')

def getlast_pid():
    cursor.execute('Select p_id from patient_info')
    data = cursor.fetchall()

    if data:
        last_pid = data[-1][0]
    else:
        last_pid = 0

    return last_pid

def add_patient():
    while True:
        p_id = getlast_pid() + 1
        name = input("\nEnter Patient First Name: ")
        name1= input("\nEnter Patient Last Name: ")
        mobile_no = int(input("\nEnter Mobile Number: "))
        email_id = input("\nEnter Email-ID: ")
        disease = input("\nEnter Admission Reason: ")
        d_ad = input("\nEnter Date of admission: ")
        dept = input("\nEnter Department (Outpatient/Inpatient): ")
        insert_query = "insert into patient_info(p_id,p_fname,p_lname,mobile_no,email_id,disease,d_ad,dept) values({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(p_id,name,name1,mobile_no,email_id,disease,d_ad,dept)
        cursor = mycon.cursor()
        cursor.execute(insert_query)
        mycon.commit()
        print("\n\tPatient Information Added Succesfully!")
        choice = input("Do you want to continue adding patient info(y/n)?")
        if choice.lower()=="y":
            continue
        else:
            pmain()
            
def search_patient(p_id):
    while True:
        query = 'select * from patient_info where p_id={}'.format(p_id)
        cursor.execute(query)
        data = cursor.fetchone()
        if data!=None:
            print_pheader()
            for j in data:
                print("%10s"%j, end="\t|")
            print()
            return True
        else:
            print('\n\tpatient Not Found!')
            return False
        choice=input("Do you want to continue searching patient info(y/n)?")
        if choice.lower()=="y":
            continue
        else:
            pmain()

def modpquery(field, new, p_id):
    mod_query = 'update patient_info set '+field+"='"+new+"' where p_id={}".format(p_id)
    cursor.execute(mod_query)
    mycon.commit()
    
def mod_patient(p_id):
    if search_patient(p_id) == True:
        while True:
            print("\n\tChoose what to modify")
            print("\n\t1.First Name of patient")
            print("\t2. Last Name of patient")
            print("\t3. Mobile Number")
            print("\t4. Email ID")
            print("\t5. Admission Reason")
            print("\t6. Date of Admission")
            print("\t7. Date of Discharge")
            print("\t8. Department (Outpatient / Inpatient)")
            print("\t0. Go back to main menu")
            ch = int(input("\n\tEnter your choice: "))
            if ch == 1:
                field = "p_fname"
                nfname = input("\nEnter New First Name: ")
                modpquery(field, nfname, p_id)
                print("\n\tFirst Name Succesfully Modified!")
            elif ch == 2:
                field = "p_lname"
                nlname = input("\nEnter New Last Name: ")
                modpquery(field, nlname, p_id)
                print("\n\tLast Name Succesfully Modified!")
            elif ch == 3:
                field = "mobile_no"
                nmob = input("\nEnter New Mobile Number: ")
                modpquery(field, nmob, p_id)
                print("\n\tMobile Number Succesfully Modified!")
            elif ch == 4:
                field = "email_id"
                nemail = input("\nEnter  New Email-Id: ")
                modpquery(field, nemail, p_id)
                print("\n\tEmail-ID Succesfully Modified!")
            elif ch == 5:
                field = "disease"
                ndis = input("\nEnter Disease name: ")
                modpquery(field, ndis, p_id)
                print("\n\tAdmission Reason Succesfully Modified!")
            elif ch == 6:
                field = "d_ad"
                naddate = input("\nEnter Admission date: ")
                modpquery(field, naddate, p_id)
                print("\n\tAdmission date Succesfully Modified!")
            elif ch == 7:
                field = "d_dis"
                ndisdate = input("\nEnter Discharge date: ")
                modpquery(field, ndisdate, p_id)
                print("\n\tDischarge date Succesfully Modified!")
            elif ch == 8:
                field = "dept"
                ndep = input("\nEnter Department(Outpatient/Inpatient): ")
                modpquery(field, ndep, p_id)
                print("\n\tDepartment Succesfully Modified!")
            elif ch == 0:
                pmain()
            else:
                print("\n\tInvalid Choice Try Again!")
                tryagain = input("Do you want to modify more(y/n)? ")
                if tryagain.lower()=="y":
                    continue
                else:
                    break
                    
def distinctp1(field):
    distinct = 'select distinct '+field+" from patient_info"
    cursor.execute(distinct)
    data = cursor.fetchall()
    return data
    
def distinctp2(field, sort):
    distinctp2 = 'select * from patient_info where '+field+'='+"'"+sort+"'"
    cursor.execute(distinctp2)
    data = cursor.fetchall()
    return data
    
def sort_pview():
    while True:
        print("\nChoose how to filter")
        print("\n\t1. Email-ID")
        print("\n\t2. Mobile Numbers")
        print("\n\t3. Admission Reason")
        print("\n\t4. Department")
        print("\n\t0. Go back to main menu")
        ch = int(input("\n\tEnter your choice: "))
        if ch == 1:
            f = "email_id"
            data = distinctp1(f)
            print('_'*20)
            print('%20s'%"EMAIL- ID")
            print('_'*20)
            for j in data:
                print("%11s"%j, end="\t|")
                print()
            sortby = input("\n\n\tEnter Email-id of Patients to be displayed: ")
            sortby = sortby.lower()
            disp = distinctp2(f, sortby)
            print_pheader()
            for i in disp:
                for j in i:
                    print("%11s"%j, end="\t|")
                print()
        elif ch == 2:
            f = "mobile_no"
            data = distinctp1(f)
            print('_'*20)
            print('%20s'%"Mobile Numbers")
            print('_'*20)
            for j in data:
                print("%11s"%j, end="\t|")
                print()
            sortby = input("\n\n\tEnter Mobile no. of patients to be displayed: ")
            sortby = sortby.lower()
            disp = distinctp2(f, sortby)
            print_pheader()
            for i in disp:
                for j in i:
                    print("%11s"%j, end="\t|")
                print()
        elif ch == 3:
            f = "disease"
            data = distinctp1(f)
            print('_'*20)
            print('%20s'%"DISEASES")
            print('_'*20)
            for j in data:
                print("%11s"%j, end="\t|")
                print()
            sortby = input("\n\n\tEnter Disease of patient to be displayed: ")
            sortby = sortby.lower()
            disp = distinctp2(f, sortby)
            print_pheader()
            for i in disp:
                for j in i:
                    print("%11s"%j, end="\t|")
                print()
        elif ch == 4:
            f = "dept"
            data = distinctp1(f)
            print('_'*20)
            print('%20s'%"DEPARTMENT")
            print('_'*20)
            for j in data:
                print("%11s"%j, end="\t|")
                print()
            sortby = input("\n\n\tEnter Department of patients to be displayed: ")
            sortby = sortby.lower()
            disp = distinctp2(f, sortby)
            print_pheader()
            for i in disp:
                for j in i:
                    print("%11s"%j, end="\t|")
                print()
        elif ch == 0:
            pmain()
        else:
            print("\n\tInvalid Choice Try Again!")
            tryagain = input("Do you want to view more patients in filtered view(y/n)? ")
            if tryagain.lower()=="y":
                continue
            else:
                break

#Staff database
            
def print_sheader():
    print('_'*145)    
    print('%11s'%'Staff ID\t|','%11s'%'Staff First Name\t|','%11s'%'Staff Last Name\t|','%11s'%'Mobile Number\t|','%25s'%'Profession\t|','%13s'%'Speciality')
    print('_'*145)
def view_sData():
    print_sheader()
    cursor.execute("select * from hos_staff")
    mydata = cursor.fetchall()
    for j in mydata:
        print('%11s'%j[0],'\t|','%20s'%j[1],'\t|','%20s'%j[2],'\t|','%11s'%j[3],'\t|','%21s'%j[4],'\t|','%13s'%j[5],'\t')
        print()

def delete_sData():
    emp_id = int(input('\nEnter the Staff ID of the Staff to be deleted:'))
    query = 'select * from hos_staff where emp_id={}'.format(emp_id)
    cursor.execute(query)
    data = cursor.fetchone()
    if data!=None:
        confirm = input('Are you sure to delete Staff Information(y/n)?  ')
        if (confirm.lower()=='y'):
            delete_query = 'delete from hos_staff where emp_id={}'.format(emp_id)
            cursor.execute(delete_query)
            mycon.commit()
            print("\n\tStaff Information Succesfully Deleted!!!!")
    else:
        print('\nStaff Not Found!')

def getlast_sid():
    cursor.execute('SELECT emp_id FROM hos_staff')
    data = cursor.fetchall()

    if data:
        last_empid = data[-1][0]
    else:
        last_empid = 0

    return last_empid

    
def add_staff():
    while True:
        emp_id = getlast_sid() + 1
        name = input("\nEnter Staff First Name: ")
        name1= input("\nEnter Staff Last Name: ")
        mobile_no = int(input("\nEnter Mobile Number: "))
        prof= input("\nEnter Profession: ")
        speciality=input("\nEnter speciality of Staff:")
        insert_query = "insert into hos_staff values({0},'{1}','{2}','{3}','{4}','{5}')".format(emp_id,name,name1,mobile_no,prof,speciality)
        cursor = mycon.cursor()
        cursor.execute(insert_query)
        mycon.commit()
        print("\n\tStaff Information Added Succesfully!!!")
        choice = input("Do you want to continue adding Staff info(y/n)?")
        if choice.lower()=="y":
            continue
        else:
            smain()
            
def search_staff(emp_id):
    while True:
        query = 'select * from hos_staff where emp_id={}'.format(emp_id)
        cursor.execute(query)
        data = cursor.fetchone()
        if data!=None:
            print_sheader()
            for j in data:
                print("%15s"%j, end="\t|")
            print()
            return True
        else:
            print('\n\tStaff Not Found!!!!!!')
            return False
        choice=input("Do you want to continue searching Staff info(y/n)?")
        if choice.lower()=="y":
            continue
        else:
            smain()
            
def modsquery(field, new, emp_id):
    mod_query = 'update hos_staff set '+field+"='"+new+"' where emp_id={}".format(emp_id)
    cursor.execute(mod_query)
    mycon.commit()
    
def mod_staff(emp_id):
    if search_staff(emp_id) == True:
        while True:
            print("\n\tChoose what to modify")
            print("\n\t1.First Name of Staff")
            print("\t2. Last Name of Staff")
            print("\t3. Mobile Number")
            print("\t4. Profession")
            print("\t5. Speciality")
            print("\t0. Go back to main menu")
            ch = int(input("\n\tEnter your choice: "))
            if ch == 1:
                field = "emp_fname"
                nfname = input("\nEnter New First Name: ")
                modsquery(field, nfname, emp_id)
                print("\n\tFirst Name Succesfully Modified !!!!")
            elif ch == 2:
                field = "emp_lname"
                nlname = input("\nEnter New Last Name: ")
                modsquery(field, nlname, emp_id)
                print("\n\tLast Name Succesfully Modified !!!!")
            elif ch == 3:
                field = "mobile_no"
                nmob = input("\nEnter New Mobile Number: ")
                modsquery(field, nmob, emp_id)
                print("\n\tMobile Number Succesfully Modified !!!!")
            elif ch == 4:
                field = "prof"
                nemail = input("\nEnter  New Profession: ")
                modsquery(field, nemail, emp_id)
                print("\n\tProfession Succesfully Modified !!!!")
            elif ch == 5:
                field = "speciality"
                nemail = input("\nEnter  New Speciality: ")
                modsquery(field, nemail, emp_id)
                print("\n\tSpeciality Succesfully Modified !!!!")
            elif ch == 0:
                smain()
            else:
                print("\n\tInvalid Choice Try Again!")
                tryagain = input("Do you want to modify more(y/n)? ")
                if tryagain.lower()=="y":
                    continue
                else:
                    break
                    
def distincts1(field):
    distinct = 'select distinct '+field+" from hos_staff"
    cursor.execute(distinct)
    data = cursor.fetchall()
    return data
    
def distincts2(field, sort):
    distincts2 = 'select * from hos_staff where '+field+'='+"'"+sort+"'"
    cursor.execute(distincts2)
    data = cursor.fetchall()
    return data
    
def sort_sview():
    while True:
        print("\nChoose how to filter")
        print("\n\t1. Profession")
        print("\n\t2. Mobile Numbers")
        print("\n\t0. Go back to main menu")
        ch = int(input("\n\tEnter your choice: "))
        if ch == 1:
            f = "prof"
            data = distincts1(f)
            print('_'*20)
            print('%20s'%"PROFESSION")
            print('_'*20)
            for j in data:
                print("%15s"%j, end="\t|")
                print()
            sortby = input("\n\n\tEnter Profession of Staff to be displayed: ")
            sortby = sortby.lower()
            disp = distincts2(f, sortby)
            print_sheader()
            for i in disp:
                for j in i:
                    print("%15s"%j, end="\t|")
                print()
        elif ch == 2:
            f = "mobile_no"
            data = distincts1(f)
            print('_'*20)
            print('%20s'%"Mobile Numbers")
            print('_'*20)
            for j in data:
                print("%15s"%j, end="\t|")
                print()
            sortby = input("\n\n\tEnter Mobile no. of staff to be displayed: ")
            sortby = sortby.lower()
            disp = distincts2(f, sortby)
            print_sheader()
            for i in disp:
                for j in i:
                    print("%15s"%j, end="\t|")
                print()
        elif ch == 0:
            smain()
        else:
            print("\n\tInvalid Choice Try Again!")
            tryagain = input("Do you want to view more patients in filtered view(y/n)? ")
            if tryagain.lower()=="y":
                continue
            else:
                break

#Appointment database

def print_eheader():
    print('_'*65)    
    print('%11s'%'Appointment ID\t|','%20s'%'Patient Name\t|','%11s'%'Treatment')
    print('_'*65)
def view_eData():
    print_eheader()
    cursor.execute("select * from appoint_sch")
    mydata = cursor.fetchall()
    for j in mydata:
        print('%11s'%j[0],'\t|','%20s'%j[1],'\t|','%20s'%j[2],'\t|')
        print()

def delete_eData():
    app_no = int(input('\nEnter the patient ID of the patient to be deleted:'))
    query = 'select * from appoint_sch where app_no={}'.format(app_no)
    cursor.execute(query)
    data = cursor.fetchone()
    if data!=None:
        confirm = input('Are you sure to delete patient Information(y/n)?  ')
        if (confirm.lower()=='y'):
            delete_query = 'delete from appoint_sch where app_no={}'.format(app_no)
            cursor.execute(delete_query)
            mycon.commit()
            print("\n\tPatient Information Succesfully Deleted!!!!")
    else:
        print('\npatient Not Found!')

def getlast_eid():
    cursor.execute('Select app_no from appoint_sch')
    data = cursor.fetchall()

    if data:
        last_empid = data[-1][0]
    else:
        last_empid = 0

    return last_empid

def add_app():
    while True:
        app_no = getlast_eid() + 1
        name = input("\nEnter patient Name: ")
        treat= input("\nEnter Treatment: ")
        insert_query = "insert into appoint_sch values({0},'{1}','{2}')".format(app_no,name,treat)
        cursor = mycon.cursor()
        cursor.execute(insert_query)
        mycon.commit()
        print("\n\tPatient Information Added Succesfully!!!")
        choice = input("Do you want to continue adding patient info(y/n)?")
        if choice.lower()=="y":
            continue
        else:
            emain()
            
def search_app(app_no):
    while True:
        query = 'select * from appoint_sch where app_no={}'.format(app_no)
        cursor.execute(query)
        data = cursor.fetchone()
        if data!=None:
            print_eheader()
            for j in data:
                print("%15s"%j, end="\t|")
            print()
            return True
        else:
            print('\n\tpatient Not Found!!!!!!')
            return False
        choice=input("Do you want to continue searching patient info(y/n)?")
        if choice.lower()=="y":
            continue
        else:
            smain()
            
def modequery(field, new, app_no):
    mod_query = 'update appoint_sch set '+field+"='"+new+"' where app_no={}".format(app_no)
    cursor.execute(mod_query)
    mycon.commit()
    
def mod_app(app_no):
    if search_app(app_no) == True:
        while True:
            print("\n\tChoose what to modify")
            print("\n\t1.Name of patient")
            print("\t2. Treatment")
            print("\t0. Go back to main menu")
            ch = int(input("\n\tEnter your choice: "))
            if ch == 1:
                field = "p_name"
                nfname = input("\nEnter New Name: ")
                modequery(field, nfname, app_no)
                print("\n\tName Succesfully Modified!")
            elif ch == 2:
                field = "Treatment"
                nemail = input("\nEnter  New Treatment: ")
                modequery(field, nemail, app_no)
                print("\n\tProfession Succesfully Modified!")
            elif ch == 0:
                emain()
            else:
                print("\n\tInvalid Choice Try Again!")
                tryagain = input("Do you want to modify more(y/n)? ")
                if tryagain.lower()=="y":
                    continue
                else:
                    break
                    
def distincte1(field):
    distinct = 'select distinct '+field+" from appoint_sch"
    cursor.execute(distinct)
    data = cursor.fetchall()
    return data
    
def distincte2(field, sort):
    distincte2 = 'select * from appoint_sch where '+field+'='+"'"+sort+"'"
    cursor.execute(distincte2)
    data = cursor.fetchall()
    return data
    
def sort_eview():
    while True:
        print("\nChoose how to filter")
        print("\n\t1. Treatment")
        print("\n\t0. Go back to main menu")
        ch = int(input("\n\tEnter your choice: "))
        if ch == 1:
            f = "treatment"
            data = distincte1(f)
            print('_'*20)
            print('%20s'%"Treatment")
            print('_'*20)
            for j in data:
                print("%15s"%j, end="\t|")
                print()
            sortby = input("\n\n\tEnter Treatment of patient to be displayed: ")
            sortby = sortby.lower()
            disp = distincte2(f, sortby)
            print_eheader()
            for i in disp:
                for j in i:
                    print("%15s"%j, end="\t|")
                print()
        elif ch == 0:
            emain()
        else:
            print("\n\tInvalid Choice Try Again!")
            tryagain = input("Do you want to view more Appointments in filtered view(y/n)? ")
            if tryagain.lower()=="y":
                continue
            else:
                break
                
#main (patient)

def pmain():
    print()
    print("**"*20,"Hospital Patient Database","**"*20)
    while True:
        print("\n\t1. View all Patient's information")
        print("\n\t2. Add new Patients")
        print("\n\t3. Search for a patient")
        print("\n\t4. Delete a Patient")
        print("\n\t5. Modify Patient Details")
        print("\n\t6. Filtered View")
        print("\n\t0. Exit Program")
        ch = int(input("\n\tEnter your choice: "))
        if ch == 1:
            view_pData()
        elif ch == 2:
            add_patient()
        elif ch == 3:
            adm = int(input('\nEnter the Patient ID of the Patient to be found: '))
            search_patient(adm)
        elif ch == 4:
            delete_pData()
        elif ch == 5:
            adm = int(input('\nEnter the Patient ID of the Patient to be found: '))
            mod_patient(adm)
        elif ch == 6:
            sort_pview()
        elif ch == 0:
            main()
        else:
            print("\n\tInvalid Choice Try Again!")
            tryagain = input("DO you want to continue(y/n)? ")
            if tryagain.lower()=="y":
                continue
            else:
                break

#main (staff)

def smain():
    print()
    print("**"*20,"Hospital Staff Database","**"*20)
    while True:
        print("\n\t1. View all Staff's information")
        print("\n\t2. Add new Staffs")
        print("\n\t3. Search for a Staff")
        print("\n\t4. Delete a Staff")
        print("\n\t5. Modify Staff Details")
        print("\n\t6. Filtered View")
        print("\n\t0. Exit Program")
        ch = int(input("\n\tEnter your choice: "))
        if ch == 1:
            view_sData()
        elif ch == 2:
            add_staff()
        elif ch == 3:
            adm = int(input('\nEnter the Staff ID of the Staff to be found: '))
            search_staff(adm)
        elif ch == 4:
            delete_sData()
        elif ch == 5:
            adm = int(input('\nEnter the Staff ID of the Staff to be found: '))
            mod_staff(adm)
        elif ch == 6:
            sort_sview()
        elif ch == 0:
            main()
        else:
            print("\n\tInvalid Choice Try Again!")
            tryagain = input("DO you want to continue(y/n)? ")
            if tryagain.lower()=="y":
                continue
            else:
                break

#main (appointment)

def emain():
    print()
    print("**"*20,"Hospital Appointment Database","**"*20)
    while True:
        print("\n\t1. View all Appointment's information")
        print("\n\t2. Book / Add new Appointments")
        print("\n\t3. Search for a Appointment")
        print("\n\t4. Delete a Appointment")
        print("\n\t5. Modify Appointment Details")
        print("\n\t6. Filtered View")
        print("\n\t0. Exit Program")
        ch = int(input("\n\tEnter your choice: "))
        if ch == 1:
            view_eData()
        elif ch == 2:
            add_app()
        elif ch == 3:
            adm = int(input('\nEnter the Appointment ID of the Appointment to be found: '))
            search_app(adm)
        elif ch == 4:
            delete_eData()
        elif ch == 5:
            adm = int(input('\nEnter the Appointment ID of the Appointment to be found: '))
            mod_app(adm)
        elif ch == 6:
            sort_eview()
        elif ch == 0:
            main()
        else:
            print("\n\tInvalid Choice Try Again!")
            tryagain = input("DO you want to continue(y/n)? ")
            if tryagain.lower()=="y":
                continue
            else:
                break
                

def main():
    print()
    print("**"*20,"Hospital Database","**"*20)
    while True:
        print("\n\t1. Display/view/edit Patient Database")
        print("\n\t2. Display/view/edit Staff Database")
        print("\n\t3. Display/view/edit Appointment Database")
        print("\n\t0. Exit Program")
        ch = int(input("\n\tEnter your Choice:  "))
        if ch == 1:
            pmain()
        elif ch == 2:
            smain()
        elif ch== 3:
            emain()
        elif ch == 0:
            sys.exit()
        else:
            print("\n\tInvalid Choice Try Again!")
            tryagain = input("Do you want to continue(y/n)? ")
            if tryagain.lower()=="y":
                continue
            else:
                break
main()
