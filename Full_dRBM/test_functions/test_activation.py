# dictionary of nodes that correspond to the input
all_nodes = {"O":0, 'p':1, 'pʲ':2, 'b':3, 'bʲ':4, 'f':5, 'fʲ':6, 'v':7, 'vʲ':8, 'm':9, 'mʲ':10, 't':11, 'tʲ':12, 'd':13, 'dʲ':14, 's':15, 'sʲ':16, 'n':17, 'nʲ':18, 'l':19, 'lʲ':20, 'r':21, 'rʲ':22, 'k':23, 'kʲ':24, 'g':25, 'gʲ':26, 'x':27, 'xʲ':28, 'ɣ':29, 'ɣʲ':30, 'ŋ':31, 'ŋʲ':32, 'h':33, 'dog':34, 'deceiver':35, 'stud/boss':36, 'May (month)':37, 'child':38, 'petal':39, 'knot':40, 'bag':41, 'increase':42, 'beer':43, 'cow':44, 'job':45, 'pepper':46, 'window':47, 'deer':48, 'poem':49, 'channel in strand':50, 'fruit':51, 'language':52, 'fox':53, 'eye':54, 'cat':55, 'fog':56, 'book':57, 'mouse':58, 'star':59, 'seal':60, 'complaint':61, 'dress':62, 'newspaper':63, 'washer (person)':64, 'butterfly':65, 'student':66, 'god':67, 'tavern':68, 'country':69, 'November':70, 'shop':71, 'friend':72, 'license':73, 'hand':74, 'lighter':75, 'bicycle':76, 'spasm':77, 'calf':78, 'generator':79, 'tradition':80, 'nervous system':81, 'NOM':82, 'GEN':83, 'DAT':84, 'SG':85, 'PL':86, 'INDEF':87, 'DEF':88}

def get_key(val, dictionary):
    # returns key of the dictionary with corresponding value
    for key, value in dictionary.items():
        if val == value:
            return key

def highest_value(new_value, highest_value, new_index, old_index):
    # if no highest value has been recorded yet, assign new value to highest value
    if highest_value == None:
        highest_value = new_value
        index = get_key(new_index, all_nodes)
    # if new value is bigger than highest value, assign new value to highest value
    elif new_value > highest_value:
        highest_value = new_value
        index = get_key(new_index, all_nodes)
    # if new value is smaller than highest value, keep old value as highest value
    else:
        index = old_index

    return highest_value, index 

def check_activation(activation_layer):
    activated_nodes = []
    highest_activated_phon = None
    highest_activated_lex = None
    highest_activated_case = None
    pl_or_sg = None
    ind_def = None
    phon_ind, lex_ind, case_ind, pl_ind, ind_ind = -1, -1, -1, -1, -1

    for index in range(len(activation_layer)):
        node = activation_layer[index]
        if index < 34:
            highest_activated_phon, phon_ind = highest_value(node, highest_activated_phon, index, phon_ind)
        elif index < 82:
            highest_activated_lex, lex_ind = highest_value(node, highest_activated_lex, index, lex_ind)
        elif index < 85:
            highest_activated_case, case_ind = highest_value(node, highest_activated_case, index, case_ind)
        elif index < 87:
            pl_or_sg, pl_ind = highest_value(node, pl_or_sg, index, pl_ind)
        else:
            ind_def, ind_ind = highest_value(node, ind_def, index, ind_ind)
        
    # returns both node name and activation level
    # activated_nodes = [(phon_ind , highest_activated_phon), (lex_ind, highest_activated_lex), (case_ind, highest_activated_case), (pl_ind, pl_or_sg), (ind_ind, ind_def)]
    # returns only node name
    activated_nodes = [phon_ind, lex_ind, case_ind, pl_ind, ind_ind]

    return activated_nodes