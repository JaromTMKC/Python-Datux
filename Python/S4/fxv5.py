def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

indeterminados_posicion(1,2,['hola','lista'],{'dni':'1231312'})

def indeterminados_nombre(**kwargs:dict):
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

indeterminados_nombre(par1=1,par2=2,par3=[1,231,32])