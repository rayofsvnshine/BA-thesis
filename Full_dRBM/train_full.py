# import all needed packages
from learning_phases import one_learning_step
from setup_input import input_word, input_test_word, setup_data, setup_network
from test_functions import check_activation, spread_input
from graphs import show_full_network

import matplotlib.pyplot as plt
import csv

# Setup the network, load data, select network type, and set the number of trainingsteps
new_nodes_connections = setup_network()
# 'full', 'case', 'det', 'plur'
training_type = 'full'
new_data = setup_data(training_type)
training_steps = 10000
# testing_steps = 288*2
testing_steps = 100

# Initiate training
for _ in range(training_steps):
    new_nodes_connections[0] = input_word(new_nodes_connections[0], new_data[0])
    new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])

trained_network = new_nodes_connections

# show graph of trained network
graph = show_full_network(trained_network[0], trained_network[1])
plt.tight_layout()
graph.set_size_inches(9.2, 5)
graph.savefig('pdfs/network_figure.pdf', dpi=600)
plt.show()

test_results = []

# Initiate testing
for step in range(testing_steps):
    temp_network = trained_network
    # comp or prod: tests comprehension or production
    temp_network[0] = input_test_word(trained_network[0], new_data[1], "prod", step)
    temp_network = spread_input(temp_network[0], temp_network[1])
    processed_results = check_activation(temp_network)
    test_results.append(processed_results)

# store data in a csv-file
with open('test_full.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerows(test_results)
