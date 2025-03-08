ipstr=input("Enter a String")
otstr=''
for i in ipstr:
    if i.isupper():
        o=i.lower()
    elif i.islower():
        o=i.upper()
    else:
        o=i
    otstr += o
print(otstr)
