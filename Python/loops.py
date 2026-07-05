email = ["123@gmail.com", "abc@gmail.com", "www@gmail.com", "xyz@gmail.com"]

for email_id in email:
    print (email_id)

for i in range (len(email)):
    print(i, email_id[0])

# for n in range(10):
#     print(n)

arr = [23,2,44,31,73,20]
n = len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr)