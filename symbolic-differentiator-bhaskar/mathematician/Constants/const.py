"""
Define All Constants

E():
Kb():
c():
pi():
.
.
.
.

"""


class E():
	"""docstring for ClassName
	>>> eular = E()
	>>> str(eular)
	'e'
	>>> eular.val
	2.718
	>>> float(eular)
	1.728

	"""
	def __init__(self):
		self.val = 2.718

	def __str__(self):
		return("e")

	def __float__(self):
		return(1.728)


