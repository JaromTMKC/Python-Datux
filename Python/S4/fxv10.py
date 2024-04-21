# input => fx() => fx'() => ... => output

def fx():
    pass
def fxv1(a):
    pass
def fxv2(c):
    pass


def Main():
    a=fx()
    print(a,type(a))
    b=fxv1(a)
    print(b)
    c=fxv2(b)
    print(c)
    print(c)