# ipl = {"MI" : "Rohit Sharma", "CSK" : "MSD"}

# print(ipl["MI"])

# captains = { "MI" : {"captain_name" : "Rohit Sharma"}
#            ,"CSK" : {"captain_name" : "MSD"}
#            ,"RCB" : {"captain_name" : "Virat Kohli"}
# }

# print(captains["MI"])

word = "data engiineer"
word_count = {}

for ch in word:
    if ch not in word_count:
        word_count[ch] = 1
    else:
        word_count[ch] = word_count[ch]+1

print(word_count)
