import os
from aquatint_classes.programmatic_aquatint import ProgrammaticAquatint
from aquatint_classes.programmatic_svg import ProgrammaticSvgManipulator
'''
# Image to aquatint file
n_aquatint_pixels = "MAX"
aq = ProgrammaticAquatint(
    "imgs/lopcrop4_and_rocks_and_sea_crop3_v2.jpg",
    # "imgs/double1/double1_bottom.jpg",
    "output",
    n_aquatint_pixels=n_aquatint_pixels,
    # sample_rate=1.5,
    use_sampled_image=False,
    # use_sampled_image=True,
    # data_channel_division_factor=10,
    # data_channel_division_factor=15,
    data_channel_division_factor=20,
    # data_channel_division_factor=2.5,
    # data_channel_division_factor=1,
    # data_channel_division_factor=40,
    # data_channel_division_factor=60,
    # data_channel_division_factor=30,
    # plot_point_size=0.008,
    # plot_point_size=0.05,
    # plot_point_size=0.8,
    # plot_point_size=0.5,
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
    "double_v2",
    "div_factor_20_point_size_0p4",
    "aquatint_pixel_concat.csv",
)

# Aquatint file to axidraw
psm = ProgrammaticSvgManipulator(aq_file, scalar=12.4)
# psm.preview()
# psm.calc_xy_size()
# psm.axidraw_xy_bounding_box()
psm.axidraw_xy_dots_inches()
# del psm

# # Add 9" offset to bottom file, then concat top and bottom files
# psm = ProgrammaticSvgManipulator(aq_file_bottom, scalar=11.9, yoffset=9)
# # psm.preview()
# psm.calc_xy_size()
# # psm.axidraw_xy_bounding_box()
# psm.axidraw_xy_dots_inches()
# del psm

