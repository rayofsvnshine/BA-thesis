"""
Iterates over all results of the cosine similarity testing.
Saves similarity matrix of each results file, then calculates
the mean and standard deviation over all of them.
"""

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def main():
    # list for phoneme matrices
    avg_phonemes = []

    for i in range(100):
        # load test results into Dataframe
        with open(f"../results/cos_matrix/test_phon_{i}.csv") as f:
            phon_results = pd.read_csv(f)

        # edit dataframe to allow conversion of string to numbers
        phon_results['Activation levels'] = phon_results['Activation levels'].str.replace(r'\s+',',', regex=True)
        phon_results['Activation levels'] = phon_results['Activation levels'].str.replace(r'[\[\]]','', regex=True)

        # create empty arrays for storing the activation levels and cosine matrix
        phonemes = np.empty((34,70))
        phonemes = np.float64(phonemes)
        cos_mat = np.empty((34,34))
        cos_mat = np.float64(cos_mat)

        # iterate over phonemes and store activation levels
        for i in range(34):
            phonemes[i] = np.fromstring(phon_results['Activation levels'].iloc[i], sep=',')

        # store cosine similarity matrix in list
        phonemes = np.round(phonemes, 15)
        cos_mat = cosine_similarity(phonemes)
        avg_phonemes.append(cos_mat)


    # calculate mean of cosine similarity matrices
    out_array = np.mean(np.array([i for i in avg_phonemes]), axis=0)
    # calculate standard deviation of cosine similarity matrices
    std_array = np.std(np.array([i for i in avg_phonemes]), axis=0)
    # round arrays to 6 decimals
    out_array = np.round(out_array, 6)
    std_array = np.round(std_array, 6)
    # times 100 to get percentages
    out_array = out_array * 100
    std_array = std_array * 100

    # turn results into a dataframe
    out_df = pd.DataFrame(out_array,columns= phon_results['Phoneme'].values, index= phon_results['Phoneme'].values)
    std_df = pd.DataFrame(std_array,columns= phon_results['Phoneme'].values, index= phon_results['Phoneme'].values)
    # store results
    out_df.to_csv('../results/fully_processed/cosine_matrix.csv',',')
    std_df.to_csv('../results/fully_processed/cosine_matrix_stdev.csv',',')



if __name__ == "__main__":
    main()