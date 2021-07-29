def addnumbers(basicsallary,benefits):
    gross_sallary=basicsallary+benefits
    basicsallary=int(input("enter basic salary"))
    benefits=int(input("input total benefits"))
    return gross_sallary 


v=addnumbers(4000,30000)
print(v)

def nhif(v):
    if v > 0 and v<=5999 :
        n=150
    elif v>=6000 and v<=7999:
        n=300
    elif v>=8000 and v<=11999:
        n=400
    elif v>=12000 and v<=14999:
        n =500
    elif v>=15000 and v<=19999:
        n=600
    elif v>=20000 and v<=24999:
        n=750
    elif v>=25000 and v<=29999:
        n=850
    elif v>=30000 and v<=34999:
        n=900
    elif v>=35000 and v<=39999:
        n=950
    elif v>=40000 and v<=44999:
        n=1000
    elif v>=45000 and v<=49999:
        n=1100
    elif v>=50000 and v<=59999:
        n=1200
    elif v>=60000 and v<=69999:
        n=1300
    elif v>=70000 and v<=79999:
        n=1400
    elif v>=80000 and v<=89999:
        n=1500
    elif v>=90000 and v<=99999:
        n=1600
    else:
        n=1700
    return n

h=nhif(v)
print(h)

def monthlypaye(v):
    if v>0 and v<=24000:
        t=0.1*v
    elif v>=24001 and v<=32333:
        t=0.25*v
    else:
        t=0.3*v
    return t
m=monthlypaye(v)
print(m)



