# Facebook Recruiting IV: Human or Robot?

> Team Member: Crystal Sun, Yixin Sun, Julia Tavares
>

## Table of Content

- Project Goal
- Data Source
- Data Preprocessing
  - [Reformatting SF Data](<https://github.com/crystalxs/human-or-robot/blob/master/data_cleaning.ipynb>)
  - [NYC Data Feature Engineering](<https://github.com/crystalxs/human-or-robot/blob/master/feature_engineering.ipynb>)
  - [SF Data Feature Engineering](<https://github.com/crystalxs/human-or-robot/blob/master/feature_engineering.ipynb>)
- [Modeling](#Modeling)
  - [K-means](<https://github.com/crystalxs/human-or-robot/blob/master/modeling_decision_tree.ipynb>)
  - [Bisecting K-Means](<https://github.com/crystalxs/human-or-robot/blob/master/modeling_random_forest.ipynb>)
- [Summary](#Summary)

## Project Goal

Can we identify different areas (residential areas, commuting center, commercial, etc) in a big city by traffic patterns?

Can we map the 2 largest cities in the US, San Francisco and New York City, by their traffic patterns?

These are the questions we want to answer. In this project, we tried to find parallels between the cities in terms of areas that have similar quantitative traffic patterns using distributed data system and unsupervised machine learning techniques. 

## Data Source

- **San Francisco taxi trip data: the epfl/mobility dataset**

  > Source: [CRAWDAD dataset epfl/mobility (v. 2009‑02‑24)](https://crawdad.org/epfl/mobility/20090224)

  This dataset contains mobility traces of taxi cabs in San Francisco, USA. It contains GPS coordinates of approximately 500 taxis collected over 2008-05-17 to 2008-06-10  in the San Francisco Bay Area. The original dataset has 4 columns for each taxi: timestamp, latitude, longitude, occupancy.

- **New York City taxi trip data: NYC TLC Trip Record Data** 

  > Source: [TLC Trip Record Data](<https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page>)

  This dataset contains mobility traces of taxi cabs in NYC. It contains GPS coordinates of yellow taxis collected over 2009-05. For each trip, the dataset contains the information of our interests including start latitude, start longitude, end latitude, end longitude, start timestamp, end timestamp.

## Data Preprocessing

The total size of our dataset is 2.5G. Thus we use MongoDB to store data, and Spark to query and process data, where SparkSQL for exploratory data analysis, and SparkML for building Machine Learning models.

AWS S3 -> MongoDB -> EC2 (Spark)


