RT1 Assignment1
================================
The goal for this project was to make the robot collect all the boxes and stack them together in the center.

Python Robotics Simulator
================================

This is a simple, portable robot simulator developed by [Student Robotics](https://studentrobotics.org).
Some of the arenas and the exercises have been modified for the Research Track I course

Installing and running
----------------------

The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Pygame, unfortunately, can be tricky (though [not impossible](http://askubuntu.com/q/312767)) to install in virtual environments. If you are using `pip`, you might try `pip install hg+https://bitbucket.org/pygame/pygame`, or you could use your operating system's package manager. Windows users could use [Portable Python](http://portablepython.com/). PyPyBox2D and PyYAML are more forgiving, and should install just fine using `pip` or `easy_install`.

## Troubleshooting

When running `python run.py <file>`, you may be presented with an error: `ImportError: No module named 'robot'`. This may be due to a conflict between sr.tools and sr.robot. To resolve, symlink simulator/sr/robot to the location of sr.tools.

On Ubuntu, this can be accomplished by:
* Find the location of srtools: `pip show sr.tools`
* Get the location. In my case this was `/usr/local/lib/python2.7/dist-packages`
* Create symlink: `ln -s path/to/simulator/sr/robot /usr/local/lib/python2.7/dist-packages/sr/`


Robot API
---------

The API for controlling a simulated robot is designed to be as similar as possible to the [SR API][sr-api].

### Motors ###

The simulated robot has two motors configured for skid steering, connected to a two-output [Motor Board](https://studentrobotics.org/docs/kit/motor_board). The left motor is connected to output `0` and the right motor to output `1`.

The Motor Board API is identical to [that of the SR API](https://studentrobotics.org/docs/programming/sr/motors/), except that motor boards cannot be addressed by serial number. So, to turn on the spot at one quarter of full power, one might write the following:

```python
R.motors[0].m0.power = 25
R.motors[0].m1.power = -25
```

### The Grabber ###

The robot is equipped with a grabber, capable of picking up a token which is in front of the robot and within 0.4 metres of the robot's centre. To pick up a token, call the `R.grab` method:

```python
success = R.grab()
```

The `R.grab` function returns `True` if a token was successfully picked up, or `False` otherwise. If the robot is already holding a token, it will throw an `AlreadyHoldingSomethingException`.

To drop the token, call the `R.release` method.

Cable-tie flails are not implemented.

### Vision ###

To help the robot find tokens and navigate, each token has markers stuck to it, as does each wall. The `R.see` method returns a list of all the markers the robot can see, as `Marker` objects. The robot can only see markers which it is facing towards.

Each `Marker` object has the following attributes:

* `info`: a `MarkerInfo` object describing the marker itself. Has the following attributes:
  * `code`: the numeric code of the marker.
  * `marker_type`: the type of object the marker is attached to (either `MARKER_TOKEN_GOLD`, `MARKER_TOKEN_SILVER` or `MARKER_ARENA`).
  * `offset`: offset of the numeric code of the marker from the lowest numbered marker of its type. For example, token number 3 has the code 43, but offset 3.
  * `size`: the size that the marker would be in the real game, for compatibility with the SR API.
* `centre`: the location of the marker in polar coordinates, as a `PolarCoord` object. Has the following attributes:
  * `length`: the distance from the centre of the robot to the object (in metres).
  * `rot_y`: rotation about the Y axis in degrees.
* `dist`: an alias for `centre.length`
* `res`: the value of the `res` parameter of `R.see`, for compatibility with the SR API.
* `rot_y`: an alias for `centre.rot_y`
* `timestamp`: the time at which the marker was seen (when `R.see` was called).

For example, the following code lists all of the markers the robot can see:

```python
markers = R.see()
print "I can see", len(markers), "markers:"

for m in markers:
    if m.info.marker_type in (MARKER_TOKEN_GOLD, MARKER_TOKEN_SILVER):
        print " - Token {0} is {1} metres away".format( m.info.offset, m.dist )
    elif m.info.marker_type == MARKER_ARENA:
        print " - Arena marker {0} is {1} metres away".format( m.info.offset, m.dist )
```

[sr-api]: https://studentrobotics.org/docs/programming/sr/


Flowchart
================================
![RT1_A1_FlowChart](https://github.com/tanvirrsajal/RT1_Assignment1/assets/148011962/3b9e1e5d-f2f1-44ca-9847-999364b8411d)



Description:
================================

To make the robbot grab and put all the boxes together we defined a few functions to find the box, to grab the box, to realease the box, to find the drop location. A list is also created in order to store the information of the boxes it has already grabbed so that it doesn't grab the same box again and for finding the drop location. The funtions we defined are given below.

<h3><ins>Drive</ins></h3>

With this function the robot can go forward and also backward if the value is negative. To drive the robot it is needed to give the a speed and declare a span of time(for how long the robot will drive in secods).

<h3><ins>Turn</ins></h3>

With this function the robot can move left or right. To make it work same speed is given to both the wheels of the robot but in opposite signs. With the speed we also need to give the value for the time (in seconds).

<h3><ins>FindBox</ins></h3>

This function searches for the nearest box. The robot uses R.see() attribiute to look for the boxes. If the robot can not find any box, it returns -1 for all the parameters. It only searches for boxes that are not in the GrabbedBox list.

<h3><ins>GrabBox</ins></h3>

This function grabs the box when it is within reach of the robot's grabber. It uses the attribiute R.grab() to grab the box. The robot uses a_th and d_th to determine the distance and the angle between itself and the box. It adjusts the angle or distance accordingly with respect to the box.

<h3><ins>FindDropLocation</ins></h3>

This function searches for the robot to find the nearest box it has previously dropped. The robot uses R.see() attribiute to look for the boxes that it has previously dropped. If the robot can not find any box, it returns -1 for all the parameters. It searches for boxes that are in the GrabbedBox list.


<h3><ins>ReleaseBox</ins></h3>

This function releases the box it is holding when the robot reaches the desired location. It uses the attribiute R.release() to release the box. The robot uses a_th and d_th to determine the distance and the angle between itself and the nearest box it has previously grabbed. It adjusts the angle or distance accordingly with respect to that box.

Giving instruction to the robot to do the task
-----------------------------
After defining the functions we make the robot search for boxes. When the robot finds the box it will grab the box using GrabBox() and R.grab(). Then we will make the robot go towards the center of the window. Then the robot releases the box using ReleaseBox() and R.release(). After releasing the box the robot turns and goes a little behind to avoid colliding with the box it has just dropped. The information of the dropped box is stored after releasing the box. Then a loop is created for the rest of the boxes. The process is the same, it will search for boxes, grab the box, find a drop location (it will search for the nearest box it has previously dropped), then release the box at the drop location and finally store the information of the dropped box in the GrabbedBox list. The loop will continue until the robot releases all the boxes.



Run the program
================================

To run the program the following command should be given.

```bash
$ python run.py assignment.py
```


Outcome
================================


![Screenshot 2023-11-16 213615](https://github.com/tanvirrsajal/RT1_Assignment1/assets/148011962/8922324e-ec8e-44d3-aac2-69898ba67f73)

Initial Phase


![Screenshot 2023-11-16 214024](https://github.com/tanvirrsajal/RT1_Assignment1/assets/148011962/13dc43d6-34fd-44a7-a091-1138770f7e24)


Final Phase
