# def gst_calculate(amount, rate):
#     gst = amount * (rate/100)
#     final_amount = amount + gst
#     print("final amount is: ",final_amount)
#     return gst
    

# total_value = gst_calculate(1000,5)

# print(total_value)

my_list = [1,2,3,4,55,55,63,23]

def first_repeating_element (input_list):
    my_set= set()
    for num in input_list:
        if num in my_set:
            return num
        else:
            my_set.add(num)
    
print(first_repeating_element(my_list))
