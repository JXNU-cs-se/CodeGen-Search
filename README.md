# CodeGen-Search

## 1. 介绍 codegen-search模型的主要思想和方法

We proposes a CodeGen-Search model to improve code generation quality by incorporating similar samples. To fully utilize the information of similar samples, the model adopts the “pre- training+fine-tuning” pattern. The model uses a minimum edit distance algorithm to find some similar samples with natural language, and uses different encoders to extract the features of the natural language and the code in similar samples.

我们所提出的模型是基于TreeGen提出的，所采用的数据集亦是TreeGen所公开的已经预处理后的数据集。https://github.com/zysszy/TreeGen

## 2. 项目中使用的数据集：

ATIS数据集：https://github.com/JXNU-cs-se/CodeGen-Search/tree/main/CodeGen-search%20back/ATIS

HS数据集：https://github.com/JXNU-cs-se/CodeGen-Search/tree/main/CodeGen-search%20back/HS-B


## 3. 介绍如何使用项目：  (使用的步骤：)
### 1. 数据集准备和预处理 ： 两个数据集均源自TreeGen：https://github.com/zysszy/TreeGen ，该项目提供了已经预处理的数据集，并未提供数据集预处理的代码。本项目使用的是已经预处理的数据集。 

### 2. 模型调用和使用： 
首先使用原始数据集对模型进行训练，然后再使用CodeGen-search get中的genSearchFIle.py检索相似样例，并将相似样例文件放入该文件夹CodeGen-Search/CodeGen-search back/ATIS
/data/ 对应的数据集文件夹中，并再次进行模型训练。

训练模型

python3 run.py ATIS|HS-B

模型测试（ATIS|HS）

python3 predict.py ATIS 5

python3 predict_HS-B.py HS-B 5

结果评估

python3 eval.py ATIS|HS-B

实验环境

NLTK 3.2.1

Tensorflow 1.12.1

Python 3.7

Ubuntu 16.04

    
    
 ## 4. 本篇文章 CodeGen-Search  引用信息：
 
 


