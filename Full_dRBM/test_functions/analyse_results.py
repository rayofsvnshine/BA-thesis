import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import pandas as pd
# import numpy as np

# total_results = {'O':0, 'p':0, 'pʲ':0, 'b':0, 'bʲ':0, 'f':0, 'fʲ':0, 'v':0, 'vʲ':0, 'm':0, 'mʲ':0, 
# 't':0, 'tʲ':0, 'd':0, 'dʲ':0, 's':0, 'sʲ':0, 'n':0, 'nʲ':0, 'l':0, 'lʲ':0, 
# 'r':0, 'rʲ':0, 'k':0, 'kʲ':0, 'g':0, 'gʲ':0, 'x':0, 'xʲ':0, 'ɣ':0, 'ɣʲ':0, 
# 'ŋ':0, 'ŋʲ':0, 'h':0}
# phonemes = ['O', 'p', 'pʲ', 'b', 'bʲ', 'f', 'fʲ', 'v', 'vʲ', 'm', 'mʲ', 
# 't', 'tʲ', 'd', 'dʲ', 's', 'sʲ', 'n', 'nʲ', 'l', 'lʲ', 
# 'r', 'rʲ', 'k', 'kʲ', 'g', 'gʲ', 'x', 'xʲ', 'ɣ', 'ɣʲ', 
# 'ŋ', 'ŋʲ', 'h']

def main():
    
    # results = pd.DataFrame()
    
    # for i in range(100):
    #     # load production test results into Dataframe
    #     with open(f"../results/case_nom/prod/test_case_nom_prod_{i}.csv") as f:
    #         prod_results = pd.read_csv(f, usecols=['Expected Output', 'Actual Output'], index_col=False)

    #     # edit strings to allow comparison
    #     prod_results['Expected Output'] = prod_results['Expected Output'].str.replace(r'[\[\]\' ]','', regex=True)
    #     prod_results['Actual Output'] = prod_results['Actual Output'].str.replace(r'(?:\[\')', '', regex=True)
    #     prod_results['Actual Output'] = prod_results['Actual Output'].str.replace(r'(?:\').{1,}', '', regex=True)

    #     # calculate how many results were (in)correct
    #     # prod_results['compare'] = np.where((prod_results['Actual Output'] == prod_results['Expected Output']), 1, 0)
    #     # group results by expected & actual output phoneme
    #     temp_df = prod_results.groupby(['Expected Output','Actual Output']).size().reset_index()
    #     # append results to DF
    #     results = results.append(temp_df, ignore_index=True)

    # # group total results
    # results = results.groupby(['Expected Output','Actual Output']).sum(['0'])
    # # save results to csv
    # results.to_csv('../results/processed/test_case_nom_prod_results.csv', ',')


    case_results = pd.DataFrame()
    plur_results = pd.DataFrame()
    def_results = pd.DataFrame()

    for i in range(100):
        # load comprehension test results into Dataframe
        with open(f'../results/case_nom/comp/test_case_nom_comp_{i}.csv') as f:
            comp_results = pd.read_csv(f, usecols=['Expected Output', 'Actual Output'])

        # test 2
        # edit strings to allow comparison
        # comp_results['Expected Output'] = comp_results['Expected Output'].str.replace(r'[^A-Z,]','', regex=True)
        # comp_results['Actual Output'] = comp_results['Actual Output'].str.replace(r'[^\w,]', '', regex=True)

        # test 1
        # edit strings to allow comparison
        comp_results['Expected Output'] = comp_results['Expected Output'].str.replace(r'[^A-Z,]','', regex=True)
        comp_results['Actual Output'] = comp_results['Actual Output'].str.replace(r'[^A-Z,]', '', regex=True)
        comp_results['Actual Output'] = comp_results['Actual Output'].str.replace(r',N,|,M,|O,,', '', regex=True)
        comp_results['Actual Output'] = comp_results['Actual Output'].str.replace(r'^,,', '', regex=True)
        
        # split columns by case/plurality/definiteness
        comp_results[['Exp. Out. Case', 'Exp. Out. Plur', 'Exp. Out. Def']] = comp_results['Expected Output'].str.split(',', expand=True).dropna(axis=1)

        comp_results[['Act. Out. Case', 'Act. Out. Plur', 'Act. Out. Def']] = comp_results['Actual Output'].str.split(',', expand=True).dropna(axis=1) # test 1
        # comp_results[['Act. Out. Phon', 'Act. Out. Lex','Act. Out. Case', 'Act. Out. Plur', 'Act. Out. Def']] = comp_results['Actual Output'].str.split(',', expand=True).dropna(axis=1) # test 2

        # drop duplicated columns
        comp_results.drop(['Expected Output', 'Actual Output'], axis=1, inplace=True)
        
        
        for morphosyntax in ['Case', 'Plur', 'Def']:
            # test 1
            # calculate how many cases were (in)correct
            temp_df = comp_results[[f'Exp. Out. {morphosyntax}',f'Act. Out. {morphosyntax}']]
            # group results by expected & actual output case
            temp_df = temp_df.groupby([f'Exp. Out. {morphosyntax}',f'Act. Out. {morphosyntax}']).size().reset_index()

            # test 2
            # # group results by lexeme/phoneme and morphosyntactic feature
            # temp_df = comp_results.groupby(['Act. Out. Lex', 'Act. Out. Phon', f'Act. Out. {morphosyntax}']).size().reset_index()

            # append results to correct DF
            if morphosyntax == 'Case':
                case_results = case_results.append(temp_df, ignore_index=True)
            elif morphosyntax == 'Plur':
                plur_results = plur_results.append(temp_df, ignore_index=True)
            elif morphosyntax == 'Def':
                def_results = def_results.append(temp_df, ignore_index=True)
        
    # test 1
    # group total case results
    case_results = case_results.groupby(['Exp. Out. Case','Act. Out. Case']).sum(['0'])
    # save results to csv
    case_results.to_csv('../results/processed/test_case_nom_comp_case_results.csv', ',')
    # group total plurality results
    plur_results = plur_results.groupby(['Exp. Out. Plur','Act. Out. Plur']).sum(['0'])
    # save results to csv
    plur_results.to_csv('../results/processed/test_case_nom_comp_plur_results.csv', ',')
    # group total definiteness results
    def_results = def_results.groupby(['Exp. Out. Def','Act. Out. Def']).sum(['0'])
    # save results to csv
    def_results.to_csv('../results/processed/test_case_nom_comp_def_results.csv', ',')


    # test 2
    # # group total case results
    # case_results = case_results.groupby(['Act. Out. Lex', 'Act. Out. Phon','Act. Out. Case']).sum(['0'])
    # # save results to csv
    # case_results.to_csv('../results/processed/test_case_nom_comp_phon_case_results.csv', ',')
    # # group total plurality results
    # plur_results = plur_results.groupby(['Act. Out. Lex', 'Act. Out. Phon','Act. Out. Plur']).sum(['0'])
    # # save results to csv
    # plur_results.to_csv('../results/processed/test_case_nom_comp_phon_plur_results.csv', ',')
    # # group total definiteness results
    # def_results = def_results.groupby(['Act. Out. Lex', 'Act. Out. Phon','Act. Out. Def']).sum(['0'])
    # # save results to csv
    # def_results.to_csv('../results/processed/test_case_nom_comp_phon_def_results.csv', ',')


if __name__ == "__main__":
    main()