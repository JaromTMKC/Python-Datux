class Persona:

    def __init__(self,fullname,fecha_nacimiento):
        self.fullname=fullname
        self.fecha_nacimiento=fecha_nacimiento
    def __str__(self) -> str:
        return f"la persona tiene nombre {self.fullname} y fecha de nacimiento {self.fecha_nacimiento}"

ListaPersonas=[]

with open('./S6/personas.txt','r') as f:
    data=f.readlines()
    for i in data:
        info=i.split(';')
        fullname=info[1]+info[2]
        pTemp=Persona(fullname,info[3].split("\n")[0])
        ListaPersonas.append(pTemp)

for personaI in ListaPersonas:
    print(personaI)
