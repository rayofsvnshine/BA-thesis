############################# Settling Phase ##############################
import numpy as np

def settling_phase(new_nodes, new_connections):
    """ This function calculates the activation on the top and middle layer
        after spreading from the other layers, 10 times
    
    Parameters:
    ----------
    new_nodes: an array containing the node activations and biases 

    new_connections: an array containing all weights for all connections


    Returns:
    --------
    new_nodes_connections: a list containing the node array and, all with 
        the new values after one spreading activations
    
    """ 
    # Spread the activation 10 times
    for _ in range(9):
        new_nodes = middle_spread(new_nodes, new_connections)
        new_nodes = top_spread(new_nodes, new_connections)

    return new_nodes

def middle_spread(new_nodes, new_connections):
    """ This function calculates the activation on the middle layer
        after spreading from the input and top layers
    
    Parameters:
    ----------
    new_nodes: an array containing the node activations and biases 

    new_connections: an array containing all weights for all connections


    Returns:
    --------
    new_nodes_connections: a list containing the node array and, all with 
        the new values after one spreading activations
    
    """
    # bottomup spreading
    inp_act_weight = np.matmul(new_nodes[0][0,:],new_connections[0]) 
    
    # top down spreading
    top_act_weight = np.matmul(new_connections[1],new_nodes[2][0,:])
    
    # store new activations
    new_nodes[1][0,:] = np.random.binomial(1, 1 / (1 + np.exp(-(new_nodes[1][1,:] + inp_act_weight + top_act_weight))))

    return new_nodes


def top_spread(new_nodes, new_connections):
    """ This function calculates the activation on the top layer
        after spreading from the middle layers
    
    Parameters:
    ----------
    new_nodes: an array containing the node activations and biases 

    new_connections: an array containing all weights for all connections


    Returns:
    --------
    new_nodes_connections: a list containing the node array and, all with 
        the new values after one spreading activations
    
    """
    # bottomup spreading
    mid_act_weight = np.matmul(new_nodes[1][0,:],new_connections[1])
    
    # store new activations
    new_nodes[2][0,:] = np.random.binomial(1, 1 / (1 + np.exp(-(new_nodes[2][1,:] + mid_act_weight))))
    
    return new_nodes
