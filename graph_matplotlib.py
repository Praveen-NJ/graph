import matplotlib.pyplot as plt


class PlotGraph:
    def check_input_inrange(self, values):
        for val in values:
            if not val < 20 and val > 1:
                raise Exception("Value must be in the range 1 to 20")

    def plot_graph(self, values):
        print("Creating Graph")

        fig = plt.figure()
        ax = fig.add_subplot(111)

        x = range(0, len(values))
        y = values
        line = ax.plot(x, y, linestyle='dashed')

        ymax = max(y)
        xpos = y.index(ymax)
        xmax = x[xpos]

        ax.annotate('-|-', xy=(xmax, ymax), xytext=(xmax, ymax))
        ax.set_ylim(0, 20)
        plt.show()


def main():
    values = list(map(int, input().strip().split()))
    plot = PlotGraph()
    plot.check_input_inrange(values)
    plot.plot_graph(values)


if __name__ == "__main__":
    main()
