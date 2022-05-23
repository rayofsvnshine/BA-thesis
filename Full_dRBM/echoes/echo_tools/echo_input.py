import random
import numpy as np
from math import pi, cos, sin


def random_input_echo(vowel_system):
    """ This function chooses an random input sound and changes the activations 
            on the input layer accordingly
        
        Parameters:
        ----------
        new_nodes: an array containing the node activations and biases 
        vowel_system: a string of 'four' or 'five' that states the used vowel
            system
        
        Returns:
        --------
        new_nodes: an array containing the node activations and biases 
        
    """
    erb = np.linspace(4,28,65)
    
    f1 = 0
    f2 = 0
    activity = erb
    proto_f1 = 0
    proto_f2 = 0
    
    f1f2_act = [f1,f2,activity, proto_f1, proto_f2]

    return f1f2_act

