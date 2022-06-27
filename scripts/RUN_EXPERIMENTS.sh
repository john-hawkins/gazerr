#!/bin/bash

mkdir results/MREC_MAE_25
python ./gazerr-runner.py data/validation_25_MAE.csv 400 1000 40,40 340,290 results/MREC_MAE_25

mkdir results/MREC_MAE_50
python ./gazerr-runner.py data/validation_50_MAE.csv 400 1000 40,40 340,290 results/MREC_MAE_50

mkdir results/MREC_MAE_75
python ./gazerr-runner.py data/validation_75_MAE.csv 400 1000 40,40 340,290 results/MREC_MAE_75

mkdir results/MREC_MAE_100
python ./gazerr-runner.py data/validation_100_MAE.csv 400 1000 40,40 340,290 results/MREC_MAE_100

mkdir results/MREC_MAE_125
python ./gazerr-runner.py data/validation_125_MAE.csv 400 1000 40,40 340,290 results/MREC_MAE_125

mkdir results/MREC_MAE_150
python ./gazerr-runner.py data/validation_150_MAE.csv 400 1000 40,40 340,290 results/MREC_MAE_150


