lst1=str(input("enter numbers by commas:"))
newlist=(lst1.split(","))
s=0
for i in newlist:
    s=s+int(i)
print(s)
     