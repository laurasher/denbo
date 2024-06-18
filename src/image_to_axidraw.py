from aquatint_classes.programmatic_aquatint import ProgrammaticAquatint
from aquatint_classes.programmatic_svg import ProgrammaticSvgManipulator

# Image to aquatint file
n_aquatint_pixels = "MAX"
aq = ProgrammaticAquatint(
    # "imgs/rocks_and_sea.jpg",
    "imgs/rocks_and_sea_crop_2.jpg",
    "output",
    n_aquatint_pixels=n_aquatint_pixels,
    # sample_rate=1.5,
    use_sampled_image=False,
    # use_sampled_image=True,
    data_channel_division_factor=10,
    # data_channel_division_factor=2.5,
    # data_channel_division_factor=1,
    # data_channel_division_factor=40,
    # data_channel_division_factor=60,
    # data_channel_division_factor=30,
    # plot_point_size=0.008,
    # plot_point_size=0.05,
    # plot_point_size=0.8,
    plot_point_size=0.3,
    # plot_point_size=0.2,
)
aq_file = aq.aquatint()

# Hardcode file name if you are ready to plot and don't want to redo the above
# aq_file = "output/printed/lop56011_crop1/aquatint_pixel_concat.csv"
# aq_file = "output/lop56011_crop5_v3/aquatint_pixel_concat.csv"

# Aquatint file to axidraw
# psm = ProgrammaticSvgManipulator(aq_file)
# psm.calc_xy_size()
# psm.axidraw_xy_bounding_box()
# psm.axidraw_calibrate()
# psm.axidraw_xy_dots_inches()

"""
# This is still under construction. The input file here is an svg, not an image.
# Aquatint file to axidraw with SVG paths translated to x,y points
svg = "glyph_dictionary_lines/35.svg"
print(f"Loading in {aq_file}...")
print(f"Loading in svg image path {svg}...")
"""
