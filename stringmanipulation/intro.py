# for i in "abcd":
#     print(i)

# a="abcd"
# for i in a:
#     print(i)
#>>>>>>common element in two strings
# a="afgh"
# b="cdfk"
# for i in a:
#     for a in b:
#         if i==a:
#             print(i)
#alternate
# a="afdh"
# b="cdfk"
# for i in a:
#     if i not in b:
#         print(i)
# s="string"
# p=len(s)
# print(p)

def stutter(word):
		return '{0}... {0}... {1}?'.format(word[:2], word)
word=stutter("incredible")
print(word)
#in... in... incredible?