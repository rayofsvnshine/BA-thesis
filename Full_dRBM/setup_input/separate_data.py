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

    if training_type == 'full':
        return new_data
    elif training_type == 'case':
        training_data = new_data[0]
        test_data = new_data[1]
        nom_train = test_data[test_data['case'] == 'NOM']
        test_data = test_data[test_data['case'] != 'NOM']
        training_data = training_data.append(nom_train, ignore_index=True)

        return (training_data, test_data)
    elif training_type == 'det':
        training_data = new_data[0]
        test_data = new_data[1]
        def_train = test_data[test_data['case'] == 'DEF']
        test_data = test_data[test_data['case'] != 'DEF']
        training_data = training_data.append(def_train, ignore_index=True)

        return (training_data, test_data)
    elif training_type == 'plur':
        training_data = new_data[0]
        test_data = new_data[1]
        plur_train = test_data[test_data['case'] == 'SG']
        test_data = test_data[test_data['case'] != 'SG']
        training_data = training_data.append(plur_train, ignore_index=True)

        return (training_data, test_data)