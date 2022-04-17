import numpy as np

def spread_to_inp(new_nodes, new_connections):
    """ This function calculates the activation on the input layer nodes
        after spreading from the middle layer
    
    Parameters: 
    ----------
    new_nodes: an array containing the node activations and biases 

    new_connections: an array containing all weights for all connections

    Returns:
    --------
    new_nodes: an array containing the node activations and biases
    
    """
    mid_act_weight = np.matmul(new_connections[0],new_nodes[1][0,:])
    new_nodes[0][0,:] = new_nodes[0][1,:] + mid_act_weight

 

    return new_nodes