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


# If you want to delete a specific object in the list, use remove method.
# If you want to delete the object at a specific location (index) in the list, you can either use del or pop.
# Use the pop, if you want to delete and get the object at the specific location.

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
            print(schoolDict)

    # delete the standard
    if user_Edit == "2":
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
            print(schoolDict)

    if user_Edit == "3":
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
            print(schoolDict)


if user == "2":
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
        print(schoolDict)



