import numpy as np
import matplotlib.pyplot as plt

# own functions import 
from .echo_tools import  echo_peaks, echo_spread, random_input_echo

def random_echo_visual(new_nodes, new_connections):

    # set up coordinate lists and the erb values
    drifts_coord_x = []
    drifts_coord_y = []
    erb = np.linspace(4,28,49)

    # ensure correct activations on mid and top layer
    new_nodes[1][0,:] = 0.5
    new_nodes[2][0,:] = 0.5

    # gather 1000 echoes, 200 per prototype
    for i in range(1000):
        f1f2_act = random_input_echo()

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

    fig, ax = plt.subplots()
    for i, coord in enumerate(drift_coords[0]):
        ax.plot(drift_coords[0][i], drift_coords[1][i], '-')



    ax.invert_xaxis()
    ax.invert_yaxis()

    ax.text(29.5,10, 'F1', ha='center')
    ax.text(19,17, 'F2', ha='center')

    graph = fig

    return graph