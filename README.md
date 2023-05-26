# CodeGen-Search

## 1. 介绍 codegen-search模型的主要思想和方法

1. Introduction to the main ideas and methods of the codegen-search model

We proposes a CodeGen-Search model to improve code generation quality by incorporating similar samples. To fully utilize the information of similar samples, the model adopts the “pre- training+fine-tuning” pattern. The model uses a minimum edit distance algorithm to find some similar samples with natural language, and uses different encoders to extract the features of the natural language and the code in similar samples.

我们所提出的模型是基于TreeGen提出的，所采用的数据集亦是TreeGen所公开的已经预处理后的数据集。 （The proposed model is based on TreeGen, and the dataset used is also the preprocessed dataset disclosed by TreeGen.）https://github.com/zysszy/TreeGen

## 2. 项目中使用的数据集：

2. Datasets used in the project:

ATIS数据集（ATIS dataset）：https://github.com/JXNU-cs-se/CodeGen-Search/tree/main/CodeGen-search%20back/ATIS

HS数据集（HS dataset）：https://github.com/JXNU-cs-se/CodeGen-Search/tree/main/CodeGen-search%20back/HS-B


## 3. 介绍如何使用项目：  (使用的步骤：)

3. How to use the project (steps used):

### 1. 数据集准备和预处理 ： 两个数据集均源自TreeGen：https://github.com/zysszy/TreeGen ，该项目提供了已经预处理的数据集，并未提供数据集预处理的代码。本项目使用的是已经预处理的数据集。 

1. Dataset preparation and preprocessing: Both datasets are derived from TreeGen : https://github.com/zysszy/TreeGen, which provides a preprocessed dataset and does not provide the code for dataset preprocessing. This project uses a dataset that has already been preprocessed.

### 2. 模型调用和使用： 

2. Model invocation and use:

首先使用原始数据集对模型进行训练，然后再分别使用CodeGen-search get中gensearchflies1,2,3得到相似数据的训练集 验证集和测试集，并将相似样例文件放入该文件夹CodeGen-Search/CodeGen-search back/ATIS
/data/ 对应的数据集文件夹中，并再次进行模型训练。

First use the original dataset to train the model, and then use gensearchflies1, 2, 3 in CodeGen-search get to obtain the training set validation set and test set of similar data, and put the similar sample files into the folder CodeGen-Search/CodeGen-search back/ATIS/data/ corresponds to the dataset folder and train the model again.

A. 训练模型

model traing instructions

```python3 run.py ATIS | HS-B```

B. 模型测试（ATIS|HS）

testing instructions

- for ATIS dataset:

```python3 predict.py ATIS 5 ```  

- for HS dataset:

```python3 predict_HS-B.py HS-B 5```

C. 结果评估

Evaluation of results instructions

```python3 eval.py ATIS | HS-B```

### 实验环境

Experimental environment and needed tools：

- TOOLS: NLTK 3.2.1

- TOOLS: Tensorflow 1.12.1

- Programming language: Python 3.7

- OS: Ubuntu 16.04 

    
## 4. 本篇文章 CodeGen-Search  引用信息：

4. This article CodeGen-Search quotes information

 
 


