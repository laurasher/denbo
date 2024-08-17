import os
from aquatint_classes.programmatic_aquatint import ProgrammaticAquatint
from aquatint_classes.programmatic_svg import ProgrammaticSvgManipulator
from aquatint_classes.aquatint_patch import AquatintPatch
from aquatint_classes.patch_plot import PatchPlot

"""
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
"""

# Hardcode file name if you are ready to plot and don't want to redo the above
aq_file_squash1 = os.path.join(
    "output",
    "squash1",
    "div_factor_25_point_size_0p4",
    "aquatint_pixel_concat.csv",
)
aq_file = os.path.join(
    "output",
    "squash2",
    "div_factor_30_point_size_0p4",
    "aquatint_pixel_concat.csv",
)

# Aquatint file to axidraw
psm = ProgrammaticSvgManipulator(aq_file, scalar=11.5)
# psm.preview()
psm.calc_xy_size()
# psm.go_to_top_right()
# psm.go_to_bottom_left()
# psm.axidraw_xy_bounding_box()
# psm.axidraw_calibrate()
psm.axidraw_xy_dots_inches()
'''
psm_squash1 = ProgrammaticSvgManipulator(aq_file_squash1, scalar=11.5)

# Patch workflow
print_page_w = 12
print_page_h = 18

# ------------ Patch 1 ------------ #
patch_pos_on_page = [6, 10] # [x_dim, y_dim] upper right point
patch_pos_from_source = [11, 1]  # [x_dim, y_dim] upper right point
patch_w = 4
patch_h = 2
patch1 = AquatintPatch(
    psm.get_xy(),
    patch_pos_from_source,
    patch_w,
    patch_h,
    patch_pos_on_page,
    print_page_w,
    print_page_h,
)
# patch1.preview()

# ------------ Patch 2 ------------ #
patch_pos_on_page = [3, 4] # [x_dim, y_dim] upper right point
patch_pos_from_source = [3, 2]  # [x_dim, y_dim] upper right point
patch_w = 5
patch_h = 10
patch2 = AquatintPatch(
    psm_squash1.get_xy(),
    patch_pos_from_source,
    patch_w,
    patch_h,
    patch_pos_on_page,
    print_page_w,
    print_page_h,
)
# patch2.preview()

# ------------ Patch 3 ------------ #
patch_pos_on_page = [1, 13] # [x_dim, y_dim] upper right point
patch_pos_from_source = [7, 10]  # [x_dim, y_dim] upper right point
patch_w = 4
patch_h = 8
patch3 = AquatintPatch(
    psm.get_xy(),
    patch_pos_from_source,
    patch_w,
    patch_h,
    patch_pos_on_page,
    print_page_w,
    print_page_h,
)

# ------------ Patch 4 ------------ #
patch_pos_on_page = [4, 1] # [x_dim, y_dim] upper right point
patch_pos_from_source = [1, 3]  # [x_dim, y_dim] upper right point
patch_w = 6
patch_h = 8
patch4 = AquatintPatch(
    psm.get_xy(),
    patch_pos_from_source,
    patch_w,
    patch_h,
    patch_pos_on_page,
    print_page_w,
    print_page_h,
)

# ------------ Patch 5 ------------ #
patch_pos_on_page = [0, 2] # [x_dim, y_dim] upper right point
patch_pos_from_source = [8, 6]  # [x_dim, y_dim] upper right point
patch_w = 5
patch_h = 4
patch5 = AquatintPatch(
    psm.get_xy(),
    patch_pos_from_source,
    patch_w,
    patch_h,
    patch_pos_on_page,
    print_page_w,
    print_page_h,
)

# ------------ Patch 6 ------------ #
patch_pos_on_page = [7, 11] # [x_dim, y_dim] upper right point
patch_pos_from_source = [6, 1]  # [x_dim, y_dim] upper right point
patch_w = 4
patch_h = 5
patch6 = AquatintPatch(
    psm.get_xy(),
    patch_pos_from_source,
    patch_w,
    patch_h,
    patch_pos_on_page,
    print_page_w,
    print_page_h,
)

patch_plot = PatchPlot([
                        patch1, 
                        patch2, 
                        patch3, 
                        patch4, 
                        patch5,
                        patch6
                        ], print_page_w, print_page_h)
patch_plot.preview()
'''