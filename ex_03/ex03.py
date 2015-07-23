while True:


	def add_two_integers():
		try:
			print int(x) + int(y)
			print "Add successful!"
		except ValueError as e:
			print e
			print "You did not pass two integers, you passed: %r and %r" % (x,y)
			exit(2)

		

		
	print "Enter 2 integers"	
	characters = raw_input()
	if "exit" in characters:
		exit(0)
	x = characters[0:1]
	y = characters[1:2]
	add_two_integers()