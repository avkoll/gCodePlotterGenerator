from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode.compiler import Compiler, interfaces
from svgpathtools import svg2paths2
import svgwrite


def scale_svg(svg_path, output_path, max_width, max_height):
    # Read and parse the original SVG
    paths, attributes, svg_attributes = svg2paths2("./svgs/star-984.svg")

    # Calculate the bounding box of the original SVG
    min_x, min_y, max_x, max_y = paths[0].bbox()
    for path in paths[1:]:
        bbox = path.bbox()
        min_x = min(min_x, bbox[0])
        min_y = min(min_y, bbox[1])
        max_x = max(max_x, bbox[2])
        max_y = max(max_y, bbox[3])

    # Calculate the original width and height
    original_width = max_x - min_x
    original_height = max_y - min_y

    # Calculate the scaling factor
    scale_factor = min(max_width / original_width, max_height / original_height)

    # Create a new scaled SVG
    dwg = svgwrite.Drawing(output_path)
    dwg.viewbox(width=max_width, height=max_height)

    for path in paths:
        scaled_path = path.scaled(scale_factor, scale_factor)
        dwg.add(dwg.path(d=scaled_path.d()))

    dwg.save()


def generate_curves(svgPath):
    scaled_svg_path = "scaled_drawing.svg"
    scale_svg(svgPath, scaled_svg_path, 1, 1)
    # Instantiate a compiler, specifying the interface type and the speed at which the tool should move. pass_depth controls
    # how far down the tool moves after every pass. Set it to 0 if your machine does not support Z axis movement.
    gcode_compiler = Compiler(interfaces.Gcode, movement_speed=1000, cutting_speed=300, pass_depth=0)

    curves = parse_file(scaled_svg_path)  # Parse an svg file into geometric curves

    gcode_compiler.append_curves(curves)
    gcode_compiler.compile_to_file("drawing.gcode", passes=1)

