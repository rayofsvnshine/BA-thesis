# import all needed packages
from learning_phases import one_learning_step
from setup_input import input_five, setup_network
from echoes.echo_tools import echo_spread, edge_input_echo
from graphs import show_erb_layer
import matplotlib.pyplot as plt

# setup the network 
new_nodes_connections = setup_network()

# training steps
for i in range(1000):
    new_nodes_connections[0] = input_five(new_nodes_connections[0])
    new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])


# get input
f1f2_act = edge_input_echo()
new_nodes_connections[0][0][0,:] = f1f2_act[2]

# Show input graph
graph = show_erb_layer(new_nodes_connections[0])
plt.tight_layout()
graph.set_size_inches(9.2, 1.7)
graph.savefig('inp-act.pdf', dpi=600)
plt.show()

# Spread activations
new_nodes = echo_spread(new_nodes_connections[0], new_nodes_connections[1])

# show echo graph
graph = show_erb_layer(new_nodes_connections[0])
plt.tight_layout()
graph.set_size_inches(9.2, 1.7)
graph.savefig('echo-act.pdf', dpi=600)
plt.show()

