# ignores FutureWarning
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd


def main():
    # read input from csv file
    with open("../input_data.csv") as f:
        train_df = pd.read_csv(f, usecols=['translation', 'initial phoneme', 'case', 'plurality', 'definiteness'])
    # read input from csv file
    with open("../test_data.csv") as f:
        test_df = pd.read_csv(f, usecols=['translation', 'initial phoneme', 'case', 'plurality', 'definiteness'])

    # separate training and test data according to training type
    full_data_df = train_df.append(test_df, ignore_index=True)

    full_data_df = full_data_df.groupby(['translation', 'initial phoneme', 'definiteness']).size()
    # print(full_data_df)
    full_data_df.to_csv("../results/processed/input_analysis_def.csv")

if __name__ == "__main__":
    main()