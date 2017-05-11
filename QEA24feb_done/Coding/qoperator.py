import random, numpy as np, math
import copy
from ClassQea import *
from operator import attrgetter

def Initialize(fragment, lenBin, PopulationSize):
	#print "Initialize"
	ListQubitSolution = []

	for p in range(PopulationSize):

		SolutionQ = []

		for f in range(fragment):

			a = []
			b = []


			for m in range(lenBin):
				'''
				if m ==0:
					a.append(1/math.sqrt(math.pow(2,1)))
					b.append(math.sqrt(1-math.pow(a[m],2)))
				
				elif m ==1:
					a.append(1/math.sqrt(math.pow(2,1)))
					b.append(-math.sqrt(1-math.pow(a[m],2)))

				else:
				'''
				a.append(1/math.sqrt(math.pow(2, m)))
				b.append(math.sqrt(1-math.pow(a[m],2)))

			d = [a, b]
			SolutionQ.append(copy.deepcopy(d))

		OneQubit = qubit(SolutionQ)
		ListQubitSolution.append(copy.deepcopy(OneQubit))

	return ListQubitSolution

def make(ListQubitSolution, csv):
	'''Observe Q(t-1) to produce P(t)'''
	#print "Make"
	P = []	# List of Binary population

	for n in range(len(ListQubitSolution)):
		Xsolution = []

		for c in range(len(ListQubitSolution[n].qbit)):
			bitP = []

			for m in range(len(ListQubitSolution[n].qbit[c][1])):

				if random.random() < math.pow(ListQubitSolution[n].qbit[c][1][m], 2):
					bitP.append(0)

				else:
					bitP.append(1)

			Xsolution.append(copy.deepcopy(bitP))
		
		P.append(copy.deepcopy(Xsolution))


	'''Now produce X list. X list is Fragment arrangement'''


	Xlist = []
	'''
	for n in range(len(P)):
		bintodec = []

		for c in range(len(P[n])):

			a = "".join(str(y) for y in P[n][c])
			b = int(a, 2)
			bintodec.append(copy.deepcopy(b))

		for k in range(len(bintodec)):

			if bintodec[k] >= len(csv):
				bintodec[k] = random.randrange(0, len(csv))

		for k in range(len(bintodec)):

			indexi = [y for y, x in enumerate(bintodec) if x==k]

			if len(indexi)>1:

				for h in range(1, len(indexi)):
					i = 0

					while i<len(bintodec):

						if i not in bintodec:
							bintodec[indexi[h]] = i
							break
						i = i + 1

		x = X(bintodec, 0)
	'''

	for n in range(len(P)):

		bintodec=[]

		for c in range(len(P[n])):

			a="".join(str(y) for y in P[n][c])
			b=int(a,2)
			bintodec.append(copy.deepcopy(b))

		#print bintodec

		for k in range(len(bintodec)):

			if bintodec[k]>=len(csv):
				bintodec[k]= None

		for k in range(len(bintodec)):

			indexi=[y for y, x in enumerate(bintodec) if x==k]

			if len(indexi)>1:
				for h in range(1, len(indexi)):
					bintodec[indexi[h]]=None
						
		possiblefragment=[]
		
		i=0
		
		while i<len(bintodec):
			if i not in bintodec:
				possiblefragment.append(copy.deepcopy(i))
			i=i+1

		for k in range(len(bintodec)):
			if bintodec[k]==None:
				bintodec[k]=copy.deepcopy(random.choice(possiblefragment))
				#print bintodec[k]
				possiblefragment.remove(bintodec[k])
		
		#print bintodec

		x=X(bintodec, 0)
				
		Xlist.append(copy.deepcopy(x))

	return Xlist

def evaluate(Xlist, c):
	#print "evaluate"
	for i in range(len(Xlist)):

		score_add = 0
		
		for k in range(len(Xlist[i].x) - 1):

			a = c[ Xlist[i].x[k]   ] [ Xlist[i].x[k+1] ]

			b = c[ Xlist[i].x[k+1] ] [ Xlist[i].x[k]   ]
		
			if a >= b :
				score_add = score_add + a

			else :
				score_add = score_add + b

		score_add = score_add + Xlist[i].x[0]	

		Xlist[i].Fit = score_add


