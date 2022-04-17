# import all needed packages
from setup_input import input_vowels, setup_network
from learning_phases import one_learning_step
from echoes import echo_drift
import matplotlib.pyplot as plt
##########################################################################
##########  setup parameters to run the distance calculations  ###########
steps = 50000
original_vowels = 'five'
test_vowel = '_spec'   # if test for specific vowels add: '_spec'
split_merge = 'merge'  # enter: 'split' or 'merge' or 'none4' or 'none5'
split_merge_steps= 50000   # if no split or merger, set to 0
input_type = 'edge'    # state if you'd like random or cat-edge inputs
returner = True        # true if you want to test original vowel retention
##########################################################################

# setting up some variables
if split_merge == 'split':
    new_vowels = 'five'
elif split_merge == 'merge':
    new_vowels = 'four'

# setup the network 
new_nodes_connections = setup_network()

# set up empty lists of drifts to plot
inp_drifts = []
echo_drifts = []
trainingsteps = []

# Train the network in L1 and collect median distances per 500 steps
for i in range(steps):
    new_nodes_connections[0] = input_vowels(new_nodes_connections[0], original_vowels)
    new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])
    if i > 1 and i%500 == 0:
        echo_drift_nodes = echo_drift(new_nodes_connections[0], new_nodes_connections[1], 'five_spec', input_type)
        inp_drifts.append(echo_drift_nodes[0])
        echo_drifts.append(echo_drift_nodes[1])
        trainingsteps.append(i)

# Train the network in L2 and collect median distances per 500 steps
if split_merge == 'merge' or split_merge == 'split':
    for i in range(split_merge_steps):
        new_nodes_connections[0] = input_vowels(new_nodes_connections[0], 'four')
        new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])
        if i > 1 and i%500 == 0:
            echo_drift_nodes = echo_drift(new_nodes_connections[0], new_nodes_connections[1], 'four_spec', input_type)
            inp_drifts.append(echo_drift_nodes[0])
            echo_drifts.append(echo_drift_nodes[1])
            trainingsteps.append(i+split_merge_steps)

# Re-train the network in L1 and collect median distances per 500 steps
if returner == True:
    for i in range(50000):
        new_nodes_connections[0] = input_vowels(new_nodes_connections[0], original_vowels)
        new_nodes_connections = one_learning_step(new_nodes_connections[0], new_nodes_connections[1])
        if i > 1 and i%500 == 0:
            echo_drift_nodes = echo_drift(new_nodes_connections[0], new_nodes_connections[1], 'five_spec', input_type)
            inp_drifts.append(echo_drift_nodes[0])
            echo_drifts.append(echo_drift_nodes[1])
            trainingsteps.append(i+split_merge_steps+50000)

# Setup the figure and plot the distances
fig, ax = plt.subplots()
ax.plot(trainingsteps, inp_drifts, 'b-',label='Input distance')
ax.plot(trainingsteps,echo_drifts, 'r-',label='Echo distance')
ax.text(-10500,2, 'Distance (ERB)', va='center', rotation=90)

# add vertical dotted lines to show vowel system switch
if split_merge == 'merge' or split_merge == 'split':
    ax.axvline(steps, 0, 4, c='k', ls='--', label='Vowel sytem switch')

# set axis labels and sizes
if returner == True:
    ax.axvline((steps+split_merge_steps), 0, 4, c='k', ls='--')
    ax.text((steps+split_merge_steps+50000)/2,-0.5, 'Trainingsteps', ha='center')
    plt.axis([0, (steps+split_merge_steps+50000), 0, 4])
else:
    plt.axis([0, (steps+split_merge_steps), 0, 4])
    ax.text((steps+split_merge_steps)/2,-0.5, 'Trainingsteps', ha='center')

# add a legend and save (show) the figure
ax.legend()
fig.set_size_inches(10, 5)
if returner == True:
    fig.savefig('new_pdfs/distance_returner_merge.pdf', dpi=600)
else: 
    fig.savefig('new_pdfs/distance_'+ split_merge +'_'+str(steps+split_merge_steps)+ str(test_vowel) +'.pdf', dpi=600)
plt.show()
 