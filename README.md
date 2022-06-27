# Gaze Duration Error

Gazerr is an application for estimating the expected error in a gaze duration
measurement derived from repeated application of a point of gaze model.

The method requires an input dataset of validation points from the point
of gaze predictive model. This data is used to generate the probability 
distribution of true gaze durations given a measured gaze duration.

### Usage

The application can be used from the command line by passing in a path to the
calibration file and the parameters for the duration measurement that will be
bounded. Note: that the penultimate two parameters should be comma separated sets
of integers that depict x,y coordiantes in pixels. The measurement length and
session lenth should be expressed in milliseconds.

The final parameter is a path to a directory in which to store the raw results

```
gazerr <CALIBRATION> <MEASUREMENT> <SESSION> <TARGET TOP LEFT> <TARGET BOTTOM RIGHT> <RESULTS>
```

To use the application without installing it you can employ the runner script.
Example below, using the supplied calibration data:

```
mkdir results/MREC_MAE_50
python ./gazerr-runner.py data/validation_50_MAE.csv 400 1000 40,40 340,290 results/MREC_MAE_50
```

Alternatively, you may inspect the code and use the library functions directly
inside your own application.


### Documentation

Preparing a paper that outlines the technique here: [paper/paper.tex](paper/paper.tex)

Intending to submit to this conference
http://asyu.inista.org/?language=EN#:~:text=The%20Innovations%20in%20Intelligent%20Systems,will%20be%20English%20and%20Turkish.





