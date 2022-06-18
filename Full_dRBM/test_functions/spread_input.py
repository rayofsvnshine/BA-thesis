import numpy as np

def clamp_nodes(nodes, clamped_nodes, test_direction):
    """ This function returns the nodes to the values of the clamped nodes
        for either the lexical and phoneme nodes (comprehension) or the
        lexical and morphosyntactic nodes (production)
    """
    temp_nodes = nodes[0][0]

    if test_direction == "comp":
        temp_nodes = np.append(clamped_nodes[:82], temp_nodes[82:])
    elif test_direction == "prod":
        temp_nodes = np.append(temp_nodes[:34], clamped_nodes[34:])
    elif test_direction == "phon":
        temp_nodes = np.append(clamped_nodes[:34], temp_nodes[34:])

    return temp_nodes

def spread_input(new_nodes, new_connections, test_direction=None):
    """ This function calculates the activation on the top and middle layer
        after spreading from the other layers, 10 times
    
    Parameters:
    ----------
    new_nodes: an array containing the node activations and biases 
    new_connections: an array containing all weights for all connections
    test_direction: ensures either the phoneme or morphosyntax nodes are clamped

    Returns:
    --------
    new_nodes_connections: a list containing the node array and its connections, all with 
        the new values after one spreading activations
    
    """ 
    # create new array to store the values of the nodes for clamping 
    clamped_nodes = np.copy(new_nodes[0][0])

    # iterate over spreading steps 10 times, clamping the input layer at the end
    for _ in range(9):
        new_nodes = middle_spread(new_nodes, new_connections)
        new_nodes = top_spread(new_nodes, new_connections)
        new_nodes = middle_to_bottom_spread(new_nodes, new_connections)
        new_nodes[0][0] = clamp_nodes(new_nodes, clamped_nodes, test_direction)

    new_nodes_connections = [new_nodes, new_connections]

    return new_nodes_connections

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
    new_nodes[1][0,:] = 1 / (1 + np.exp(-(new_nodes[1][1,:] + inp_act_weight + top_act_weight)))

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
    new_nodes[2][0,:] = 1 / (1 + np.exp(-(new_nodes[2][1,:] + mid_act_weight)))

    return new_nodes


def middle_to_bottom_spread(new_nodes, new_connections):
     # top-to-bottom spreading
    mid_act_weight = np.matmul(new_connections[0], new_nodes[1][0,:])
    
    # store new activations
    new_nodes[0][0,:] = 1 / (1 + np.exp(-(new_nodes[0][1,:] + mid_act_weight)))
    
    return new_nodes