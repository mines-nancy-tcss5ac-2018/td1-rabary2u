#PROJET EULER

##projet16

def projet16(n):
    N=list(str(2**n))
    Nu=[int(i) for i in N]
    s=sum(Nu)
    return s



assert  projet16(15)==26
print(projet16(1000))



##projet22

f = open('p022_names.txt', 'r')

#création de la liste et tri par ordre alphabétique

def tri(f):
    Paragraphe=[]
    for i in f:
        Paragraphe.append(i)
    Noms=Paragraphe[0].replace('"','')
    Noms=Noms.split(",")
    Noms_t=sorted(Noms,key=str.lower)
    return Noms_t
        
#Fonction qui associe à une lettre son numéro dans l'alphabet

def alpha_num(lettre):
    alphabet=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    c=0
    while lettre!=alphabet[c] and c<25:
        c+=1
    return c+1

#Calacul du score de chaque nom ( calcul le score du #ième nom )

def score(liste,i):
    nom=list(liste[i-1])
    score=0
    for lettre in nom:
        score+= alpha_num(lettre)
    return score*i

#calcul final

def projet22(f):
    triee=tri(f)
    score_total=0
    for i in range(len(triee)):
        score_total+=score(triee,i+1)
    return score_total

assert score(tri(f),938)==49714



f = open('p022_names.txt', 'r')
print(projet22(f))



##Projet 55

#Créateur de palindromes entre 0 et 1000

def palyndromes():
    S=[]
    #palyndromes de 2 chiffres
    for i in range(1,10):
        S.append(int(str(i)*2))
    #palyndromes de 3 et 4 chiffres
    for i in range(1,10):
        for j in range(0,10):
            S.append(int(str(i)+str(j)*2+str(i)))
            S.append(int(str(i)+str(j)+str(i)))
    return S
            
#vérificateur de palyndrome:

def verification(nombre):
    L=list(str(nombre))
    longueur=len(L)
    for k in range(longueur//2):
        if L[k]!=L[longueur-k-1]:
            return False
    return True
    
#"addition palyndromique"

def somme_pal(pal):
    lpal=list(str(pal))
    ppal=''
    for i in range(len(lpal)-1,-1,-1):
        ppal+=lpal[i]
    return int(ppal)+pal


#verifcateur de nombre palindromique :

def ver_nom_pal(nombre):
    pal=nombre
    for i in range(50):
        pal=somme_pal(pal)
        if verification(pal)==True:
            return True
    return False
    

#creation de la liste finale :

def Lychrel(entree):
    lych_liste=[]
    for nombre in entree:
        if ver_nom_pal(nombre)==False:
            lych_liste.append(nombre)
    return lych_liste

def projet55():
    liste=palyndromes()
    return len(Lychrel(liste))



assert ver_nom_pal(4994)==False
print(projet55())






















