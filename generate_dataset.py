import importlib
from rule import Rule
import random
import pickle
import numpy as np

#XX 'slide_to_hit',
#xx'grid_fill',
#xx'color_closed',

rule_names = [
       'color_swap_random',
    'extend_lines',
    'extend_lines_random_colors',
    'ext_lines_diag',
    'color_bars_by_length',
    'count_stamps',
    'simple_fill',
    'majority_fill',
    'slide_dots_to_side',
    'connect_diag_lines',
    'line_grants_color',
    'expand_stamp',
    'slide_section',
    'diag_shape_adjust',
    'fill_interior',
    'project_stamp',
    'logical_and',
    'tile_diag',
    'pick_four_color',
    'odd_color_out',
    'blossom_flowers',
    'blossom_flowers_2',
    'tile_lines',
    'fill_behind_lines',
    'pick_lone_color_quadrant',
    'lone_color_quad_to_common_color',
    'check_majority',
    'check_minority',
    'slide_side',
    'majority_row',
    'color_based_blossom',
    'dot_to_stamp',
    'fill_in_carpet',
    'tile_and_corners',
    'complete_pattern',
    'count_sections',
    'stack_stamp',
    'resize_stamp_pattern',
    'rotate_and_tile',
    'erode_ones',
    'color_closed',
    #'rotate_and_transfer_stamp',
    'extend_lines_overlap',
    'extend_lines_overlap_2',
    'slide_dots_to_lines',
    'complete_pinwheel',
    'line_to_box',
    'crop_box',
    'identify_crop_box',
    #'slide_to_color',
]

rule_names = ['rules.rules.' + r for r in rule_names]

print(len(rule_names))


random.seed(33)

train_samples_per_rule = 1000
val_samples_per_rule = 50

train_samples = []
val_samples = []


for ii, rfn in enumerate(rule_names):
    rule_module = importlib.import_module(rfn)
    print(ii, rfn)

    for ts in range(train_samples_per_rule):
        if ts % 100 == 0:
            print(ts)
        cfg = rule_module.generate_config()
        gex = rule_module.example_func()
        r = Rule(cfg, gex)
        exs = r.generate_example_set()
        #exs.display()
        train_samples.append(exs)
    for vs in range(val_samples_per_rule):
        cfg = rule_module.generate_config()
        gex = rule_module.example_func()
        r = Rule(cfg, gex)
        exs = r.generate_example_set()
        val_samples.append(exs)

print(len(train_samples))
print(len(val_samples))


def pad_to_size(arr, size):
    z = np.ones((size, size)) * 10
    z[:arr.shape[0], :arr.shape[1]] = arr

    return z

def blank_arr():
    return np.ones((24, 24)) * 10

def pad_example_set(example_set):
    for ex in example_set.example_list:
        ex.input = pad_to_size(ex.input, 24)
        ex.output = pad_to_size(ex.output, 24)
    return example_set

def package_example_set(example_set):
    inputs = []
    example_set = pad_example_set(example_set)
    for ex in example_set.example_list:
        # if ex.input.shape != (24, 24) or ex.output.shape != (24, 24):
        #     print("SHAPES", ex.input.shape, ex.output.shape)
        inputs.append(ex.input)
        inputs.append(ex.output)
    outputs = [inputs[-1]]
    inputs = inputs[:-1]

    # TODO: think more about this, would like to avoid padding all these with blank arrays
    while len(inputs) < 9:
        inputs.append(blank_arr())
    return np.array(inputs), np.array(outputs)

def package_dataset(ds):
    inputs = []
    outputs = []
    for exs in ds:
        i, o = package_example_set(exs)
        inputs.append(i)
        #print(i.shape, o.shape)
        outputs.append(o)
    return {
        'inputs': np.array(inputs),
        'outputs': np.array(outputs)
    }

train_arrays = package_dataset(train_samples)
val_arrays = package_dataset(val_samples)

print(train_arrays['inputs'].shape, train_arrays['outputs'].shape)
print(val_arrays['inputs'].shape, val_arrays['outputs'].shape)

with open('train_arrays_2.pkl', 'wb') as f:
    pickle.dump(train_arrays, f)
with open('val_arrays_2.pkl', 'wb') as f:
    pickle.dump(val_arrays, f)


# max_input_dim = 0
# max_output_dim = 0

# for ts in train_samples:
#     s = ts.get_shapes()
#     for i, o in s:
#         for d in i:
#             if d > max_input_dim:
#                 max_input_dim = d
#         for d in o:
#             if d > max_output_dim:
#                 max_output_dim = d


# print(max_input_dim)
# print(max_output_dim)

# with open('train_samples.pkl', 'wb') as f:
#     pickle.dump(train_samples, f)
# with open('val_samples.pkl', 'wb') as f:
#     pickle.dump(val_samples, f)
        
