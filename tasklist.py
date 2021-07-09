tasklist = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
x=str(tasklist[3])[::-1]
tasklist[3]=int(x)
print(tasklist)
