import io
import json
import os

schoolDict={"Schools":{}}


if os.path.exists("dynamic.json"):
    with open('dynamic.json') as f:
        schoolDict=json.loads(f.read())
print(schoolDict)

def add():
    print('Pls fill below students details')
    name = input('Enter name: ')
    roll_no = input('Enter roll number: ')
    address = input("Add the address: ")
    father_name = input('Enter Fathers name: ')
    mother_name = input('Enter Mothers name: ')
    details = print("Added Successfully!!!\nName:{}\nAddress:{}\nFather_name:{}\nMothersname:{}".format(name,address,father_name,mother_name))
    payload={
            "name":name,
            "address":address,
            "father_name":father_name,
            "mother_name":mother_name
            }
    return payload,roll_no


print('Pls Select Your Request')
print('1. Enroll Student')
print('2. Update Student Info')
print('3. Remove Student')
print('4. Fetch Student Details')
print('5. Quit')

while True:
    operation  = input('Enter Your query: ')
    if operation == "5":
        break

    # Enroll Operation
    elif operation == "1":  

        school=input('Enter School name in which you would like to enroll: ')
        if school in schoolDict["Schools"].keys():
            
            std = input('Enter Standard in which you would like to enroll the student: ')            
            if std in schoolDict["Schools"][school].keys():
                
                # Taking student details from the user calling the function add()
                payload,roll_no=add()
                
                if roll_no not in schoolDict["Schools"][school][std].keys():
                    schoolDict["Schools"][school][std].update({roll_no:payload})
                else:
                    print("Roll number already exist.. pls try to enrol with another roll number")
                    pass
            else:
                schoolDict["Schools"][school].update({std:{}})
                payload,roll_no=add()
                schoolDict["Schools"][school][std].update({roll_no:payload})
        else:
            schoolDict["Schools"].update({school:{}})
            std = input("Enter standard: ")
            schoolDict["Schools"][school].update({std:{}})
            payload,roll_no=add()
            schoolDict["Schools"][school][std].update({roll_no:payload})


        # print(schoolDict)
        with open("dynamic.json","w") as f:
            json.dump(schoolDict,f, indent=4)
        print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")

    elif operation == "2":
        print("Pls select the user type: ")
        print("1. Admin")
        print("2. Teacher")

        user = input("Select user type: ")
        

        if user == "1":
            
            print("Pls select which details you would like to edit:\n 1. Edit School Name\n 2. Edit standard's\n 3. Edit student details")    
            user_Edit = input("select Your edit type: ")
            
            if user_Edit == "1":
                
                print(list(schoolDict["Schools"].keys()))
                school_edit = input("Enter school name You would want to edit: ")
                dict1 = schoolDict["Schools"].keys()

                while school_edit not in dict1:
                    school_edit = input("Pls enter correct school name from above list.. you  want to update: ")

                enter_new_school_name = input("Enter new school name: ")
        
                # If new school name already exist in dict
                while enter_new_school_name in schoolDict["Schools"].keys():
                    enter_new_school_name = input("School name already exist.. Pls enter another school name: ")

                schoolDict["Schools"][enter_new_school_name] = schoolDict["Schools"].pop(school_edit)
                print("Edited School Name successfully")
                print()
                print(schoolDict)

                with open("dynamic.json","w") as f:
                    json.dump(schoolDict,f, indent=4)
                print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")
            
            elif user_Edit == "2":
                print(list(schoolDict["Schools"].keys()))
                school = input("Select school name from above list in which you would like to edit standard: ")
                dict1 = schoolDict["Schools"].keys()

                while school not in dict1:
                    school = input("Pls enter correct school name from above list.. you  want to update: ")

                print(list(schoolDict["Schools"][school].keys()))
                std_edit = input("Enter standard name you want to edit: ")

                while std_edit not in schoolDict["Schools"][school].keys():
                    std_edit = input("Pls enter correct standard name you want to update: ")

                enter_new_std_name = input("Enter new standard name: ")

                # If new standard name already exist in schools where user want to update standard 
                while enter_new_std_name in schoolDict["Schools"][school].keys():
                    enter_new_school_name = input("Standard name already exist.. Pls enter another standard name: ")

                schoolDict["Schools"][school][enter_new_std_name] = schoolDict["Schools"][school].pop(std_edit)
                print("Edited Standard Name successfully")
                print()
                print(schoolDict)

                with open("dynamic.json","w") as f:
                    json.dump(schoolDict,f, indent=4)
                print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")

            elif user_Edit == "3":
                print(list(schoolDict["Schools"].keys()))
                school = input("Enter school name from above in which the student is: ")

                while school not in schoolDict["Schools"].keys():
                    school = input("Pls enter valid school name from above list: ")
                
                print(list(schoolDict["Schools"][school].keys()))
                std = input("Enter standard from above in which the student is: ")

                while std not in schoolDict["Schools"][school].keys():
                    std = input("pls enter correct standard of the student from above list: ")
                
                print(list(schoolDict["Schools"][school][std].keys()))
                roll_no = input("select roll number of the student from above list whose details you wanna update: ")

                while roll_no not in schoolDict["Schools"][school][std].keys():
                    print("pls enter correct roll number")
                    roll_no = input("Select roll number of the student from above list whose details you wanna update: ")       
                dict1 = schoolDict["Schools"][school][std]
                if roll_no in dict1.keys():
                    # if k.get(roll_no):
                    name = input('Enter name: ')
                    address = input("Add the address: ")
                    father_name = input('Enter Fathers name: ')
                    mother_name = input('Enter Mothers name: ')
                    payload={
                        "name":name,
                        "address":address,
                        "father_name":father_name,
                        "mother_name":mother_name
                    }

                    dict1[roll_no].update(payload)
                    print("Edited student details successfully")
                    print()
                    
                # print(schoolDict)

                with open("dynamic.json","w") as f:
                    json.dump(schoolDict,f, indent=4)
                print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")

        elif user == "2":
            print()
            print("pls provide with below details to update student details: ")
            print()
            print(list(schoolDict["Schools"].keys()))
            school = input("Enter school name from above in which the student is: ")

            while school not in schoolDict["Schools"].keys():
                school = input("Pls enter valid school name from above list: ")
            
            print(list(schoolDict["Schools"][school].keys()))
            std = input("Enter standard from above in which the student is: ")

            while std not in schoolDict["Schools"][school].keys():
                std = input("pls enter correct standard of the student from above list: ")
            
            print(list(schoolDict["Schools"][school][std].keys()))
            roll_no = input("select roll number of the student from above list whose details you wanna update: ")

            while roll_no not in schoolDict["Schools"][school][std].keys():
                print("pls enter correct roll number")
                roll_no = input("Select roll number of the student from above list whose details you wanna update: ")       
            dict1 = schoolDict["Schools"][school][std]
            if roll_no in dict1.keys():
                # if k.get(roll_no):
                name = input('Enter name: ')
                address = input("Add the address: ")
                father_name = input('Enter Fathers name: ')
                mother_name = input('Enter Mothers name: ')
                payload={
                    "name":name,
                    "address":address,
                    "father_name":father_name,
                    "mother_name":mother_name
                }

                dict1[roll_no].update(payload)
            # print(schoolDict)
            with open("dynamic.json","w") as f:
                json.dump(schoolDict,f, indent=4)
            print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")

    elif operation == "3":
        
        print("Pls select the user type: ")
        print("1. Admin")
        print("2. Teacher")


        user = input("Select user type: ")
        if user == "1":
            
            print("Pls select which details you would like to delete:\n 1. Delete School \n 2. Delete standard\n 3. Delete student details")    
            user_Edit = input("select Your edit type: ")
            
            # Delete School
            if user_Edit == "1":
                print(list(schoolDict["Schools"].keys()))
                school_del = input("Enter school name You would want to delete: ")
                dict1 = schoolDict["Schools"].keys()

                while school_del not in dict1:
                    school_del = input("Pls enter correct school name from above list.. you  want to delete: ")
                
                if school_del in dict1:  
                    del schoolDict["Schools"][school_del]
                    print("School deleted successfully..!!!")
                    # schoolDict["Schools"].pop(school_del)
                    # print(schoolDict)
                with open("dynamic.json","w") as f:
                    json.dump(schoolDict,f, indent=4)
                print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")

            # delete the standard
            elif user_Edit == "2":
                print(list(schoolDict["Schools"]))
                school = input("Enter school name You would want to delete: ")
                dict1 = schoolDict["Schools"].keys()
                
                while school not in dict1:
                    school = input("Pls enter correct school name from above list.. you  want to delete the standard from: ")

                print(list(schoolDict["Schools"][school].keys()))
                std_del = input("Enter standard name you want to edit: ")

                while std_del not in schoolDict["Schools"][school].keys():
                    std_del = input("Pls enter correct standard from above list.. you want to delete: ")

                if std_del in schoolDict["Schools"][school].keys():
                    del schoolDict["Schools"][school][std_del]
                    print("Standard deleted successfully..!!")
                    # print(schoolDict)

                with open("dynamic.json","w") as f:
                    json.dump(schoolDict,f, indent=4)
                print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")
            
            elif user_Edit == "3":
                print(list(schoolDict["Schools"]))
                school = input("Enter school name You would want to delete: ")
                dict1 = schoolDict["Schools"].keys()
                
                while school not in dict1:
                    school = input("Pls enter correct school name from above list.. you  want to delete the standard from: ")

                print(list(schoolDict["Schools"][school].keys()))
                std = input("Enter standard name you want to edit: ")

                while std not in schoolDict["Schools"][school].keys():
                    std = input("Pls enter correct standard from above list.. you want to delete: ")

                print(list(schoolDict["Schools"][school][std].keys()))
                roll_no = input("select roll number of the student from above list whose details you wanna delete: ")

                while roll_no not in schoolDict["Schools"][school][std].keys():
                    print("pls enter correct roll number")
                    roll_no = input("Pls enter correct roll number of the student from above list.. you wanna delete ")

                if roll_no in schoolDict["Schools"][school][std].keys():
                    del schoolDict["Schools"][school][std][roll_no]
                    print("Deleted student details successfully..!!")
                    # print(schoolDict)
                with open("dynamic.json","w") as f:
                    json.dump(schoolDict,f, indent=4)
                print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")


        elif user == "2":
            print()
            print("pls provide with below details to delete student details: ")
            print()
            print(list(schoolDict["Schools"]))
            school = input("Enter school name in which student is enrolled: ")
            dict1 = schoolDict["Schools"].keys()
            
            while school not in dict1:
                school = input("Pls enter correct school name from above list:  ")

            print(list(schoolDict["Schools"][school].keys()))
            std = input("Enter standard name in which thw student is: ")

            while std not in schoolDict["Schools"][school].keys():
                std = input("Pls enter correct standard from above list: ")

            print(list(schoolDict["Schools"][school][std].keys()))
            roll_no = input("select roll number of the student from above list whose details you wanna delete: ")

            while roll_no not in schoolDict["Schools"][school][std].keys():
                roll_no = input("Pls enter correct roll number of the student from above list.. you wanna delete: ")

            if roll_no in schoolDict["Schools"][school][std].keys():
                del schoolDict["Schools"][school][std][roll_no]
                print("Deleted student details successfully..!!")
                # print(schoolDict)
            
            with open("dynamic.json","w") as f:
                json.dump(schoolDict,f, indent=4)
            print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")


    elif operation == "4":
        print("Pls select the user type: ")
        print("1. Admin")
        print("2. Teacher")


        user = input("Select user type: ")
        if user == "1":
            
            print("Pls select which details you would like to see:\n 1. Fetch School details\n 2. Fetch standard details\n 3. Fetch student details")    
            user_Edit = input("Pass your choice here: ")
            
            # fetch all the standards present in School details
            if user_Edit == "1":
                print(list(schoolDict["Schools"].keys()))
                school_details = input("Enter school name you want to see the details: ")
                print()
                dict1 = schoolDict["Schools"].keys()

                while school_details not in dict1:
                    school_details = input("Pls enter correct school name from above list.. you  want to see details: ")
                    print()
                
                if school_details in dict1:  
                    print("Below are the list of standards in this school: ")
                    print("\n".join("{}".format(k) for k in schoolDict["Schools"][school_details].keys()))
                    print()
                    print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")

                    

            # fetch the roll numbers list of standard
            if user_Edit == "2":
                print(list(schoolDict["Schools"].keys()))
                school_details = input("Enter school name you want to see the details: ")
                print()
                dict1 = schoolDict["Schools"].keys()

                while school_details not in dict1:
                    school_details = input("Pls enter correct school name from above list.. you  want to see details: ")
                    print()

                print(list(schoolDict["Schools"][school_details].keys()))
                std_details = input("Enter the standard details you want to see the details: ")

                while std_details not in schoolDict["Schools"][school_details].keys():
                    std_details = input("Pls enter correct standard name from above list: ")

                if std_details in schoolDict["Schools"][school_details].keys():

                    print("Below are the list of student roll numbers with their name in the standard")
                    # print(schoolDict["Schools"][school_details][std_details])
                    print("\n".join("{} - {}".format(k,v["name"]) for k,v in schoolDict["Schools"][school_details][std_details].items()))
                    print()
                    print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")

            # fetch student details from its roll number
            if user_Edit == "3":
                print(list(schoolDict["Schools"].keys()))
                school_details = input("Enter school name you want to see the details: ")
                print()
                dict1 = schoolDict["Schools"].keys()

                while school_details not in dict1:
                    school_details = input("Pls enter correct school name from above list.. you  want to see details: ")
                    print()

                print(list(schoolDict["Schools"][school_details].keys()))
                std_details = input("Enter the standard details you want to see the details: ")
                print()

                while std_details not in schoolDict["Schools"][school_details].keys():
                    std_details = input("Pls enter correct standard name from above list: ")

                list_of_roll_no=list(schoolDict["Schools"][school_details][std_details].keys())
                a = list_of_roll_no.sort()
                string = "All"
                list_of_roll_no.append(string)
                print(list_of_roll_no)

                roll_no_details = input("Enter the roll number of the students whose details you wanna fetch: ")
                if roll_no_details == string:
                    print(schoolDict["Schools"][school_details][std_details].values())

                while roll_no_details not in schoolDict["Schools"][school_details][std_details].keys():
                    roll_no_details = input("Pls enter correct roll number from above list: ")

                if roll_no_details in schoolDict["Schools"][school_details][std_details].keys():
                    print("\n".join("{}: {}".format(k,v) for k,v in schoolDict["Schools"][school_details][std_details][roll_no_details].items())) 
                    print()
                    print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")

        if user == "2":
                print(list(schoolDict["Schools"].keys()))
                school_details = input("Enter school name you want to see the details: ")
                print()
                dict1 = schoolDict["Schools"].keys()

                while school_details not in dict1:
                    school_details = input("Pls enter correct school name from above list.. you  want to see details: ")
                    print()

                print(list(schoolDict["Schools"][school_details].keys()))
                std_details = input("Enter the standard details you want to see the details: ")
                print()

                while std_details not in schoolDict["Schools"][school_details].keys():
                    std_details = input("Pls enter correct standard name from above list: ")

                list_of_roll_no=list(schoolDict["Schools"][school_details][std_details].keys())
                a = list_of_roll_no.sort()
                string = "All"
                list_of_roll_no.append(string)
                print(list_of_roll_no)

                roll_no_details = input("Enter the roll number of the students whose details you wanna fetch: ")
                if roll_no_details == string:
                    print(schoolDict["Schools"][school_details][std_details].values())

                while roll_no_details not in schoolDict["Schools"][school_details][std_details].keys():
                    roll_no_details = input("Pls enter correct roll number from above list: ")

                if roll_no_details in schoolDict["Schools"][school_details][std_details].keys():
                    print("\n".join("{}: {}".format(k,v) for k,v in schoolDict["Schools"][school_details][std_details][roll_no_details].items())) 
                    print()
                    print("Pls Select Your Request\n1. Enroll Student\n2. Update Student Info\n3. Remove Student\n4. Fetch Student Details\n5. Quit")

                