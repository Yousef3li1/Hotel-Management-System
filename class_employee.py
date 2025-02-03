# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:09:24 2021

@author: LEGION
"""
import pickle

class employee:
    id = 0
    name = ''
    ssn = ''
    password = '' 
    counter = 0
    emp = []
    #=================================================================================================
    def __init__(self,id=0 , name='', ssn=0 , password='' ):
      employee.counter+=1
      self.id=employee.counter
      self.name =name
      self.ssn =ssn
      self.password =password
    #=================================================================================================
    def signin (self):
        id1=0
        id1 =input ('enter id :')
        password1 =input ('enter password :')
       # if(id1 == self.id) and (password1 == self.password):
        return 1
       # else :
        #    return (0)
    #===================================================================================================        
        
    def __str__(self):
     return "id : " + str (self.id) + "\nname :" + self.name +"\nssn = " + self.ssn + "\nress" + str (self.ress)
    #=========================================================================================================
    def save  (emp):
        try :
            file = open ("employee" , "wb+")
            pickle .dump (emp , file )
            print ("saved")
            file.clase()
        except
            print ("saved")
    def load ():
        try :
            file = open ("employee' , "rb")
            emp = pickle.load(file)
            file.close()
            return emp
        except :
            print ("load fail")
            return ()





