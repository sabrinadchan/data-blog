Title: Splitting CSV files by column values with pandas
Date: 2018-12-30 16:00
Category: posts
Tags: python, pandas, data science
Slug: splitting-csv-pandas
Authors: Spencer Chan
Summary: A recipe for splitting delimited text files by a given column's values into separate files using pandas.

In my first *real* post, I'm going to share a construct that I use often. Below is a recipe for splitting delimited text files into separate files based on a chosen column's values using pandas. Suppose for example, you had a dataset of all reported Bigfoot sightings in the US over a 50-year period, and that one of the columns in the dataset listed the state where the sightings occurred. The following script could split the dataset into separate files for each state with a Bigfoot sighting.

First, load the data. Change the delimeter as needed.
```python
import pandas as pd

data_filepath = "cryptid_data/bigfoot_sightings.csv"
delimeter = ","
df = pd.read_csv(data_filepath, sep=delimeter)
```

Next, choose the column to split the file by. If the column contains null values, you can either drop the corresponding rows or write those rows to their own file. To do the latter, it is a good idea to replace all of the null values with a string describing the missing data. This string will appear in the output filename.
```python
split_by_col = "state"
df[split_by_col].fillna("unknown-state", inplace=True)
```

Loop over each of the possible column values and write the data to a file named after the current value. The new files will be saved to the same directory as the input file. For example, the California sightings will be written to a file called *bigfoot_sightings_CA.csv* (or something similar), and all the files will be saved to the directory `cryptid_data`.
```python 
import os

data_directory = os.path.dirname(data_filepath)
for col_value in df[split_by_col].unique():
    col_value_df = df[df[split_by_col] == col_value]

    basename, file_ext = os.path.splitext(os.path.basename(data_filepath))
    new_filename = "{}_{}{}".format(basename, col_value, file_ext)
    new_filepath = os.path.join(data_directory, new_filename)
    
    col_value_df.to_csv(new_filepath, index=False, sep=delimeter)
```

I imagine future posts will be longer, but I wanted to share a small teaser to tide you over while I curate older work into a form suitable for blog posts. 