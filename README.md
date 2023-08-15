# TDConvED Implementation

This project offers an implementation based on the TDConvED research by Jingwen Chen et al. For an in-depth study, refer to the original paper [here](https://arxiv.org/abs/1905.01077v1?fbclid=IwAR3PIjrHeMBZYcXfPm6J6mIkndjihtIlqsAjQopD_g-TlVvuwZWzEBMf-1Y).

## Prerequisites
- Dataset (available on Kaggle)
- Python libraries: pytube, ffmpeg-python

## Installation

1. Download the required dataset from Kaggle.
2. Install necessary Python packages using the commands:
```bash
pip install pytube ffmpeg-python
```
## Dataset Update

An enhanced dataset in video format is now available on Kaggle, comprising both the training and test sets.

## Execution Guide

For a comprehensive guide on executing the implementation, kindly refer to the [official GitHub repository](https://github.com/b05902062/TDConvED).

## Bug Fixes & Troubleshooting

- **Pytube Update Issue**: In case of issues stemming from Pytube updates, make the following change in `cipher.py`:
Replace:
```python
var_regex = re.compile(r"^\w+\W")
```
With
```python
var_regex = re.compile(r"^\$*\w+\W")
```

## Reproducing Dataset from JSON
To reproduce the dataset from its JSON format:

Uncomment the respective test section within acquire_images.
Execute the program. You'll be prompted to grant YouTube access to your device. Adhere to the provided instructions to proceed.


