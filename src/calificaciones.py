def convert_to_float(lista):
    for i in range(len(lista)):
        if(lista[i]=="None"):
            lista[i]=0
        else:
            lista[i]=float(lista[i])
    return lista
def check_none(lista):
    for i in range(len(lista)):
        if(lista[i]==None):
            lista[i]=0
    return lista

def check_none_or_4(lista): 
    for i in range(len(lista)):
        if(lista[i]==None or lista[i]<4):
            lista[i]=0
    if(len(lista))==1:
        return lista[0]
    else:
        return lista

def nota_media(lista):
    lista=check_none_or_4(lista)
    #lista1=[]
    #for i in lista:
     #   lista1.append(lista[i])

    suma=sum([i for i in lista])
    return suma/len(lista)


def nota_cuatrimestre(t,p):
    (t1,t2)=t
    t1,t2=check_none_or_4([t1,t2])
    p=check_none_or_4([p])
    result=(0.1*(t1+t2)+0.8*p)
    if result>4:
        return result
    else:
        return 0

def nota_continua(tupla_t,tupla_p):
    med_cuat1=nota_cuatrimestre(tupla_t[:2],tupla_p[0])
    med_cuat2=nota_cuatrimestre(tupla_t[2:],tupla_p[1])

    return nota_media([med_cuat1,med_cuat2])
