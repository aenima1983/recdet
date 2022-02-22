#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 17:26:48 2022

Determinant calculator! Completed on Feb 10 2022 after days of grueling
homework dealt with.

@author: aidan, cosmicchasm1983
"""

import timeit 
import copy

# Matrix class -- a 'list of lists', each list within the main list represents
# a row, each element of these lists represents column entries


class matrixbuild:
    
    #initializing list of lists
    
    def __init__(self):
        self.body = []
    
    # implementing a way to add new rows
    
    def addrow(self, l):
        self.body.append(l)
        
    # circumventing using the submatrix method when only one row is desired
    
    def nrow(self, n):
        return self.body[n]
    
    # rough submatrix identifier -- returns a new instance of the matrixbuild
    # class, which is preferred as our main determinant function will be 
    # recursive!!
    
    def submatrix(self, rs, rf, cs, cf):
        try:
            new = matrixbuild()
            b = self.body[rs:rf+1]
            for i in b:
                new.addrow(i[cs:cf+1])
            return(new)
        except:
            print(f"Unexpected error. Your list is: {str(self.body)}")
            
    # def selectelements(self, r, c):
    #     return self.body[r][c]
    
    # quite literally removes a selected column from an object (generally a
    # submatrix)
    
    def mslice(self, c):
        a = copy.deepcopy(self.body)
        new = matrixbuild()
        for i in a:
            del i[c]
            new.addrow(i)
        return new
            
    def nottwobytwo(self):
        if (len(self.body) == 2) and (len(self.body[0]) == 2):
            return False
        else:
            return True
        
    def size(self):
        return len(self.body)
    
    def __str__(self):
        return str(self.body)
            
    
def twobytwo(matobj):
    if (len(matobj) != 2) or (len(matobj[0]) != 2):
        return None
    else:
        res = ((matobj[0][0]*matobj[1][1]) - (matobj[0][1]*matobj[1][0]))
        print(f"matobj in twobytwo() is: {matobj}")
        print("Result of 2x2 determinant is: %d" % res)
        return res
        
    
def det(matobj):
    if matobj.nottwobytwo():
        a,coeff,n = 0,matobj.nrow(0),matobj.size()
        # commence breaking up matrix into smaller parts
        sub = matobj.submatrix(1,n-1,0,n)
        print(f"matobj is: {matobj.body}")
        print(f"sub is: {sub.body}")
        for i in range(sub.size()+1):
            print("pass #%d" % i)
            a += ((-1)**i)*coeff[i]*det(sub.mslice(i))
            print("a is: %d" % a)
        return a
        return None
    else:
        return twobytwo(matobj.body)
    
    
def main():
    b = matrixbuild()

    n = int(input("What is the size of your matrix? Enter an integer: "))
    
    for i in range(n):
        a = []
        for j in range(n):
            c = float(input("Enter element of row %d column %d: " % (i+1,j+1)))
            a.append(c)
        b.addrow(a)
    print(det(b))

# ___________________________________________

main()

# timing code
print(timeit.timeit(setup = "pass", stmt = """main()""", number = 1))