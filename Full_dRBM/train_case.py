"""
Does the same as show_dRBM_network.py but resets activations to 0
"""
# import all needed packages
from learning_phases import one_learning_step
from setup_input import input_word, setup_data, setup_network
from graphs import show_full_network

import matplotlib.pyplot as plt
# ignores FutureWarning
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Setup the network, load data, select network type, and set the number of trainingsteps
new_nodes_connections = setup_network()
training_type = 'full'
new_data = setup_data(training_type)
training_steps = 100000

# Initiate training
for _ in range(training_steps):
    new_nodes_connections[0] = input_word(new_nodes_connections[0], new_data[0])
    new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])

# reset activations of all layers to 0
new_nodes_connections[0][0][0,:] = 0.0
new_nodes_connections[0][1][0,:] = 0.0
new_nodes_connections[0][2][0,:] = 0.0

# Show input graph
graph = show_full_network(new_nodes_connections[0], new_nodes_connections[1])
plt.tight_layout()
graph.set_size_inches(9.2, 5)
graph.savefig('pdfs/visualisation.pdf', dpi=650)
plt.show()