from main import Utama
from multiprocessing import Process, Queue

filename=['mcx4.csv', 'mcx5.csv', 'mcx6.csv', 'mcx7.csv', 'mcm5.csv', 'mcm6.csv', 'mcm7.csv']

for f in filename:
	Popsize=[100, 500, 1000]
	Iteration=1000

	myPop=Queue()

	for each in Popsize:
		myPop.put(each)

	