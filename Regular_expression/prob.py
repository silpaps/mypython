# import re
#
# x='[abc]'
# matcher=re.finditer(x,'abc @htkabc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x='[^abc]'
# matcher=re.finditer(x,'abc @htkdeabc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x='[a-z]'
# matcher=re.finditer(x,'abc @htkAQ9abc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

#import re

# x='[A-Z]'
# matcher=re.finditer(x,'abc @htkAVBbc')
# for match in matcher:
#     print(match.start())
#     print(match.group())
# import re
#
# x='[a-zA-Z]'
# matcher=re.finditer(x,'abc @htk345AVBbc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x='[0-9a-zA-Z]'
# matcher=re.finditer(x,'abc @htk345AVBbc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x='[^0-9a-zA-Z]'
# matcher=re.finditer(x,'abc @htk345AVBbc')
# for match in matcher:
#     print(match.start())
#     print(match.group())
# import re
#
# x='\w'
# matcher=re.finditer(x,'abc @htk345AVBbc')
# for match in matcher:
#     print(match.start())
#     print(match.group())
import re

x='\s'
matcher=re.finditer(x,'abc @htk34  5AVBbc')
for match in matcher:
    print(match.start())
    print(match.group())
# import re
#
# x='\d'
# matcher=re.finditer(x,'abc @htk345AVBbc')
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
#
# x='\D'
# matcher=re.finditer(x,'abc @htk345AVBbc')
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x='\W'
# matcher=re.finditer(x,'abc @htk345AVBbc')
# for match in matcher:
#     print(match.start())
#     print(match.group())
