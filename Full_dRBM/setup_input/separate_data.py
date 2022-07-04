def separate_data(training_type, new_data):
    """ This function separates the test data from the training data,
        returning a new tuple with correctly sorted test and training data
        
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
    # only select non-nominative forms for training, use nominative forms for testing
    elif training_type == 'case_nom':
        training_data = new_data[0]
        test_data = new_data[1]
        nom_train = test_data[test_data['case'] != 'NOM']
        test_data = test_data[test_data['case'] == 'NOM']
        test_data = test_data.reset_index()
        training_data = training_data.append(nom_train, ignore_index=True)
    # only select non-genitive forms for training, use genitive forms for testing
    elif training_type == 'case_gen':
        training_data = new_data[0]
        test_data = new_data[1]
        gen_train = test_data[test_data['case'] != 'GEN']
        test_data = test_data[test_data['case'] == 'GEN']
        test_data = test_data.reset_index()
        training_data = training_data.append(gen_train, ignore_index=True)
    # only select non-dative forms for training, use dative forms for testing
    elif training_type == 'case_dat':
        training_data = new_data[0]
        test_data = new_data[1]
        dat_train = test_data[test_data['case'] != 'DAT']
        test_data = test_data[test_data['case'] == 'DAT']
        test_data = test_data.reset_index()
        training_data = training_data.append(dat_train, ignore_index=True)
    # only select indefinite forms for training, use definite forms for testing
    elif training_type == 'def':
        training_data = new_data[0]
        test_data = new_data[1]
        def_train = test_data[test_data['definiteness'] != 'DEF']
        test_data = test_data[test_data['definiteness'] == 'DEF']
        test_data = test_data.reset_index()
        training_data = training_data.append(def_train, ignore_index=True)
    # only select definite forms for training, use indefinite forms for testing
    elif training_type == 'indef':
        training_data = new_data[0]
        test_data = new_data[1]
        indef_train = test_data[test_data['definiteness'] != 'INDEF']
        test_data = test_data[test_data['definiteness'] == 'INDEF']
        test_data = test_data.reset_index()
        training_data = training_data.append(indef_train, ignore_index=True)
    # only use singular forms for training, use plural forms for testing
    elif training_type == 'plur':
        training_data = new_data[0]
        test_data = new_data[1]
        plur_train = test_data[test_data['plurality'] != 'PL']
        test_data = test_data[test_data['plurality'] == 'PL']
        test_data = test_data.reset_index()
        training_data = training_data.append(plur_train, ignore_index=True)
    # only use plural forms for training, use singular forms for testing
    elif training_type == 'sing':
        training_data = new_data[0]
        test_data = new_data[1]
        sing_train = test_data[test_data['plurality'] != 'SG']
        test_data = test_data[test_data['plurality'] == 'SG']
        test_data = test_data.reset_index()
        training_data = training_data.append(sing_train, ignore_index=True)

    # returns the training and test data
    return (training_data, test_data)