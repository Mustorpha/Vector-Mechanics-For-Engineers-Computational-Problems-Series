'''
***********************************************************
Vector mechanics for engineers ----- Computer problems 2.C1
***********************************************************
The program takes the forces and their corresponding
direction in a tuple and the tuples of forces and their
direction in a list. i.e (F1,<01),(F2,<02),.. and return
the resultant force with its direction in the same manner.
***********************************************************
The direction are taking in order of their angle with the
positive x-axis to the point in anticlockwise direction
in degrees.
***********************************************************
'''

__version__ = "1.0"
__status__ = "Beta"
__date__ = "19-09-2022"
__author__ = "Jamiu Mustorpha"

import math

def component (*forces, decimal = 1):

    '''
    Returns the sum of the horizontal components of the 
    forces and the sum of the vertical components of forces. 
    The function takes the forces and their corresponding
    direction in a tuple and the tuples of forces and their
    direction in a list. i.e (F1,<01),(F2,<02),... and return
    the resultant force with its direction in the same manner.
    '''
    sum_of_Fx = 0.0         #intialize the variables as floating digits
    sum_of_Fy = 0.0
    f = 0.0
    direction = 0.0

    for data in forces:
        if type(data)!= tuple: #check if each value in the list is a tupule
            raise Exception ('Input error!, please input your data in the form (F1,<01),(F2,<02),...')
        else:
            f = float(data[0])
            direction = float(data[1])

            Fx = f*math.cos(math.radians(direction))    #the horizontal component of the force
            sum_of_Fx = sum_of_Fx + Fx                  #add the component to the total sum of horizontal forces
            Fy = f*math.sin(math.radians(direction))    #the vertical component of the force
            sum_of_Fy = sum_of_Fy + Fy                  #add the component to the total sum of vertical forces

    return round(sum_of_Fx, decimal), round(sum_of_Fy, decimal)

def resultant(*components, decimal = 1):

    ''' 
    Returns the resultant and direction of two
    component forces. The function takes the two
    component forces in a tuple i.e (Fx,Fy)
    '''

    Fx = 0.0                #intialize the variables as floating digits
    Fy = 0.0
    R = 0.0
    direction = 0.0
    
    Fx, Fy = components

    R = math.sqrt((Fx**2) + (Fy**2))        #compute the resultant

    direction = math.degrees(math.atan(Fy/Fx))           #computer the direction

    return round(R, decimal), round(direction, decimal)    
