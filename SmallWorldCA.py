'''
Created on Feb 3, 2018

@author: aditya

This class can be used to generate spatio temporal patterns of 1D cellular automata 
'''
import numpy as np
class CA_SmallWorld:
    def __init__(self, rule, p = 1, q = 0.1, world_size = 1080, lifespan = 1920, config = 'regular'):
        self.rule = np.array([int(i) for i in '{:08b}'.format(rule)])
        self.height_img = world_size
        self.width_img = lifespan
        self.X = np.zeros((world_size, lifespan), dtype = int)
        self.gates = np.zeros(world_size, dtype=int)
        self.p = p
        self.q = q
        
        if config not in ['regular', 'random']:
            raise ValueError('Configurations not present in available options:[\'regular\', \'random\', \'smallworld\']')
        self.config = config
        
        # neighbors for periodic boundary conditions
        self.left = [world_size-1]+[i for i in range(world_size-1)]
        self.right = [i for i in range(1, world_size)]+[0]
        
        self.setup()
    
    def resetworld(self):
        self.X = np.zeros((self.height_img, self.width_img), dtype = int)
        self.setup()
        
    def setup(self):
        if self.config=='regular':
            start_life = [i for i in range(int(self.height_img/2-len(self.rule)/2),int(self.height_img/2+len(self.rule)/2))]
            self.X[start_life,0]=1
        else:
            p = np.random.rand(self.height_img)
            self.X[p>0.5,0] = 1
            
    def simulation(self):
        # This method takes care of cellular automata with given rule and randomness       
        # Main Logic
        for t in range(self.width_img):
            world = self.X[:, t]
            
            p_t, q_t = np.random.rand(self.height_img), np.random.rand(self.height_img)
            
            self.gates[p_t<=self.p] = 1
            
            world_future_1 = 4*world[self.left] + 2*world + world[self.right]
            world_future_1 = self.rule[world_future_1.astype(int)]
            world_future_1 = np.multiply(world_future_1, self.gates)
            
            world_future_2 = np.zeros(self.height_img, dtype=int)
            world_future_2[q_t<=self.q]=1
            world_future_2 = np.multiply(world_future_2, np.logical_not(self.gates))
            
            world = world_future_1 + world_future_2
            
            if t+1>=self.width_img: break
            
            self.X[:,t+1] = world
        
        image = np.multiply(self.X,255)
        image = image.astype(np.uint8)
            
        self.resetworld()
        return image  
        
    def smallworld(self, f = 0.1):
        # This method takes care of small world simulation
        left, right = self.setneighbor_smallworld(f)
        
        # Main Logic
        for t in range(self.width_img):
            world = self.X[:, t]
            
            p_t, q_t = np.random.rand(self.height_img), np.random.rand(self.height_img)
            
            self.gates[p_t<=self.p] = 1
            
            world_future_1 = 4*world[left] + 2*world + world[right]
            world_future_1 = self.rule[world_future_1.astype(int)]
            world_future_1 = np.multiply(world_future_1, self.gates)
            
            world_future_2 = np.zeros(self.height_img, dtype=int)
            world_future_2[q_t<=self.q]=1
            world_future_2 = np.multiply(world_future_2, np.logical_not(self.gates))
            
            world = world_future_1 + world_future_2
            
            if t+1>=self.width_img: break
            
            self.X[:,t+1] = world
        
        image = np.multiply(self.X,255)
        image = image.astype(np.uint8)

        self.resetworld()
        return image

    def setneighbor_smallworld(self, f):
        # randomizing the neighborhood for small world
        left = self.left
        right = self.right
        for i in range(self.height_img):
            rand = np.random.rand(2)
            if rand[0]<f and rand[1]<0.5:
                left[i] = np.random.randint(self.height_img)
            elif rand[0]<f and rand[1]>0.5:
                right[i] = np.random.randint(self.height_img)        
        return left, right

if __name__=='__main__':
    
    import matplotlib.pyplot as plt
    RULE = 129
    CA = CA_SmallWorld(RULE)
    
    image1 = CA.simulation()
    im = plt.imshow(image1)
    plt.xticks([]), plt.yticks([])
    plt.title('Rule {}'.format(RULE))
    plt.show()
    
    image2 = CA.smallworld()
    im = plt.imshow(image2)
    plt.xticks([]), plt.yticks([])
    plt.title('Small World Network - Rule {}'.format(RULE))
    plt.show()
    