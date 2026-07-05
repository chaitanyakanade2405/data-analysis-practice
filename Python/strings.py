# name = "Chaitanya"

# print(name[1:4])
# print(name[-4:-1])
# print(name[::-1])
# print(name.upper())

# s = 'abccba'
# s_len = len(s)
# first_half = s[0:s_len//2]
# second_half = s[s_len//2:]
# second_half = second_half[::-1]

# print(first_half)
# print(second_half)

text = "data engineer"
vowels = "aeiou" 
count = 0
for ch in text:
    if ch in vowels:
        count = count+1
print (count)