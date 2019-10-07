import numpy as np  
import matplotlib.pyplot as plt  

def graph(formula, x_range):  
	
	plt.style.use('seaborn')

	x = np.array(x_range)  
	y = formula(x)  
	plt.plot(x, y)
	plt.title('Your Graph!')  
	plt.show()  

def my_formula(x):
	return 2**x

graph(my_formula, range(0, 10, .001))
