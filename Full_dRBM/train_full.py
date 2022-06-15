# import all needed packages
from learning_phases import one_learning_step
from setup_input import input_word, input_test_word, setup_data, setup_network, copy_network
from test_functions import check_activation, spread_input
from graphs import show_full_network

import matplotlib.pyplot as plt
import csv

def run_model(learner_nr, training_type, training_steps, testing_steps, test_direction):
    # Setup the network, load data, select network type, and set the number of trainingsteps
    new_nodes_connections = setup_network()
    new_data = setup_data(training_type)

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

    # # show graph of trained network
    # graph = show_full_network(trained_network[0], trained_network[1])
    # plt.tight_layout()
    # graph.set_size_inches(9.2, 5)
    # graph.savefig('pdfs/network_figure.pdf', dpi=600)
    # plt.show()

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
        temp_network[0], actual_input, expected_output = input_test_word(temp_network[0], new_data[1], test_direction, step)
        # spread test input
        temp_network = spread_input(temp_network[0], temp_network[1], test_direction)
        # store activated nodes as results
        processed_results = check_activation(temp_network[0][0][0])
        test_results.append([actual_input, expected_output, processed_results])

    results_file_name = f"results/{training_type}/{test_direction}/test_{training_type}_{test_direction}_{learner_nr}.csv"

    # store data in a csv-file
    with open(results_file_name, 'w', newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(["Input", "Expected Output", "Actual Output"])
        wr.writerows(test_results)

def main():
    # set parameters
    # 'full', 'case_nom', 'case_gen', 'case_dat', 'def', 'plur'
    training_type = 'full'
    training_steps = 30000
    # training_steps = 1000
    testing_steps = 576
    # testing_steps = 10
    # comp or prod: tests comprehension or production
    test_direction = "prod"

    for i in range(22, 100):
        run_model(i, training_type, training_steps, testing_steps, test_direction)

if __name__ == "__main__":
    main()