import pandas as pd
import numpy as np


def main():
    # load production test results into Dataframe
    print("10.000")
    with open("../results/test_full_prod.csv") as f:
        prod_results = pd.read_csv(f, usecols=['Expected Output', 'Actual Output'])

    # edit strings to allow comparison
    prod_results['Expected Output'] = prod_results['Expected Output'].str.replace(r'[\[\]\' ]','', regex=True)
    prod_results['Actual Output'] = prod_results['Actual Output'].str.replace(r'(?:\[\')', '', regex=True)
    prod_results['Actual Output'] = prod_results['Actual Output'].str.replace(r'(?:\').{1,}', '', regex=True)

    # calculate how many results were (in)correct
    prod_results['compare'] = np.where((prod_results['Actual Output'] == prod_results['Expected Output']), 1, 0)
    print("Results production:")
    print(prod_results.value_counts(prod_results['compare']))
    save_df = prod_results[prod_results['compare'] == 0]
    save_df = save_df.sort_values(by=['Expected Output'])
    save_df = save_df.groupby(['Expected Output']).size()
    print(save_df)
    # print_df = prod_results.sort_values(by=['Expected Output'])
    # print_df = print_df.groupby(['Expected Output']).size()
    # print(print_df)
    # save_df.to_csv('../results/test_full_prod_incorrect.csv', ',', index=False)

    # # load comprehension test results into Dataframe
    # with open("../results/test_full_comp.csv") as f:
    #     comp_results = pd.read_csv(f, usecols=['Expected Output', 'Actual Output'])

    # # edit strings to allow comparison
    # comp_results['Expected Output'] = comp_results['Expected Output'].str.replace(r'[^A-Z,]','', regex=True)
    # comp_results['Actual Output'] = comp_results['Actual Output'].str.replace(r'[^A-Z,]', '', regex=True)
    # comp_results['Actual Output'] = comp_results['Actual Output'].str.replace(r'^,,', '', regex=True)

    # case_results = comp_results.replace(r',[A-Z]{2},[A-Z]+$', '', regex=True)
    # pl_results = comp_results.replace(r'^[A-Z]{3},', '', regex=True)
    # pl_results = pl_results.replace(r',[A-Z]+$', '', regex=True)
    # def_results = comp_results.replace(r'^[A-Z]{3},[A-Z]{2},', '', regex=True)
    
    # case_results['compare'] = np.where((case_results['Actual Output'] == case_results['Expected Output']), 1, 0)
    # print("Results case:")
    # print(case_results.value_counts(case_results['compare']))
    # pl_results['compare'] = np.where((pl_results['Actual Output'] == pl_results['Expected Output']), 1, 0)
    # print("Results plurality:")
    # print(pl_results.value_counts(pl_results['compare']))
    # def_results['compare'] = np.where((def_results['Actual Output'] == def_results['Expected Output']), 1, 0)
    # print("Results definiteness:")
    # print(def_results.value_counts(def_results['compare']))

if __name__ == "__main__":
    main()