from xml.dom import minidom
from svg.path import parse_path

doc = minidom.parse("imgs/squash/SVG/squash_stencil.svg")
width_inches = 12
height_inches = 15.4
coords = []
for ipath, path in enumerate(doc.getElementsByTagName("path")):
    print("Path", ipath)
    d = path.getAttribute("d")
    parsed = parse_path(d)
    print("Objects:\n", parsed, "\n" + "-" * 20)
    for obj in parsed:
        print(
            type(obj).__name__,
            ", start/end coords:",
            (
                (round(obj.start.real, 3), round(obj.start.imag, 3)),
                (round(obj.end.real, 3), round(obj.end.imag, 3)),
            ),
        )
        coords.append([round(obj.start.real, 3), round(obj.start.imag, 3)])
        coords.append([round(obj.end.real, 3), round(obj.end.imag, 3)])
    print("-" * 20)
doc.unlink()
# print(coords)
# for c in coords:
#     print(c)
#     print("----------")
