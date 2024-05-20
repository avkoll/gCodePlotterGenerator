import subprocess


def svg_to_gcode(input_file, output_gcode):
    try:
        # Run Vpype commands
        commands = [
            "vpype",
            "read", input_file,
            "gwrite",
            "--profile",
            "gcode",
            output_gcode
        ]

        # Execute commands
        result = subprocess.run(commands, check=True, capture_output=True, text=True)
        print(result.stdout)
        print(f"G-code saved to: {output_gcode}")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")


def main():
    svg_in = "../svgs/star-svgrepo-com.svg"
    output_file = "./gcodes/output.gcode"

    svg_to_gcode(svg_in, output_file)


main()
