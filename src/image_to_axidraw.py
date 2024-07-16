from aquatint_classes.programmatic_aquatint import ProgrammaticAquatint
from aquatint_classes.programmatic_svg import ProgrammaticSvgManipulator

'''
# Image to aquatint file
n_aquatint_pixels = "MAX"
aq = ProgrammaticAquatint(
    "imgs/double2/double2_top.jpg",
    # "imgs/double_3.jpg",
    # "imgs/final/lop56011_crop7.jpg",
    "output",
    n_aquatint_pixels=n_aquatint_pixels,
    # sample_rate=1.5,
    use_sampled_image=False,
    # use_sampled_image=True,
    # data_channel_division_factor=10,
    # data_channel_division_factor=15,
    data_channel_division_factor=25,
    # data_channel_division_factor=1,
    # data_channel_division_factor=40,
    # data_channel_division_factor=60,
    # data_channel_division_factor=30,
    # plot_point_size=0.008,
    # plot_point_size=0.05,
    # plot_point_size=0.8,
    plot_point_size=0.5,
    # plot_point_size=0.9,
    # plot_point_size=0.3,
    # plot_point_size=0.2,
)
aq_file = aq.aquatint()
'''
# Hardcode file name if you are ready to plot and don't want to redo the above
aq_file = "output/double2/double2_bottom/div_factor_25_point_size_0p5/aquatint_pixel_concat.csv"

# Aquatint file to axidraw
psm = ProgrammaticSvgManipulator(aq_file)
psm.calc_xy_size()
# psm.axidraw_xy_bounding_box()
# psm.axidraw_calibrate()
psm.axidraw_xy_dots_inches()
