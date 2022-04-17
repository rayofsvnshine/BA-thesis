import numpy as np

def echo_spread(new_nodes, new_connections):
    """ This function spreads the activation given through the network
    from bottom to middle to the top, back to the middle (x10) and then back
    to the bottom. This activation final state it then returns
    
    Parameters:
    ---------- 
    new_nodes: an array containing the node activations and biases 
    new_connections: an array containing all weights for all connections

    Returns:
    --------
    new_nodes: an array containing the node activations and biases 
    """
    # spread to middle (while top = 0)
    inp_act_weight = np.matmul(new_nodes[0][0,:],new_connections[0])
    top_act_weight = np.matmul(new_connections[1],new_nodes[2][0,:])
    new_nodes[1][0,:] = 1 / (1 + np.exp(-(new_nodes[1][1,:] + inp_act_weight + top_act_weight)))

    # echo calculation (from middle to top and bottom, then back to middle)
    # 10 times
    for _ in range(9):
        # top layer
        mid_act_weight = np.matmul(new_nodes[1][0,:],new_connections[1])
        new_nodes[2][0,:] = 1 / (1 + np.exp(-(new_nodes[2][1,:] + mid_act_weight)))
        # spread back to erb-layer
        mid_act_weight = np.matmul(new_connections[0],new_nodes[1][0,:])
        new_nodes[0][0,:] = new_nodes[0][1] + mid_act_weight
        # back to mid layer 
        inp_act_weight = np.matmul(new_nodes[0][0,:],new_connections[0])
        top_act_weight = np.matmul(new_connections[1],new_nodes[2][0,:])
        new_nodes[1][0,:] = 1 / (1 + np.exp(-(new_nodes[1][1,:] + inp_act_weight + top_act_weight)))

    return new_nodes