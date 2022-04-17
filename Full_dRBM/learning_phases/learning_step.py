#### The full learning step

from learning_phases.phases.dreaming import spread_to_inp
from .phases import settling_phase, hebbian_learning_nodes, hebbian_learning_connections, dreaming_phase
from .phases import anti_hebbian_learning_nodes, anti_hebbian_learning_connections

def one_learning_step(new_nodes, new_connections):
    """ This function goes through all learning steps and adjusts
        the network's values. finally it returns the entire network
        of nodes and connections new values
    
    Parameters:
    ---------- 
    new_nodes: an array containing the node activations and biases 

    new_connections: an array containing all weights for all connections


    Returns:
    --------
    new_nodes_connections: a list containing the node array and
        connections array, all with the new values after one entire 
        training step 
    
    """
    # Settling phase
    new_nodes = settling_phase(new_nodes, new_connections)

    # Hebbian learning phase       
    new_nodes = hebbian_learning_nodes(new_nodes, 0.001)
    new_connections = hebbian_learning_connections(new_nodes, new_connections, 0.001)
    
    # Dreaming phase
    new_nodes = dreaming_phase(new_nodes, new_connections)
    
    # Anti-Hebbian learning
    new_nodes = anti_hebbian_learning_nodes(new_nodes)
    new_connections = anti_hebbian_learning_connections(new_nodes, new_connections)

    # Combine new nodes and connections data and return
    new_nodes_connections = [new_nodes, new_connections]

    return new_nodes_connections