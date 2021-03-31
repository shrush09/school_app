schoolDict = {
    "Schools": {
        "School_A": {
            "Standard1": {
                "1": {
                    "name": "Chandler",
                    "address": "LA",
                    "father_name": "Charles bing",
                    "mother_name": "Nora bing"
                }
            }
        },
        "School_B": {
            "Standard1": {
                "1": {
                    "name": "Monica",
                    "address": "NY",
                    "father_name": "JAck",
                    "mother_name": "Judy"
                },
                "2":{
                    "name": "Deepak",
                    "address": "NY",
                    "father_name": "JAck",
                    "mother_name": "Judy"
                }
            },
            "Standard2": {
                "2": {
                    "name": "Ross",
                    "address": "NY",
                    "father_name": "JAck",
                    "mother_name": "Judy"
                }
            }
        }
    }
}



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
        print(schoolDict)
    
    if user_Edit == "2":
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
        print(schoolDict)

    if user_Edit == "3":
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
        print(schoolDict)

if user == "2":
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
    print(schoolDict)