import pandas as pd


def main():

    for morph, data_sort, file_dir in [('Case', 'case', 'case'),('Def', 'definiteness', 'def'),('Plur', 'plurality', 'plur')]:
        # open input data file
        with open(f'../results/processed/input_analysis_{file_dir}.csv') as f:
            comp_input = pd.read_csv(f)
        print(comp_input)
        # select relevant data from csv
        comp_input = comp_input[comp_input[data_sort] == 'NOM'].reset_index(drop=True)
        print(comp_input)
        # remove non-letters from translation to make input same to output
        comp_input['translation'] = comp_input['translation'].str.replace(r'[^\w,]', '', regex=True)
        # rename columns
        comp_input.columns = ['Act. Out. Lex', 'Act. Out. Phon', f'Act. Out. {morph}','0']
        # multiply numbers by 100 for nr of learners
        comp_input['0'] = comp_input['0'].multiply(-50)

        with open(f'../results/processed/test_case_nom_comp_phon_{file_dir}_results.csv') as f:
            comp_output = pd.read_csv(f)

        comparison = pd.DataFrame()
        comparison = comp_output.merge(comp_input, indicator = True, how = 'outer')
        # comparison = comparison.groupby(['Act. Out. Lex', 'Act. Out. Phon', f'Act. Out. {morph}']).sum(['0'])
        comparison = comparison.groupby([f'Act. Out. {morph}']).sum(['0'])

        # file_name = f'../results/processed/input_vs_output_comp_case_nom_{file_dir}.csv'
        # comparison.to_csv(file_name, ',')

if __name__ == "__main__":
    main()