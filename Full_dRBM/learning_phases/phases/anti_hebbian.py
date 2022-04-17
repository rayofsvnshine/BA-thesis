####################### Anti-Hebbian Learning ############################
def anti_hebbian_learning_nodes(new_nodes):
    """ This function calculates the bias changes 
        of all nodes by unlearning the dreaming phase
    
    Parameters:
    ----------
    new_nodes: an array containing the node activations and biases 

    Returns:
    --------
    new_nodes: an array containing the node activations and biases 
    
    """
    # Bias changes
    new_nodes[0][1,:] -= 0.001 * new_nodes[0][0,:]
    new_nodes[1][1,:] -= 0.001 * new_nodes[1][0,:]
    new_nodes[2][1,:] -= 0.001 * new_nodes[2][0,:]

    return new_nodes

def anti_hebbian_learning_connections(new_nodes, new_connections):
    """ This function calculates the weight changes 
        of all  connections by unlearning the dreaming phase
    
    Parameters:
    ----------
    new_nodes: an array containing the node activations and biases 
    new_connections: an array containing all weights for all connections

    Returns:
    --------
    new_connections: an array containing all weights for all connections
    
    """
    # Weight changes 
    for i, row in enumerate(new_connections[0]):
        new_connections[0][i,:] = new_connections[0][i,:] - 0.001 * new_nodes[0][0,i] * new_nodes[1][0,:]
    for i, row in enumerate(new_connections[1]):
        new_connections[1][i,:] = new_connections[1][i,:] - 0.001 * new_nodes[1][0,i] * new_nodes[2][0,:]

    return new_connections