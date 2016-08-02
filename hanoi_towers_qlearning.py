import random

def moveInstruction(s1,s2):
	for c in range(0,len(s1)):
		if s1[c]!=s2[c]:
			return "Mover el Disco {} de: '{}' a: '{}'.".format(c+1,s1[c],s2[c]) 

def solve(pattern):
	state = symbols[pattern]
	x=0
	while True:		
		s = bestAction(state)
		print("Paso: {} = {}".format(x+1,moveInstruction(states[state][0],states[s][0])))
		pattern = states[s][0]
		a,b,c = states[s][1:]
		showStatus(state,pattern,a,b,c)
		state = s
		x+=1
		if s==80:
			break
	print("Resuelto en: {} pasos.".format(x))

def menu():
	while True:
		print('''1) Entrenar
2) Resolver
3) Salir''')
		o = int(input("Seleccione una opcion: "))
		if o == 1:
			train()
		elif o == 2:
			patron = input("Introduzca el estado inicial (AAAA - CCCC): ")
			solve(patron)
		else:
			break
	

def train():
	global R
	global Q
	global epoch
	state = random.randint(0,80)
	print("Epoch# {}, Inicio: {}".format(epoch,state))
	while True:
		while True:
			ra = random.randint(0,2)
			r = R[state][ra]
			if r != -1:
				break
		action = valid_states[state][ra]		
		Q[state][ra]=R[state][ra]+(0.8*max(Q[action]))
		#print("Epoch# {}, Q[{},{}] = {}".format(x,state,ra,int(Q[state][ra])))
		state = action
		if action == 80:
			break
	epoch+=1

def bestAction(state):
	index = 0
	maximum = -1
	for c in range(0,len(valid_states[state])):
		if Q[state][c]> maximum:
			maximum = Q[state][c]
			index = c
		elif Q[state][c] == maximum and random.randint(0,1)==1:
			maximum = Q[state][c]
			index = c			
	return valid_states[state][index]

def calculatePath(start):
	state = start
	c=0
	while True:		
		s = bestAction(state)
		print("{} -> {} ".format(state,s))
		state = s
		c+=1
		if s==80:
			break
	print("Resuelto en: {} pasos.".format(c))

def printLine(n):
    if n=="-":
        return "     |     "
    elif n == "1":
        return "    111    "
    elif n =="2":
        return "   22222   "
    elif n=="3":
        return "  3333333  "
    elif n=="4":
        return " 444444444 "
    else:
        return None
    
def showStatus(state, combination, a,b,c):
    print("_"*32)
    print()
    #print("Estado: {}".format(state))
    #print("Combinacion: {}\n".format(combination))    
    print("     A     "+"     B     "+"     C     ")
    for x in range (0,4):
        print(printLine(a[x])+ printLine(b[x]) + printLine(c[x]))
    #print("    {}       {}       {}   ".format(a,b,c))
    print()

def letter2State(letters):
    A=B=C=""
    n = len(letters)    
    c=1
    for l in letters:
        if l == "A":
            A+=str(c)
        elif l =="B":
            B+=str(c)
        elif l =="C":
            C+=str(c)
        c+=1
    A=A.rjust(n,"-")
    B=B.rjust(n,"-")
    C=C.rjust(n,"-")
    return [A,B,C]

def state2Letter(a,b,c):
    l =""
    for x in range(1,5):
        if str(x) in a:
            l+="A"
        if str(x) in b:
            l+="B"
        if str(x) in c:
            l+="C"
    return l

def topElement(x):
    if len(x)>0:
        return x[0]
    else:
        return ""

def normalizeState(a,b,c):
    a = a.rjust(4,'-')
    b = b.rjust(4,'-')
    c = c.rjust(4,'-')    
    return state2Letter(a,b,c)

