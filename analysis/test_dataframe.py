# Data 515, Software Engineering for Data Scientists
# Homework 3
# M.S. Data Science, University of Washington, Spr. 2019.
# Francisco Javier Salido Magos.

from dataframe import comp_dataframe
from dataframe import validateSizeDF
import pytest

import requests
import io
import copy
import pandas as pd


# Testing wrong number of columns leads to ValueError
def test_exception():
    df_file = ("dataframe.csv")
    df = pd.read_csv(df_file, header=0)
    columns_df = list(df.columns)
    data_types_df = list(df.dtypes)
    url = ("http://data-seattlecitygis.opendata.arcgis.com/datasets/"
           "a2e1128bd7a041358ce455c628ec9834_8.csv")
    req = requests.get(url)
    raw_df = pd.read_csv(io.StringIO(req.text))
    try:
        validateSizeDF(raw_df, columns_df)
        assert(not comp_dataframe(raw_df))
    except ValueError:
        assert(True)


# Testing correct number of columns and other requirements is True
def test_one_shot1():
    df_file = ("dataframe.csv")
    df = pd.read_csv(df_file, header=0)
    columns_df = list(df.columns)
    data_types_df = list(df.dtypes)
    url = ("http://data-seattlecitygis.opendata.arcgis.com/datasets/"
           "a2e1128bd7a041358ce455c628ec9834_8.csv")
    req = requests.get(url)
    raw_df = pd.read_csv(io.StringIO(req.text))
    good_df = raw_df[["X", "Y", "TYPE", "SCHOOL", "WEBSITE"]]
    good_df = good_df.reindex(sorted(good_df.columns), axis=1)
    assert(comp_dataframe(good_df))


# Testing column with wrong data type results in False
def test_edgetest1():
    df_file = ("dataframe.csv")
    df = pd.read_csv(df_file, header=0)
    columns_df = list(df.columns)
    data_types_df = list(df.dtypes)
    url = ("http://data-seattlecitygis.opendata.arcgis.com/datasets/"
           "a2e1128bd7a041358ce455c628ec9834_8.csv")
    req = requests.get(url)
    raw_df = pd.read_csv(io.StringIO(req.text))
    bad_df = raw_df[["X", "Y", "TYPE", "SCHOOL", "WEBSITE"]]
    bad_df = bad_df.reindex(sorted(bad_df.columns),axis=1)
    bad_df["WEBSITE"] = 1
    assert(not comp_dataframe(bad_df))


# Testing NaN in data results in False
def test_edgetest2():
    df_file = ("dataframe.csv")
    df = pd.read_csv(df_file, header=0)
    columns_df = list(df.columns)
    data_types_df = list(df.dtypes)
    url = ("http://data-seattlecitygis.opendata.arcgis.com/datasets/"
           "a2e1128bd7a041358ce455c628ec9834_8.csv")
    req = requests.get(url)
    raw_df = pd.read_csv(io.StringIO(req.text))
    bad_df = raw_df[["X", "Y", "TYPE", "SCHOOL", "WEBSITE"]]
    bad_df = bad_df.reindex(sorted(bad_df.columns),axis=1)
    bad_df.iloc[0, 3] = 'nan'
    assert(not comp_dataframe(bad_df))
