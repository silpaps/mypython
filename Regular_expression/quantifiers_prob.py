# import re
#
# x='a+'
# r="aaa abc aaa cba"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x='a*'
# r="ab abc aaaa cba"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

import re

x='a?'
r="aaa abc aaa cba"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())

# import re
#
# x='a{2}'
# r="aaa abc aaaa cba"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x='a{1,3}'
# r="aaa abc aa aaaa cba"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x='^a'
# r="aaa abc aaaa cba"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x='a$'
# r="aaa abc aaaa cba"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())