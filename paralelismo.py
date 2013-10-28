import multiprocessing
from datetime import datetime
import time
from multiprocessing import Pool

"""
def worker(x):
	time.sleep(10)
	print datetime.now()

	return x*x, 2*x

if __name__=='__main__':
	jobs=[]
	for i in range(10):
		p= multiprocessing.Process(target=worker,args=(i,))
		jobs.append(p)
		p.start()

		raise NameError("altos")
		"""

def f(x, Auxiliar = 4):
    return x*x+Auxiliar, x*Auxiliar

if __name__ == '__main__':
	pool = Pool(processes=4)
	# start 4 worker processes
	result = pool.apply_async(f, [10])    
	# evaluate "f(10)" asynchronously
	print result.get(timeout=1)           
	# prints "100" unless your computer is *very* slow
	print pool.map_async(f, range(10) ).get()          
	resultados = pool.map(f, [6,3,8,2])
	# prints "[0, 1, 4,..., 81]"

