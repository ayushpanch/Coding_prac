# Input: s = "babad"
# Output: "bab"
# # Explanation: "aba" is also a valid answer.

s = "babad"
empty_list = []
for x in range(len(s)):
    print(x)

    for y in range(len(s),0,-1):
        print(y)

        string_to_check = s[x:y]
        if string_to_check == string_to_check[::-1]:

            print("correct")
            if len(string_to_check) == 3:

                empty_list.append(string_to_check)
        else:
            print("wrong")

empty_list






