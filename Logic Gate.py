#Logic Gate

A = [False, False, True, True]
B = [False, True, False, True]
not_A = []
not_A_and_B = []
not_B = []
A_and_not_B = []
C_or_D = []

columns = [A, B, not_A, not_A_and_B, not_B, A_and_not_B, C_or_D]

for element in range(0,len(A)):
    not_A.append(not A[element])
#generates not_A array


for element in range(0, len(not_A)):
    not_A_and_B.append(not_A[element] and B[element])

#generates not_A_and_B array

for element in range(0,len(B)):
    not_B.append(not B[element])

#generates not_B array

for element in range(0,len(A)):
    A_and_not_B.append(A[element] and not_B[element])

#generates A_and_not_B array

for element in range(0,len(not_A_and_B)):
    C_or_D.append(not_A_and_B[element] or A_and_not_B[element])

#generates C_or_D (output) array



truth_table = [["A ","B ","¬A ","(¬A) AND B = C","¬B","A AND (¬B) = D","C V D (output)"],[],[],[],[]]

for i in range(0,7):
    for x in range(1,5):
        truth_table[x].append((columns[i])[x - 1])

print("Truth Table:")

for element in truth_table[0]:
    while len(element) < 20:
        #print("len(element) before: " + str(len(element)))
        element = element + " "
        #print("len(element) after: " + str(len(element)))
    print(element, end = "")
print()

for element in range(1,len(truth_table)):
    for x in truth_table[element]:
        if x == True:
            x = 1
        elif x == False:
            x = 0
        print(x, end = "                   ")
    print()


#inputs for logic gate

input_A = int(input("Input A: "))
input_B = int(input("Input B: "))

if input_A == 1:
    input_A = True
else:
    input_A = False

if input_B == 1:
    input_B = True
else:
    input_B = False

for element in range(0,4):
    if A[element] == input_A and B[element] == input_B:
        output = C_or_D[element]
        if output == True:
            output = 1
        else:
            output = 0
        print(output)


