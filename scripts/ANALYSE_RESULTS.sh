#!/bin/bash

# NOTE: This script depends on the outputs of the folling scripts:
# RUN_EXPERIMENTS.sh
# RUN_BIAS_EXPERIMENTS.sh
# RUN_PRECISE_BIAS_EXPERIMENTS.sh
#

# Generate the Measured Versus Expected Plot
python scripts/plot_measured_vs_expected.py

# Generate the fixation versus duration error
python scripts/plot_expected_errors.py

# Error surface over MAE and Measured Duration
python scripts/plot_error_surface.py


