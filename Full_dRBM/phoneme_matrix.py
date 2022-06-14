# import all needed packages
from learning_phases import one_learning_step
from setup_input import input_word, input_phoneme, phoneme_data, setup_network, copy_network
from test_functions import spread_input

import csv

# Setup the network, load data, select network type, and set the number of trainingsteps
new_nodes_connections = setup_network()
new_data = phoneme_data()
# training_steps = 10000
training_steps = 1000
testing_steps = 34

# Initiate training
for _ in range(training_steps):
    new_nodes_connections[0] = input_word(new_nodes_connections[0], new_data[0])
    new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])

# reset activations of all layers to 0
new_nodes_connections[0][0][0,:] = 0.0
new_nodes_connections[0][1][0,:] = 0.0
new_nodes_connections[0][2][0,:] = 0.0
# store trained network
trained_network = new_nodes_connections

# create list to store results of testing
test_results = []
temp_network = []

# Initiate testing
for step in range(testing_steps):
    # reset to the unactivated network/variables
    temp_network = copy_network(trained_network)
    actual_input = ""
    expected_output = ""
    # input only the needed nodes for testing
    temp_network[0], phoneme = input_phoneme(temp_network[0], new_data[1], step)
    # spread test input
    temp_network = spread_input(temp_network[0], temp_network[1])
    # store activated nodes as results
    results = temp_network[0][1][0]
    test_results.append([phoneme, results])

# store data in a csv-file
with open('results/phoneme_activation.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Activation levels"])
    wr.writerows(test_results)