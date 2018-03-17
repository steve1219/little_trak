# little_trak
A program to control a robot using the Explorer Hat Pro from Pimoroni.

Uses the capacative touch pads to place directions into a list, this list is then used to drive the motors.
The directions are as follows:
1 - Forwards
2 - Backwards
3 - Left
4 - Right
5 - Enter (used when desired program has been entered to switch into movement mode)

Please note this program will require the libraries from Pimoroni for the Explorer Hat Pro.
These can be obtained by entering the following into a terminal:
curl https://get.pimoroni.com/explorerhatpro | bash

Alternatively, if you are using Raspbian they provide a gui installer by running the following in a terminal:
sudo apt-get install pimoroni
This will then be in the menu under accessories or can be run from the terminal by entering:
pimoroni-dashboard  

