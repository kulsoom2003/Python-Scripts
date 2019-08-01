student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}


dictionary1 = {"name": "Pikachu", "age": 7, "type": "Electric"}


lake = {
    "name" : "River Eden",
    "location" : "Cumbria",
    "size" : 145,
    "rock types" : ["igneous", "sandstone", "clay", "limestone"]
}

print("This program will create a phone book")

phone_book = {}
n = int(input("Enter the number of entries: "))
for x in range(0,n):
    line = input("Enter the entry's name and phone number separated by a space: ")
    line = line.split()
    name = line[0]
    number = line[1]
    phone_book[name] = number

while 1 == 1:
    name = input("Type the name of the entry you'd like to look up: ")
    if name in phone_book:
        print(name+" = "+phone_book[name])
    else:
        print("Name not in phone book.")
 
