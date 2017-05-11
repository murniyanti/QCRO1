def stat(var):
	b=np.max(var)
	w=np.min(var)
	x=np.mean(var)
	m=np.median(var)
	s=np.std(var)

	print "Best= ", b
	print "Worst= ", w
	print "Mean= ", x
	print "Median= ", m
	print "Std= ", s