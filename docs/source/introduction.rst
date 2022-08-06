Introduction
============

``gazerr`` is a Python package which provide a command line utility to estimate the
error distribution of gaze duration measurements. It requires
a calibration file from an eye tracking application that indicates the underlying
error in the fixation model, then uses that to generate the expected distribiution
of true duration for any measurement.

Motivation
**********

The use of eye fixation models to estimate gaze duration (or dwell time) in Area of
Interest studies (AOI) was discussed by Holmqvist et al (2012). The
authors simulated the impact of gaze fixation error by adding noise according to
manufacturer specifications to data sets of low margin areas of interest. We extend
this idea to calculate probabilistic bounds on the error in gaze duration using
calibration data as a source of noise distribution that is specific to both the
study participants and the device/environment of the study. The result is an open
source application that may be used by a wide variety of reserachers to provide
error bounds on any gaze duration measurements.


