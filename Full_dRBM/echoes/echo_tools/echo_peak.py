from scipy.signal import find_peaks
from scipy import interpolate
import numpy as np

def echo_peaks(erb, new_nodes):
    """ This function finds the two highest activations in the ERB layer.
    
    Parameters:
    ---------- 
    erb: 
    new_nodes: an array containing the node activations and biases 

    Returns:
    --------
    echo_f1f2: a list containing the two highest activaded erb values 
    """
    # Interpolate the heights to get more refined peaks
    f = interpolate.interp1d(erb, new_nodes[0][0,:], kind='cubic')
    new_erb = np.linspace(4,28,490)
    new_heights = f(new_erb)

    # get all local maxima
    local_maxima_ind = find_peaks(new_heights, height=-4)
    # create lists for height values and erb index
    heights = local_maxima_ind[1]['peak_heights']
    indexes = local_maxima_ind[0]
    
    # sort both lists to get two maxima heights and erb at the end of the list
    zipped = zip(heights, indexes)
    sorted_pairs = sorted(zipped)
    tuples = zip(*sorted_pairs)
    act_height, index_erb = [ list(tuple) for tuple in  tuples]
    
    # get two highest peaks and sort by index
    highest_acts = [index_erb[-1], index_erb[-2]]
    highest_acts = sorted(highest_acts)
    # get erb values for two highest maxima
    echo_f1 = new_erb[highest_acts[0]]
    echo_f2 = new_erb[highest_acts[1]]

    echo_f1f2 = [echo_f1, echo_f2]

    return echo_f1f2