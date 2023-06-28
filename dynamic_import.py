import importlib
from rule import Rule

rule_names = [
    #'color_swap_random',
    #'extend_lines',
    #'extend_lines_random_colors',
    #'ext_lines_diag',
    #'color_bars_by_length',
    #'count_stamps',
    #'simple_fill',
    #'majority_fill',
    #'slide_dots_to_side',
    #'connect_diag_lines',
    #'line_grants_color',
    #'expand_stamp',
    #'slide_section',
    #'diag_shape_adjust',
    #'fill_interior',
    #'project_stamp',
    #'logical_and',
    #'tile_diag',
    #XX 'slide_to_hit',
    #xx'grid_fill',
    #'pick_four_color',
    #'odd_color_out',
    #'blossom_flowers',
    #'blossom_flowers_2',
    #'tile_lines',
    #'fill_behind_lines',
    #'pick_lone_color_quadrant',
    #'lone_color_quad_to_common_color',
    #'check_majority',
    #'check_minority',
    #'slide_side',
    #'majority_row',
    #'color_based_blossom',
    #'dot_to_stamp',
    #'fill_in_carpet',
    #'tile_and_corners',
    #'complete_pattern',
    #'count_sections',
    #'stack_stamp',
    #'resize_stamp_pattern',
    #'rotate_and_tile',
    #'erode_ones',
    #'color_closed',
    #'rotate_and_transfer_stamp',
    #'extend_lines_overlap',
    #'extend_lines_overlap_2',
    #'slide_dots_to_lines',
    #'complete_pinwheel',
    #'line_to_box',
    #'crop_box',
    #'identify_crop_box',
    #'slide_to_color',
    #'test_rotate_dots',
    #'test_step_pattern',
    #'test_fill_band',
    #'test_destroy_fewest_dots',
    'test_count_lines',
    
]

rule_names = ['rules.rules.' + r for r in rule_names]

for rfn in rule_names:
    rule_module = importlib.import_module(rfn)

    for i in range(3):
        cfg = rule_module.generate_config()
        gex = rule_module.example_func()
        r = Rule(cfg, gex)
        exs = r.generate_example_set()
        exs.display()
