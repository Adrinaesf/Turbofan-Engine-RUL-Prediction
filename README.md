# Turbofan Engine Remaining Useful Life (RUL) Prediction

Predicts how many operating cycles a jet engine has left before failure,
using sensor time-series data from NASA's CMAPSS FD001 dataset.

## The problem
Each engine in the dataset ran from a healthy state to failure, with 21
sensors (temperature, pressure, speed, etc.) recorded every cycle. Given
an engine's current sensor readings, predict its Remaining Useful Life
(RUL) in cycles.

## Setup

1. **Create and activate a virtual environment** (from this folder):
   ```
   python -m venv venv
   source venv/bin/activate        # Mac/Linux
   venv\Scripts\activate           # Windows
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Download the dataset:**
   Search "NASA CMAPSS Jet Engine Simulated Data" — it's on NASA's
   Prognostics Data Repository and also mirrored on Kaggle. Grab
   `train_FD001.txt`, `test_FD001.txt`, and `RUL_FD001.txt`, and place
   all three in `notebooks/data/`.

4. **Explore the data** (open in Jupyter or VS Code's notebook viewer):
   ```
   notebooks/01_exploration.ipynb
   ```

5. **Run the baseline model:**
   ```
   python src/train_baseline.py
   ```
   This should print an MAE and RMSE (in cycles) — that's your baseline
   accuracy to try to beat as you iterate.

## Project structure
```
turbofan-rul-prediction/
├── notebooks/
│   ├── data/                    <- put train_FD001.txt, test_FD001.txt,
│   │                                RUL_FD001.txt here (not tracked by git)
│   └── 01_exploration.ipynb     <- start here to look at the data
├── src/
│   ├── data_loader.py    <- loading the raw files, computing RUL
│   ├── features.py       <- which sensor columns to use as features
│   └── train_baseline.py <- trains a Random Forest baseline, evaluates
│                              on the official FD001 test set
├── requirements.txt
└── README.md
```

The baseline evaluates against the **official FD001 test split**: train
on `train_FD001.txt`, predict RUL for the last recorded cycle of each
engine in `test_FD001.txt`, and score those predictions against the
true values in `RUL_FD001.txt`. This is the standard way this dataset
gets evaluated, so your results are directly comparable to published
benchmarks if you want to compare later.

## Notes / next steps
- The baseline splits data **by engine**, not by row — this matters,
  see the comment in `train_baseline.py` for why.
- Good next steps once the baseline runs: try XGBoost instead of Random
  Forest, engineer rolling-average features (trend over the last N
  cycles instead of a single snapshot), or clip RUL at a max value
  (a common trick in this dataset — see the piecewise linear RUL
  approach used in published work on FD001).