x = [0, 1, 4, 9]
for a in x:
	for b in x:
		for c in x:
			print((a**2+b**2+10*c**2)%16)

