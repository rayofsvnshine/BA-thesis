"""
Trains the Neural Network, then analyses the phoneme activations and saves the output.
Number of models to train, number of training steps,
and number of testing steps are all determined in the main function.
"""

from learning_phases import one_learning_step
from setup_input import input_word, input_phoneme, phoneme_data, setup_network, copy_network
from test_functions import spread_input

import csv
# ignores FutureWarning
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def run_model(learner_nr, training_steps, testing_steps):
    # Setup the network and load data
    new_nodes_connections = setup_network()
    new_data = phoneme_data()

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
        # input only the needed nodes for testing
        temp_network[0], phoneme = input_phoneme(temp_network[0], new_data[1], step)
        # spread test input
        temp_network = spread_input(temp_network[0], temp_network[1], "phon")
        # store activated nodes as results
        results = temp_network[0][1][0]
        test_results.append([phoneme, results])

        results_file_name = f"results/cos_matrix/test_phon_{learner_nr}.csv"

        # store data in a csv-file
        with open(results_file_name, 'w', newline='') as myfile:
            wr = csv.writer(myfile)
            wr.writerow(["Phoneme", "Activation levels"])
            wr.writerows(test_results)


def main():
    # set parameters
    training_steps = 100000
    testing_steps = 34

    for i in range(100):
        run_model(i, training_steps, testing_steps)


if __name__ == "__main__":
    main()