def validMoves(letters, state):	
    #print("State: {}".format(state))
    #print("Valid moves for: {}".format(letters))
    ta=tb=tc=""
    a,b,c=letter2State(letters)
    a=a.strip('-')
    b=b.strip('-')
    c=c.strip('-')
    ta,tb,tc = map(topElement,[a,b,c])    
    A,B,C=a,b,c
    lista = []
    if ta!="":
        if  tb == "" or int(ta) < int(tb):
            B=ta+b
            A=a[1:]            
            lista.append(normalizeState(A,B,C))
            A,B,C=a,b,c
        if tc == "" or int(ta) < int(tc):
            C=ta+c
            A=a[1:]            
            lista.append(normalizeState(A,B,C))
            A,B,C=a,b,c
    if tb!="":
        if ta == "" or int(tb) < int(ta):
            A=tb+a
            B=b[1:]            
            lista.append(normalizeState(A,B,C))
            A,B,C=a,b,c
        if tc == "" or int(tb) < int(tc):
            C=tb+c
            B=b[1:]            
            lista.append(normalizeState(A,B,C))
            A,B,C=a,b,c
    if tc!="":
        if ta == "" or int(tc) < int(ta):
            A=tc+a
            C=c[1:]            
            lista.append(normalizeState(A,B,C))
            A,B,C=a,b,c
        if tb == "" or int(tc) < int(tb):
            B=tc+b
            C=c[1:]            
            lista.append(normalizeState(A,B,C))
            A,B,C=a,b,c
    return lista
    
 

states = {
	0:['AAAA','1234','----','----'],
	1:['BAAA','-234','---1','----'],
	2:['CAAA','-234','----','---1'],
	3:['ABAA','-134','---2','----'],
	4:['BBAA','--34','--12','----'],
	5:['CBAA','--34','---2','---1'],
	6:['ACAA','-134','----','---2'],
	7:['BCAA','--34','---1','---2'],
	8:['CCAA','--34','----','--12'],
	9:['AABA','-124','---3','----'],
	10:['BABA','--24','--13','----'],
	11:['CABA','--24','---3','---1'],
	12:['ABBA','--14','--23','----'],
	13:['BBBA','---4','-123','----'],
	14:['CBBA','---4','--23','---1'],
	15:['ACBA','--14','---3','---2'],
	16:['BCBA','---4','--13','---2'],
	17:['CCBA','---4','---3','--12'],
	18:['AACA','-124','----','---3'],
	19:['BACA','--24','---1','---3'],
	20:['CACA','--24','----','--13'],
	21:['ABCA','--14','---2','---3'],
	22:['BBCA','---4','--12','---3'],
	23:['CBCA','---4','---2','--13'],
	24:['ACCA','--14','----','--23'],
	25:['BCCA','---4','---1','--23'],
	26:['CCCA','---4','----','-123'],
	27:['AAAB','-123','---4','----'],
	28:['BAAB','--23','--14','----'],
	29:['CAAB','--23','---4','---1'],
	30:['ABAB','--13','--24','----'],
	31:['BBAB','---3','-124','----'],
	32:['CBAB','---3','--24','---1'],
	33:['ACAB','--13','---4','---2'],
	34:['BCAB','---3','--14','---2'],
	35:['CCAB','---3','---4','--12'],
	36:['AABB','--12','--34','----'],
	37:['BABB','---2','-134','----'],
	38:['CABB','---2','--34','---1'],
	39:['ABBB','---1','-234','----'],
	40:['BBBB','----','1234','----'],
	41:['CBBB','----','-234','---1'],
	42:['ACBB','---1','--34','---2'],
	43:['BCBB','----','-134','---2'],
	44:['CCBB','----','--34','--12'],
	45:['AACB','--12','---4','---3'],
	46:['BACB','---2','--14','---3'],
	47:['CACB','---2','---4','--13'],
	48:['ABCB','---1','--24','---3'],
	49:['BBCB','----','-124','---3'],
	50:['CBCB','----','--24','--13'],
	51:['ACCB','---1','---4','--23'],
	52:['BCCB','----','--14','--23'],
	53:['CCCB','----','---4','-123'],
	54:['AAAC','-123','----','---4'],
	55:['BAAC','--23','---1','---4'],
	56:['CAAC','--23','----','--14'],
	57:['ABAC','--13','---2','---4'],
	58:['BBAC','---3','--12','---4'],
	59:['CBAC','---3','---2','--14'],
	60:['ACAC','--13','----','--24'],
	61:['BCAC','---3','---1','--24'],
	62:['CCAC','---3','----','-124'],
	63:['AABC','--12','---3','---4'],
	64:['BABC','---2','--13','---4'],
	65:['CABC','---2','---3','--14'],
	66:['ABBC','---1','--23','---4'],
	67:['BBBC','----','-123','---4'],
	68:['CBBC','----','--23','--14'],
	69:['ACBC','---1','---3','--24'],
	70:['BCBC','----','--13','--24'],
	71:['CCBC','----','---3','-124'],
	72:['AACC','--12','----','--34'],
	73:['BACC','---2','---1','--34'],
	74:['CACC','---2','----','-134'],
	75:['ABCC','---1','---2','--34'],
	76:['BBCC','----','--12','--34'],
	77:['CBCC','----','---2','-134'],
	78:['ACCC','---1','----','-234'],
	79:['BCCC','----','---1','-234'],
	80:['CCCC','----','----','1234']
	}

