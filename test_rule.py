from rule import Rule
#from rules.simple_rule_1 import simple_rule_1, simple_rule_config
from rules.color_swap_random import color_swap_random_config, color_swap_random_gex


z = Rule(color_swap_random_config, color_swap_random_gex)

exs = z.generate_example_set()

exs.display()
