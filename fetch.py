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
                
