# denbo

To run:

Activate virtual environment with dependencies installed from programmatic_svg_manipular/requirements.txt class

`source ~/.venv/axicli/bin/activate`

Change parameters in ProgrammaticAquatint class constructor to include:
1) image file name
2) output folder path
3) number aquatint pixels (or leave set to "MAX")
4) whether to use sampled image (True or False). this will reduce image resolution. I usually leave this to False.
5) data_channel_division_factor: 10, 20, .., 80. This higher this number is, the lower your range of tonal values will be, and the lower your number of plotted points.
6) plot_point_size greatly affects the preview image plot. Usually this parameter and data_channel_division_factor are the ones I tweak the most.

Run the image to axidraw script to execute the image to AxiDraw plotting process, or to draw the bounding box before plotting.

`python image_to_axidraw.py`