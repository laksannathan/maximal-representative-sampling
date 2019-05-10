## Discriminative Machine Learning for Maximal Representative Subsampling
This project deals with selection bias in social sciences. Discriminative learners are trained and combined to reduce the effects of bias in psychological and political studies. With positive-unlabeled learning and artificial data synthesis, performance estimation becomes more accurate in a non-traditional setting.

## Motivation
Apply machine learning to the fields of survey analytics.

## Installation
Python 3.6+ with Jupyter notebook and WEKA are necessary to get a development env running. If random_state is not provided, any init will come close to analysed results.

## Project Structure
    .
    ├── ...
    ├── data                    # data sources: GESIS and GBS
    |   ├── raw input           # survey results
    |   └── ._proc.csv          # preprocessed (ml ready) data
    ├── docs                    # documentation on data sources
    ├── src                     # source code: Python, WEKA
    └── tex                     # thesis: LaTex Code
        ├── paper               # MRS thesis
        └── fig                 # figures, tables and plots

## ToDo

- Temperature sampling (https://en.wikipedia.org/wiki/Softmax_function
)

- KS-test instead of ROC-curve (https://www.sciencedirect.com/science/article/abs/pii/S0167865513000020)

## License
MIT © [Laksan Nathan]