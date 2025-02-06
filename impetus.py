# 4
# bcdef
# abcdefg
# bcde
# bcdef

input_list = ['bcdef',
'abcdefg',
'bcde',
'bcdef'
]

len(set(input_list))
empty_dictonary ={}
for x in input_list:
    if x not in empty_dictonary.keys():
        empty_dictonary[x] = 1 
    else:
        empty_dictonary[x] = empty_dictonary[x] + 1 

empty_dictonary



