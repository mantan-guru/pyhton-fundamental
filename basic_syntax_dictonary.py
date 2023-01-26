#declare type data dictonary
users = {
    "id" : 1, #key : value
    "name" : "John Doe",
    "username" : "johndoe",
    "email" : "jondoe@gmail.com",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    },
}

#print  dictonary

print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])

#print dictonary in dictonary
print(users["address"])
print(users["address"]["street"])
print(users["address"]["geo"]["lat"])
print(users["address"]["geo"]["lng"])

print(type(users))
print('Dictonary')
print(users)
#manage dict to json in python
import json
print('JSON')
result = json.dumps(users)
print(result)

#using dump to write file

with open("result.json", "w") as file :
    json.dump(users, file)

