import matplotlib.pyplot as pylot

def generate_pie_chart():
    labels = ["A","B","C"]
    values = [333,44, 77]

    ax = pylot.subplot()
    ax.pie(values, labels=labels)
    pylot.savefig("pie.png")
    pylot.close()