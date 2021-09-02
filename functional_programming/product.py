from functools import reduce
products=[
    {"p_name":"complan","mrp":230,"avl_qty":50},
    {"p_name": "horlicks", "mrp": 250, "avl_qty": 10},
    {"p_name": "bournvita", "mrp": 220, "avl_qty": 0},
    {"p_name": "nutricharge", "mrp": 200, "avl_qty": 100},
    {"p_name": "mylo", "mrp": 100, "avl_qty": 0},

]
#print all products name in shop
# p_name=list(map(lambda item:item["p_name"],products))
# print(p_name)
#print all available products in shop
# p_name=list(filter(lambda item:item["avl_qty"]>0,products))
# print(p_name)
#print out of stock product
# prdct=list(filter(lambda item:item["avl_qty"]==0,products))
# print(prdct)
#highest product
# prices=list(map(lambda product:product["mrp"],products ))
# print(max(prices))
items=lambda item,i:item[i]
for i in range(1,len(products)):
   print(items(products,i))