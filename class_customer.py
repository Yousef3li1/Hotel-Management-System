# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:27:19 2021

@author: LEGION
"""
import pickle
from class_reservation import reservation
class customer :
    id = 0
    name = ''
    ssn = ''
    ress = []
    counter = 0
    cus = []
    #===============================================================================================
    def __init__(self,id=0 , name='', ssn=0 , password='',ress = [] ):
      customer.counter+=1
      self.id=customer.counter
      self.name =name
      self.ssn =ssn
    #==============================================================================================
    def __str__ (self):
        return "id : " + str (self.id) + "\nname :" + self.name +"\nssn = " + self.ssn + "\nress" + str (self.ress)
    #==============================================================================================
    def add_res (self , ress):
        self.ress.append(reservation)
    #==============================================================================================
    def save  (cus):
        try :
            file = open ("customer" , "wb+")
            pickle .dump (cus , file )
            print ("saved")
            file.clase()
        except
            print ("saved")
    def load ():
        try :
            file = open ("customer' , "rb")
            cus = pickle.load(file)
            file.close()
            return cus
        except :
            print ("load fail")
            return ()