def adding(a,b):
	c = a+b
	return c

def substract(a,b):
	c = a-b
	return c

def multiple(a,b):
	c = a*b
	return c

def divide(a,b):
	try:
		c = a/b
		return c
	except:
		ZeroDivisionError
		print('Dzielenie przez zero nie możliwe')
		return ''







print(adding(6,3))
print(substract(6,3))
print(multiple(6,3))
print(divide(6,3))
print(divide(6,0))