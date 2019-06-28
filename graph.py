from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib import style


def plotGraph():
    #graph style
    style.use('ggplot')

    #create plot
    fig=plt.figure()

    #type of projection
    ax1=fig.add_subplot(111,projection='3d')

    #list of r,phi,z values (5 points each)
    r=np.random.randint(0,100,size=5)
    phi=np.random.uniform(0,2*np.pi,size=5)
    z=[]

    #generate z values using r and phi values using given formula
    for i in range(0,5):
        #change function if you wish to.
        z.append(r[i]+math.sin(phi[i]))
    

    #verify z values
    print(z)

    ax1.plot_trisurf(r,phi,np.array(z),linewidth=2,antialiased=False)

    #deploy values to graph and show
    ax1.set_xlabel('radius')
    ax1.set_ylabel('phi')
    ax1.set_zlabel('z')

    plt.show()



plotGraph()    
    

   