symbols = {
	'AAAA':0,
	'BAAA':1,
	'CAAA':2,
	'ABAA':3,
	'BBAA':4,
	'CBAA':5,
	'ACAA':6,
	'BCAA':7,
	'CCAA':8,
	'AABA':9,
	'BABA':10,
	'CABA':11,
	'ABBA':12,
	'BBBA':13,
	'CBBA':14,
	'ACBA':15,
	'BCBA':16,
	'CCBA':17,
	'AACA':18,
	'BACA':19,
	'CACA':20,
	'ABCA':21,
	'BBCA':22,
	'CBCA':23,
	'ACCA':24,
	'BCCA':25,
	'CCCA':26,
	'AAAB':27,
	'BAAB':28,
	'CAAB':29,
	'ABAB':30,
	'BBAB':31,
	'CBAB':32,
	'ACAB':33,
	'BCAB':34,
	'CCAB':35,
	'AABB':36,
	'BABB':37,
	'CABB':38,
	'ABBB':39,
	'BBBB':40,
	'CBBB':41,
	'ACBB':42,
	'BCBB':43,
	'CCBB':44,
	'AACB':45,
	'BACB':46,
	'CACB':47,
	'ABCB':48,
	'BBCB':49,
	'CBCB':50,
	'ACCB':51,
	'BCCB':52,
	'CCCB':53,
	'AAAC':54,
	'BAAC':55,
	'CAAC':56,
	'ABAC':57,
	'BBAC':58,
	'CBAC':59,
	'ACAC':60,
	'BCAC':61,
	'CCAC':62,
	'AABC':63,
	'BABC':64,
	'CABC':65,
	'ABBC':66,
	'BBBC':67,
	'CBBC':68,
	'ACBC':69,
	'BCBC':70,
	'CCBC':71,
	'AACC':72,
	'BACC':73,
	'CACC':74,
	'ABCC':75,
	'BBCC':76,
	'CBCC':77,
	'ACCC':78,
	'BCCC':79,
	'CCCC':80
	}

ordered = sorted(zip(symbols.values(), symbols.keys()))
valid_states = []
for s in ordered:
    l=[]        
    moves = validMoves(s[1],s[0])
    for m in moves:
        l.append(symbols[m])
        #print("Estado: {}, Simbolo: {}".format(symbols[m], m))
    valid_states.append(l)

R = [[0,0,0]for c in range(0,81)]
Q = [[0,0,0]for c in range(0,81)]
R[0][2]=-1
R[40][2]=-1
valid_states[80].append(80)
R[80][2]=100
R[78][1]=100
R[79][1]=100
action = -1
epoch = 0

menu()
#for c in range(0,15):
#	train()
#for x in range(0,81):
#	print("Estado = {}, Mejor Accion: {}".format(x,bestAction(x)))
#calculatePath(0)
