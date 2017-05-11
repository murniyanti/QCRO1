from main import Utama
import numpy as np 
import copy
from multiprocessing import Process, Queue

filename=['mcx4.csv', 'mcx5.csv', 'mcx6.csv', 'mcx7.csv', 'mcm5.csv', 'mcm6.csv', 'mcm7.csv']

for f in filename:
	allResult=[]
	Run=10
	myRun=Queue()
	myResult=Queue()

	for each in range(Run):
		myRun.put(each)

	RunWorkers=[Process(target=Utama, args=(myRun, myResult,f)) for i in range(Run)]

	for each in RunWorkers:
		each.start()

	while Run:
		result=myResult.get()
		allResult.append(copy.deepcopy(result))
		Run-=1

	fwrite=open('Data-{0}-statistics.txt'.format(f), 'w+')

	MEAN=np.mean(allResult)
	STDEV=np.std(allResult)
	VAR=np.var(allResult)

	sortResult=sorted(allResult, reverse=True)

	for j in range(len(allResult)):
		print>>fwrite, "Run {0}={1}".format(j, allResult[j])

	print>>fwrite, "Best Result= {0}".format(sortResult[0])
	print>>fwrite, "Mean={0}".format(MEAN)
	print>>fwrite, "Standard Deviation={0}".format(STDEV)
	print>>fwrite, "Variance={0}".format(VAR)

	fwrite.close()