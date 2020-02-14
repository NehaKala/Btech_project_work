# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:35:52 2020

@author: Neha sanjay Kala
"""

from copy import deepcopy

def minor(array,i,j):
    c = array
    c = c[:i] + c[i+1:]
    for k in range(0,len(c)):
        c[k] = c[k][:j]+c[k][j+1:]
    return c

def det(array,n):
    if n == 1 :return array[0][0]
    if n == 2 :return array[0][0]*array[1][1] - array[0][1]*array[1][0]
    sum = 0
    for i in range(0,n):
        m = minor(array,0,i)
        sum =sum + ((-1)**i)*array[0][i] * det(m,n-1)
    return sum



y = [[4,2,3,8],[1,4,5,6],[5,3,4,5],[4,9,1,4]]
n=4

r = deepcopy(y)

for i in range(4):
    for j in range(4):
        m=minor(y,i,j)
        d=det(m,3)
        r[i][j]=d
print('minor_matrix=',r)



cof=deepcopy(r)
for i in range(4):
    for j in range(4):
        c=((-1)**(i+j))*r[i][j]
        cof[i][j]=c
print("cof=",cof)

adj=deepcopy(cof)
for i in range(4):
    for j in range(4):
        a=cof[j][i]
        adj[i][j]=a
print('adj_matrix=',adj)   


determinant=det(y,4)
print('Determinant=',determinant)

inv=deepcopy(adj)
for i in range(4):
    for j in range(4):
        s=(1/float(determinant))*adj[i][j]
        inv[i][j]=s
print('inv=',inv) 

    

