# schoolDict = {
#     "Schools": {"School_A":"St. Mary's High school"}
# }
# schoolDict["Schools"]["School_B"] = schoolDict["Schools"].pop('School_A')

# print(schoolDict)


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
                }
            },
            "Standard2": {
                "2": {
                    "name": "Ross",
                    "address": "NY",
                    "father_name": "JAck",
                    "mother_name": "Judy"
                },
                "1": {
                    "name": "Monica",
                    "address": "NY",
                    "father_name": "JAck",
                    "mother_name": "Judy"
                }
            }
        }
    }
}
# num = 2
# dict2 = schoolDict["Schools"]["School_B"]["Standard2"]
# # print(dict2)
# # if num in dict2.keys():
# #     print(dict2)
# # else:
# #     ("NO")

# for k,v in dict2.items():
#     print(k,v['name'])



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