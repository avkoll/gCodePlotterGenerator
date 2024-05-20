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
    gcodelist.append("G1 X0 Y0 F1500\n")
    #gcodelist.append("G91\n")

    return "".join(gcodelist)


def create_shapes():
    generate_curves("./svgs/star-svgrepo-com.svg")

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


def main():
    gcode = [starting_gcode()]

    gcode.append(create_shapes())

    with open('plotter_output.gcode', 'w') as f:
        f.writelines(gcode)


if __name__ == "__main__":
    main()
