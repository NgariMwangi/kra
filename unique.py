numbers=[3,8,3,9,1,2,2,5,3]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)