import defdemeo
price=25.173
product="nirma powder"
qty=5
t=defdemo.total(price,qty)
#print(t)
txt="rate of {} is {} and qty is {} so total is {:.3f} "
print(txt.format( product,price,qty,t))
txt2="rate of {product} is {price}"
o=product.upper()
print(txt2.format(product=o,price=price))
