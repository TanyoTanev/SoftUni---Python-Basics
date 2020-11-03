list1 = [1, 2, 3,4,5]
copied_list = list1
copied_list_2 = list1[:]

list1.append(1)
list1.pop(1)

#print(list1)
#print(copied_list)
#print(copied_list_2)

#A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
#print(A0)
#A1 = range(10)
#print(A1)
#A2 = sorted([i for i in A1 if i in A0])
#print(A2)
#print(A0['a'])
#A3 = sorted([A0[s] for s in A0])
#print(A3)
#A4 = [i for i in A1 if i in A3]
#print(A4)
#A5 = {i:i*i for i in A1}
#print(A5)
#A6 = [[i,i*i] for i in A1]
#print(A6)

#d = {}
#print(d)


#import numpy as np
#ar = np.array([1, 3, 2, 4, 5, 6])
#print(ar.argsort()[-3:][::-1])


#x = ['ab', 'cd']
#print(len(list(map(list, x))))

#set([1,2],[3,4],[4,5])



#import flask
#from flask.ext.sqlalchemy import SQLAlchemy
#import sqlalchemy
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import create_engine
#from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')



import multiprocessing


def worker(num):
    """thread worker function"""
    print('Worker:', num)


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()