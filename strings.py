#All variables originate from a class
#Strings- symbols, words sentences...etc  surround them with double or single quotes 
#Do not surround variable names wit quotes


first="Dennis"
last="Mwangi"
fullname=first+" "+last
print(fullname)
print(fullname.lower())
fullname=fullname.lower()
print(fullname)
print(fullname.count("a"))
print(fullname.count("r"))

print(fullname[-7])
print(fullname[7:10])
print(fullname)
sentences_one="The dog Breed is German Shepherd"
print(sentences_one[7:23])
sentences_two="Defeats for the Clinton forces,this was hermoment of triumph"
print(sentences_two[15:29])
sentences='The lazy dog, ran so fast, it hit the wall'

chunk=sentences.split(',')

print(chunk)
split_one=chunk[0]
print(split_one)
print(len(split_one))
