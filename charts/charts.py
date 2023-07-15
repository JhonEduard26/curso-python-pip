import matplotlib.pyplot as plt


def generate_pie_chart():
    labels = ['a', 'b', 'c']
    values = [35, 100, 55]
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()
