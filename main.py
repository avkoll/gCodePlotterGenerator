from svgConverter import generate_curves  # Converts a svg file to gcode


def starting_gcode():
    gcodelist = []

    # Initialize the plotter
    gcodelist.append("G21 ; Set units to millimeters\n")
    gcodelist.append("G90 ; Use absolute positioning\n")
    gcodelist.append("G28 X0 Y0 ; Home X and Y axes\n")  # Home only X and Y axes
    gcodelist.append("G4 P2000 ; Wait for 2 seconds to ensure homing is completed\n")
    gcodelist.append("G92 E0 ; Reset extruder position\n")

    # Move to the starting point
    gcodelist.append("G1 X100 Y100 F1500\n")
    #gcodelist.append("G91\n")

    return "".join(gcodelist)


def create_shapes():
    generate_curves("./svgs/star-984.svg")

    # read from drawing.gcode 'buffer'
    with open('drawing.gcode', 'r') as f:
        lines = f.readlines()

    # Skip certain lines and flatten the list
    lines_to_append = (
                       lines[5:] +
                        [
                        # Finish the plot
                        "G28 X0 Y0 ; Home X and Y axes\n",
                        "G4 P2000 ; Wait for 2 seconds to ensure homing is completed\n",
                        "M84 ; Disable motors\n"])

    return "".join(lines_to_append)


def scale_gcode(gcode_file, output_file, scaling_factor):
    with open(gcode_file, 'r') as f:
        lines = f.readlines()

    scaled_lines = []
    for line in lines:
        if line.startswith('G1') or line.startswith('G0'):
            parts = line.split(' ')
            new_parts = []
            for part in parts:
                if part.startswith('X') or part.startswith('Y'):
                    coordinate = float(part[1:]) * scaling_factor
                    new_parts.append(f'{part[0]}{coordinate:.6f}')
                else:
                    new_parts.append(part)
            scaled_lines.append(' '.join(new_parts) + '\n')
        else:
            scaled_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(scaled_lines)


def main():
    gcode = [starting_gcode()]

    gcode.append(create_shapes())

    with open('plotter_output.gcode', 'w') as f:
        f.writelines(gcode)


if __name__ == "__main__":
    main()
