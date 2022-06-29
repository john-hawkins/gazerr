#!/bin/bash

# NOTE: This script depends on the output of RUN_EXPERIMENTS.sh

# Generate the Measured Versus Expected Plot
python scripts/plot_measured_vs_expected.py

# Generate the fixation versus duration error
python scripts/plot_expected_errors.py

