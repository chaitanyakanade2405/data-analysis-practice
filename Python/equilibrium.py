# arr = [-7,1,5,2,-4,3,0]
arr = [1,2,0,3]

def equi(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        else:
            left_sum = left_sum + arr[i]
    return -1

print(equi(arr))