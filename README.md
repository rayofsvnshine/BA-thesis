# BA-thesis
A GitHub repository for all the code used in my thesis for the BA Linguistics.

## Directories:
- /graphs: code for the graphing of the visualisations
- /learning_phases: contains the phases and calculations to complete a single training step
- /pdfs: all images produced by the graphing code are stored here
- /results: stores all results (in .csv format)
- /setup_input: sets up network, training & test data, and regulates the initial activation of the input layer based on the data
- /test_functions: contains all functions needed for testing

## Files:
- input_data.csv: contains data for training
- test_data.csv: contains data for both training & testing
- dRBM_network.py: trains a network and saves an image of its trained state
- train_full.py: trains a network on all data and tests either production or comprehension (no unseen data)