# import all needed packages
from learning_phases import one_learning_step
from setup_input import input_word, setup_data, setup_network
from graphs import show_full_network

import matplotlib.pyplot as plt

# Setup the network, load data, select network type, and set the number of trainingsteps
new_nodes_connections = setup_network()
new_data = setup_data()
training_steps = 1000

# Initiate training
for _ in range(training_steps):
    new_nodes_connections[0] = input_word(new_nodes_connections[0], new_data)
    new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])

# show graph
graph = show_full_network(new_nodes_connections[0], new_nodes_connections[1])
plt.tight_layout()
graph.set_size_inches(9.2, 5)
graph.savefig('pdfs/network_figure.pdf', dpi=600)
plt.show()

