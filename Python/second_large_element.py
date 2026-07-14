arr = [10,1,4,101,5,76,101,54,68,5,10,23,97,100,99, 101.5,102,102]
# arr = list(set(arr))
# arr.sort()
# print(arr)
# print (arr[-2])

def second_large (arr):
    first = float('-inf')
    second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second

print(second_large(arr))