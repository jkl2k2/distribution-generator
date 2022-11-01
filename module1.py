from math import floor
import numpy as np
import matplotlib.pyplot as plt

# A constant to specify how many games should be simulated
NUM_TO_GENERATE = 100000

def hist(ax, values, x_label, title='', y_label='Frequency', density=False, bin_w=0, bin_start=0.0):
    # Find the max value in the values list
    m = max(values)
    h = []

    if (bin_w > 0):
        modified = []
        x_axis = []
        i = bin_start
        while (i < m):
            modified.append(0)
            x_axis.append(0)
            i += bin_w
        # x_axis.append(0)
        for k in range(int(m / bin_w) + 1):
            x_axis[k] = bin_start + k * bin_w
            k += bin_w
        for num in values:
            for n in range(int(m / bin_w) + 1):
                if (num <= (bin_w + (n * bin_w))):
                    modified[n] += 1
                    break
        
        if (density):
            for i in range(len(modified)):
                modified[i] /= len(values)

        # the histogram of the data
        ax.bar(x_axis, modified, width=bin_w, align='edge')
        # the x and y axis labels and title
        ax.set_ylabel(y_label)
        ax.set_xlabel(x_label)
        if len(title) > 0:
            ax.set_title(title + ", avg = " + str(np.round(np.mean(values), 2)) + ", std = " + str(np.round(np.std(values), 2)))
    else:
        for i in range(m + 1):
            h.append(0)
    
        for num in values:
            h[num] += 1

        if (density):
            for i in range(len(h)):
                h[i] /= len(values)

        # the histogram of the data
        ax.bar(range(m+1), h, 1)
        # the x and y axis labels and title
        ax.set_ylabel(y_label)
        ax.set_xlabel(x_label)
        if len(title) > 0:
            ax.set_title(title)

def insults(rank):
    if (rank == "bronze"):
        return round(np.random.normal(8, 2))
    elif (rank == "gold"):
        return round(np.random.normal(10, 3))
    elif (rank == "diamond"):
        return round(np.random.normal(15, 4))
    else:
        return round(np.random.normal(12, 2))

def generateListInsults(rank=""):
    numInsults = []
    for i in range(NUM_TO_GENERATE):
        remarksPerGame = insults(rank)
        if (remarksPerGame < 0):
            remarksPerGame = 0
        numInsults.append(remarksPerGame)
    return numInsults

def roles():
    rand = floor(np.random.uniform(0, 5))
    if (rand == 0):
        return "top"
    elif (rand == 1):
        return "mid"
    elif (rand == 2):
        return "adc"
    elif (rand == 3):
        return "support"
    else:
        return "jungle"

def generateListRoles():
    problematicPlayers = []
    for i in range(NUM_TO_GENERATE):
        problematicPlayers.append(roles())
    return problematicPlayers

def main():
    ## Part 1 - Random normal distribution values

    # These are normally distributed
    # The amount of insults directed at a player varies...
    # ...but is centered around an average depending on rank
    numInsultsGeneral = generateListInsults()
    numInsultsBronze = generateListInsults("bronze")
    numInsultsGold = generateListInsults("gold")
    numInsultsDiamond = generateListInsults("diamond")

    # The roles are uniformly distributed
    # Any type of player equally likely to be angry
    rolesGeneral = generateListRoles()
    rolesBronze = generateListRoles()
    rolesGold = generateListRoles()
    rolesDiamond = generateListRoles()

    print("Average League Game:")
    print("\tToxic remarks per game:")
    print("\t\t" + str(numInsultsGeneral))
    print("\tCorresponding role of problem player:")
    print("\t\t" + str(rolesGeneral))

    print("Bronze game:")
    print("\tToxic remarks per game:")
    print("\t\t" + str(numInsultsBronze))
    print("\tCorresponding role of problem player:")
    print("\t\t" + str(rolesBronze))

    print("Gold game:")
    print("\tToxic remarks per game:")
    print("\t\t" + str(numInsultsGold))
    print("\tCorresponding role of problem player:")
    print("\t\t" + str(rolesGold))

    print("Diamond game:")
    print("\tToxic remarks per game:")
    print("\t\t" + str(numInsultsDiamond))
    print("\tCorresponding role of problem player:")
    print("\t\t" + str(rolesDiamond))

    ## Part 2 - Graphing the data
    # Create plot
    fix, axes = plt.subplots(2, 5)

    # The distributions are uniform, as expected
    hist(axes[0,0], numInsultsGeneral, "Number of insults", "Insults in any average game", "Frequency")
    hist(axes[0,1], numInsultsBronze, "Number of insults", "Insults in bronze", "Frequency")
    hist(axes[0,2], numInsultsGold, "Number of insults", "Insults in gold", "Frequency")
    hist(axes[0,3], numInsultsDiamond, "Number of insults", "Insults in diamond", "Frequency")

    # Separate by role
    allRoles = [rolesGeneral, rolesBronze, rolesGold, rolesDiamond]
    allInsults = [numInsultsGeneral, numInsultsBronze, numInsultsGold, numInsultsDiamond]
    
    fromTop = []
    fromMid = []
    fromAdc = []
    fromSupport = []
    fromJungle = []

    # Use for loops to separate out the count by role
    for array in range(len(allRoles)):
        for i in range(len(allRoles[array])):
            if (allRoles[array][i] == "top"):
                fromTop.append(allInsults[array][i])
            elif (allRoles[array][i] == "mid"):
                fromMid.append(allInsults[array][i])
            elif (allRoles[array][i] == "adc"):
                fromAdc.append(allInsults[array][i])
            elif (allRoles[array][i] == "support"):
                fromSupport.append(allInsults[array][i])
            elif (allRoles[array][i] == "jungle"):
                fromJungle.append(allInsults[array][i])

    # Something interesting about these separated...
    # ...graphs is how they are skewed right.
    # The lower ranks having less toxic remarks...
    # ...causes the data to clump toward the left.
    # The uniform nature of the roles results...
    # ...in identical graph shapes for these.
    hist(axes[1,0], fromTop, "Number of insults", "Insults from top lane", "Frequency")
    hist(axes[1,1], fromMid, "Number of insults", "Insults from mid lane", "Frequency")
    hist(axes[1,2], fromAdc, "Number of insults", "Insults from ADC", "Frequency")
    hist(axes[1,3], fromSupport, "Number of insults", "Insults from support", "Frequency")
    hist(axes[1,4], fromJungle, "Number of insults", "Insults from jungle", "Frequency")

    # Show plot
    plt.show()

main()