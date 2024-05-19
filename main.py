from svgConverter import generate_curves  # Converts a svg file to gcode


def generate_2d_plotter_gcode(points):


    # Plot the points
    for point in points[1:]:
        x, y = point
        gcode.append(f"G1 X{x:.2f} Y{y:.2f} F1500")



    return "\n".join(gcode)


def starting_gcode(gcodelist):

    # Initialize the plotter
    gcodelist.append("G21 ; Set units to millimeters")
    gcodelist.append("G90 ; Use absolute positioning")
    gcodelist.append("G28 X0 Y0 ; Home X and Y axes")  # Home only X and Y axes
    gcodelist.append("G4 P2000 ; Wait for 2 seconds to ensure homing is completed")
    gcodelist.append("G92 E0 ; Reset extruder position")

    # Move to the starting point
    gcodelist.append(f"G1 X10 Y10 F1500")

    return "\n".join(gcodelist)


def create_shapes():
    generate_curves("./svgs/star-svgrepo-com.svg")

    # Finish the plot
    gcode.append("G28 X0 Y0 ; Home X and Y axes")  # Home only X and Y axes
    gcode.append("G4 P2000 ; Wait for 2 seconds to ensure homing is completed")
    gcode.append("M84 ; Disable motors")


def main():
    gcode = []



    with open('plotter_output.gcode', 'w') as f:
        f.write(gcode)


if __name__ == "__main__":
    main()
