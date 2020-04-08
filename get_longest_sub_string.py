#!/usr/bin/env python3

def get_longest_sub_string(st):

    sub_st = ''
    lg = 0

    for i in range(len(st)):
        s = st[i]
        l = 1
        for j in range(i, len(st)-1):
            if st[j+1] >= st[j]:
                s += st[j+1]
                l += 1
            else:
                break
        if l > lg:
            lg = l
            sub_st = s 
    
    return(sub_st)

s = input("Input:")
out = get_longest_sub_string(s)
print("Longest substring in alphabetical order is:",out)
