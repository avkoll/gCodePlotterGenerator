G21 ; Set units to millimeters
G90 ; Use absolute positioning

$H ; Home the machine

G1 F1000 ; Set feed rate to 1000 mm/min

G0 X10 Y10 ; Move to position X10 Y10
G0 X20 Y20 ; Move to position X20 Y20
G0 X10 Y20 ; Move to position X10 Y20
G0 X20 Y10 ; Move to position X20 Y10
G0 X0 Y0 ; Move back to the origin

$H ; Home the machine again
