#string concatenation is how to put strings together
# youtuber="silpa"
# print("subscribe to "+youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscirbe to {youtuber}")
noun="------------"
ADJECTIVE="-----------"
Noun="----------"
madlibs=f"Be careful not to vacuum the {noun}when you clean under your bed." \
        f"Flip-flops are a staple of any {ADJECTIVE} summer wardrobe.,"\
        f"What came first, the chicken or the {Noun}?"
print(madlibs)
noun=input("fill the first blank")
ADJECTIVE=input("fill the second blank")
Noun=input("fill the third blank")
madlibs=f"Be careful not to vacuum the {noun}when you clean under your bed." \
        f"Flip-flops are a staple of any {ADJECTIVE} summer wardrobe.,"\
        f"What came first, the chicken or the {Noun}?"
print(madlibs)

