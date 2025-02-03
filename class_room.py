# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:27:22 2021

@author: LEGION
"""
import pickle
class room :
    type = ''
    number = 0
    ress = []
    reserved = False
    counter = 0
    rooms = []
    #===============================================================================================
    def __init__(self,type = '' , reserved = False  ):
         room.counter+=1
         self.number=room.counter
         self.type =type
         self.reserved =reserved 
         
    #================================================================================================
    def isreserved (self):
        return str(self.reserved)
    #=================================================================================================

    def __str__(self):
        return "number : " + str(self.number) + "\ttype :" + self.type + "\treserved = " + str(self.reserved)

    def reserved (self):
        
        if(self.reserved == False):
            return( "the room has been booked , enjoy your time")
        else:
            return("the room is booked  , you can book other room" )
        
    #==================================================================================================
    def free(self): 
        if (self.reserved == True):
           self.reserved = False
    #===================================================================================================
    def add_res (self , ress):
        self.ress.append(reservation)
    #=====================================================================================================


    def save(rooms):
        try:
            file = open("rooms", "wb+")
            pickle.dump(rooms, file)
            print("saved")
            file.clase()
        except:
            print("saved")


    def load():
        try:
            file = open("rooms" , "rb")
            rooms = pickle.load(file)
            file.close()
            return rooms
        except:
            print("load fail")
            return []