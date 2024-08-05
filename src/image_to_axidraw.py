import os
from aquatint_classes.programmatic_aquatint import ProgrammaticAquatint
from aquatint_classes.programmatic_svg import ProgrammaticSvgManipulator
'''
# Image to aquatint file
n_aquatint_pixels = "MAX"
aq = ProgrammaticAquatint(
    "imgs/squash/squash_double3.jpg",
    "output",
    n_aquatint_pixels=n_aquatint_pixels,
    # sample_rate=1.5,
    use_sampled_image=False,
    # use_sampled_image=True,
    # data_channel_division_factor=10,
    # data_channel_division_factor=15,
    # data_channel_division_factor=25,
    # data_channel_division_factor=1,
    # data_channel_division_factor=40,
    data_channel_division_factor=50,
    # data_channel_division_factor=60,
    # data_channel_division_factor=30,
    # plot_point_size=0.008,
    # plot_point_size=0.05,
    # plot_point_size=0.8,
    plot_point_size=0.6,
    # plot_point_size=0.4,
    # plot_point_size=0.9,
    # plot_point_size=0.3,
    # plot_point_size=0.2,
)
aq_file = aq.aquatint()
'''

# Hardcode file name if you are ready to plot and don't want to redo the above
aq_file = os.path.join(
    "output",
    "squash1",
    "div_factor_25_point_size_0p4",
    "aquatint_pixel_concat.csv",
)
# aq_file = os.path.join(
#     "output",
#     "squash2",
#     "div_factor_30_point_size_0p4",
#     "aquatint_pixel_concat.csv",
# )

import pandas as pd
import json

scalar = 11.5
df = pd.read_csv(aq_file)
df['x_val'] = df['x_val']/scalar
df['y_val'] = df['y_val']/scalar

# For AxiDraw SE/A3 working area is 11"x17"
df = df.drop(df[df['x_val']>=12].index)
df = df.drop(df[df['y_val']>=18].index)
aq_file_trunc = f'{aq_file.split(".csv")[0]}_trunc_SEA3.csv'
df.to_csv(aq_file_trunc)

# Aquatint file to axidraw
psm = ProgrammaticSvgManipulator(aq_file_trunc, scalar=1)
# psm.preview()
# psm.calc_xy_size()
# psm.go_to_top_right()
# psm.go_to_bottom_left()
# psm.axidraw_xy_bounding_box()
# psm.axidraw_calibrate()
# psm.axidraw_xy_dots_inches()
psm.make_grid()