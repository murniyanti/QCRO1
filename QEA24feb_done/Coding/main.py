from qoperator import *
from sys import argv
import numpy as np
import math
import timeit

def Utama(myRun, myResult, filename):
	Run=myRun.get()
	start = timeit.default_timer()
	#script, filename = argv

	open(filename)

	data = np.genfromtxt(filename, delimiter=",")

	'''

	suggested parameter theta:

	1. 0.0015
	2. 0.0025
	3. 0.01
	4. 0.02

	'''

	'''QEA parameter'''
	globalmigrationCounter = 100
	gmIncrement = 100

	localmigrationCounter = 20
	lmIncrement = 20

	m = len(np.binary_repr(len(data)))

	#theta, popsize, iteration, migration(local,global)

	theta = 0.015

	'''Standard Parameter'''
	t = 0
	Iteration  = 1000
	populationSize = 1000
	BvsI = []	# to produce convergence graph

	fw = open('{0}-QiEA-P={1}-I={2}-T={3}-Run={4}.txt'.format(filename, populationSize, Iteration, theta, Run), 'w+')

	Qlist = Initialize(len(data), m, populationSize)

	X = make(Qlist, data)

	evaluate(X, data)

	B = copy.deepcopy(X)

	B = StoreTheb(B)
	b=B[0]
	print>>fw, "{0}\t{1}\t{2}".format(t, b.Fit, B[-1].Fit)
	print t, b.Fit

	while t < Iteration:
		n = len(Qlist)
		t = t + 1

		X = make(Qlist, data)

		evaluate(X, data)

		update(Qlist, X, b, m, theta)
		
		StoreXtoB(X, B)

		B = StoreTheb(B)
		b = copy.deepcopy(B[0])
		
		''' Local/Global Migration '''
		
		if t==localmigrationCounter:

			Localmigration(B)
			localmigrationCounter = localmigrationCounter + lmIncrement
		'''
		if t==globalmigrationCounter:

			Globalmigration(B, b)
		'''
		
		BvsI.append(copy.deepcopy(b))

		#i, best, worst
		print>>fw, "{0}\t{1}\t{2}".format(t, b.Fit, B[-1].Fit)
		print t, "|b=", b.Fit, "|w", B[-1].Fit

	

	stop = timeit.default_timer()

	taken = stop - start	
	fr=open('{0}-Record-P={1}-I={2}-t={3}-Run={4}.txt'.format(filename, populationSize,Iteration,theta, Run), 'w+')

	B = StoreTheb(BvsI)
	b = copy.deepcopy(B[0])
		
	print>>fr, "Best structure= {0}".format(b.x)
	print>>fr, "Best Fit= {0}".format(b.Fit)
	print>>fr, "Time taken= ", taken, "Seconds"

	fw.close()
	fr.close()

	myResult.put(b.Fit)









