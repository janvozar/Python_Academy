def wrapper(func,*argument):
    lst = []
    for arg in argument:
        lst.append(int(arg))
        return func(*lst)

print(wrapper(abs, '-46'))