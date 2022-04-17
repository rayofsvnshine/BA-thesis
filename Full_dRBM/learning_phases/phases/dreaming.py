####################### Dreaming Phase ############################
import numpy as np

def dreaming_phase(network_nodes, network_connections):
    """ This function calculates the new random binary activation on the 
        middle and top layers after spreading from the other layers, 10 times
    
    Parameters:
    ----------
    new_nodes: an array containing the node activations and biases 
    new_connections: an array containing all weights for all connections


    Returns:
    --------
    new_nodes: an array containing the node activations and biases
    
    """
    new_nodes = network_nodes
    
    for _ in range(9):
        new_nodes = spread_to_inp(new_nodes, network_connections)
        new_nodes = bernoulli_top_spread(new_nodes, network_connections)
        new_nodes = bernoulli_mid_spread(new_nodes, network_connections)

    return new_nodes

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

def bernoulli_top_spread(new_nodes, new_connections):
    """ This function calculates the new random binary activation on the top layer 
        nodes after spreading from the middle layer
    
    Parameters:
    ----------
    new_nodes: an array containing the node activations and biases 
    new_connections: an array containing all weights for all connections

    Returns:
    --------
    new_nodes: an array containing the node activations and biases
    
    """
    # Loop through all nodes on middle layer
        # bottomup
    mid_act_weight = np.matmul(new_nodes[1][0,:],new_connections[1])
    
    # store new with bernoulli randomness
    sigmoided_exci = 1 / (1 + np.exp(-(new_nodes[2][1,:] + mid_act_weight)))
    new_nodes[2][0,:] = np.random.binomial(1, sigmoided_exci)
    
    return new_nodes

def bernoulli_mid_spread(new_nodes, new_connections):
    """ This function calculates the new random binary activation on the 
        middle layer nodes after spreading from the bottom and top layer
    
    Parameters:
    ----------
    new_nodes: an array containing the node activations and biases 
    new_connections: an array containing all weights for all connections

    Returns:
    --------
    new_nodes: an array containing the node activations and biases
    
    """
    # bottomup
    inp_act_weight = np.matmul(new_nodes[0][0,:],new_connections[0])
    
    # top down
    top_act_weight = np.matmul(new_connections[1],new_nodes[2][0,:])
    
    # store new
    sigmoided_exci = 1 / (1 + np.exp(-(new_nodes[1][1,:] + inp_act_weight + top_act_weight)))
    new_nodes[1][0,:] = np.random.binomial(1, sigmoided_exci)
    
    return new_nodes
