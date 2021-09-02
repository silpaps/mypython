#pattern matching
# re - package is used for pattern matching
# import re
# count=0
# matcher=re.finditer("ab","abaabbab")
# for match in matcher:
#     count+=1
# print(count)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import re
count=0
matcher=re.finditer("ab","abaabbab")
for match in matcher:
    print("match available at :",match.start())
    print("group is",match.group())
    count+=1
print(count)