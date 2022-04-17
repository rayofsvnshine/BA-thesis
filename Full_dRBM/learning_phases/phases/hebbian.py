########################### Hebbian Learning ##############################
# Calculate node training
def hebbian_learning_nodes(new_nodes, lr):
    """ This function calculates the bias changes of all nodes
    
    Parameters:
    ----------
    network_nodes: a dictionary containing all nodes in the network 
        with their coordinates, activation and bias values

    network_connections: a dictionary containg all connections as keys 
        and their parent-node coordinates and weights

    learning_rate: a float value for the learning rate

    Returns:
    --------
    nodes_connections: a list of two dictionaries of all nodes and 
        connections with updates values biases and weights respectively
    
    """
    #bias + (lr * act)
    new_nodes[0][1,:] += lr * new_nodes[0][0,:]
    new_nodes[1][1,:] += lr * new_nodes[1][0,:]
    new_nodes[2][1,:] += lr * new_nodes[2][0,:]

    return new_nodes

# Calculate connection training
def hebbian_learning_connections(new_nodes, new_connections, lr):
    """ This function calculates the bias changes of all connections
    
    Parameters:
    ----------
    new_nodes: an array containing the node activations and biases 

    new_connections: an array containing all weights for all connections

    Returns:
    --------
    new_connections: an array containing all weights for all connections
    
    """
    # weight + (lr * act_a * act_b) 
    for i, row in enumerate(new_connections[0]):
        new_connections[0][i,:] = new_connections[0][i,:] + lr * new_nodes[0][0,i] * new_nodes[1][0,:]
    for i, row in enumerate(new_connections[1]):
        new_connections[1][i,:] = new_connections[1][i,:] + lr * new_nodes[1][0,i] * new_nodes[2][0,:]



    return new_connections