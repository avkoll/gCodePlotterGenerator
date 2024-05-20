from svgConverter import generate_curves  # Converts a svg file to gcode


def calculate_scaling_factor(max_dimension, limit):
    return limit / max_dimension


def extract_max_dimensions(gcode_file):
    max_x, max_y = 0, 0
    with open(gcode_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('G1') or line.startswith('G0'):
                parts = line.split(' ')
                for part in parts:
                    if part.startswith('X'):
                        max_x = max(max_x, abs(float(part[1:])))
                    elif part.startswith('Y'):
                        max_y = max(max_y, abs(float(part[1:])))
    return max_x, max_y


def scale_gcode_with_g51(gcode_file, output_file, scaling_factor):
    with open(gcode_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        f.write(f'G51 X{scaling_factor:.6f} Y{scaling_factor:.6f}\n')
        f.writelines(lines)


def main():
    starting_gcode_content = starting_gcode()
    generate_curves("./svgs/star-984.svg")

    # Extract maximum dimensions from the generated G-code
    max_x, max_y = extract_max_dimensions("drawing.gcode")

    if max_x == 0 or max_y == 0:
        raise ValueError("The generated G-code has zero dimensions, please check the SVG content.")

    max_dimension = max(max_x, max_y)
    limit = 100  # Your coordinate limit
    scaling_factor = calculate_scaling_factor(max_dimension, limit)

    # Apply the scaling factor using G51
    scale_gcode_with_g51("drawing.gcode", "scaled_drawing.gcode", scaling_factor)

    # Read the scaled G-code file
    with open("scaled_drawing.gcode", "r") as f:
        lines = f.readlines()

    # Skip certain lines
    lines_to_append = lines[4:]

    final_gcode = starting_gcode_content + "".join(lines_to_append)

    with open("plotter_output.gcode", "w") as f:
        f.write(final_gcode)


def starting_gcode():
    gcodelist = []

    # Initialize the plotter
    gcodelist.append("G21 ; Set units to millimeters\n")
    gcodelist.append("G90 ; Use absolute positioning\n")
    gcodelist.append("G28 X0 Y0 ; Home X and Y axes\n")  # Home only X and Y axes
    gcodelist.append("G4 P2000 ; Wait for 2 seconds to ensure homing is completed\n")
    gcodelist.append("G92 E0 ; Reset extruder position\n")

    # Move to the starting point
    gcodelist.append("G1 X10 Y10 F1500\n")

    return "".join(gcodelist)


if __name__ == "__main__":
    main()
