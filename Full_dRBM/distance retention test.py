# import all needed packages
from setup_input import input_vowels, setup_network
from learning_phases import one_learning_step
from echoes import echo_drift
import csv
#########################################################
##########  setup parameters to run the test  ###########
steps = 50000
original_vowels = 'five'  # L1 vowels
l2 = True          # if you want the network to learn an L2
new_vowels = 'four'     # L2 vowels
test_vowel = 'five'   # set L2(or L1) vowel
split_merge_steps= 50000
##########################################################################
# setup the network 
new_nodes_connections = setup_network()

# set up empty lists of drifts to plot
echo_drifts = []

# repeat calculations for virtual 200 learners
for i in range(200):
    # train network in native vowel system
    for _ in range(steps):
        new_nodes_connections[0] = input_vowels(new_nodes_connections[0], original_vowels)
        new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])

    if l2 == True:
        # train network in L2
        for _ in range(split_merge_steps):
            new_nodes_connections[0] = input_vowels(new_nodes_connections[0], new_vowels)
            new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])

    # Get only the median distance between input and echo
    echo_drift_nodes = echo_drift(new_nodes_connections[0], new_nodes_connections[1], test_vowel+'_spec', 'edge')
    echo_drifts.append([str(echo_drift_nodes[1])])

# store data in a csv-file
with open('retention_five_merge.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(echo_drifts)