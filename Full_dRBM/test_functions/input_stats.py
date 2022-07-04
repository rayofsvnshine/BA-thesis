import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd


def main():
    with open("../test_data.csv") as f:
        input_df = pd.read_csv(f, index_col=False)

    input_df = input_df[input_df['case'] == 'NOM']
    input_df = input_df[input_df['definiteness'] == 'INDEF']
    input_df = input_df.groupby(['initial phoneme', 'process']).size() # for phoneme data
    # input_df = input_df.groupby(['case', 'process']).size() # for morphosyntactic data

    print(input_df)


if __name__ == "__main__":
    main()