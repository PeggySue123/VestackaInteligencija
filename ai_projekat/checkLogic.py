from tkinter import Frame, Label

def jelSlobodno(a: int, b: int, fields: list[Label]) -> bool:
    for field in fields :
        if(field.grid_info()['row']-1 == a*2 and field.grid_info()['column'] == b*2):
            if(field.cget("text")=="X1" or field.cget("text")=="X2" or field.cget("text")=="O1" or field.cget("text")=="O2"):
                return False
    return True


def dijagonalaGoreDesno(a: int, b: int, zidovi: list[Label], fields: list[Label], pocetnoStanje: list[int]) -> bool :
    index1 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2 +1, b*2+1)]
    index2 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2, b*2)]
    index3 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2, b*2+2)]
    index4 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2-1, b*2+1)]
    if(postojiPutanja(pocetnoStanje, zidovi, fields)):
        if (index1):
            if(index2 or index4):
                return False
            else: return True
        elif (index2):
            if (index4):
                return False
            else: return True
        elif (index3):
            if (index4):
                return False
            else: return True
        else: return True
    else:
        return False

def dijagonalaGoreLevo(a: int, b: int, zidovi: list[Label], fields: list[Label], pocetnoStanje: list[int]) -> bool :
    index1 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2, b*2-2)]
    index2 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2+1, b*2-1)]
    index3 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2, b*2)]
    index4 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2-1, b*2-1)]
    if(postojiPutanja(pocetnoStanje, zidovi, fields)):
        if (index1):
            if(index3 or index4):
                return False
            else: return True
        elif (index2):
            if (index3 or index4):
                return False
            else: return True
        else:
            return True
    else:
        return False

def dijagonalaDoleDesno(a: int, b: int, zidovi: list[Label], fields: list[Label], pocetnoStanje: list[int]) -> bool :
    index1 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2+2, b*2+2)]
    index2 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2+1, b*2+1)]
    index3 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2+2, b*2)]
    index4 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2+3, b*2+1)]
    if(postojiPutanja(pocetnoStanje, zidovi, fields)):
        if (index1):
            if(index3 or index4):
                return False
            else: return True
        elif (index2):
            if (index3 or index4):
                return False
            else: return True
        else:
            return True
    else:
        return False

def dijagonalaDoleLevo(a: int, b: int, zidovi: list[Label], fields: list[Label], pocetnoStanje: list[int]) -> bool :
    index1 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2+2, b*2-2)]
    index2 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2+1, b*2-1)]
    index3 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2+2, b*2)]
    index4 = [idx for idx, element in enumerate(zidovi) if condition(element, a*2+3, b*2-1)]
    if(postojiPutanja(pocetnoStanje, zidovi, fields)):
        if (index1):
            if(index3 or index4):
                return False
            else: return True
        elif (index2):
            if (index3 or index4):
                return False
            else: return True
        else:
            return True
    else:
        return False

