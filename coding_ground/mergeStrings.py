# Problem Statement: You are given two strings. You need to create a new string made up of these two strings where the first character of each string is compared with each other 
#         and based on a sorted arrangement, the smaller letter be added to the new string first. The comparison should be done for all characters in both strings.

s1='super'
s2='tower'

from collections import Counter
def mergeStrings(s1,s2):
    output=''
    s1_dict=Counter(s1)
    s2_dict=Counter(s2)
    while s1 and s2:
        if (s1[0]<=s2[0] and s1_dict[s1[0]]<=s2_dict[s2[0]]) or (s1[0]>s2[0] and s1_dict[s1[0]]<s2_dict[s2[0]]):
            output+=s1[0]
            s1=s1[1:]
        elif (s1[0]>s2[0] and s1_dict[s1[0]]>=s2_dict[s2[0]]) or (s1[0]<s2[0] and s1_dict[s1[0]]>s2_dict[s2[0]]) or (s1[0]==s2[0] and s1_dict[s1[0]]>s2_dict[s2[0]]):
            output+=s2[0]
            s2=s2[1:]
    if s1:
        output+=s1
    else:
        output+=s2
    
mergeStrings(s1,s2)
