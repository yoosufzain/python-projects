user_input= input("Enter your list")
user_list = []

if ","in user_input :
   input_list =  user_input.split(",")
else:
   input_list = user_input.split(" ")
num= 0
for list in input_list:
    int_values = int(list)
    user_list.append(int_values)
    num+=1
def creat_odered_number_of_list(unodered_list):
    num = 0
    num2= 1
    for list in unodered_list:        
        if (list % unodered_list[0]) != 0:
            unodered_list[num]= num2*unodered_list[0]
                 
        num += 1
        num2+=1
    return unodered_list
        
value = creat_odered_number_of_list(user_list)
print(value)

