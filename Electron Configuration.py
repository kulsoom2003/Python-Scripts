'''FULL ELECTRON CONFIGURATION GENERATOR'''


def find_sum():
    find_sum = 0
    for x in range(0,len(char3_list)):
        find_sum = find_sum + int(char3_list[x])
    return find_sum
#function which adds up all numbers in list char3_list
        
def find_capacity(subshell):
    if char2_s_list[subshell] == "s":
       subshell_capacity = 2
    elif char2_s_list[subshell] == "p":
        subshell_capacity = 6
    elif char2_s_list[subshell] == "d":
        subshell_capacity = 10
    return subshell_capacity
#function which finds the capacity of the subshell
#variable 'subshell' is the index of the source lists 
    

electron_number = int(input("Enter atomic number: "))

configuration = []

char1_s_list = [1,2,2,3,3,4,3,4]

char2_s_list = ["s","s","p","s","p","s","d","p"]
#source lists

char3_list = []
#char3_list must be generated

char3 = 0

configuration = []


subshell = 0
#because the index starts at 0

while find_sum() < electron_number:
#this ensures the number of electrons in char3_list hasn't reached the atomic number
    char3 = 0
    #must be reset once character 3 has been appended to its list
    while char3 < find_capacity(subshell) and (find_sum() + char3) < electron_number:
    #find_sum() must be called again with the addition of character 3, which is the number of electrons 
    #outside the subshell so that electrons can be added to the list while the subshell is not full
        char3 = char3 + 1
        #adds an electron
    char3_list.append(str(char3))
    #when the program breaks out of the loop it means the capacity is full OR the number of
    #electrons in the list are equal to the atomic number
    subshell = subshell + 1
    #if the capacity of the subshell is full a new subshell must be added

for x in range(0,len(char3_list)):
    configuration.append(str(char1_s_list[x]) + str(char2_s_list[x]) + str(char3_list[x]))
#concatenates lists to form full configuration


if electron_number == 24:
    print("Chromium is an exception.  Here is its configuration: ")
    configuration = ["1s2", "2s2", "2p6", "3s2", "3p6", "4s1", "3d5"]
elif electron_number == 29:
    print("Coppuer is an exception.  Here is its configuration: ")
    configuration = ["1s2", "2s2", "2p6", "3s2", "3p6", "4s1", "3d10"]


print("FULL ELECTRON CONFIGURATION: ")
for x in configuration:
    print(x, end = " ")
#prints configuration




