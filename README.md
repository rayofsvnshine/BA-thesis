# Can an AI learn Irish?
## The emergence of phonological features in Irish initial mutations
A GitHub repository for all the code used in my thesis for the BA Linguistics, as found
on the IFA Archive: https://www.fon.hum.uva.nl/archive/

## Directories:
- /graphs: code for the graphing of the visualisations
- /learning_phases: contains the phases and calculations to complete a single training step
- /learning_phases/phases: the individual phases for a single learning step
- /pdfs: all images produced by the graphing code are stored here
- /results: stores all results in a directory corresponding to the training-type (in .csv format)
- /setup_input: sets up network, training & test data, and regulates the initial activation of the input layer based on the data
- /test_functions: contains all functions needed for testing and analysis of the test results

## Files:
- input_data.csv: contains data for training
- test_data.csv: contains data for both training & testing (is split depending on the training-type)
- phonemes_only.csv: contains all initial phonemes used in the data
- show_dRBM_network.py: trains a network and saves an image of its trained state
- train_full.py: trains a network on data and tests production and comprehension (training-type determines input/test data)
- phoneme_matrix.py: trains a network on the full data and creates a cosine similarity matrix