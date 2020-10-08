#  A* maze pathfinder with pygame

This project is a simple maze solver that uses the A* algorithm to find the best path and displays it using pygame library


##  Getting started
Requirements:

- python3.8^

To install the project:

    pip3 install poetry
    poetry shell
    python ui.py

### Known installation problem:
If poetry fails to install pygame use:

    sudo apt-get install python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev


## Important files:
- maze.txt: stores the actual maze (0 is walk-able and 1 is not)
- config.py: config file for the project
- astar.py: the actual A* algorithm
- structures.py: contains aditional structures used for the A*
- ui.py: the UI part (pygame)
