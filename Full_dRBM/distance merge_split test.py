# import all needed packages
from setup_input import input_vowels, setup_network
from learning_phases import one_learning_step
from echoes import echo_drift
import csv
##########################################################################
##########  setup parameters to run the distance calculations  ###########
learners = 200
steps = 100000
original_vowels = 'five' # Set vowel of L1
test_vowel = 'five'   # set L2(or L1) test vowel
##########################################################################
# setup the network 
new_nodes_connections = setup_network()

# set up an empty list of drifts to store
echo_drifts = []

# repeat calculations for virtual 200 learners
for _ in range(learners):
    # train the network
    for i in range(steps):
        new_nodes_connections[0] = input_vowels(new_nodes_connections[0], original_vowels)
        new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])

    # Get only the median distance between input and echo
    echo_drift_nodes = echo_drift(new_nodes_connections[0], new_nodes_connections[1], test_vowel+'_spec', 'edge')
    echo_drifts.append([str(echo_drift_nodes[1])])

# export data to a csv file
with open(original_vowels+'_trained_with_'+test_vowel+'_'+steps+'.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerows(echo_drifts)