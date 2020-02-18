# Code task
# Would it be possible to iterate over a tuple that consists of 3-item tuples? How should we do that?

data = (('Age',43,True),('Name','John',True),('Surname','Smith',False))

for a,b,c in data:
    print(a,b,c)