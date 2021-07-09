num=str(input("enter a phonenumber"))
if num[0:2]=="07":
   num="+254"+ num[1:]
   print(num)
elif num[0:2]=="71":
    num="+254"+num[0:]
    print(num)
elif num[0:3]=="254":
    num="+"+ num[0:]
    print(num)
elif num[0:4]=="+254":
    print(num)
elif num[0:2]=="01":
    num="+254"+ num[1:]
    print(num)
else:
    print("number is invalid")


