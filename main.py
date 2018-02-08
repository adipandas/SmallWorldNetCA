'''
Created on Feb 3, 2018

@author: aditya
'''

from SmallWorldCA import CA_SmallWorld as CAS
import matplotlib.pyplot as plt

if __name__=='__main__':
    RULE = 129
    subplot_h, subplot_v = 3, 2
    
    p = [1, 0.999, 0.99, 0.9, 0.5, 0]
    q = [0.5, 0.1] 
    for j in range(len(q)): # col    
        fig = plt.figure()
        fig.suptitle("RULE {}".format(RULE), fontsize="x-large")
        for i in range(len(p)):     # row
            CA = CAS(RULE, p[i], q[j], world_size=400, lifespan=400)
            image1 = CA.simulation()
            plt.subplot(subplot_h, subplot_v, i+1)
            plt.imshow(image1)
            plt.xticks([]), plt.yticks([])
            plt.title('p = {0}, q = {1}'.format(p[i], q[j]) )
        plt.tight_layout()
        plt.show()
    
    f = [0 , 0.001, 0.01, 0.1, 0.5, 1]
    fig = plt.figure()
    fig.suptitle("SMALL WORLD NETWORK - RULE {}".format(RULE), fontsize="x-large")
    for j in range(len(f)):
        CA = CAS(RULE, world_size=400, lifespan=400)
        image2 = CA.smallworld(f[j])
        plt.subplot(subplot_h, subplot_v, j+1)
        im = plt.imshow(image2)
        plt.xticks([]), plt.yticks([])
        plt.title('p = {0}, f = {1}'.format(1, f[j]) )
    plt.tight_layout()
    plt.show()
    