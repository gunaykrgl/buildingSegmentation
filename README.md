---
title: building_footprint_segmentation
app_file: demo.py
sdk: gradio
sdk_version: 4.24.0
---
A U-Net model for segmenting buildings from satellite imagery

A binary segmentation mask (of the same height and width with the input image) should be created The segmentation mask should have a value of 1 at pixels where there is a building and 0 at other pixels.

The figure below showcases the input and output image expected. In the mask pixels that correspond to pixels in the input image are white and background is black.

![Expected input and output](images/task_definition.png)

# Data
The data used in this project is sourced from [Road and Building Detection Datasets](https://www.cs.toronto.edu/~vmnih/data/) with the following citation:

```
@phdthesis{MnihThesis,
    author = {Volodymyr Mnih},
    title = {Machine Learning for Aerial Image Labeling},
    school = {University of Toronto},
    year = {2013}
}

```

For the ease of use, relevant parts of this dataset was sourced from [kaggle.com](https://www.kaggle.com/datasets/balraj98/massachusetts-buildings-dataset)
