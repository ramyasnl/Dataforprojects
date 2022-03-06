from Module1.invoice import invoice
from Module1.order import order
#  input("Enter torder he options "invoice" or "order":)
print('Enter your  options "invoice" or "order":')
x = input()
if (x =="invoice"):
    f= invoice()
    print(f)
    # print("d")
elif(x =="order"):
    e = order()
    print(e)
else:
    print("wrong order")
