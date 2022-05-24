def separate_data(training_type, new_data):
    """ This function separates the test data from the training data, returning a new tuple with correctly sorted test and training data
        
        Parameters:
        ----------
        training_type: the type of training that determines the test/training data split
        new_data: two dataframes containing the pure training data and the data to be split into test/training
        
        Returns:
        --------
        tuple of newly assigned training and test data
        
    """

    # if full dataset is used, make both training and test data the combination of all datapoints
    if training_type == 'full':
        training_data = new_data[0]
        test_data = new_data[1]
        training_data = training_data.append(test_data, ignore_index=True)
        test_data = training_data
    # only select nominative forms for training, use non-nominative forms for testing
    elif training_type == 'case':
        training_data = new_data[0]
        test_data = new_data[1]
        nom_train = test_data[test_data['case'] == 'NOM']
        test_data = test_data[test_data['case'] != 'NOM']
        training_data = training_data.append(nom_train, ignore_index=True)
    # only select definite forms for training, use indefinite forms for testing
    elif training_type == 'det':
        training_data = new_data[0]
        test_data = new_data[1]
        def_train = test_data[test_data['case'] == 'DEF']
        test_data = test_data[test_data['case'] != 'DEF']
        training_data = training_data.append(def_train, ignore_index=True)
    # only use singular forms for training, use plural forms for testing
    elif training_type == 'plur':
        training_data = new_data[0]
        test_data = new_data[1]
        plur_train = test_data[test_data['case'] == 'SG']
        test_data = test_data[test_data['case'] != 'SG']
        training_data = training_data.append(plur_train, ignore_index=True)

    # returns the training and test data
    return (training_data, test_data)