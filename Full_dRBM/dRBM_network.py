# import all needed packages
from learning_phases import one_learning_step
from setup_input import input_vowels, setup_network
from graphs import show_full_network

import matplotlib.pyplot as plt

# Setup the network and set the number of trainingsteps
new_nodes_connections = setup_network()
training_steps = 2000

# Initiate training
for _ in range(training_steps):
    new_nodes_connections[0] = input_vowels(new_nodes_connections[0], 'five')
    new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])

# show graph
graph = show_full_network(new_nodes_connections[0], new_nodes_connections[1])
plt.tight_layout()
graph.set_size_inches(9.2, 5)
graph.savefig('pdfs/network_figure.pdf', dpi=600)
plt.show()

