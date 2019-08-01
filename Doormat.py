N = int(input("Enter the length of your doormat (it should be an odd number): "))
M = 3 * N
print("These are the dimensions of your doormat: "+str(N)+" x "+str(M))
print("")
design_string = ".|."
num_lines = int(((N - 1)/2) + 1)
num_des_str = 1
for x in range(1,num_lines):

    num_des_char = num_des_str * 3
    line = ("-" * int(((M + 1) / 2) - ((num_des_char + 1) / 2)) + (design_string * num_des_str) + ("-" * int(((M + 1) / 2) - ((num_des_char + 1) / 2))))
    print(line)
    num_des_str = num_des_str + 2


print(("-" * int(((M + 1) / 2) - 4)) + "WELCOME" + ("-" * int(((M + 1) / 2) - 4)))

for x in range(1,num_lines):
    num_des_str = num_des_str - 2
    num_des_char = num_des_str * 3
    line = ("-" * int(((M + 1) / 2) - ((num_des_char + 1) / 2)) + (design_string * num_des_str) + ("-" * int(((M + 1) / 2) - ((num_des_char + 1) / 2))))
    print(line)

