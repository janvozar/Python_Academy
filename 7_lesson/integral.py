print()

def our_print(par1, par2, key_par=1, key_par2=None):
    print(par1, par2, key_par1, key_par2)

def our_better_print(part1,part2,args, kwarg1 = None, kwargs):
    print(type(args))
    print(type(kwargs))
    for arg in args
        print(arg)

our_better_print('string1','string3',4,5,key='value', key2=4)