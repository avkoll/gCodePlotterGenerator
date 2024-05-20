import subprocess


def svg_to_gcode(input_file, output_gcode):
    try:
        # Run Vpype commands
        commands = [
            "vpype",
            "read", input_file,
            "linemerge",
            "linesimplify",
            "linesort",
            "write", "--gwrite", output_gcode
        ]

        # Execute commands
        result = subprocess.run(commands, check=True, capture_output=True, text=True)
        print(result.stdout)
        print(f"G-code saved to: {output_gcode}")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")


def main():
    svg_in = "./svgs/star-984.svg"
    output_file = "./gcodes/star-984"

    svg_to_gcode(svg_in, output_file)


main()
