Usage Guide
===========

Command Line Utility
^^^^^^^^^^^^^^^^^^^^

After installation with pip, gazerr can be invoked from the command line:

.. code-block:: bash

    > gazerr


Without parameters it will display the usage instructions :

.. code-block:: bash

    usage: gazerr-runner.py [-h]
                        calibration_data measurement session_length
                        target_top_left target_bottom_right results
    gazerr-runner.py: error: the following arguments are required: calibration_data, measurement, session_length, target_top_left, target_bottom_right, results



All parameters are mandatory. They express that the error distibution will be specific to 
a particular calibration file, and will calculate the expected duration distribition for
a given measurement, within a given session length for an Area of Interest (AOI) with the
specified coordinates on screen.

The final parameter is a path to a directory where a collection of raw results will be
written including the posterior distributions of gazeduration for all given measurements
less than the session length. Note that the allowable measurements are quantised for 
computational efficiency at intyervals of 50ms. 


Python Package Usage
^^^^^^^^^^^^^^^^^^^^

You can import the gazerr package within python and then make use of the
functions directly.

.. code-block:: python

    import gazerr as gazerr
    dir(gazerr)


This will list the functions avaiable inside the `gazerr` package
 
