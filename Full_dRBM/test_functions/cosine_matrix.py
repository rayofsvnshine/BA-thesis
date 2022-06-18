import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def main():
    # load test results into Dataframe
    with open("../results/phoneme_activation.csv") as f:
        phon_results = pd.read_csv(f)

    # edit dataframe to allow conversion of string to numbers
    phon_results['Activation levels'] = phon_results['Activation levels'].str.replace(r'\s+',',', regex=True)
    phon_results['Activation levels'] = phon_results['Activation levels'].str.replace(r'[\[\]]','', regex=True)

    # create an empty array for storing the activation levels
    phonemes = np.empty((34,70))

    for i in range(34):
        phonemes[i] = np.fromstring(phon_results['Activation levels'].iloc[i], sep=',')
    
    # calculate cosine similarity and round to 15 decimals
    sim_mat = cosine_similarity(phonemes, phonemes)
    sim_mat = np.round(sim_mat, 15)

    # turn results into a dataframe
    out_df = pd.DataFrame(sim_mat,columns= phon_results['Phoneme'].values, index= phon_results['Phoneme'].values)
    # store results
    out_df.to_csv('../results/cosine_matrix.csv',',')



if __name__ == "__main__":
    main()