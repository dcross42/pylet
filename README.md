# pylet: Python ETL Framework 

PyLET is intended to be a flexible and extensible framework for designing ETL pipelines and procedures in python.

Create Extractors to extract data, Transformers to transform data, and Loaders to load data.

The goal is to allow developers and analysts to take what they need and leave out what they don't need.

Using dbt to transform data once it is in a warehouse? Just use an extractor and a loader to get your data into the warehouse.

Have a data science project and want to focus your efforts on modeling and analysis? Use an extractor and transformers to get the data where you need it in the format you want it.

