import random
import numpy as np
import pandas as pd
from .separate_data import separate_data

def setup_data(training_type):
    """ This function loads in the dataset for both training and testing
        
        Parameters:
        ----------
        training_type: indicates in what way the data needs to be split into test/training
        
        Returns:
        --------
        A tuple containing two dataframes
        train_df: a dataframe of data only used for training
        test_df: a dataframe of data only used for testing
        
    """
    # read input from csv file
    with open("input_data.csv") as f:
        train_df = pd.read_csv(f, usecols=['translation', 'initial phoneme', 'case', 'plurality', 'definiteness'])
    # read input from csv file
    with open("test_data.csv") as f:
        test_df = pd.read_csv(f, usecols=['translation', 'initial phoneme', 'case', 'plurality', 'definiteness'])

    # separate training and test data according to training type
    new_data = separate_data(training_type, (train_df, test_df))
    
    return new_data

def input_word(new_nodes, full_dataset):
    """ This function chooses a random input word and changes the 
        activations on the input layer accordingly
        
        Parameters:
        ----------
        new_nodes: an array containing the node activations and biases 
        full_dataset: a dataframe with training data
        
        Returns:
        --------
        new_nodes: an array containing the new node activations (and unchanged biases)
        
    """
    # select a random word of the training set
    random_index = random.choice(full_dataset.index)
    random_word = full_dataset.loc[random_index]

    # select all aspects relevant to the model
    translation = random_word['translation']
    phoneme = random_word['initial phoneme']
    case = random_word['case']
    plurality = random_word['plurality']
    definiteness = random_word['definiteness']
    nodes = [translation, phoneme, case, plurality, definiteness]

    # dictionary of nodes that correspond to the input
    all_nodes = {"O":0, 'p':1, 'pʲ':2, 'b':3, 'bʲ':4, 'f':5, 'fʲ':6, 'v':7, 'vʲ':8, 'm':9, 'mʲ':10, 't':11, 'tʲ':12, 'd':13, 'dʲ':14, 's':15, 'sʲ':16, 'n':17, 'nʲ':18, 'l':19, 'lʲ':20, 'r':21, 'rʲ':22, 'k':23, 'kʲ':24, 'g':25, 'gʲ':26, 'x':27, 'xʲ':28, 'ɣ':29, 'ɣʲ':30, 'ŋ':31, 'ŋʲ':32, 'h':33, 'dog':34, 'deceiver':35, 'stud/boss':36, 'May (month)':37, 'child':38, 'petal':39, 'knot':40, 'bag':41, 'increase':42, 'beer':43, 'cow':44, 'job':45, 'pepper':46, 'window':47, 'deer':48, 'poem':49, 'channel in strand':50, 'fruit':51, 'language':52, 'fox':53, 'eye':54, 'cat':55, 'fog':56, 'book':57, 'mouse':58, 'star':59, 'seal':60, 'complaint':61, 'dress':62, 'newspaper':63, 'washer (person)':64, 'butterfly':65, 'student':66, 'god':67, 'tavern':68, 'country':69, 'November':70, 'shop':71, 'friend':72, 'license':73, 'hand':74, 'lighter':75, 'bicycle':76, 'spasm':77, 'calf':78, 'generator':79, 'tradition':80, 'nervous system':81, 'NOM':82, 'GEN':83, 'DAT':84, 'SG':85, 'PL':86, 'INDEF':87, 'DEF':88}

    # np array with new activation values
    changed_nodes = np.full((89,), -0.5)

    # loop over nodes to be changed
    for node in nodes:
        # select correct node and change activation
        node_nr = all_nodes[node]
        changed_nodes[node_nr] = 5.0

    # Set the new activitions for all layers
    new_nodes[0][0,:] = changed_nodes
    new_nodes[1][0,:] = 0.0
    new_nodes[2][0,:] = 0.0

    return new_nodes

def input_test_word(new_nodes, testing_dataset, comp_or_prod, step):
    """ This function chooses a test word and changes the 
        activations on the input layer accordingly
        
        Parameters:
        ----------
        new_nodes: an array containing the node activations and biases 
        testing_dataset: a dataframe with test data
        comp_or_prod: variable to check if production or comprehension is being tested
        step: the current step of the testing cycle
        
        Returns:
        --------
        new_nodes: an array containing the node activations and biases 
        nodes: the nodes that were activated
        expected_output: a list of what the network should produce
        
    """
    # select the current step's entry in the dataset
    random_word = testing_dataset.loc[step]

    # select all aspects relevant to the model
    translation = random_word['translation']
    phoneme = random_word['initial phoneme']
    case = random_word['case']
    plurality = random_word['plurality']
    definiteness = random_word['definiteness']

    # decide which aspects are activated and which are part of the expected output
    if comp_or_prod == "comp":
        nodes = [translation, phoneme]
        expected_output = [case, plurality, definiteness]
    elif comp_or_prod == "prod":
        nodes = [translation, case, plurality, definiteness]
        expected_output = [phoneme]

    # dictionary of nodes that correspond to the input
    all_nodes = {"O":0, 'p':1, 'pʲ':2, 'b':3, 'bʲ':4, 'f':5, 'fʲ':6, 'v':7, 'vʲ':8, 'm':9, 'mʲ':10, 
    't':11, 'tʲ':12, 'd':13, 'dʲ':14, 's':15, 'sʲ':16, 'n':17, 'nʲ':18, 'l':19, 'lʲ':20, 
    'r':21, 'rʲ':22, 'k':23, 'kʲ':24, 'g':25, 'gʲ':26, 'x':27, 'xʲ':28, 'ɣ':29, 'ɣʲ':30, 
    'ŋ':31, 'ŋʲ':32, 'h':33, 'dog':34, 'deceiver':35, 'stud/boss':36, 'May (month)':37, 'child':38, 'petal':39, 'knot':40, 
    'bag':41, 'increase':42, 'beer':43, 'cow':44, 'job':45, 'pepper':46, 'window':47, 'deer':48, 'poem':49, 'channel in strand':50, 
    'fruit':51, 'language':52, 'fox':53, 'eye':54, 'cat':55, 'fog':56, 'book':57, 'mouse':58, 'star':59, 'seal':60, 
    'complaint':61, 'dress':62, 'newspaper':63, 'washer (person)':64, 'butterfly':65, 'student':66, 'god':67, 'tavern':68, 'country':69, 'November':70, 
    'shop':71, 'friend':72, 'license':73, 'hand':74, 'lighter':75, 'bicycle':76, 'spasm':77, 'calf':78, 'generator':79, 'tradition':80, 
    'nervous system':81, 'NOM':82, 'GEN':83, 'DAT':84, 'SG':85, 'PL':86, 'INDEF':87, 'DEF':88}

    # np array with new activation values
    changed_nodes = np.full((89,), -0.5)

    # loop over nodes to be changed
    for node in nodes:
        # select correct node and change activation
        node_nr = all_nodes[node]
        changed_nodes[node_nr] = 5.0

    # Set the new activitions for all layers
    new_nodes[0][0,:] = changed_nodes
    new_nodes[1][0,:] = 0.0
    new_nodes[2][0,:] = 0.0

    return new_nodes, nodes, expected_output