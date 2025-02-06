# Input: s = "babad"
# Output: "bab"
empty_list = []
s = "babad"
for x in range(len(s) ):
    # print(s)
    for y in range(len(s),1,-1):
        # print(y)
        
        string_1 = s[x:y]
        if len(string_1) > 2:
            if string_1 == string_1[::-1]:
                print(string_1)
                empty_list.append(string_1)
            else:
                pass
