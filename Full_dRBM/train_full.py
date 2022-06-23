# import all needed packages
from learning_phases import one_learning_step
from setup_input import input_word, input_test_word, setup_data, setup_network, copy_network
from test_functions import check_activation, spread_input
# from graphs import show_full_network

# import matplotlib.pyplot as plt
import csv

# ignores FutureWarning
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def run_model(learner_nr, training_type, training_steps, testing_steps):
    # Setup the network, load data, select network type, and set the number of trainingsteps
    new_nodes_connections = setup_network()
    new_data = setup_data(training_type)

    # Initiate training
    for _ in range(training_steps):
        # choose random input word and activate corresponding nodes
        new_nodes_connections[0] = input_word(new_nodes_connections[0], new_data[0])
        # train network on this word
        new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])

    # reset activations of all layers to 0
    new_nodes_connections[0][0][0,:] = 0.0
    new_nodes_connections[0][1][0,:] = 0.0
    new_nodes_connections[0][2][0,:] = 0.0
    # store trained network
    trained_network = new_nodes_connections

    # test both production and comprehension for the same model
    for test_direction in ["comp", "prod"]:
        # create list to store results of testing
        test_results = []
        temp_network = []

        # Initiate testing
        for step in range(testing_steps):
            # reset to the unactivated network/variables
            temp_network = copy_network(trained_network)
            actual_input = ""
            expected_output = ""
            # input only the needed nodes for testing and store input & expected output
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
    # for all types except 'full', the name indicates which group is left out of training
    # 'full', 'case_nom', 'case_gen', 'case_dat', 'def', 'indef', 'plur', 'sing'
    training_type = 'sing'

    training_steps = 100000 # for proper training
    # training_steps = 1000 # for trial runs

    # testing_steps = 576 # full
    # testing_steps = 96 # case
    testing_steps = 144 # det/plur
    # testing_steps = 10 # for trial runs

    # train and test 100 learners
    for i in range(100):
        run_model(i, training_type, training_steps, testing_steps)

if __name__ == "__main__":
    main()