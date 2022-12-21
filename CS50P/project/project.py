import sys
from datetime import datetime
import pyfiglet



def main():
    print(pyfiglet.figlet_format("Welcome to booking with Huzaifa"))
    ans = input("Do you want to book an appointment? (yes/no)")
    if ans == ("yes"):
        print ("We are delighted to assist you. To begin, enter the information shown below.")
        #Ask for information
        user_information()
        #Ask if they wanna register for examinations
        examregister()

    else:
        SystemExit()

def user_information():

    #Ask for full name and check if its correct
    while True:
        name = input("Enter your full name: ")
        if len(name.split())<2:
            print ("Not Valid")
        else:
            break

    #Ask for date of birth and check if its correct.
    while True:
        bday = input("Birthdate (day/month/year): ")
        try:
            bday1 = datetime.strptime(bday, '%d/%m/%Y')
            break
        except ValueError:
            print("Incorrect format")
            continue


    #Ask for nationality.
    nationality = input ("Nationalty: ")

    #Check emirates ID number
    emirates_id = int(input("Emirates ID Number: "))

    #Show user entered information and ask user if he wants to make change to any info entered
    print("----------------------------------------------------")
    print(f"Name: {name}\nDate of Birth: {bday}\nNationality: {nationality}\nEmirates ID Number: {emirates_id}")
    print("----------------------------------------------------")

    ask_for_change = input ("Do you want to edit any information entered? (yes/no)")
    if ask_for_change == ("yes"):
        user_information()
    if ask_for_change == ("no"):
        print ("\nChecking your information...\n")
        print ("Please wait...\n")
        print ("Information Checked. Now you're ready to book an appointment\n")
    subject_selection()

def subject_selection():
    subjects = ["Math", "Science", "English"]
    while True:
        subject_selected = input("What subject teachers appointment do you wanna book ? (math/english/science): ")
        if subject_selected == "math":
            math_teacher()
            break
        elif subject_selected == "english":
            english_teacher()
            break
        elif subject_selected == "science":
            science_teacher()
            break



def english_teacher():
    eng_teachers =  ["Nabeela", "Nazia", "Liji", "Krishna"]
    #Print name of english teachers and ask user to choose one
    for z in eng_teachers:
        print(f"Ms.{z}")
    teacher = input ("Please enter the name of the teacher you want to book an appointment of: ")
    teachers_list(teacher)

def math_teacher():
    math_teachers = ["Raj", "Sulogna", "Usha", "Namrata"]
    #Print name of math teachers and ask user to choose one
    for z in math_teachers:
        print(f"Ms.{z}")
    teacher = input ("Please enter the name of the teacher you want to book an appointment of: ")
    teachers_list(teacher)



def science_teacher():
    science_teachers = ["Noline", "Melainie", "Riza", "Jinny" ]
    #Print name of science teachers and ask user to choose one
    for z in math_teachers:
        print(f"Ms.{z}")
    teacher = input ("Please enter the name of the teacher you want to book an appointment of: ")
    teachers_list(teacher)

def teachers_list(teacher):
    teachers = ["Noline", "Melainie", "Riza", "Jinny","Raj", "Sulogna", "Usha", "Namrata","Nabeela", "Nazia", "Liji", "Krishna"]
    if teacher in teachers:
        print("Perfect")
    else:
        print("Invalid Selection")
        sys.exit()

    while True:
        timeoptions = ["07 AM", "08 AM", "09 AM", "10 AM", "11 AM" , "12 PM", "1 PM", "2 PM"]
        for i in timeoptions:
            print(i)
        time1 =  input("Please select at what time you would like your appointment: ")
        if time1 in timeoptions:
            print("Checking if the teacher is avalaible...")
            print ("Slots are still avalaible!")
            break
        else:
            print("Choose from the time available")

def examregister():
    yesorno = input("Do you wanna register for IGCSE examination ?: (yes/no)")
    if yesorno == "yes":
        placeOrder()
    elif yesorno == "no":
        print("Thank you for using booking with Huzaifa!")
        sys.exit


shopping = [{"Exam": "English", "Name": "0500",   "Price": 250},
            {"Exam": "Maths", "Name": "0580",   "Price": 350},
            {"Exam": "Physics", "Name": "0625",   "Price": 280},
            {"Exam": "Chemistry", "Name": "0620",   "Price": 600},
            {"Exam": "Biology", "Name": "0610",   "Price": 240},
            {"Exam": "Business", "Name": "0450",   "Price": 350},
            {"Exam": "Economics", "Name": "0455",   "Price": 150},
            {"Exam": "Accounting", "Name": "0452",   "Price": 450},
            {"Exam": "Arabic", "Name": "0544",   "Price": 200},
            {"Exam": "Urdu", "Name": "0539",   "Price": 120}]

def placeOrder():
    p_Exam = input("\nEnter the Exam : ")

    for d in shopping:
        if d["Exam"] == p_Exam:
            print("\nExam\tExam Code\tPrice")
            print("=============================================================")
            print(f'{d["Exam"]}\t{d["Name"]}\t\t{d["Price"]}')
            order = '{d["Exam"]}\t{d["Name"]}\t\t{d["Price"]}'
            conform = input("\nDo you want to place an order on the above shown product : Y/N ")

            if conform == 'Y' or conform == 'y':
                paying_creds()
                print("\nSuccessfully registered for {} {}".format(d["Exam"], d["Name"]))
                break

            elif conform == 'N' or conform == 'n':
                print("Registeration Cancelled!")
                break
            else:
                print("\nYou have entered wrong option. Please enter again\n")
                conform = input("\nDo you want to place an order on the above shown product : Y/N ")
                break


def paying_creds():
    print ("Please enter your credit card information")
    cc = input("What type of credit card do you have? (Mastercard/Paypal) ")
    if cc == ("Mastercard"):
        Mastercard_f()

    if cc == ("Paypal"):
        Paypal_f()

    while True:
        end = input("Do you want to proceed with the payment? (yes/no) ")
        if end == ("yes"):
            print ("Validating payment...")
            break
        else:
            xcx = input("Do you want to cancel your booking? (yes/no) ")
            if xcx == ("y"):
                sys.exit()
            else:
                pass

def Mastercard_f():
    while True:
        owner = input("Owner of the card: ")
        if len(owner.split())<2:
            print ("Invalid Name ")
        else:
            break
    creditcardno = int (input("Credit card number: "))
    expirydate = input("Expiration Date (month/year): ")
    cvc = int (input("CVC: "))

def Paypal_f():
    username = input("Username/E-mail: ")
    password = input ("Password: ")

main()