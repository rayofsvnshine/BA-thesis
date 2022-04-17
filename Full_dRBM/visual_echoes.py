# import all needed packages
from learning_phases import one_learning_step
from setup_input import input_vowels, setup_network
from echoes import echo_visual
import matplotlib.pyplot as plt
##########################################################################
##############  setup parameters to show the visual echoes  ##############
steps = 50000
vowels = 'four'          # initial vowel system
initial_intsteps = 2000  # steps for interval for visual echo display
change_vowels = 'five'   # if split/merge, set to opposite of vowels
split_merge = 'split'    # enter: 'split' or 'merge' or 'none4' or 'none5'
split_merge_steps= 50000     # if no split or merger, set to 0
split_merge_intsteps = 2000 # steps for interval for visual echo display
input_type = 'edge'      # state if you'd like random or cat-edge inputs
returner = True
##########################################################################
# setup the network 
new_nodes_connections = setup_network()

# run first round of training
for i in range(steps):
    new_nodes_connections[0] = input_vowels(new_nodes_connections[0], vowels)
    new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])
    
    # save a figure of the drift lines at the interval step-count
    if i == initial_intsteps:
            echo_drift_nodes = echo_visual(new_nodes_connections[0], new_nodes_connections[1], vowels, input_type)
            plt.tight_layout()
            echo_drift_nodes.set_size_inches(8, 5)
            echo_drift_nodes.savefig('pdfs/visualecho_'+ split_merge + '_' + str(+i) +'.pdf', dpi=600)

# save a figure of the drift lines after first training round
echo_drift_nodes = echo_visual(new_nodes_connections[0], new_nodes_connections[1], vowels, input_type)
plt.tight_layout()
echo_drift_nodes.set_size_inches(8, 5)
echo_drift_nodes.savefig('pdfs/visualecho_'+ split_merge + '_' + str(steps) +'.pdf', dpi=600)

# run second training for split or merger test
if split_merge == 'split' or split_merge == 'merge':
    
    # save a figure of the drift lines with L2 before training L2
    echo_drift_nodes = echo_visual(new_nodes_connections[0], new_nodes_connections[1], change_vowels, input_type)
    plt.tight_layout()
    echo_drift_nodes.set_size_inches(8, 5)
    echo_drift_nodes.savefig('pdfs/visualecho_'+ split_merge + '_immediate_' + str(steps) +'.pdf', dpi=600)
    
    # start training in L2
    for i in range(split_merge_steps):
        new_nodes_connections[0] = input_vowels(new_nodes_connections[0], change_vowels)
        new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])
        
        # save a figure of the drift lines at the interval step-count
        if i == split_merge_intsteps:
            echo_drift_nodes = echo_visual(new_nodes_connections[0], new_nodes_connections[1], change_vowels, input_type)
            plt.tight_layout()
            echo_drift_nodes.set_size_inches(8, 5)
            echo_drift_nodes.savefig('pdfs/visualecho_'+ split_merge + '_' + str(steps+i) +'.pdf', dpi=600)

    # save a figure of the drift values for the final state of L2
    echo_drift_nodes = echo_visual(new_nodes_connections[0], new_nodes_connections[1], change_vowels, input_type)
    plt.tight_layout()
    echo_drift_nodes.set_size_inches(8, 5)
    echo_drift_nodes.savefig('pdfs/visualecho_'+ split_merge + '_' + str(steps+split_merge_steps) +'.pdf', dpi=600)

# Do a third round of training by returning to L1
if returner == True:
    
    # save a figure of the drift lines with L1 before re-training L1
    echo_drift_nodes = echo_visual(new_nodes_connections[0], new_nodes_connections[1], vowels, input_type)
    plt.tight_layout()
    echo_drift_nodes.set_size_inches(8, 5)
    echo_drift_nodes.savefig('pdfs/visualecho_'+ split_merge +'_returner_immediate.pdf', dpi=600)

    # start L1 training
    for i in range(50000):
        new_nodes_connections[0] = input_vowels(new_nodes_connections[0], vowels)
        new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])
        
        # save a figure of the drift values at the interval step-count
        if i == split_merge_intsteps:
            echo_drift_nodes = echo_visual(new_nodes_connections[0], new_nodes_connections[1], vowels, input_type)
            plt.tight_layout()
            echo_drift_nodes.set_size_inches(8, 5)
            echo_drift_nodes.savefig('pdfs/visualecho_'+ split_merge +'_returner_2000.pdf', dpi=600)

    # save a figure of the drift values for the final state
    echo_drift_nodes = echo_visual(new_nodes_connections[0], new_nodes_connections[1], vowels, input_type)
    plt.tight_layout()
    echo_drift_nodes.set_size_inches(8, 5)
    echo_drift_nodes.savefig('pdfs/visualecho_'+ split_merge +'_returner_500000.pdf', dpi=600)
