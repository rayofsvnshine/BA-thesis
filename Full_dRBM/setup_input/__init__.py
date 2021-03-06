""" (short description) Collection of the network setup tools!

(long description)  This collection contains the creation of the network via: nodes_connections
    It also contains the code to get the activations on the erb layer for each input sound
"""
from .initialize_network_data import setup_network, copy_network
from .irish_input import setup_data, phoneme_data, input_word, input_test_word, input_phoneme
from .separate_data import separate_data