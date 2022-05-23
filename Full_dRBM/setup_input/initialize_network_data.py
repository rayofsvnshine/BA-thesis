#######################################################
# Create all nodes and connections using an np.array ##
#######################################################
import numpy as np

def setup_network():
    """ This function returns an list containing all nodes and connections 
            and their activation, bias, weights and coordinates 
    
    Parameters:
    ----------
    

    Returns:
    --------
    nodes_connections: an list containing two lists for nodes and connections
            each with an array of data for each layer
    
    """

    # For each nodelayer, create four values per node
    inp_nodes = np.full((4,89), 0.0)
    mid_nodes = np.full((4,70), 0.0)
    top_nodes = np.full((4,35), 0.0)

    # for each node set the final two values as the coordinates (for graphing purposes)
    for i in range(89):
        if i < 34:
            inp_nodes[2,i] = i*1.2+4    # x-axis
        elif i < 82:
            x_ax = ((i - 34) / 2) + 34
            inp_nodes[2,i] = x_ax*1.2+5.5  # x-axis
        else:
            inp_nodes[2,i] = (i - 24)*1.2+7 # x-axis

        if i%2 == 1:
                inp_nodes[3,i] = 2.25   # y-axis
        else:
            inp_nodes[3,i] = 2      # y-axis

    for i in range(70):
        mid_nodes[2,i] = i*1.15+4.2
        mid_nodes[3,i] = 5
    for i in range(35):
        top_nodes[2,i] = i*2.1+8
        top_nodes[3,i] = 8

    # combine all node arrays into one list
    all_nodes = [inp_nodes, mid_nodes, top_nodes]

    # Setup the connections for all nodes in a matrix
    inp_mid_connections = np.zeros((89,70))
    mid_top_connections = np.zeros((70,35))
    
    # Also combine in a list
    all_connections = [inp_mid_connections, mid_top_connections]

    # Combine all nodes and connections in another list
    nodes_connections = [all_nodes, all_connections]

    return nodes_connections
