def calculadora_impuesto(salario,rubro="dependiente"):
    taxBase=0.18
    porcentajeSalario=0.0
    porcentajeRubro=0.0
    if salario<=1000:
        porcentajeSalario=0.04
    elif salario>1000 and salario <5000:
        porcentajeSalario=0.05
    else:
        porcentajeSalario=0.07

    if rubro=='independiente':
        porcentajeRubro=0.01
    else:
        porcentajeRubro=0.02

    return taxBase+porcentajeSalario+porcentajeRubro


tax1=calculadora_impuesto(1500)
tax2=calculadora_impuesto(2200,'independiente')
print(tax1,tax2)