"""
Analyses results and outputs them into a new csv.
Covers both production and comprehension results.
"""

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
import numpy as np
from math import sqrt

def main():
    
    test_types = ['full', 'case_nom', 'case_gen', 'case_dat', 'def', 'indef', 'plur', 'sing']
    # iterate over all test types
    for test_type in test_types:

        # create a dataframe for the production results
        results = pd.DataFrame()
        
        # iterate over the results of all learners
        for i in range(100):
            # load production test results into Dataframe
            with open(f"../results/{test_type}/prod/test_{test_type}_prod_{i}.csv") as f:
                prod_results = pd.read_csv(f, usecols=['Expected Output', 'Actual Output'], index_col=False)

            # edit strings to allow comparison
            prod_results['Expected Output'] = prod_results['Expected Output'].str.replace(r'[\[\]\' ]','', regex=True)
            prod_results['Actual Output'] = prod_results['Actual Output'].str.replace(r'(?:\[\')', '', regex=True)
            prod_results['Actual Output'] = prod_results['Actual Output'].str.replace(r'(?:\').{1,}', '', regex=True)

            # calculate how many results were (in)correct
            prod_results['compare'] = np.where((prod_results['Actual Output'] == prod_results['Expected Output']), 0.5, -0.5)
            # group results by expected & actual output phoneme
            temp_df = prod_results.groupby(['Expected Output','Actual Output', 'compare']).size().reset_index()
            # append results to DF
            results = results.append(temp_df, ignore_index=True)

        # group total results and calculate percentages
        final_results = results.groupby(['Expected Output','Actual Output']).sum(['0'])
        final_results = final_results / final_results.groupby(['Expected Output']).sum(['0'])
        final_results = final_results * 100
        final_results = final_results.reset_index(level=['Expected Output','Actual Output'])

        # save results to csv
        final_results.to_csv(f'../results/fully_processed/test_{test_type}_prod_results.csv', ',')


        # create dataframes for all morphosyntactic results
        case_results = pd.DataFrame()
        plur_results = pd.DataFrame()
        def_results = pd.DataFrame()

        # iterate over the comprehension results of all 100 learners
        for i in range(100):
            # load comprehension test results into Dataframe
            with open(f'../results/{test_type}/comp/test_{test_type}_comp_{i}.csv') as f:
                comp_results = pd.read_csv(f, usecols=['Expected Output', 'Actual Output'])

            # edit strings to allow comparison
            comp_results['Expected Output'] = comp_results['Expected Output'].str.replace(r'[^A-Z,]','', regex=True)
            comp_results['Actual Output'] = comp_results['Actual Output'].str.replace(r'[^\w,]', '', regex=True)
            
            # split "expected output" columns by case/plurality/definiteness
            comp_results[['Exp. Out. Case', 'Exp. Out. Plur', 'Exp. Out. Def']] = comp_results['Expected Output'].str.split(',', expand=True).dropna(axis=1)

            # split "actual output" columns by case/plurality/definiteness
            comp_results[['Act. Out. Phon', 'Act. Out. Lex','Act. Out. Case', 'Act. Out. Plur', 'Act. Out. Def']] = comp_results['Actual Output'].str.split(',', expand=True).dropna(axis=1)

            # drop duplicated columns
            comp_results.drop(['Expected Output', 'Actual Output'], axis=1, inplace=True)
            
            for morphosyntax in ['Case', 'Plur', 'Def']:
                # group results
                temp_df = comp_results.groupby(['Act. Out. Lex', 'Act. Out. Phon', f'Act. Out. {morphosyntax}', f'Exp. Out. {morphosyntax}']).size()
                temp_df = temp_df.reset_index()

                # append results to correct DF
                if morphosyntax == 'Case':
                    case_results = case_results.append(temp_df, ignore_index=True)
                elif morphosyntax == 'Plur':
                    plur_results = plur_results.append(temp_df, ignore_index=True)
                elif morphosyntax == 'Def':
                    def_results = def_results.append(temp_df, ignore_index=True)
            
        # group results by word, phoneme, and actual/expected output
        case_results = case_results.groupby(['Act. Out. Lex', 'Act. Out. Phon','Exp. Out. Case', 'Act. Out. Case']).sum()
        plur_results = plur_results.groupby(['Act. Out. Lex', 'Act. Out. Phon','Exp. Out. Plur', 'Act. Out. Plur']).sum()
        def_results = def_results.groupby(['Act. Out. Lex', 'Act. Out. Phon','Exp. Out. Def', 'Act. Out. Def']).sum()
        # create new column and initialize to 0, put index in columns again
        case_results = case_results.reset_index()
        plur_results = plur_results.reset_index()
        def_results = def_results.reset_index()
        case_results['corr'] = 0
        plur_results['corr'] = 0
        def_results['corr'] = 0
        # calculate correctness
        case_results['corr'] = case_results.apply(lambda row: corr_count(row, case_results, 'Case'), axis=1)
        plur_results['corr'] = plur_results.apply(lambda row: corr_count(row, plur_results, 'Plur'), axis=1)
        def_results['corr'] = def_results.apply(lambda row: corr_count(row, def_results, 'Def'), axis=1)
        # groups all output by expected values and stores nr of correctly produced values
        case_results = case_results.groupby(['Exp. Out. Case']).sum(['corr']).reset_index()
        plur_results = plur_results.groupby(['Exp. Out. Plur']).sum(['corr']).reset_index()
        def_results = def_results.groupby(['Exp. Out. Def']).sum(['corr']).reset_index()
        # calculate percentages
        case_results['%'] = (case_results['corr'] / case_results[0]) * 100
        plur_results['%'] = (plur_results['corr'] / plur_results[0]) * 100
        def_results['%'] = (def_results['corr'] / def_results[0]) * 100
        # calculate stdev
        case_results['stdev'] = case_results.apply(lambda row: stdev_calc(row), axis=1)
        plur_results['stdev'] = plur_results.apply(lambda row: stdev_calc(row), axis=1)
        def_results['stdev'] = def_results.apply(lambda row: stdev_calc(row), axis=1)
        # save results to csv
        case_results.to_csv(f'../results/fully_processed/new_test_{test_type}_comp_case_results.csv', ',')
        plur_results.to_csv(f'../results/fully_processed/new_test_{test_type}_comp_plur_results.csv', ',')
        def_results.to_csv(f'../results/fully_processed/new_test_{test_type}_comp_def_results.csv', ',')