def StoreXtoB(Xlist, Blist):
	'''Use this in while loop/iteration only'''
	#print "StoreXtoB"
	for i in range(len(Xlist)):

		if Xlist[i].Fit > Blist[i].Fit:
			Blist[i] = copy.deepcopy(Xlist[i])


def StoreTheb(Blist):
	'''Store best solution b among B(t)'''
	#print "StoreTheb"
	B = sorted(Blist, key=attrgetter('Fit'), reverse=True)

	return B

def Localmigration(Blist):
	#print "Localmigration"
	'''
	Use migration period. 
	
	Example: 
	1- Global migration happen after 100 generation 
	2- Local migration happen after 10 generation

	In local migration, may apply mutation to migrate 
	the solution in current generation (exchange neighbor)

	'''

	mutationRate = 0.8

	ind1 = Blist

	newsol = ind1

	for i in range(len(ind1) - 1):

		if random.random() < mutationRate:

			v = newsol[i]
			newsol[i] = newsol[i+1]
			newsol[i+1] = v

	Blist = newsol


def Globalmigration(Blist, b):
	#print "Globalmigration"
	for i in range(len(Blist)):

		Blist[i] = copy.deepcopy(b)


def mutation(varpass2 ):
	
	mutationRate = 1.0
	ind1 = varpass2
	
	#newsol = np.zeros( len(ind1) )
	newsol = ind1
	
	for i in range( len(ind1)-1 ):
		if random.random() < mutationRate :
			v = newsol[i]
			newsol[i] = newsol[i+1]
			newsol[i+1] = v
	
	return newsol

def update(ListQubitSolution, X, b, m, theta):
	#print "update"
	for n in range(len(ListQubitSolution)):

		for c in range(len(ListQubitSolution[n].qbit)):

			xs = np.binary_repr(X[n].x[c], m)

			bs = np.binary_repr(b.x[c], m)

			new_a = []
			new_b = []

			for k in range(len(ListQubitSolution[n].qbit[c][0])):

				cxs = int(xs[k])
				cbs = int(bs[k])

				if cxs==0 and cbs==1 and X[n].Fit <= b.Fit:
					angle = -theta*math.pi 

				elif cxs==1 and cbs==0 and X[n].Fit <= b.Fit:
					angle = theta*math.pi 

				else:
					angle = random.uniform(0, 0.005)*math.pi

				Rotate_Gate = [ [np.cos(angle), -1*np.sin(angle)], [-1*np.sin(angle), np.cos(angle)]]

				new_ab = np.dot(Rotate_Gate, ([ListQubitSolution[n].qbit[c][0][k]], [ListQubitSolution[n].qbit[c][1][k]]))

				new_a.append(copy.deepcopy(new_ab[0][0]))
				new_b.append(copy.deepcopy(new_ab[1][0]))

			ListQubitSolution[n].qbit[c][0] = new_a
			ListQubitSolution[n].qbit[c][1] = new_b
	pass

def updateMultiprocess(task, passX, b, m, theta):
	
	ListQubitSolution = task.get()
	X = passX.get()

	for c in range(len(ListQubitSolution.qbit)):

		xs = np.binary_repr(X.x[c], m)

		bs = np.binary_repr(b.x[c], m)

		new_a = []
		new_b = []

		for k in range(len(ListQubitSolution.qbit[c][0])):

			cxs = int(xs[k])
			cbs = int(bs[k])

			if cxs==0 and cbs==1 and X.Fit <= b.Fit:
				angle = -theta

			elif cxs==1 and cbs==0 and X.Fit <= b.Fit:
				angle = theta

			else:
				angle = 0

			Rotate_Gate = [ [np.cos(angle), -1*np.sin(angle)], [-1*np.sin(angle), np.cos(angle)]]

			new_ab = np.dot(Rotate_Gate, ([ListQubitSolution.qbit[c][0][k]], [ListQubitSolution.qbit[c][1][k]]))

			new_a.append(copy.deepcopy(new_ab[0][0]))
			new_b.append(copy.deepcopy(new_ab[1][0]))

		ListQubitSolution.qbit[c][0] = new_a
		ListQubitSolution.qbit[c][1] = new_b
	pass



