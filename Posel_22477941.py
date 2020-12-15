#import libraries
import numpy as np
import math as m
import matplotlib.pyplot as plt

#define first function
def microcar(list1, list2):
    exp_H_list = []
    exp_V_list = []
    exp_D_list = []
    act_H_list = []
    act_V_list = []
    act_D_list = []
    for x in range(len(list1)): #remove 'NA' from files
        with open(list1[x], 'r') as file1:
            with open(list2[x], 'r') as file2:
                file1 = file1.readlines()
                file2 = file2.readlines()
                for lines in range(len(file1)):
                    if 'NA' in file1[lines] or 'NA' in file2[lines]:
                        file1[lines] = ''
                        file2[lines] = ''
                      
            
        array = np.loadtxt(file1,delimiter=',',dtype = [("direction", float), ("time", float), ("speed", float)]) #create expected array
        ExpHor = 0
        ExpV = 0
        ExpD = 0
        for i in array:
            ExpHor = ExpHor + (([i][0][1] * [i][0][2]) * m.cos(m.radians(([i][0][0])))) #calculate expected displacements and distances 
            ExpV = ExpV + (([i][0][1] * [i][0][2]) * m.sin(m.radians([i][0][0])))
            ExpD = ExpD + [i][0][1] * [i][0][2]
        exp_D_list.append(round(ExpD,2))
        exp_H_list.append(round(ExpHor,2))              
        exp_V_list.append(round(ExpV,2))
            

           
            
        array = np.loadtxt(file2,delimiter=',',dtype = [("direction", float), ("time", float), ("speed", float)]) #create second array
        ActHor = 0
        ActV = 0
        ActD = 0
        for i in array:
            ActHor = ActHor + (([i][0][1] * [i][0][2]) * m.cos(m.radians(([i][0][0])))) #calculate actual displacement and distances 
            ActV = ActV + (([i][0][1] * [i][0][2]) * m.sin(m.radians([i][0][0])))
            ActD = ActD + [i][0][1] * [i][0][2]
        act_D_list.append(round(ActD,2))
        act_H_list.append(round(ActHor,2))              
        act_V_list.append(round(ActV,2))
    actDistance = np.array(act_D_list)       #create expected 6 arrays
    actHorizontal = np.array(act_H_list)  
    actVert = np.array(act_V_list)
    expDistance = np.array(exp_D_list)    
    expHorizontal = np.array(exp_H_list)  
    expVert = np.array(exp_V_list)


           
            
    return expHorizontal, expVert, actHorizontal, actVert, expDistance, actDistance 
        
def plotmicrocar(list1, list2): #define second function
    eh, ev, ah, av, ed, ad = microcar(list1, list2) #call first function
    
    if eh.min()<ah.min(): #create variables for scatter plot scaling
        horizontal_min = eh.min()
    else:
        horizontal_min = ah.min()
    if eh.max()>ah.max():
        horizontal_max = eh.max()
    else:
        horizontal.max = ah.max()
        
    if ev.min()<av.min():
        vert_min = ev.min()
    else:
        vert_min = av.min()
    if ev.max()>av.max():
        vert_max = ev.max()
    else:
        vert_max = av.max()
    
    plt.subplot(2,2,(1,2)) #create bar chart
    xAxis = np.arange(len(ed))
    plt.xticks(np.linspace(0,len(ed),len(ed)+1))
    plt.bar(xAxis-0.2,ed,width = 0.4, label = "Expected")
    plt.bar(xAxis+0.2,ad,width = 0.4, label = "Actual")
    plt.xlabel("Micrcar number")
    plt.ylabel("Distance(m)")
    plt.title('Expected vs Actual Distance Covered')
    plt.legend()

    
    plt.subplot(2,2,3) #create first scatter plot
    plt.xlim(horizontal_min-50,horizontal_max+50)
    plt.ylim(vert_min-50,vert_max+50)
    for i in range(len(ev)):
        plt.scatter(eh[i], ev[i],label = f'microcar {i}')
    plt.xlabel('horizontal displacement(m)')
    plt.ylabel('vertical displacement(m)')
    plt.title("Expected displacement by microcars")
    plt.legend()
    
    plt.subplot(2,2,4) #create second scatter plot
    plt.xlim(horizontal_min-50,horizontal_max+50)
    plt.ylim(vert_min-50,vert_max+50)
    for i in range(len(av)):
        plt.scatter(ah[i], av[i],label = f'microcar {i}')
    plt.xlabel('horizontal displacement(m)')
    plt.ylabel('vertical displacement(m)')
    plt.title("Actual displacements by microcars")
    plt.legend()
    plt.tight_layout()
    plt.show()
    

    
    
 
    


        
        
    
    
