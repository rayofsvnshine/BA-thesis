import numpy as np
import math

# own functions import
from .echo_tools import random_input_echo, edge_input_echo, echo_peaks, echo_spread

def echo_drift(new_nodes, new_connections, vowel_system, input_method):
    """ This function calculates the median distance over X inputs from
    the input(and echo) coordinates to the vowel mean formants.
    
    Parameters:
    ---------- 
    new_nodes: an array containing the node activations and biases 
    new_connections: an array containing all weights for all connections
    vowel_system: a string stating the vowel system to be used
    input_method: a string stating a random input or an edge input


    Returns:
    --------
    [av_inp_dist, av_echo_dist]: a list containing median distance to the 
        prototype values from the input coordinates and the echo coordinates
    
    """
    # set steps depending on code goal
    if vowel_system == 'five':
        steps = 1000
    elif vowel_system == 'four':
        steps = 800
    elif vowel_system == 'five_spec':
        steps = 400
    elif vowel_system == 'four_spec':
        steps = 200
    
    # set up coordinate lists and the erb values
    inp_dists = []
    echo_dists = []
    erb = np.linspace(4,28,49)

    # ensure correct activations on mid and top layer
    new_nodes[1][0,:] = 0.5
    new_nodes[2][0,:] = 0.5

    # gather X echoes, 200 per prototype
    for i in range(steps):
        if input_method == 'edge':
            f1f2_act = edge_input_echo(vowel_system)
        else:
            f1f2_act = random_input_echo(vowel_system)
        
        new_nodes[0][0,:] = f1f2_act[2]
        f1 = f1f2_act[0]
        f2 = f1f2_act[1]
        proto_f1 = f1f2_act[3]
        proto_f2 = f1f2_act[4]

        # per input, let activation spread through system
        new_nodes = echo_spread(new_nodes, new_connections)

        # Find formants of the echo
        echo_f1f2 = echo_peaks(erb, new_nodes)
        echo_f1 = echo_f1f2[0]
        echo_f2 = echo_f1f2[1]
      
        # get distance from input to prototype, and append
        input_distance = math.sqrt( (f1 - proto_f1)**2 + (f2 - proto_f2)**2 )
        inp_dists.append(input_distance)

        # get distance from echo to prototype, and append
        echo_distance = math.sqrt( (echo_f1 - proto_f1)**2 + (echo_f2 - proto_f2)**2 )
        echo_dists.append(echo_distance)

    # find the median of all distances 
    av_inp_dist = np.median(inp_dists)
    av_echo_dist = np.median(echo_dists)

    return [av_inp_dist, av_echo_dist]