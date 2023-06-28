import matplotlib.pyplot as plt
from plotter_utils import cmap, norm


class Example:
    def __init__(self, i, o) -> None:
        self.input = i
        self.output = o

    def display(self):
        #f, axarr = plt.subplots(2, 2)
        f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
        ax1.imshow(self.input, cmap=cmap, norm=norm)
        ax2.imshow(self.output, cmap=cmap, norm=norm)
        ax1.axis('off')
        ax2.axis('off')
        plt.show()
