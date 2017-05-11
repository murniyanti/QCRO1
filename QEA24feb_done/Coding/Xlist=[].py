Xlist=[]

for n in range(len(P)):

	bintodec=[]

	for c in range(len(P[n])):

		a="".join(str(y) for y in P[n][c])
		b=int(a,2)
		bintodec.append(copy.deepcopy(b))

	for k in range(len(bintodec)):

		if bintodec[k]>=len(csv):
			bintodec[k]= None

	for k in range(len(bintodec)):

		indexi=[y for y, x in enumerate(bintodec) if x==k]

		if len(indexi)>1:
			for h in range(1, len(indexi)):
				i=0
				while i<len(bintodec):

					if i not in bintodec:
						bintodec[indexi[h]]=None
						break
					i=i+1
					
	possiblefragment=[]
	
	while i<len(bintodec):
		if i is not in bintodec:
			possiblefragment.append(copy.deepcopy(i))

	for k in range(len(bintodec)):
		if bintodec[k]==None:
			bintodec[k]=copy.deepcopy(random.choice(possiblefragment))
			possiblefragment.remove(bintodec[k])