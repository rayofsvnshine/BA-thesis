import numpy as np

class dRBM():
    """Creates an object that contains all the information for the dRBM."""

    def __init__(self):
        # initialize the nodes
        self.input_layer = np.full((4,65), 0.0)
        self.middle_layer = np.full((4,70), 0.0)
        self.top_layer = np.full((4,35), 0.0)

        # assigns each node coordinates for plotting purposes
        for i in range(65):
            if i < 34:
                self.input_layer[2,i] = i*1.2+4     # x-axis
            elif i < 58:
                self.input_layer[2,i] = i*1.2+5.5
            else:
                self.input_layer[2,i] = i*1.2+7
            self.input_layer[3,i] = 2               # y-axis

        for i in range(70):
            self.middle_layer[2,i] = i*1.15+4.2
            self.middle_layer[3,i] = 5

        for i in range(35):
            self.top_layer[2,i] = i*2.1+8
            self.top_layer[3,i] = 8

        # creates connections between the nodes
        self.inp_mid_connections = np.zeros((65,70))
        self.mid_top_connections = np.zeros((70,35))

    def one_learning_step(self):
        self.settling_phase()
        self.hebbian_phase()
        self.dreaming_phase()
        self.anti_hebbian_phase()

    def settling_phase(self):
        for _ in range(9):
            pass
            # # bottomup spreading
            # inp_act_weight = np.matmul(new_nodes[0][0,:],new_connections[0]) 
            # # top down spreading
            # top_act_weight = np.matmul(new_connections[1],new_nodes[2][0,:])
            # # store new activations
            # new_nodes[1][0,:] = np.random.binomial(1, 1 / (1 + np.exp(-(new_nodes[1][1,:] + inp_act_weight + top_act_weight))))

            # # bottomup spreading
            # mid_act_weight = np.matmul(new_nodes[1][0,:],new_connections[1])
            # # store new activations
            # new_nodes[2][0,:] = np.random.binomial(1, 1 / (1 + np.exp(-(new_nodes[2][1,:] + mid_act_weight))))

    def hebbian_phase(self):
        #bias + (lr * act)
        # new_nodes[0][1,:] += lr * new_nodes[0][0,:]
        # new_nodes[1][1,:] += lr * new_nodes[1][0,:]
        # new_nodes[2][1,:] += lr * new_nodes[2][0,:]

        # weight + (lr * act_a * act_b) 
        # for i, row in enumerate(new_connections[0]):
        #     new_connections[0][i,:] = new_connections[0][i,:] + lr * new_nodes[0][0,i] * new_nodes[1][0,:]
        # for i, row in enumerate(new_connections[1]):
        #     new_connections[1][i,:] = new_connections[1][i,:] + lr * new_nodes[1][0,i] * new_nodes[2][0,:]
        pass

    def dreaming_phase(self):
        for _ in range(9):
            # mid_act_weight = np.matmul(new_connections[0],new_nodes[1][0,:])
            # new_nodes[0][0,:] = new_nodes[0][1,:] + mid_act_weight


            # # Loop through all nodes on middle layer
            #     # bottomup
            # mid_act_weight = np.matmul(new_nodes[1][0,:],new_connections[1])
            
            # # store new with bernoulli randomness
            # sigmoided_exci = 1 / (1 + np.exp(-(new_nodes[2][1,:] + mid_act_weight)))
            # new_nodes[2][0,:] = np.random.binomial(1, sigmoided_exci)


            # # bottomup
            # inp_act_weight = np.matmul(new_nodes[0][0,:],new_connections[0])
            
            # # top down
            # top_act_weight = np.matmul(new_connections[1],new_nodes[2][0,:])
            
            # # store new
            # sigmoided_exci = 1 / (1 + np.exp(-(new_nodes[1][1,:] + inp_act_weight + top_act_weight)))
            # new_nodes[1][0,:] = np.random.binomial(1, sigmoided_exci)
            pass
        pass

    def anti_hebbian_phase(self):
        # Bias changes
        # new_nodes[0][1,:] -= 0.001 * new_nodes[0][0,:]
        # new_nodes[1][1,:] -= 0.001 * new_nodes[1][0,:]
        # new_nodes[2][1,:] -= 0.001 * new_nodes[2][0,:]

        # Weight changes 
        # for i, row in enumerate(new_connections[0]):
        #     new_connections[0][i,:] = new_connections[0][i,:] - 0.001 * new_nodes[0][0,i] * new_nodes[1][0,:]
        # for i, row in enumerate(new_connections[1]):
        #     new_connections[1][i,:] = new_connections[1][i,:] - 0.001 * new_nodes[1][0,i] * new_nodes[2][0,:]
        pass