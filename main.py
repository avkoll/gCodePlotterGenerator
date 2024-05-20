def generate_2d_plotter_gcode(points):
    gcode = ["G21 ; Set units to millimeters", "G90 ; Use absolute positioning", "G28 ; Home all axes",
             "G92 E0 ; Reset extruder position"]

    # Initialize the plotter

    # Move to the starting point
    start_point = points[0]
    gcode.append(f"G1 X{start_point[0]:.2f} Y{start_point[1]:.2f} F1500")

    # Plot the points
    for point in points[1:]:
        x, y = point
        gcode.append(f"G1 X{x:.2f} Y{y:.2f} F1500")

    # Finish the plot
    gcode.append("G28 ; Home all axes")
    gcode.append("M84 ; Disable motors")

    return "\n".join(gcode)


def main():
    # Define the points to plot
    points = [(10, 10), (10, 50), (50, 50), (50, 10), (10, 10)]

    gcode = generate_2d_plotter_gcode(points)
    with open('plotter_output.gcode', 'w') as f:
        f.write(gcode)


if __name__ == "__main__":
    main()
