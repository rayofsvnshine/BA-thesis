import random
import numpy as np
from math import pi, cos, sin

# For inputs that are at a set distance from prototype
def edge_input_echo(vowel_system, step):
    """ This function chooses an input sound from the category edge and changes 
        the activations on the input layer accordingly 
        
        Parameters:
        ----------
        vowel_system: a string of 'four' or 'five' (or +'_spec') that states 
            the used vowel system
        step: a integer containing the number of the current input   

        
        Returns:
        --------
        new_nodes: an array containing the node activations and biases 
        
    """
    erb = np.linspace(4,28,49)
    bumb_width = 0.68
    radius = 2

    if vowel_system == 'five':
        angle = 1.8 * (step % 200)
        
        if step <= 200: # 'a'
            f1 = sin(angle)*radius + 13
            f2 = cos(angle)*radius + 19
            proto_f1 = 13
            proto_f2 = 19
        if 200 < step <= 400: # 'e'
            f1 = sin(angle)*radius + 10
            f2 = cos(angle)*radius + 22
            proto_f1 = 10
            proto_f2 = 22
        if 400 < step <= 600: # 'i':
            f1 = sin(angle)*radius + 7
            f2 = cos(angle)*radius + 25
            proto_f1 = 7
            proto_f2 = 25
        if 600 < step <= 800: # 'o':
            f1 = sin(angle)*radius + 10
            f2 = cos(angle)*radius + 16
            proto_f1 = 10
            proto_f2 = 16
        if 800 < step <= 1000: # 'u':
            f1 = sin(angle)*radius + 7
            f2 = cos(angle)*radius + 13
            proto_f1 = 7
            proto_f2 = 13
        
    elif vowel_system == 'four':
        angle = 1.8 * (step % 250)
        if step <= 250: # 'a'
            f1 = sin(angle)*radius + 13
            f2 = cos(angle)*radius + 19
            proto_f1 = 13
            proto_f2 = 19
        if 250 < step <= 500: # 'ei'
            f1 = sin(angle)*radius + 8.5
            f2 = cos(angle)*radius + 23.5
            proto_f1 = 8.5
            proto_f2 = 23.5
        
        if 500 < step <= 750: # 'o':
            f1 = sin(angle)*radius + 10
            f2 = cos(angle)*radius + 16
            proto_f1 = 10
            proto_f2 = 16

        if 750 < step <= 1000: # 'u':
            f1 = sin(angle)*radius + 7
            f2 = cos(angle)*radius + 13
            proto_f1 = 7
            proto_f2 = 13

    # the following two inputs are only used in the distance tests and are random
    elif vowel_system == 'four_spec':
        angle = random.random() * 2 * pi
        f1 = sin(angle)*radius + 8.5
        f2 = cos(angle)*radius + 23.5
        proto_f1 = 8.5
        proto_f2 = 23.5
    elif vowel_system == 'five_spec':
        sounds = ['a', 'i']
        angle = random.random() * 2 * pi
        step_input = random.choice(sounds)
        if step_input == 'e':
            f1 = sin(angle)*radius + 10
            f2 = cos(angle)*radius + 22
            proto_f1 = 10
            proto_f2 = 22
        elif step_input == 'i':
            f1 = sin(angle)*radius + 7
            f2 = cos(angle)*radius + 25
            proto_f1 = 7
            proto_f2 = 25

    # calculate the activation of all nodes on the auditory layer
    activity = 5.0 * (np.exp(-(erb-f1)**2/(2*bumb_width**2)) + np.exp(-(erb-f2)**2/(2*bumb_width**2))) - 0.5
    
    # combine and return all needed variables
    f1f2_act = [f1,f2,activity, proto_f1, proto_f2]
    return f1f2_act


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
    erb = np.linspace(4,28,49)
    bumb_width = 0.68

    if vowel_system == 'five':
        sounds = ['a', 'e', 'i', 'o', 'u']
        step_input = random.choice(sounds)
    elif vowel_system == 'four':
        sounds = ['a', 'ei', 'o', 'u']
        step_input = random.choice(sounds)
    elif vowel_system == 'four_spec':
        sounds = ['ei']
        step_input = 'ei'
    elif vowel_system == 'five_spec':
        sounds = ['a', 'i']
        step_input = random.choice(sounds)

    if step_input == 'a':
        f1 = np.random.normal(13,0.9)
        f2 = np.random.normal(19,0.9)
        proto_f1 = 13
        proto_f2 = 19

    elif step_input == 'e':
        f1 = np.random.normal(10,0.9)
        f2 = np.random.normal(22,0.9)
        proto_f1 = 10
        proto_f2 = 22

    elif step_input == 'i':
        f1 = np.random.normal(7,0.9)
        f2 = np.random.normal(25,0.9)
        proto_f1 = 7
        proto_f2 = 25

    elif step_input == 'o':
        f1 = np.random.normal(10,0.9)
        f2 = np.random.normal(16,0.9)
        proto_f1 = 10
        proto_f2 = 16

    elif step_input == 'u':
        f1 = np.random.normal(7,0.9)
        f2 = np.random.normal(13,0.9)
        proto_f1 = 7
        proto_f2 = 13

    activity = 5.0 * (np.exp(-(erb-f1)**2/(2*bumb_width**2)) + np.exp(-(erb-f2)**2/(2*bumb_width**2))) - 0.5
    f1f2_act = [f1,f2,activity, proto_f1, proto_f2]

    return f1f2_act