def corr_count(row, df, morphsynt):
    """calculates correctness of a row"""
    # select row from df to compare total count with output
    temp_df = df.groupby(['Act. Out. Lex', 'Act. Out. Phon', f'Exp. Out. {morphsynt}']).sum(['0'])
    temp_df = temp_df.reset_index()
    check_row = temp_df.loc[(temp_df['Act. Out. Lex'] == row['Act. Out. Lex']) & (temp_df['Act. Out. Phon'] == row['Act. Out. Phon']) & (temp_df[f'Exp. Out. {morphsynt}'] == row[f'Exp. Out. {morphsynt}'])]

    # in case there is no row, check_value is 0
    if check_row.empty == False:
        check_row = check_row.iloc[0]
        check_value = check_row[[0]].values[0]
    else:
        check_value = 0

    # checks expected vs actual output, assigns correctness to these values
    correctness = 0
    if row[[f'Act. Out. {morphsynt}']].values == row[[f'Exp. Out. {morphsynt}']].values:
        if row[[0]].values[0] > check_value:
            correctness = check_value
        elif check_value > row[[0]].values[0]:
            correctness = row[[0]].values[0]
        elif check_value == row[[0]].values[0]:
            correctness = row[[0]].values[0]
    
    return correctness

def stdev_calc(row):
    """ calculates the stdev of a row"""
    # number of positive/negative/total datapoints
    pos = row[['corr']].values[0]
    neg = row[[0]].values[0] - pos
    tot = row[[0]].values[0]
    # calculate success and error rate
    pos = pos / tot
    neg = neg / tot
    # calculate the standard deviation
    stdev = sqrt(tot*pos*neg)

    return stdev


if __name__ == "__main__":
    main()