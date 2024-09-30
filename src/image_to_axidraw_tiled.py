import os
import pandas as pd
import json

from aquatint_classes.programmatic_aquatint import ProgrammaticAquatint
from aquatint_classes.programmatic_svg import ProgrammaticSvgManipulator
'''
# Image to aquatint file
n_aquatint_pixels = "MAX"
aq = ProgrammaticAquatint(
    "imgs/tree_shapes/tree_shapes_4.jpg",
    "output",
    n_aquatint_pixels=n_aquatint_pixels,
    # sample_rate=1.5,
    use_sampled_image=False,
    # use_sampled_image=True,
    # data_channel_division_factor=10,
    data_channel_division_factor=15,
    # data_channel_division_factor=20,
    # data_channel_division_factor=25,
    # data_channel_division_factor=30,
    # # data_channel_division_factor=1,
    # data_channel_division_factor=40,
    # data_channel_division_factor=50,
    # data_channel_division_factor=60,
    # data_channel_division_factor=30,
    # plot_point_size=0.008,
    # plot_point_size=0.05,
    # plot_point_size=0.8,
    # plot_point_size=0.6,
    plot_point_size=0.4,
    # plot_point_size=0.9,
    # plot_point_size=0.3,
    # plot_point_size=0.2,
)
aq_file = aq.aquatint()
'''

# Hardcode file name if you are ready to plot and don't want to redo the above
aq_file = os.path.join(
    "output",
    "tree_shapes",
    "tree_shapes_4",
    "div_factor_20_point_size_0p4",
    "aquatint_pixel_concat.csv",
)

scalar = 18.7
df = pd.read_csv(aq_file)
df['x_val'] = df['x_val']/scalar
df['y_val'] = df['y_val']/scalar

#################################################

# Tile is X_INC by Y_INC
X_INC_INCHES = 4
Y_INC_INCHES = 6
# 24x18
FINAL_IMG_X_DIM = 16
FINAL_IMG_Y_DIM = 24

num_x_tiles = int(FINAL_IMG_X_DIM/X_INC_INCHES)
num_y_tiles = int(FINAL_IMG_Y_DIM/Y_INC_INCHES)

x_row_1 = (df['x_val']<=4)
x_row_2 = (df['x_val']>4) & (df['x_val']<=8)
x_row_3 = (df['x_val']>8) & (df['x_val']<=12)
x_row_4 = (df['x_val']>12) & (df['x_val']<=16)
y_col_1 = (df['y_val']<=6)
y_col_2 = (df['y_val']>6) & (df['y_val']<=12)
y_col_3 = (df['y_val']>12) & (df['y_val']<=18)
y_col_4 = (df['y_val']>18) & (df['y_val']<=24)

tiledict = [{
        "tilenum" : 1,
        "x_mask" : x_row_1,
        "y_mask" : y_col_1,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_1.csv'
    },{
        "tilenum" : 2,
        "x_mask" : x_row_1,
        "y_mask" : y_col_2,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_2.csv'
    },{
        "tilenum" : 3,
        "x_mask" : x_row_1,
        "y_mask" : y_col_3,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_3.csv'
    },{
        "tilenum" : 4,
        "x_mask" : x_row_1,
        "y_mask" : y_col_4,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_4.csv'
    },{
        "tilenum" : 5,
        "x_mask" : x_row_2,
        "y_mask" : y_col_1,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_5.csv'
    },{
        "tilenum" : 6,
        "x_mask" : x_row_2,
        "y_mask" : y_col_2,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_6.csv'
    },{
        "tilenum" : 7,
        "x_mask" : x_row_2,
        "y_mask" : y_col_3,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_7.csv'
    },{
        "tilenum" : 8,
        "x_mask" : x_row_2,
        "y_mask" : y_col_4,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_8.csv'
    },{
        "tilenum" : 9,
        "x_mask" : x_row_3,
        "y_mask" : y_col_1,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_9.csv'
    },{
        "tilenum" : 10,
        "x_mask" : x_row_3,
        "y_mask" : y_col_2,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_10.csv'
    },{
        "tilenum" : 11,
        "x_mask" : x_row_3,
        "y_mask" : y_col_3,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_11.csv'
    },{
        "tilenum" : 12,
        "x_mask" : x_row_3,
        "y_mask" : y_col_4,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_12.csv'
    },{
        "tilenum" : 13,
        "x_mask" : x_row_4,
        "y_mask" : y_col_1,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_13.csv'
    },{
        "tilenum" : 14,
        "x_mask" : x_row_4,
        "y_mask" : y_col_2,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_12.csv'
    },{
        "tilenum" : 15,
        "x_mask" : x_row_4,
        "y_mask" : y_col_3,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_13.csv'
    },{
        "tilenum" : 16,
        "x_mask" : x_row_4,
        "y_mask" : y_col_4,
        "filename" : f'{aq_file.split(".csv")[0]}_tile_14.csv'
    }
]

# For AxiDraw SE/A3 working area is 11"x17"
for tile in tiledict:
    _df = df.copy()
    _df = _df[tile["x_mask"]] # horizontal max 16
    _df = _df[tile["y_mask"]] # vertical max 24
    _df = _df.reset_index(drop=True)
    print(_df)

    # print(_df["x_val"].max())
    # print(_df["y_val"].max())
    # print(_df["x_val"].min())
    # print(_df["y_val"].min())
    # input()
    # normalize to origin
    _df["x_val"] = _df["x_val"]-_df["x_val"].min()
    _df["y_val"] = _df["y_val"]-_df["y_val"].min()
    # print(_df["x_val"].max())
    # print(_df["y_val"].max())
    # print(_df["x_val"].min())
    # print(_df["y_val"].min())
    # input()

    _df.to_csv(tile["filename"])
    del _df

    # Aquatint file to axidraw
    psm = ProgrammaticSvgManipulator(tile["filename"], scalar=1)
    psm.calc_xy_size()
    psm.preview_trunc(savepath=f'{tile["filename"].split(".csv")[0]}.png')
    # psm.go_to_top_right()
    # psm.go_to_bottom_left()
    # psm.axidraw_xy_bounding_box()
    # psm.axidraw_calibrate()
    # psm.axidraw_xy_dots_inches()
