Sure! Here's a README template for your project:

---

# Plotter Table Project

## Overview

This project involves creating a table that integrates a Raspberry Pi and an Arduino to control a plotter. The table is designed to move along the X and Y axes to create precise 2D drawings based on G-code instructions.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Hardware Requirements](#hardware-requirements)
4. [Software Requirements](#software-requirements)
5. [Setup Instructions](#setup-instructions)
6. [Usage](#usage)
7. [Troubleshooting](#troubleshooting)
8. [Contributing](#contributing)
9. [License](#license)
10. [Acknowledgments](#acknowledgments)

## Introduction

This project I aimed to repurpose a Monoprice Maker Select V2 3D printer into a 2D plotter and attach it to a table to mimic 
those designed by [Sisyphus Industries](https://sisyphus-industries.com/). I ended up designing a 2-D plotter 
and just used some parts from the printer. The plotter is 
controlled using a Raspberry Pi and an Arduino running [GRBL](https://github.com/grbl/grbl) firmware. The Raspberry Pi sends G-code files to the Arduino,
(using [UGS](https://winder.github.io/ugs_website/)) 
which then drives the stepper motors to create precise movements along the X and Y axes.

## Features

- Precise 2D plotting using stepper motors.
- Controlled via G-code commands.
- Integration with Raspberry Pi for processing and sending G-code.
- Uses an Arduino with GRBL firmware for motor control.
- Receives commands through the UGS web pendant accessible through wi-fi.


## Hardware I Used

- Raspberry Pi 3 B+
- Arduino Uno R3
- Arduino CNC shield
- Stepper motors and TMC2208 motor drivers 
- Power supply (from the old 3-D printer)
- LED Strip
- Table from craigslist
- 16" round piece of glass
- Wiring and connectors


## Software Requirements

- Raspbian OS 
- Python3
- GRBL firmware (installed on Arduino)
- UGS installed on Raspberry Pi.
- Vpype to generate GCode from SVG images
- 

## Setup Instructions

1. **Hardware Assembly:**
    - Assemble the plotter frame using the salvaged parts from the Monoprice Maker Select V2.
    - Connect the stepper motors to the motor drivers and the drivers to the Arduino.
    - Connect the Arduino to the Raspberry Pi using a USB cable.
    - Ensure all power connections are secure and properly insulated.

2. **Software Setup:**
    - Install Raspbian OS on the Raspberry Pi.
    - Install Python and `pySerial` on the Raspberry Pi:
      ```sh
      sudo apt-get update
      sudo apt-get install python3 python3-pip
      pip3 install pyserial
      ```
    - Flash the GRBL firmware onto the Arduino:
      - Follow the instructions [here](https://github.com/gnea/grbl) to install GRBL on your Arduino.
    - Clone the project repository to the Raspberry Pi:
      ```sh
      git clone https://github.com/yourusername/plotter-table-project.git
      cd plotter-table-project
      ```

## Usage

1. **Starting the Plotter:**
    - Power on the Raspberry Pi and Arduino.
    - Navigate to the project directory on the Raspberry Pi and run the Python script to send G-code:
      ```sh
      python3 send_gcode.py
      ```
    - The plotter will start drawing based on the provided G-code file.

2. **G-code Generation:**
    - Use any CAD software to design your drawing and export it as a G-code file.
    - Place the G-code file in the project directory on the Raspberry Pi.

## Troubleshooting

- **Motor Not Moving:**
  - Check connections between the Arduino, stepper drivers, and motors.
  - Ensure the GRBL firmware is correctly installed on the Arduino.
  
- **Incorrect Drawing:**
  - Verify the G-code file for errors.
  - Check the calibration of the plotter's axes.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the creators of GRBL for their excellent firmware.
- Inspiration for this project came from [Sisyphus Industries](https://sisyphus-industries.com/)

