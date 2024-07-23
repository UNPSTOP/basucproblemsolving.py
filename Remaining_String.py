# #Input: s = "Thisisdemostring", ch = 'i', count = 3
s1=""
s = "iikhain"
ch = 'i'
count = 3
count2=0
for i in range(len(s)):
    if s[i]==ch:
        count2 +=1
    elif count2 ==count:
        for j in range(len(s)-1,-1,-1):
            if ch !=s[j]:
               s1 +=s[j]
            else:
                break
print(s1[::-1])
# class Solution:
#     def remaining_substring(self, s, ch, count):
#         occurrence_count = 0
#         for i in range(len(s)):
#             if s[i] == ch:
#                 occurrence_count += 1
#             if occurrence_count == count:
#                 return s[i+1:]
#         return ""

# # Test cases
# solution = Solution()
# # print(solution.remaining_substring("Thisisdemostring", 'i', 3))  # Output: ng
# print(solution.remaining_substring("Thisisdemostri", 'i', 3))  # Output: 
