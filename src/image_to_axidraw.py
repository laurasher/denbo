import os
from aquatint_classes.programmatic_aquatint import ProgrammaticAquatint
from aquatint_classes.programmatic_svg import ProgrammaticSvgManipulator
'''
# Image to aquatint file
n_aquatint_pixels = "MAX"
aq = ProgrammaticAquatint(
<<<<<<< HEAD
    "imgs/final/lop56011_crop4.jpg",
=======
    # "imgs/lopcrop4_and_rocks_and_sea_crop3_v2.jpg",
    "imgs/double1/double1_bottom.jpg",
>>>>>>> 12by18/rocks_and_sea_crop_3_and_lop56011_crop4
    "output",
    n_aquatint_pixels=n_aquatint_pixels,
    # sample_rate=1.5,
    use_sampled_image=False,
    # use_sampled_image=True,
    # data_channel_division_factor=10,
    # data_channel_division_factor=15,
<<<<<<< HEAD
=======
    data_channel_division_factor=20,
>>>>>>> 12by18/rocks_and_sea_crop_3_and_lop56011_crop4
    # data_channel_division_factor=2.5,
    # data_channel_division_factor=1,
    # data_channel_division_factor=40,
    # data_channel_division_factor=60,
    data_channel_division_factor=30,
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
aq_file = "output/FINAL_DONT_OVERWRITE/9by12_printed_proofs/lop56011_crop4/div_factor_30_point_size_0p5/aquatint_pixel_concat.csv"

# Aquatint file to axidraw
psm = ProgrammaticSvgManipulator(aq_file, scalar=12)
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

