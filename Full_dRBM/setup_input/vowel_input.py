import random
import numpy as np

def input_vowels(new_nodes, vowel_system):
    """ This function chooses a random input sound and changes the 
        activations on the input layer accordingly
        
        Parameters:
        ----------
        new_nodes: an array containing the node activations and biases 
        vowel_system: a string stating the needed amount of vowels
        
        Returns:
        --------
        new_nodes: an array containing the node activations and biases 
        
    """
    # Set up parameters
    erb = np.linspace(4,28,49)
    bump_width = 0.68

    # Choose vowel system and pick a random sound from the inventory
    if vowel_system == 'five':
        sounds = ['a', 'e', 'i', 'o', 'u']
    else:
        sounds = ['a', 'ei', 'o', 'u']
    step_input = random.choice(sounds)

    # Find the formant values dependent on the picked vowel
    if step_input == 'a':
        f1 = np.random.normal(13,1)
        f2 = np.random.normal(19,1)
    elif step_input == 'e':
        f1 = np.random.normal(10,1)
        f2 = np.random.normal(22,1)
    elif step_input == 'ei':
        f1 = np.random.normal(8.5,1)
        f2 = np.random.normal(23.5,1)
    elif step_input == 'i':
        f1 = np.random.normal(7,1)
        f2 = np.random.normal(25,1)
    elif step_input == 'o':
        f1 = np.random.normal(10,1)
        f2 = np.random.normal(16,1)
    elif step_input == 'u':
        f1 = np.random.normal(7,1)
        f2 = np.random.normal(13,1)

    # Calculate the activities of the node on the auditory layer
    activity = 5.0 * (np.exp(-(erb-f1)**2/(2*bump_width**2)) + np.exp(-(erb-f2)**2/(2*bump_width**2))) - 0.5
    
    # Set the new activitions for all layers (input decides erb, rest is 0.5)
    new_nodes[0][0,:] = activity
    new_nodes[1][0,:] = 0.0
    new_nodes[2][0,:] = 0.0

    return new_nodes