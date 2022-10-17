# Download and install: 
- https://openrefine.org/download.html

# Why openrefine

<p>OpenRefine is designed for messy data. Said differently, if you have clean data that simply needs to be reorganized, you’re better off using Microsoft Excel, R, SAS, Python pandas or virtually any other database software. [Alex Petralia]</p>

# Todo

1. Text filter
2. Facet
3. Sort
4. Transform (Edit)
   * 4.1 Edit date (filter '{' then invert, filter '-', Edit cell --> transform --> value.toDate().toString("MM/dd/yyyy") )
   * 4.2 Add column based on this column (value.length()) --> Facet by numeric
   * 4.3 Split into multiple columns (Format digital)
   * 4.4 Edit columns by fetching URL
   * 4.5 Edit cells: Clustering methods https://docs.openrefine.org/manual/cellediting#clustering-methods

# Good tutorial
- https://evanwill.github.io/clean-your-data/
- https://www.youtube.com/watch?v=yTJ6x6zEQmI


# Big data handle?
- https://pandas.pydata.org/pandas-docs/stable/user_guide/scale.html
- Handle million rows of data: https://webscraper.io/blog/data-transformation-with-Open-Refine
- https://www.kaggle.com/code/robikscube/fast-data-loading-and-low-mem-with-parquet-files

