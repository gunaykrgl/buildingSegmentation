# Building Footprint Segmentation
A U-Net model for segmenting buildings from satellite imagery

A binary segmentation mask (of the same height and width with the input image) should be created The segmentation mask should have a value of 1 at pixels where there is a building and 0 at other pixels.

The figure below showcases the input and output image expected. In the mask pixels that correspond to pixels in the input image are white and background is black.

![Expected input and output](https://raw.githubusercontent.com/gunaykrgl/buildingSegmentation/main/Notebook/task_definition.png)

The training and Machine-learning related code is found at [the Notebook](https://github.com/gunaykrgl/buildingSegmentation/blob/main/Notebook/Building_Segmentation.ipynb).

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

# Remote Running
You can try the application without installation by navigating to the following link:
[Building Footprint Segmentation](https://huggingface.co/spaces/gunayk3/building_footprint_segmentation)

## Screenshots
<picture>
<img src="https://raw.githubusercontent.com/gunaykrgl/buildingSegmentation/main/screenshots/scr1.png" width="600"/>
</picture>
<picture>
<img src="https://raw.githubusercontent.com/gunaykrgl/buildingSegmentation/main/screenshots/scr2.png" width="600"/>
</picture>
<picture>
<img src="https://raw.githubusercontent.com/gunaykrgl/buildingSegmentation/main/screenshots/scr3.png" width="600"/>
</picture>

# Local Installation
```
gh repo clone gunaykrgl/buildingSegmentation
cd buildingSegmentation
pip install -r requirements.txt
```

## Running Locally
After local installation, the application can be run by the following command:
```
gradio run demo.py
```

After this command is run, there will be a localhost url be generated at the end of the outputs. Later, the application can be used by navigating to the url in a web browser.