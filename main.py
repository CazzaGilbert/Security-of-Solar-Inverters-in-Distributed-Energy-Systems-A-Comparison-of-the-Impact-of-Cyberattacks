from inverter import Inverter
from config import LETTER, ACRONYM, ATTACKS
import matplotlib
matplotlib.use('Agg') # required for making the output image
import matplotlib.pyplot as plt
import pandas as panda

def getInput():
    # show possible cyber defences to implement
    print("\nAvailable Defence Methods for Implementation:")
    for letter, fullTerm in LETTER.items():
        print(f" {letter} {fullTerm}")

    # get user to choose the method to implement
    while 1:
        method = input("Enter feature (letter or full name): ").strip()

        # confirm method in list
        if method in LETTER:
            selected = LETTER[method]
            break
        else:
            print("No matches. Try again.")

    # get user to choose the level of the method to implement
    while 1:
        try:
            levelImp = int(input("Enter level (1-5): "))
            if 1 <= levelImp <= 5:
                break
        except ValueError:
            pass
        print("Invalid. Try again.")

    # return chosen values
    return selected, levelImp

def addLabels(axis, graph): # add raw value to the graph for easier understanding
    for bar, (_, row) in zip(axis.containers[0], graph.iterrows()):
        axis.annotate(f"${row['Implementation Cost']:,}", (bar.get_x() + bar.get_width()/2, bar.get_height() + 1), ha='center', fontsize=8)
    for bar, (_, row) in zip(axis.containers[1], graph.iterrows()):
        axis.annotate(f"${row['Cost Saved']:,}", (bar.get_x() + bar.get_width()/2, bar.get_height() + 1), ha='center', fontsize=8)

def main(): # main function
    print("Solar Inverter Cyber Attack Simulator")
    print("*Disclamer: the values used in this simulator to predict costs and savings are best estimations and should not be used for any real world modelling!")
    while 1: # get user to tell say how many models they would like to compare 
        try:
            compCount = int(input("How many methods would you like to compare? (2-5): "))
            if 2 <= compCount <= 5:
                break
        except ValueError: # user didn't give valid input
            pass
        print("Invalid input, please choose a number betteen 2 and 5.")

    # intialise variables
    results = []
    impCost = 0
    labels = ""

    for i in range(compCount): # for each method for comparison
        print(f"\n~~~ Method {i + 1} ~~~")
        inverter = Inverter()
        method, levelImp = getInput()
        inverter.implementDefence(method, levelImp) # add defece method at implementation level

        # get values for graphed output
            # cost to implement
        impCost = inverter.total_cost 
            # money saved from stopped attacks
        mitAttacks = inverter.defences[0].mitigates 
        mitCosts = sum(ATTACKS[attack] for attack in mitAttacks if attack in ATTACKS)
            # title for graph
        labels = f"{ACRONYM.get(method, method[:4].upper())} L{levelImp}"
        
        # group results for graph
        results.append({
            "Name": labels,
            "Implementation Cost": impCost,
            "Cost Saved": mitCosts
        })

    # display results
    graph = panda.DataFrame(results)
    print("\nResults:")
    print(graph.to_string(index=False)) # show as table. Edit: false removes row count

    # graph results
    axis = graph.set_index("Name")[['Implementation Cost', 'Cost Saved']].plot(
        kind='bar', figsize=(10, 6), color=["Red", "Green"]
    )

    # graph settings 
    plt.title("Inverter Security Method Economic Impact Comparison")
    plt.ylabel("AUD $ (Thousands)")
    plt.xticks(rotation=0)
    plt.legend()
    addLabels(axis, graph)
    plt.tight_layout()
    plt.savefig("Comparison.png")
    print("Results outputed in: Comparison.png")

if __name__ == "__main__":
    main()