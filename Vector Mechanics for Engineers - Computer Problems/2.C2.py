'''
***********************************************************
Vector mechanics for engineers ----- Computer problems 2.C2
***********************************************************
This program computes the force and the opposite angles of 
all forces in a system of three force in equilibrum using 
the lami's theorem provided that at least a force and the 
opposite angle (in degrees) to the force is given.
***********************************************************
'''

__version__ = "1.0"
__status__ = "Beta"
__date__ = "01-10-2022"
__author__ = "Jamiu Mustorpha"

import math


def lami (*values):
    '''
    The function takes in avaliable forces and their opposite 
    angle in tuple i.e in the form (F1,<01),(F2,<02),(F1,<03) and
    fill out the missing values in the sytem. Unknown value 
    in force and direction in the sytem of forces should be 
    replaced with desirable variable name in string format 
    i.e ('force_1', 34), (750, 'angle_2'),.... the program will 
    replace the value correctly after calculation, provided
    that at least a force and the opposite angle in degrees 
    to the force is given. 
    '''


    lami_constant = 0.0            #initalizes the ratio of a force and it's opposing angle as floating digit
    count = 0

    #check if the system contains more than three forces in equilibrum
    if len(values) != 3: 
        raise Exception ("Lami's theorem only works with a system of three forces in equilibrum")

    #chech if at least one force exist with it's opposite angle in the given system
    for data in values:     
        if type(data[0]) == int and type(data[1]) == int:
            count += 1
    
    #raise exception if there is no force with it's opposite angle in the given system
    if count == 0:    
        raise Exception("Incomplete data!... at least a tuple of a force and it's opposite angle should be given")
    else:
        values = values
        for data in values:
            if type(data[0]) == int and type(data[1]) == int:
                lami_constant = int(data[0])/math.sin(math.radians(data[1]))    #compute the lami's constant which is the ratio of a force to the sine of it's opposite angle

        #compute the unknown values in the given system
        for data in values:
            if type(data[0]) == str or type(data[1]) == str:
                if type(data[0]) == str and type(data[1]) == int:
                    data[0] = math.sin(math.radians(data[1]))*lami_constant
                if type(data[0]) == int and type(data[1]) == str:
                    data[1] = math.degrees(math.asin(data[0]/lami_constant))
            else:
                continue