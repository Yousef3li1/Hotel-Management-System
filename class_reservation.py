# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 18:13:43 2021

@author: LEGION
"""
import pickle
from class_customer import customar
from class_employee import employee
from class_room import room
class reservation :
     id = 0 
     data_created = ''
     duration = ''
     room = []
     customar = []
     employee = []
     counter = 0
     rese = []
  #===============================================================================================
     def __init__(self,id = '' , data_created = '' , duration = ''):
         room.reservation+=1
         self.id=reservation.counter
         self.data_created =data_created
         self.duration =duration
   #=================================================================================================
     def add_cus (self , customar):
        self.customer.append(reservation)
   #==============================================================================================
     def add_emp (self , employee):
        self.employee.append(reservation)
   #=================================================================================================

     def add_room (self , room):
        self.room.append(reservation)
   #=================================================================================================
     def __str__ (self):
        return "id : " + str (self.id) + "\data_created :" + self.data_created +"\duration = " + self.duration
     #===================================================================================================

     def save(rese):
         try:
             file = open("reservaition", "wb+")
             pickle.dump(rese, file)
             print("saved")
             file.clase()
         except
             print("saved")

     def load():
         try:
             file = open("reservation' , "rb")
             rese = pickle.load(file)
             file.close()
             return rese
         except:
             print("load fail")
             return ()