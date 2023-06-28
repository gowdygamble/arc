from matplotlib import colors

color_dict = {
    0: 'grey',
    1: 'red',
    2: 'blue',
    3: 'green',
    4: 'yellow',
    5: 'orange',
    6: 'purple',
    7: 'black',
    8: 'brown',
    9: 'pink',
    10: 'cyan', #padding, never used by rules
}

vals, colorz = list(color_dict.keys()), list(color_dict.values())
vals.append(vals[-1]+1)

cmap = colors.ListedColormap(colors=colorz)
bounds=vals
norm = colors.BoundaryNorm(bounds, cmap.N)