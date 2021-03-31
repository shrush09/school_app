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

school=input('Enter School name in which you would like to enroll: ')
if school in schoolDict["Schools"].keys():
    std = input('Enter Standard in which you would like to enroll the student: ')
    if std in schoolDict["Schools"][school].keys():
        # Taking student details from the user 
        payload,roll_no=add()
        # schoolDict["Schools"][school][std][roll_no]={}
        if roll_no not in schoolDict["Schools"][school][std].keys():
            schoolDict["Schools"][school][std].update({roll_no:payload})
        else:
            print("User already present")
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



        