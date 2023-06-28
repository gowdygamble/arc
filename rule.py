from example import Example
from example_set import ExampleSet

class Rule:
    def __init__(self, config, example_func):
        self.config = config
        self.example_func = example_func

    def generate_example(self):
        i, o = self.example_func(self.config)
        ex = Example(i,o)
        return ex

    def generate_example_set(self):
        example_list = []
        for i in range(self.config['nb_examples']):
            example_list.append(self.generate_example())
        exs = ExampleSet(example_list)
        return exs