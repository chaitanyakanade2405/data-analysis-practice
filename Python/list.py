my_list = [1,2,3,4,5,6]

output_list =[]

for num in my_list:
    if(num%2==0):
        output_list.append("even")
    else:
        output_list.append("odd")

print(output_list)