# Data 515, Software Engineering for Data Scientists
# Homework 3
# M.S. Data Science, University of Washington, Spr. 2019.
# Francisco Javier Salido Magos.

import requests
import io
import copy
import pandas as pd

from dataframe import test_create_dataframe
from dataframe import validateSizeDF

# Read dataframe created in homework 2.
df_file = ("c:/Users/Castor18/OneDrive/MSDS_UW/Data515_Spr19_Sw_Eng/"
           "Session3/Homework3/homework-3-4-testing-exceptions-"
           "and-coding-style-PrivacyEngineer/analysis/dataframe.csv")
df = pd.read_csv(df_file, header=0)
# Extracting column names and data types.
columns_df = list(df.columns)
data_types_df = list(df.dtypes)

# Read data we are going to use for comparison tests.
url = ("http://data-seattlecitygis.opendata.arcgis.com/datasets/"
       "a2e1128bd7a041358ce455c628ec9834_8.csv")
req = requests.get(url)
raw_df = pd.read_csv(io.StringIO(req.text))


# Should be good, exception is thrown because of incorrect number of columns.
def test_exception1():
    try:
        assert(test_create_dataframe(raw_df))
    except ValueError:
        assert(True)

# Generating dataframe for next test.
good_df = raw_df[["X", "Y", "TYPE", "SCHOOL", "WEBSITE"]]
good_df = good_df.reindex(sorted(good_df.columns), axis=1)


# Should be good, dataframe has same number of columns.
def test_oneshot1():
    assert(test_create_dataframe(good_df))

# Modifying content of good_df for next test.
bad_df = copy.deepcopy(good_df)
bad_df["WEBSITE"] = 1


# Should fail, datatypes are incorrect.
def test_edgetest1():
    assert(not test_create_dataframe(bad_df))

# Adding NaN value to good_df
good_df.iloc[0, 3] = 'nan'


# Should fail, NaN value included.
def test_edgetest2():
    assert(not test_create_dataframe(good_df))
