# packages 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def show_erb_layer(network_nodes):
    """ This outputs the data to the input layer activations
    
    Parameters:
    ----------
    network_nodes: a dictionary containing all nodes in the network 
        with their coordinates, activation and bias values



    Returns:
    --------
    ax: data to show the network's erb layer activations
    
    """
    
    # import data
    all_nodes = network_nodes

    # set-up variables for legibility 
    inp_nodes = all_nodes[0]

    ####################
    # Plot everything ##
    ####################
    fig, ax = plt.subplots()
    #### plot nodes ####
    inp_node_size = 15

    # Plot erb nodes
    for i in range(89):
        ax.plot(inp_nodes[2,i], inp_nodes[3,i],
                'o', mfc= (0.1, 0.2, 1.0, 0.0), mec = 'k', markersize=inp_node_size)
       
    # and activations
    for i in range(89):
        if inp_nodes[0,i] < 0:
            dot = 'bo'
            color = 'blue'   
        else:
            dot = 'ro'
            color = 'red'
        size = abs(inp_nodes[0,i]*2.6)
        ax.plot(inp_nodes[2,i], inp_nodes[3,i], dot, mfc=color, markersize=size)

    # add layer labels
    ax.text(2, 2, 'Input\nLayer', ha='right', va='center')

    # ERB text axis
    text_y =1.8
    ax.text(22,text_y, 'Phoneme nodes', ha='center')
    ax.text(60,text_y, 'Lexical nodes', ha='center')
    ax.text(80,text_y, 'Morphosyntax\nnodes', ha='center')
    
    # remove all ticks
    ax.set_xticks(ticks=[])
    ax.set_yticks(ticks=[])

    # Setting the background color of the plot
    ax.axis([2.5, 85.5, 1.9, 2.1])
    ax.set_facecolor("0.7")

    network = fig
    return network
