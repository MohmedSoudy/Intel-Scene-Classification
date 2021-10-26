# Intel-Scene-Classification
This repo for scene classification on Intel scenes derived from Kaggle challenge 

The data contains around 25k images of size 150x150 distributed under 6 categories (building; forest; glacier; mountain; sea; street). There are around 14k images in Train, 3k in Test, and 7k in Prediction.
This data was initially published on https://datahack.analyticsvidhya.com by Intel to host an image classification challenge.

### Our Contribution 

- We re-categorize the data for the binary classification problem (natural scenes vs. real scenes), with natural scenes being forest, glacier, mountain, and sea, and real scenes including building and streets. The six categories are included in the multi-classification task.

- We built a novel architecture for binary classification (natural scenes vs. real scenes) achieving 98.08 ± 0.05, 92.70 ± 0.086 accuracies for training and validation data respectively.

- We built a novel architecture for multi-classification (building; forest; glacier; mountain; sea; street) achieving 93.55 ± 0.11, 75.54 ± 0.14 accuracies for training and validation data respectively.

### Model Architecture

![](https://raw.githubusercontent.com/MohmedSoudy/Intel-Scene-Classification/main/Figure%201_cut.png)

### Results 

|Backbone Model    | Parameters       | Accuracy         |          
|------------------|------------------|------------------|
| ResNet50         | 25,636,712       |  94.63           |
| ResNet 101       | 44,707,176       |  94.72           |
| SE ResNext 101   | 44,177,704       |  94.36           |
| RepConv          | 160,390          | 94.58            |
