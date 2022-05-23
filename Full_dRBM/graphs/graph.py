# packages 
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def show_full_network(network_nodes, network_connections):
    """ This outputs the data to show the network
    
    Parameters:
    ----------
    network_nodes: a dictionary containing all nodes in the network 
        with their coordinates, activation and bias values

    network_connections: a dictionary containg all connections as 
            keys and their parent-node coordinates and weights


    Returns:
    --------
    ax: data to show the network
    
    """
    
    # import data
    all_nodes = network_nodes
    all_connection = network_connections

    # set-up variables for legibility 
    inp_nodes = all_nodes[0]
    hidden_mid_nodes = all_nodes[1]
    hidden_top_nodes = all_nodes[2]

    inp_mid_links= all_connection[0]
    mid_top_links= all_connection[1]



    ####################
    # Plot everything ##
    ####################
    fig, ax = plt.subplots()
    #### plot connections ####
    # inp-mid Connections
    for t, row in enumerate(inp_mid_links):
        for i, cell in enumerate(row):
            if cell > 0.02 or cell < -0.02:
                if cell < 0:
                    color = 'w'
                else:
                    color = 'k' 
                ax.plot((inp_nodes[2,t],hidden_mid_nodes[2,i]),(inp_nodes[3,t]+0.16,hidden_mid_nodes[3,i]-0.133),
                    color, linestyle='-', linewidth=abs(cell*3))


    # mid-top connections
    for t, row in enumerate(mid_top_links):
        for i, cell in enumerate(row):
            if cell > 0.02 or cell < -0.02:
                if cell < 0:
                    color = 'w'
                else:
                    color = 'k' 
                ax.plot((hidden_mid_nodes[2,t],hidden_top_nodes[2,i]),(hidden_mid_nodes[3,t]+0.13,hidden_top_nodes[3,i]-0.23), 
                color, linestyle='-', linewidth=abs(cell*3))


    #### plot nodes ####
    inp_node_size = 15
    mid_node_size = 10
    top_node_size = 20
    
    
    # Plot erb nodes
    for i in range(89):
        if i < 90:
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

    # Plot Hidden mid nodes
    for i in range(70):
        ax.plot(hidden_mid_nodes[2,i], hidden_mid_nodes[3,i], 
            'o', mfc= (0.1, 0.2, 1.0, 0.0), mec = 'k',
            markersize=mid_node_size) 
        # and activation
        if hidden_mid_nodes[0,i] < 0.50:
            dot = 'bo'
            color = 'blue'
            size = mid_node_size - (hidden_mid_nodes[0,i]*2)*(mid_node_size)-1
        else:
            dot = 'ro'
            color = 'red'
            size = (hidden_mid_nodes[0,i]*2-1)*(mid_node_size)-1

        ax.plot(hidden_mid_nodes[2,i], hidden_mid_nodes[3,i], 
            dot, mfc=color, markersize=size) 

    # Plot Hidden top nodes 
    for i in range(35):
        ax.plot(hidden_top_nodes[2,i], hidden_top_nodes[3,i],
            'o', mfc= (0.1, 0.2, 1.0, 0.0), mec = 'k',
            markersize=top_node_size)  
        # and activation
        if hidden_top_nodes[0,i] < 0.50:
            dot = 'bo'
            color = 'blue'
            size = top_node_size - ((hidden_top_nodes[0,i]*2)*top_node_size)-1
        else:
            dot = 'ro'
            color = 'red'
            size = (hidden_top_nodes[0,i]*2-1)*(top_node_size)-1
        
        ax.plot(hidden_top_nodes[2,i], hidden_top_nodes[3,i],
            dot, mfc=color, markersize=size)  

    # add layer labels
    ax.text(2, 2, 'Input\nlayer', ha='right', va='center')
    ax.text(2, 5, 'Hidden\nmiddle\nlayer', ha='right', va='center')
    ax.text(2, 8, 'Hidden\ntop\nlayer', ha='right', va='center')

    # ERB text axis
    text_y = 1.4
    ax.text(25,text_y, 'Phoneme nodes', ha='center')
    ax.text(60,text_y, 'Lexical nodes', ha='center')
    ax.text(80,0.9, 'Morpho-\nsyntactic\nnodes', ha='center')
    
    # remove all ticks
    ax.set_xticks(ticks=[])
    ax.set_yticks(ticks=[])

    # Setting the background color of the plot
    ax.axis([2.5, 85.5, 1.7, 8.6])
    ax.set_facecolor("0.7")

    network = fig
    return network
