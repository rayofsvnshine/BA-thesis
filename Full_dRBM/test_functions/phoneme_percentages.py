import pandas as pd

# load production results into Dataframe
with open(f'../results/processed/test_case_nom_prod_results.csv') as f:
    comp_results = pd.read_csv(f)

correct = comp_results[comp_results['Expected Output'] == comp_results['Actual Output']]
correct.drop(['Actual Output'], axis=1, inplace=True)
correct = correct.reset_index(drop=True)
totals = comp_results.groupby(['Expected Output']).sum(['0'])
totals.reset_index(inplace=True)
totals['Percentage'] = correct['0'].divide(totals['0'])
totals['Percentage'] = totals['Percentage'].multiply(100)
print(totals)