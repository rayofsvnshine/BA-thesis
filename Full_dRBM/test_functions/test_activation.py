def get_key(val, dictionary):
    for key, value in dictionary.items():
         if val == value:
             return key

def check_activation(nodes):
    # return nodes[0][0]
    activation_layer = nodes[0][0]

    # dictionary of nodes that correspond to the input
    all_nodes = {"O":0, 'p':1, 'pʲ':2, 'b':3, 'bʲ':4, 'f':5, 'fʲ':6, 'v':7, 'vʲ':8, 'm':9, 'mʲ':10, 't':11, 'tʲ':12, 'd':13, 'dʲ':14, 's':15, 'sʲ':16, 'n':17, 'nʲ':18, 'l':19, 'lʲ':20, 'r':21, 'rʲ':22, 'k':23, 'kʲ':24, 'g':25, 'gʲ':26, 'x':27, 'xʲ':28, 'ɣ':29, 'ɣʲ':30, 'ŋ':31, 'ŋʲ':32, 'h':33, 'dog':34, 'deceiver':35, 'stud/boss':36, 'May (month)':37, 'child':38, 'petal':39, 'knot':40, 'bag':41, 'increase':42, 'beer':43, 'cow':44, 'job':45, 'pepper':46, 'window':47, 'deer':48, 'poem':49, 'channel in strand':50, 'fruit':51, 'language':52, 'fox':53, 'eye':54, 'cat':55, 'fog':56, 'book':57, 'mouse':58, 'star':59, 'seal':60, 'complaint':61, 'dress':62, 'newspaper':63, 'washer (person)':64, 'butterfly':65, 'student':66, 'god':67, 'tavern':68, 'country':69, 'November':70, 'shop':71, 'friend':72, 'license':73, 'hand':74, 'lighter':75, 'bicycle':76, 'spasm':77, 'calf':78, 'generator':79, 'tradition':80, 'nervous system':81, 'NOM':82, 'GEN':83, 'DAT':84, 'SG':85, 'PL':86, 'INDEF':87, 'DEF':88}

    activated_nodes = []

    for index in range(len(activation_layer)):
        node = activation_layer[index]
        if node >= 0.5:
            active_node = get_key(index, all_nodes)
            # activated_nodes.append((active_node, node)) # returns both node name and activation level
            activated_nodes.append(active_node) # returns only node name

    return activated_nodes