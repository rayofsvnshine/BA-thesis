# import all needed packages
from learning_phases import one_learning_step
from setup_input import input_word, input_test_word, setup_data, setup_network, copy_network
from test_functions import check_activation, spread_input

import csv
# ignores FutureWarning
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Setup the network, load data, select network type, and set the number of trainingsteps
new_nodes_connections = setup_network()
# 'full', 'case', 'det', 'plur'
training_type = 'case_nom'
new_data = setup_data(training_type)
training_steps = 10000
# training_steps = 1000
testing_steps = 96 # case
# testing_steps = 144 # det/plur
# testing_steps = 576 # full

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
# comp or prod: tests comprehension or production
test_direction = "prod"
temp_network = []

# Initiate testing
for step in range(testing_steps):
    # reset to the unactivated network/variables
    temp_network = copy_network(trained_network)
    actual_input = ""
    expected_output = ""
    # input only the needed nodes for testing
    temp_network[0], actual_input, expected_output = input_test_word(temp_network[0], new_data[1], test_direction, step)
    # spread test input
    temp_network = spread_input(temp_network[0], temp_network[1], test_direction)
    # store activated nodes as results
    processed_results = check_activation(temp_network[0][0][0])
    test_results.append([actual_input, expected_output, processed_results])

# store data in a csv-file
with open('results/test_full_prod.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Input", "Expected Output", "Actual Output"])
    wr.writerows(test_results)