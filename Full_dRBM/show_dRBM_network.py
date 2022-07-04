"""
show_dRBM_network.py
- Sets up network and loads training data
- Trains network on the whole dataset
- After 100000 training steps, saves a pdf image of the trained network
"""

# import code for dRBM
from learning_phases import one_learning_step
from setup_input import input_word, setup_data, setup_network
from graphs import show_full_network
# import plotting code
import matplotlib.pyplot as plt


# Setup the network, load data, select network type, and set the number of trainingsteps
new_nodes_connections = setup_network()
training_type = 'full'
new_data = setup_data(training_type)
training_steps = 100000

# Initiate training
for _ in range(training_steps):
    new_nodes_connections[0] = input_word(new_nodes_connections[0], new_data[0])
    new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])

# show graph
graph = show_full_network(new_nodes_connections[0], new_nodes_connections[1])
plt.tight_layout()
graph.set_size_inches(9.2, 5)
graph.savefig('pdfs/network_figure.pdf', dpi=600)
plt.show()

