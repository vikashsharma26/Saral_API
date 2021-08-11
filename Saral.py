import requests
import json
# x=requests.get('http://saral.navgurukul.org/api/courses').json()
# file = open("Data.json","w")
# json.dump(x,file,indent=4)
file = json.loads(open("Data.json","r").read())
print("S.no","Courses",)
for data in range(len(file["availableCourses"])):
    print((data + 1),"."," ",file["availableCourses"][data]["name"])
Course = int(input("Please Serial No. To Access Course: "))
new = requests.get("http://saral.navgurukul.org/api/courses/"+file["availableCourses"][Course-1]["id"]+"/exercises").json()
for counting,content in enumerate(new['data']):
    print(counting+1,content["name"])
subtopic = int(input("Enter the topic no. "))
newdata = open("exercise.json","w")
json.dump(requests.get("http://saral.navgurukul.org/api/courses/"+file["availableCourses"][Course-1]["id"]+"/exercise/getBySlug?slug="+new["data"][subtopic-1]["slug"]).json(),newdata,indent=4)