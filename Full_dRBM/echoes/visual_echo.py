import numpy as np
import matplotlib.pyplot as plt

# own functions import 
from .echo_tools import echo_peaks, echo_spread, edge_input_echo, random_input_echo

def echo_visual(new_nodes, new_connections, vowel_system, input_method):
    """ This function creates a list of coordinates of the inputs and
    echoes of 1000 inputs (echo coordinates are found through local maxima)
    
    Parameters:
    ---------- 
    new_nodes: an array containing the node activations and biases 
    new_connections: an array containing all weights for all connections
    vowel_system: a string stating the vowelsystem to be used
    input_method: a string stating a random input or an edge input


    Returns:
    --------
    [av_inp_dist, av_echo_dist]: a list containing median distance to the 
        prototype values from the input coordinates and the echo coordinates
    """
    # set up coordinate lists and the erb values
    drifts_coord_x = []
    drifts_coord_y = []
    erb = np.linspace(4,28,49)

    # ensure correct activations on mid and top layer
    new_nodes[1][0,:] = 0.5
    new_nodes[2][0,:] = 0.5

    # gather 1000 echoes, 200 per prototype
    for i in range(1000):
        if input_method == 'edge':
            f1f2_act = edge_input_echo(vowel_system, i)
        else: # if input is required to be completely random
            f1f2_act = random_input_echo(vowel_system)
        new_nodes[0][0,:] = f1f2_act[2]
        f1 = f1f2_act[0]
        f2 = f1f2_act[1]

        # per input, let activation spread through system
        new_nodes = echo_spread(new_nodes, new_connections)

        # Interpolate the heights to get more refined peaks
        echo_f1f2 = echo_peaks(erb, new_nodes)
        echo_f1 = echo_f1f2[0]
        echo_f2 = echo_f1f2[1]
        # append x and y values to the drift lists
        drifts_coord_x.append((f2, echo_f2))
        drifts_coord_y.append((f1, echo_f1))
    
    # set new lists to return
    drift_coords = [drifts_coord_x, drifts_coord_y]

    # Set up the figure and plot data into graph
    fig, ax = plt.subplots()
    for i, coord in enumerate(drift_coords[0]):
        ax.plot(drift_coords[0][i], drift_coords[1][i], '-')

    # invert axes and add axis titles
    ax.invert_xaxis()
    ax.invert_yaxis()
    ax.text(29.5,10, 'F1', ha='center')
    ax.text(19,17, 'F2', ha='center')

    # Store and return the graph
    graph = fig
    return graph