def proveraPromenePesaka(a: int, b: int, c:int, args: list[int], zidovi: list[Label], fields: list[Label], pocetak:list[int]) -> bool :
    if(c==1):
        #provera da li se kreće dva polja ako nema zida i moze na startno polje protivnika
        if((any(int(z.grid_info()['row'])-1 == args[0]*2+3 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and any(int(z.grid_info()['row'])-1 == args[0]*2+1 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and args[0]+2 == a and args[1] == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))) or (args[0] == a and any(int(z.grid_info()['column']) == args[1]*2+3 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi)==False and any(int(z.grid_info()['column']) == args[1]*2+1 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi)==False and args[1]+2 == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11])))):
            return True
        if((any(int(z.grid_info()['row'])-1 == args[0]*2-3 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and any(int(z.grid_info()['row'])-1 == args[0]*2-1 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and args[0]-2 == a and args[1]==b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))) or (args[0]==a and any(int(z.grid_info()['column']) == args[1]*2-3 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi)==False and any(int(z.grid_info()['column']) == args[1]*2-1 and int(z.grid_info()['row'])-1 == args[0]*2 for z in zidovi)==False and args[1]-2 == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11])))):
            return True
        #provera da li se kreće dva polja ako nema zida
        if((any(int(z.grid_info()['row'])-1 == args[0]*2+3 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and any(int(z.grid_info()['row'])-1 == args[0]*2+1 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and args[0]+2 == a and args[1] == b and jelSlobodno(a, b, fields)) or (args[0] == a and any(int(z.grid_info()['column']) == args[1]*2+3 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi)==False and any(int(z.grid_info()['column']) == args[1]*2+1 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi)==False and args[1]+2 == b and jelSlobodno(a, b, fields))):
            return True
        if((any(int(z.grid_info()['row'])-1 == args[0]*2-3 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and any(int(z.grid_info()['row'])-1 == args[0]*2-1 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and args[0]-2 == a and args[1]==b and jelSlobodno(a, b, fields)) or (args[0]==a and any(int(z.grid_info()['column']) == args[1]*2-3 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi)==False and any(int(z.grid_info()['column']) == args[1]*2-1 and int(z.grid_info()['row'])-1 == args[0]*2 for z in zidovi)==False and args[1]-2 == b and jelSlobodno(a, b, fields))):
            return True
        #ako je pored startnog polja, da li se krece jedno polje
        if ((any(int(z.grid_info()['row'])-1 == args[0]*2+1 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and args[0]+1 == a and args[1] == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))) or (any(int(z.grid_info()['column']) == args[1]*2+1 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi)==False and args[0] == a and args[1]+1 == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11])))):
            return True
        if ((any(int(z.grid_info()['row'])-1 == args[0]*2-1 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and args[0]-1 == a and args[1] == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))) or (any(int(z.grid_info()['column']) == args[1]*2-1 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi)==False and args[0] == a and args[1]-1 == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11])))):
            return True
        #ako ima zida, da li se kreće jedno polje + ako ima pešaka da li se kreće jedno polje
        if((any(int(z.grid_info()['row'])-1 == args[0]*2+3 and z.grid_info()['column'] == args[1]*2 for z in zidovi) and any(int(z.grid_info()['row'])-1 == args[0]*2+1 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and args[0]+1 == a and args[1] == b and jelSlobodno(a, b, fields)) or (args[0] == a and any(int(z.grid_info()['column']) == args[1]*2+3 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi) and any(int(z.grid_info()['column']) == args[1]*2+1 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi)==False and args[1]+1 == b and jelSlobodno(a, b, fields)) or (any(int(z.grid_info()['row'])-1 == args[0]*2+1 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and args[0]+1 == a and args[1] == b and jelSlobodno(a, b, fields) and jelSlobodno(a+1, b, fields) == False) or (args[0] == a and any(int(z.grid_info()['column']) == args[1]*2+1 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi)==False and args[1]+1 == b and jelSlobodno(a, b, fields) and jelSlobodno(a, b+1, fields)==False)):
            return True
        if((any(int(z.grid_info()['row'])-1 == args[0]*2-3 and z.grid_info()['column'] == args[1]*2 for z in zidovi) and any(int(z.grid_info()['row'])-1 == args[0]*2-1 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and args[0]-1 == a and args[1]==b and jelSlobodno(a, b, fields)) or (args[0]==a and any(int(z.grid_info()['column']) == args[1]*2-3 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi) and any(int(z.grid_info()['column']) == args[1]*2-1 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi)==False and args[1]-1 == b and jelSlobodno(a, b, fields)) or (any(int(z.grid_info()['row'])-1 == args[0]*2-1 and z.grid_info()['column'] == args[1]*2 for z in zidovi)==False and args[0]-1 == a and args[1]==b and jelSlobodno(a, b, fields) and jelSlobodno(a-1, b, fields)==False) or (args[0]==a and any(int(z.grid_info()['column']) == args[1]*2-1 and z.grid_info()['row']-1 == args[0]*2 for z in zidovi)==False and args[1]-1 == b and jelSlobodno(a, b, fields) and jelSlobodno(a, b-1, fields) == False)):
            return True
        #da li se kreće jedno polje u dijagonalu
        if(args[0]+1==a and args[1]+1==b and dijagonalaDoleDesno(args[0], args[1], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        if(args[0]+1==a and args[1]-1==b and dijagonalaDoleLevo(args[0], args[1], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        if(args[0]-1==a and args[1]+1==b and dijagonalaGoreDesno(args[0], args[1], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        if(args[0]-1==a and args[1]-1==b and dijagonalaGoreLevo(args[0], args[1], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        #da li se kreće jedno polje u dijagonalu do startnog polja
        if(args[0]+1==a and args[1]+1==b and dijagonalaDoleDesno(args[0], args[1], zidovi, fields, pocetak) and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))):
            return True
        if(args[0]+1==a and args[1]-1==b and dijagonalaDoleLevo(args[0], args[1], zidovi, fields, pocetak) and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))):
            return True
        if(args[0]-1==a and args[1]+1==b and dijagonalaGoreDesno(args[0], args[1], zidovi, fields, pocetak) and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))):
            return True
        if(args[0]-1==a and args[1]-1==b and dijagonalaGoreLevo(args[0], args[1], zidovi, fields, pocetak) and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))):
            return True
        return False
    elif(c==2):
        #provera da li se kreće dva polja ako nema zida i moze na startno polje protivnika
        if((any(z.grid_info()['row']-1 == args[2]*2+3 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[2]*2+1 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and args[2]+2 == a and args[3] == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))) or (args[2] == a and any(z.grid_info()['column'] == args[3]*2+3 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[3]*2+1 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and args[3]+2 == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11])))):
            return True
        if((any(z.grid_info()['row']-1 == args[2]*2-3 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[2]*2-1 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and args[2]-2 == a and args[3]==b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))) or (args[2]==a and any(z.grid_info()['column'] == args[3]*2-3 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[3]*2-1 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and args[3]-2 == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11])))):
            return True
        #provera da li se kreće dva polja ako nema zida
        if((any(z.grid_info()['row']-1 == args[2]*2+3 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[2]*2+1 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and args[2]+2 == a and args[3] == b and jelSlobodno(a, b, fields)) or (args[2] == a and any(z.grid_info()['column'] == args[3]*2+3 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[3]*2+1 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and args[3]+2 == b and jelSlobodno(a, b, fields))):
            return True
        if((any(z.grid_info()['row']-1 == args[2]*2-3 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[2]*2-1 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and args[2]-2 == a and args[3]==b and jelSlobodno(a, b, fields)) or (args[2]==a and any(z.grid_info()['column'] == args[3]*2-3 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[3]*2-1 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and args[3]-2 == b and jelSlobodno(a, b, fields))):
            return True
        #ako je pored startnog polja, da li se krece jedno polje
        if ((any(int(z.grid_info()['row'])-1 == args[2]*2+1 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and args[2]+1 == a and args[3] == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))) or (any(int(z.grid_info()['column']) == args[3]*2+1 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and args[2] == a and args[3]+1 == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11])))):
            return True
        if ((any(int(z.grid_info()['row'])-1 == args[2]*2-1 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and args[2]-1 == a and args[3] == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))) or (any(int(z.grid_info()['column']) == args[3]*2-1 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and args[2] == a and args[3]-1 == b and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11])))):
            return True
        #ako ima zida, da li se kreće jedno polje + ako ima pešaka da li se kreće jedno polje
        if((any(z.grid_info()['row']-1 == args[2]*2+3 and z.grid_info()['column'] == args[3]*2 for z in zidovi) and any(z.grid_info()['row']-1 == args[2]*2+1 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and args[2]+1 == a and args[3] == b and jelSlobodno(a, b, fields)) or (args[2] == a and any(z.grid_info()['column'] == args[3]*2+3 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi) and any(z.grid_info()['column'] == args[3]*2+1 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and args[3]+1 == b and jelSlobodno(a, b, fields)) or (any(z.grid_info()['row']-1 == args[2]*2+1 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and args[2]+1 == a and args[3] == b and jelSlobodno(a, b, fields) and jelSlobodno(a+1, b, fields)==False) or (args[2] == a and any(z.grid_info()['column'] == args[3]*2+1 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and args[3]+1 == b and jelSlobodno(a, b, fields) and jelSlobodno(a, b+1, fields)==False)):
            return True
        if((any(z.grid_info()['row']-1 == args[2]*2-3 and z.grid_info()['column'] == args[3]*2 for z in zidovi) and any(z.grid_info()['row']-1 == args[2]*2-1 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and args[2]-1 == a and args[3]==b and jelSlobodno(a, b, fields)) or (args[2]==a and any(z.grid_info()['column'] == args[3]*2-3 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi) and any(z.grid_info()['column'] == args[3]*2-1 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and args[3]-1 == b and jelSlobodno(a, b, fields)) or (any(z.grid_info()['row']-1 == args[2]*2-1 and z.grid_info()['column'] == args[3]*2 for z in zidovi)==False and args[2]-1 == a and args[3]==b and jelSlobodno(a, b, fields) and jelSlobodno(a-1, b, fields)==False) or (args[2]==a and any(z.grid_info()['column'] == args[3]*2-1 and z.grid_info()['row']-1 == args[2]*2 for z in zidovi)==False and args[3]-1 == b and jelSlobodno(a, b, fields) and jelSlobodno(a, b-1, fields)==False)):
            return True
        #da li se kreće jedno polje u dijagonalu
        if(args[2]+1==a and args[3]+1==b and dijagonalaDoleDesno(args[2], args[3], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        if(args[2]+1==a and args[3]-1==b and dijagonalaDoleLevo(args[2], args[3], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        if(args[2]-1==a and args[3]+1==b and dijagonalaGoreDesno(args[2], args[3], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        if(args[2]-1==a and args[3]-1==b and dijagonalaGoreLevo(args[2], args[3], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        #da li se kreće jedno polje u dijagonalu do startnog polja
        if(args[2]+1==a and args[3]+1==b and dijagonalaDoleDesno(args[2], args[3], zidovi, fields, pocetak) and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))):
            return True
        if(args[2]+1==a and args[3]-1==b and dijagonalaDoleLevo(args[2], args[3], zidovi, fields, pocetak) and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))):
            return True
        if(args[2]-1==a and args[3]+1==b and dijagonalaGoreDesno(args[2], args[3], zidovi, fields, pocetak) and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))):
            return True
        if(args[2]-1==a and args[3]-1==b and dijagonalaGoreLevo(args[2], args[3], zidovi, fields, pocetak) and ((a == pocetak[8] and b == pocetak[9]) or (a == pocetak[10] and b == pocetak[11]))):
            return True
        return False
    elif(c==3):
        #provera da li se kreće dva polja ako nema zida i moze na startno polje protivnika
        if((any(z.grid_info()['row']-1 == args[4]*2+3 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[4]*2+1 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and args[4]+2 == a and args[5] == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))) or (args[4] == a and any(z.grid_info()['column'] == args[5]*2+3 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[5]*2+1 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and args[5]+2 == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7])))):
            return True
        if((any(z.grid_info()['row']-1 == args[4]*2-3 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[4]*2-1 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and args[4]-2 == a and args[5]==b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))) or (args[4]==a and any(z.grid_info()['column'] == args[5]*2-3 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[5]*2-1 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and args[5]-2 == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7])))):
            return True
        #provera da li se kreće dva polja ako nema zida
        if((any(z.grid_info()['row']-1 == args[4]*2+3 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[4]*2+1 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and args[4]+2 == a and args[5] == b and jelSlobodno(a, b, fields)) or (args[4] == a and any(z.grid_info()['column'] == args[5]*2+3 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[5]*2+1 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and args[5]+2 == b and jelSlobodno(a, b, fields))):
            return True
        if((any(z.grid_info()['row']-1 == args[4]*2-3 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[4]*2-1 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and args[4]-2 == a and args[5]==b and jelSlobodno(a, b, fields)) or (args[4]==a and any(z.grid_info()['column'] == args[5]*2-3 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[5]*2-1 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and args[5]-2 == b and jelSlobodno(a, b, fields))):
            return True
        #ako je pored startnog polja, da li se krece jedno polje
        if ((any(int(z.grid_info()['row'])-1 == args[4]*2+1 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and args[4]+1 == a and args[5] == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))) or (any(int(z.grid_info()['column']) == args[5]*2+1 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and args[4] == a and args[5]+1 == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7])))):
            return True
        if ((any(int(z.grid_info()['row'])-1 == args[4]*2-1 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and args[4]-1 == a and args[5] == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))) or (any(int(z.grid_info()['column']) == args[5]*2-1 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and args[4] == a and args[5]-1 == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7])))):
            return True
        #ako ima zida, da li se kreće jedno polje + ako ima pešaka da li se kreće jedno polje
        if((any(z.grid_info()['row']-1 == args[4]*2+3 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[4]*2+1 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and args[4]+1 == a and args[5] == b and jelSlobodno(a, b, fields)) or (args[4] == a and any(z.grid_info()['column'] == args[5]*2+3 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[5]*2+1 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and args[5]+1 == b and jelSlobodno(a, b, fields)) or (any(z.grid_info()['row']-1 == args[4]*2+1 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and args[4]+1 == a and args[5] == b and jelSlobodno(a, b, fields) and jelSlobodno(a+1, b, fields) == False) or (args[4] == a and any(z.grid_info()['column'] == args[5]*2+1 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and args[5]+1 == b and jelSlobodno(a, b, fields) and jelSlobodno(a, b+1, fields)==False)):
            return True
        if((any(z.grid_info()['row']-1 == args[4]*2-3 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[4]*2-1 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and args[4]-1 == a and args[5]==b and jelSlobodno(a, b, fields)) or (args[4]==a and any(z.grid_info()['column'] == args[5]*2-3 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[5]*2-1 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and args[5]-1 == b and jelSlobodno(a, b, fields)) or (any(z.grid_info()['row']-1 == args[4]*2-1 and z.grid_info()['column'] == args[5]*2 for z in zidovi)==False and args[4]-1 == a and args[5]==b and jelSlobodno(a, b, fields) and jelSlobodno(a-1, b, fields) == False) or (args[4]==a and any(z.grid_info()['column'] == args[5]*2-1 and z.grid_info()['row']-1 == args[4]*2 for z in zidovi)==False and args[5]-1 == b and jelSlobodno(a, b, fields) and jelSlobodno(a, b-1, fields) == False)):
            return True
        #da li se kreće jedno polje u dijagonalu
        if(args[4]+1==a and args[5]+1==b and dijagonalaDoleDesno(args[4], args[5], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        if(args[4]+1==a and args[5]-1==b and dijagonalaDoleLevo(args[4], args[5], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        if(args[4]-1==a and args[5]+1==b and dijagonalaGoreDesno(args[4], args[5], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        if(args[4]-1==a and args[5]-1==b and dijagonalaGoreLevo(args[4], args[5], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        #da li se kreće jedno polje u dijagonalu do startnog polja
        if(args[4]+1==a and args[5]+1==b and dijagonalaDoleDesno(args[4], args[5], zidovi, fields, pocetak) and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))):
            return True
        if(args[4]+1==a and args[5]-1==b and dijagonalaDoleLevo(args[4], args[5], zidovi, fields, pocetak) and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))):
            return True
        if(args[4]-1==a and args[5]+1==b and dijagonalaGoreDesno(args[4], args[5], zidovi, fields, pocetak) and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))):
            return True
        if(args[4]-1==a and args[5]-1==b and dijagonalaGoreLevo(args[4], args[5], zidovi, fields, pocetak) and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))):
            return True
        return False
    else:
        #provera da li se kreće dva polja ako nema zida i moze na startno polje protivnika
        if((any(z.grid_info()['row']-1 == args[6]*2+3 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[6]*2+1 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and args[6]+2 == a and args[7] == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))) or (args[6] == a and any(z.grid_info()['column'] == args[7]*2+3 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[7]*2+1 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and args[7]+2 == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7])))):
            return True
        if((any(z.grid_info()['row']-1 == args[6]*2-3 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[6]*2-1 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and args[6]-2 == a and args[7]==b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))) or (args[6]==a and any(z.grid_info()['column'] == args[7]*2-3 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[7]*2-1 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and args[7]-2 == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7])))):
            return True
        #provera da li se kreće dva polja ako nema zida
        if((any(z.grid_info()['row']-1 == args[6]*2+3 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[6]*2+1 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and args[6]+2 == a and args[7] == b and jelSlobodno(a, b, fields)) or (args[6] == a and any(z.grid_info()['column'] == args[7]*2+3 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[7]*2+1 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and args[7]+2 == b and jelSlobodno(a, b, fields))):
            return True
        if((any(z.grid_info()['row']-1 == args[6]*2-3 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[6]*2-1 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and args[6]-2 == a and args[7]==b and jelSlobodno(a, b, fields)) or (args[6]==a and any(z.grid_info()['column'] == args[7]*2-3 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[7]*2-1 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and args[7]-2 == b and jelSlobodno(a, b, fields))):
            return True
        #ako je pored startnog polja, da li se krece jedno polje
        if ((any(int(z.grid_info()['row'])-1 == args[6]*2+1 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and args[6]+1 == a and args[7] == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))) or (any(int(z.grid_info()['column']) == args[7]*2+1 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and args[6] == a and args[7]+1 == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7])))):
            return True
        if ((any(int(z.grid_info()['row'])-1 == args[6]*2-1 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and args[6]-1 == a and args[7] == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))) or (any(int(z.grid_info()['column']) == args[7]*2-1 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and args[6] == a and args[7]-1 == b and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7])))):
            return True
        #ako ima zida, da li se kreće jedno polje + ako ima pešaka da li se kreće jedno polje
        if((any(z.grid_info()['row']-1 == args[6]*2+3 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[6]*2+1 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and args[6]+1 == a and args[7] == b and jelSlobodno(a, b, fields)) or (args[6] == a and any(z.grid_info()['column'] == args[7]*2+3 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[7]*2+1 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and args[7]+1 == b and jelSlobodno(a, b, fields)) or (any(z.grid_info()['row']-1 == args[6]*2+1 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and args[6]+1 == a and args[7] == b and jelSlobodno(a, b, fields) and jelSlobodno(a+1, b, fields) == False) or (args[6] == a and  any(z.grid_info()['column'] == args[7]*2+1 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and args[7]+1 == b and jelSlobodno(a, b, fields) and jelSlobodno(a, b+1, fields) == False)):
            return True
        if((any(z.grid_info()['row']-1 == args[6]*2-3 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and any(z.grid_info()['row']-1 == args[6]*2-1 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and args[6]-1 == a and args[7]==b and jelSlobodno(a, b, fields)) or (args[6]==a and any(z.grid_info()['column'] == args[7]*2-3 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and any(z.grid_info()['column'] == args[7]*2-1 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and args[7]-1 == b and jelSlobodno(a, b, fields)) or (any(z.grid_info()['row']-1 == args[6]*2-1 and z.grid_info()['column'] == args[7]*2 for z in zidovi)==False and args[6]-1 == a and args[7]==b and jelSlobodno(a, b, fields) and jelSlobodno(a-1, b, fields) == False) or (args[6]==a and any(z.grid_info()['column'] == args[7]*2-1 and z.grid_info()['row']-1 == args[6]*2 for z in zidovi)==False and args[7]-1 == b and jelSlobodno(a, b, fields) and jelSlobodno(a, b-1, fields)==False)):
            return True
        #da li se kreće jedno polje u dijagonalu
        if(args[6]+1==a and args[7]+1==b and dijagonalaDoleDesno(args[6], args[7], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        if(args[6]+1==a and args[7]-1==b and dijagonalaDoleLevo(args[6], args[7], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        if(args[6]-1==a and args[7]+1==b and dijagonalaGoreDesno(args[6], args[7], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        if(args[6]-1==a and args[7]-1==b and dijagonalaGoreLevo(args[6], args[7], zidovi, fields, pocetak) and jelSlobodno(a, b, fields)):
            return True
        #da li se kreće jedno polje u dijagonalu do startnog polja
        if(args[6]+1==a and args[7]+1==b and dijagonalaDoleDesno(args[6], args[7], zidovi, fields, pocetak) and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))):
            return True
        if(args[6]+1==a and args[7]-1==b and dijagonalaDoleLevo(args[6], args[7], zidovi, fields, pocetak) and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))):
            return True
        if(args[6]-1==a and args[7]+1==b and dijagonalaGoreDesno(args[6], args[7], zidovi, fields, pocetak) and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))):
            return True
        if(args[6]-1==a and args[7]-1==b and dijagonalaGoreLevo(args[6], args[7], zidovi, fields, pocetak) and ((a == pocetak[4] and b == pocetak[5]) or (a == pocetak[6] and b == pocetak[7]))):
            return True
        return False

def proveraPromeneZida(args: list[int], fields: list[Label], zidovi: list[Label], a: list[int], walls: list[Label], frame: Frame) -> bool :
    for wall in zidovi:
        if args[8] == 0:
            for w in walls:
                if (w.grid_info()['row']-1 == args[0] * 2 and w.grid_info()['column'] == args[1] * 2 + 1):
                    zidovi.append(w)
                    label = Label(frame, text='||', width=3)
                    zidovi.append(label)
                    label.grid(row = int(args[0]) * 2 + 2, column= int(args[1]) * 2 + 1)
                elif (w.grid_info()['row']-1 == args[4] * 2 and w.grid_info()['column'] == args[5] * 2 + 1):
                    zidovi.append(w)
            x = postojiPutanja(a, zidovi, fields)
            zidovi.pop()
            label = zidovi.pop()
            zidovi.pop()
            label.grid_forget()
            if (not x):
                return False
            elif ((wall.grid_info()['row']-1 == args[0]*2 and wall.grid_info()['column'] == args[1]*2 + 1) or (wall.grid_info()['row']-1 == args[4]*2 and wall.grid_info()['column'] == args[5]*2 + 1)):
                return False
            else:
                if (wall.grid_info()['row']-2 == args[0]*2 + 1 and wall.grid_info()['column'] == args[1]*2):
                    if (zidovi.index(wall) % 3 == 0):
                        return False
        else:
            for w in walls:
                if (w.grid_info()['row']-1 == args[0] * 2 + 1 and w.grid_info()['column'] == args[1] * 2):
                    zidovi.append(w)
                    label = Label(frame, text='=', width=3)
                    zidovi.append(label)
                    label.grid(row = args[0] * 2 + 2, column= args[1] * 2 + 1)
                elif (w.grid_info()['row']-1 == args[2] * 2 + 1 and w.grid_info()['column'] == args[3] * 2):
                    zidovi.append(w)
            x = postojiPutanja(a, zidovi, fields)
            zidovi.pop()
            label = zidovi.pop()
            zidovi.pop()
            label.grid_forget()
            if (not x):
                return False
            elif ((wall.grid_info()['row']-1 == args[0]*2 + 1 and wall.grid_info()['column'] == args[1]*2) or (wall.grid_info()['row']-1 == args[2]*2 + 1 and wall.grid_info()['column'] == args[3]*2)):
                return False
            else:
                if (wall.grid_info()['row']-1 == args[0]*2 and wall.grid_info()['column'] == args[1]*2 + 1):
                    if (zidovi.index(wall) % 3 == 0):
                        return False
    return True
    
def imaLiZidova(a: int, b: int, args: list[int]) -> bool:
    if(a == 0):
        if(b == 0):
            if(args[8]>0):
                return True
            else:
                return False
        else:
            if(args[9] > 0):
                return True
            else: 
                return False
    else:
        if(b == 0):
            if(args[10]>0):
                return True
            else:
                return False
        else:
            if(args[11] > 0):
                return True
            else: 
                return False

def postojiPutanja(a: list[int], zidovi: list[Label], fields: list[Label]) -> bool:
    graf = napraviGraf(int((a[0]- 3)/2 ), int((a[1] - 3)/2 ), fields, zidovi, a)
    end1 = str(fields[int((a[8] - 1)*((a[1] - 3)/2) + a[9] - 1)].cget('text'))
    end2 = str(fields[int((a[10] - 1)*((a[1] - 3)/2) + a[11] - 1)].cget('text'))
    end3 = str(fields[int((a[4] - 1)*((a[1] - 3)/2) + a[5] - 1)].cget('text'))
    end4 = str(fields[int((a[6] - 1)*((a[1] - 3)/2) + a[7] - 1)].cget('text'))
    return ((BreadthFirstSearch(graf, 'X1', end1, [], []) and BreadthFirstSearch(graf, 'X1', end2, [], [])) and (BreadthFirstSearch(graf, 'X2', end1, [], []) and BreadthFirstSearch(graf, 'X2', end2, [], [])) and (BreadthFirstSearch(graf, 'O1', end3, [], []) and BreadthFirstSearch(graf, 'O1', end4, [], [])) and (BreadthFirstSearch(graf, 'O2', end3, [], []) and BreadthFirstSearch(graf, 'O2', end4, [], [])))

def napraviGraf(n: int, m: int, fields: list[Label], zidovi: list[Label], a: list[int]) -> dict[str, list[str]]:
    graf: dict[str, list[str]] = {}
    for field in fields:
        graf[field.cget('text')] = []
        if (field.grid_info()['row'] - 1 == 2):
            if (field.grid_info()['column'] == 2):
                index1 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 1)]
                index2 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'])]
                index3 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 2, field.grid_info()['column'] + 1)]
                index4 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'] + 2)]
                if not index1:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 1)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + 1)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2)].cget('text')))
                if not index2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 3, field.grid_info()['column'])])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2 * m)].cget('text')))
                if index1:
                    if not index2 and not index3:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                elif index2:
                    if not index4:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                elif index3:
                    if not index4:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                else:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
            elif (field.grid_info()['column'] == m * 2):
                index1 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] - 1)]
                index2 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'])]
                index3 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 2, field.grid_info()['column'] - 1)]
                index4 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'] - 2)]
                if not index1:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 1)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - 1)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] - 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 2)].cget('text')))
                if not index2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2 * m)].cget('text')))
                if index1:
                    if not index2 and not index3:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                elif index2:
                    if not index4:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                elif index3:
                    if not index4:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
            else:
                index1 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] - 1)]
                index2 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'])]
                index3 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 1)]
                index4 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'] - 2)]
                index5 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 2, field.grid_info()['column'] - 1)]
                index6 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 2, field.grid_info()['column'] + 1)]
                index7 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'] + 2)]
                if not index1 and field.grid_info()['column'] != 4:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 1)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - 1)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] - 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 2)].cget('text')))
                if not index2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 3, field.grid_info()['column'])])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2 * m)].cget('text')))
                if not index3 and field.grid_info()['column'] != m * 2 - 2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 1)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + 1)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2)].cget('text')))
                if index1:
                    if not index2 and not index5:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                elif index2:
                    if not index4:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                elif index4:
                    if not index5:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                if index2:
                    if not index3 and not index7:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                elif index3:
                    if not index6:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                elif index6:
                    if not index7:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
        elif(field.grid_info()['row'] - 1 == n*2):
            if (field.grid_info()['column'] == 2):
                index1 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'])]
                index2 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 1)]
                index3 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'] + 2)]
                index4 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 2, field.grid_info()['column'] + 1)]
                if not index1:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 3, field.grid_info()['column'])])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 2 * m)].cget('text')))
                if not index2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 1)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + 1)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2 * m)].cget('text')))
                if index1:
                    if not index3 and not index2:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                elif index2:
                    if not index4:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                elif index3:
                    if not index4:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
            elif (field.grid_info()['column'] == m * 2):
                index1 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] - 1)]
                index2 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'])]
                index3 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 2, field.grid_info()['column'] - 1)]
                index4 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'] - 2)]
                if not index1:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 1)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - 1)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] - 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 2)].cget('text')))
                if not index2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 3, field.grid_info()['column'])])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 2 * m)].cget('text')))
                if index1:
                    if not index2 and not index3:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                elif index2:
                    if not index4:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                elif index3:
                    if not index4:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
            else:
                index1 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] - 1)]
                index2 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'])]
                index3 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 1)]
                index4 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'] - 2)]
                index5 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 2, field.grid_info()['column'] - 1)]
                index6 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 2, field.grid_info()['column'] + 1)]
                index7 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'] + 2)]
                if not index1 and field.grid_info()['column'] != 4:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 1)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - 1)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] - 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2 * m)].cget('text')))
                if not index2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 3, field.grid_info()['column'])])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 2 * m)].cget('text')))
                if not index3 and field.grid_info()['column'] != m * 2 - 2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 1)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + 1)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2 * m)].cget('text')))
                if index1:
                    if not index2 and not index5:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                elif index2:
                    if not index4:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                elif index4:
                    if not index5:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                if index2:
                    if not index3 and not index7:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                elif index3:
                    if not index6:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                elif index6:
                    if not index7:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
        else:
            if (field.grid_info()['column'] == 2):
                index1 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'])]
                index2 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 1)]
                index3 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'])]
                index4 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 2, field.grid_info()['column'] + 1)]
                index5 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'] + 2)]
                index6 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'] + 2)]
                index7 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 2, field.grid_info()['column'] + 1)]
                if not index1 and field.grid_info()['row'] - 1 != 4:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 3, field.grid_info()['column'])])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 2 * m)].cget('text')))
                if not index2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 1)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + 1)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2)].cget('text')))
                if not index3 and field.grid_info()['row'] - 1 != n * 2 - 2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 3, field.grid_info()['column'])])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2 * m)].cget('text')))
                if index1:
                    if not index2 and not index5:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                elif index2:
                    if not index4:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                elif index4:
                    if not index5:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                if index2:
                    if not index3 and not index7:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                elif index3:
                    if not index6:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                elif index6:
                    if not index7:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
            elif (field.grid_info()['column'] == m*2):
                index1 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'])]
                index2 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] - 1)]
                index3 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'])]
                index4 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 2, field.grid_info()['column'] - 1)]
                index5 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'] - 2)]
                index6 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'] - 2)]
                index7 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 2, field.grid_info()['column'] - 1)]
                if not index1 and field.grid_info()['row'] - 1 != 4:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 3, field.grid_info()['column'])])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 2 * m)].cget('text')))
                if not index2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 1)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - 1)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] - 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 2)].cget('text')))
                if not index3 and field.grid_info()['row'] - 1 != n * 2 - 2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 3, field.grid_info()['column'])])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2 * m)].cget('text')))
                if index1:
                    if not index2 and not index5:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                elif index2:
                    if not index4:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                elif index4:
                    if not index5:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                if index2:
                    if not index3 and not index7:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                elif index3:
                    if not index6:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                elif index6:
                    if not index7:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
            else:
                index1 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'])]
                index2 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] - 1)]
                index3 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'])]
                index4 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 1)]
                index5 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'] - 2)]
                index6 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 2, field.grid_info()['column'] - 1)]
                index7 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 2, field.grid_info()['column'] - 1)]
                index8 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'] - 2)]
                index9 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 1, field.grid_info()['column'] + 2)]
                index10 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 2, field.grid_info()['column'] + 1)]
                index11 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 1, field.grid_info()['column'] + 2)]
                index12 = [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 2, field.grid_info()['column'] + 1)]
                if not index1 and field.grid_info()['row'] - 1 != 4:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] - 3, field.grid_info()['column'])])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 2 * m)].cget('text')))
                if not index2 and field.grid_info()['column'] != 4:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 1)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - 1)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] - 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - 2)].cget('text')))
                if not index3 and field.grid_info()['row'] - 1 != n * 2 - 2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'] + 3, field.grid_info()['column'])])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2 * m)].cget('text')))
                if not index4 and field.grid_info()['column'] != m * 2 - 2:
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 1)].cget('text')))
                    if (not daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + 1)]) and (not [idx for idx, element in enumerate(zidovi) if condition(element, field.grid_info()['row'], field.grid_info()['column'] + 3)])):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + 2)].cget('text')))
                if index1:
                    if not index2 and not index5:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) -m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                elif index2:
                    if not index6:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) -m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                elif index5:
                    if not index6:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) -m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) -m - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m - 1)].cget('text')))
                if index2:
                    if not index3 and not index7:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                elif index3:
                    if not index8:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                elif index7:
                    if not index8:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m - 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m - 1)].cget('text')))
                if index3:
                    if not index4 and not index9:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                elif index4:
                    if not index10:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                elif index9:
                    if not index10:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) + m + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) + m + 1)].cget('text')))
                if index1:
                    if not index4 and not index11:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                elif index4:
                    if not index12:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                elif index11:
                    if not index12:
                        if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                            graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
                else: 
                    if daLiNijePoljeSPesakom(a, fields[int(fields.index(field) - m + 1)]):
                        graf[field.cget('text')].append(str(fields[int(fields.index(field) - m + 1)].cget('text')))
    return graf

def condition(x: Label, i: int, j: int): return int(x.grid_info()['row']) == i and int(x.grid_info()['column']) == j

def BreadthFirstSearch(graph: dict[str, list[str]], start: str, end: str, obradjeni: list[str], red: list[str]) -> bool:
    if start not in red:
        red.append(start)
    while len(red) > 0:
        keyNode = red.pop(0)
        susedi = graph[keyNode]
        for node in susedi:
            if node == end:
                return True
            if node in obradjeni:
                continue
            if node not in red:
                red.append(node)
        obradjeni.append(keyNode)
    return False

def daLiNijePoljeSPesakom(a: list[int], field: Label):
    k1 = int(int(field.grid_info()['row'] - 1) / 2)
    k2 = int(field.grid_info()['column'] / 2)
    pesak = field.cget('text')
    if (k1 == a[4] and k2 == a[5]):
        return True
    if (k1 == a[6] and k2 == a[7]):
        return True
    if (k1 == a[8] and k2 == a[9]):
        return True
    if (k1 == a[10] and k2 == a[11]):
        return True
    if (pesak != 'X1'):
        return True
    if (pesak != 'X2'):
        return True
    if (pesak != 'O1'):
        return True
    if (pesak != 'O2'):
        return True
    return False