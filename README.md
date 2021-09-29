# Gaze Duration Error

The purpose of this repository is to develop a methodology for estimating
the amount of error in a gaze duration measurement derived from an point 
of gaze model.

The system requires an input dataset of calibration points from the point
of gaze predictive model. This data is used to generate a probability 
distribution of true and false fixation events within pre-specified screen
regions.

These distributions are then used to run Monte-Carlo simualtions to estimate
the error distribution over gaze duration measurements. The user specifies
the parameter of the simulation and receives calibration bounds on gaze duration
estimations.


### Usage

```
gazerr <CALIBRATION FILE> <SESSION LENGTH> <TRUE GAZE DURATION>
```


