arr = [16,17,4,3,5,2]
leaders = []
leaders.append(arr[-1])
right_max = arr[-1]
# for i in range(len(arr)-1):
#     if arr[i] >= max(arr[i+1:]):
#         leaders.append(arr[i])

# leaders.append(arr[-1])
for i in range(len(arr)-2,-1,-1):
    if arr[i] >= right_max:
        leaders.append(arr[i])
        right_max = arr[i]

leaders = leaders[::-1]
print(leaders)