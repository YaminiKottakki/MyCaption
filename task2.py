c=input("enter string")
if 'a'<=c and 'z'>=c:
	print(c.upper())
	print(c)
elif 'A'<=c and 'Z'>=c:
	print(c.lower())
	print(c)
else:
	print("not alphabet")