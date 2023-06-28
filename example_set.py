import matplotlib.pyplot as plt
from plotter_utils import cmap, norm

class ExampleSet:

    def __init__(self, example_list) -> None:
        self.example_list = example_list

    def display(self):
        f, axarr = plt.subplots(len(self.example_list), 2, sharey=True)

        for i, ex in enumerate(self.example_list):
            axarr[i,0].imshow(ex.input, cmap=cmap, norm=norm)
            axarr[i,1].imshow(ex.output, cmap=cmap, norm=norm)
            axarr[i,0].axis('off')
            axarr[i,1].axis('off')
            axarr[i,0].autoscale(True)
            axarr[i,1].autoscale(True)

        plt.show()

    def save(self):
        pass

    def get_shapes(self):
        self.shapes = []
        for ex in self.example_list:
            self.shapes.append([ex.input.shape, ex.output.shape])
        return self.shapes


