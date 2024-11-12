def do_twice(f,arg):
    f(arg)
    f(arg)

def print_spam():
    print('foster')


def print_twice(bruce):
    print(bruce)
    print(bruce)



def twice(f,arg):
    do_twice(f,arg)
    do_twice(f,arg)

def do_four(f,arg):
    do_twice(f,arg)
    do_twice(f,arg)

do_four(print,'spam')

