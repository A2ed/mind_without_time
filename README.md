# A Mind Without Time

This project contains and EDA and classification model for patients from the [Alzheimer's Disease Neuroimaging Initiative](http://adni.loni.usc.edu). 

## Problem Statement

Alzheimer’s Disease (AD) is one of the most prevalent and debilitating forms of dementia. In Canada alone, there are 564,000 people diagnosed with dementia, a number that is expected to increase to nearly a million by 2031. Aside from the impact on an individual, dementia places a large burden on the healthcare system and persons involved with an affected individual. Dementia is currently estimated to cost 10.4 billion dollars in yearly expenses within Canada.

Early diagnosis of AD is associated with a higher quality of life and a reduced cost on a healthcare system. However, detecting AD early in the disease progression is difficult due to the multifaceted nature of how neurodegeneration affects the brain, cognitive processing, and behavior. Clinical evaluation relies on assessment of a myriad of cognitive tests and biomarkers that are not always identifiable in patients with mild cognitive impairment (MCI), a precursor to AD.

The multifaceted impact of cognitive impairment and neurodegeneration in MCI and AD suggests that machine learning algorithms such as neural networks may be beneficial in identifying and predicting disease progression. Current studies typically only incorporate one form of data, however, often relying solely on features extracted from structural magnetic resonance imaging (MRI) scans. Other forms of data that show promise in classification with machine learning algorithms include cognitive assessments and the connectivity patterns of resting-state functional networks. This is because spatial and episodic memory, cognitive processes that are typically the first affected in MCI and AD, rely on complex, dynamic interactions of distributed neural networks and are therefore susceptible to the impact of neurodegeneration. Critically, there has yet to be an assessment of how machine learning algorithms perform using features extracted from structural and functional MRI data, as well as cognitive assessments. This project aims to remedy this.

## Target audience and use cases:

Healthcare providers. Structural and resting-state functional MRIs are one of easiest and fastest methods of brain imaging. Using them to classify persons at risk or with Alzheimer’s Disease would assist in providing targeted treatments.

## Dataset:

The dataset is based on the [ADNI research initiative](http://adni.loni.usc.edu/data-samples/adni-data-inventory/)

Portions of this initiative have been populated into a single dataframe. This dataframe contains numerous variables of interest:

* Demographic information such as age and gender
* Assessment on cognitive tests
* Volumetric measures of brain regions from structural MRI data
* Measures of functional connectivity in fMRI data
* Diffusion tensor imaging of the hippocampus and entorhinal cortex
* Measures from PET imagining
* Presence of the APOE4 allele

These measures are provided a detailed overview in section 2 of the EDA notebook. Briefly, they are based on research showing that Alzheimer’s Disease affects them and therefore may be useful in forecasting patients that convert from cognitively normal or MCI.

 ## Data cleaning:

All data cleaning is contained and summarized in the data_cleaning.ipynb notebook. The steps taken were:

* Rename columns to make them more interpretable and pythonic
* Extract columns of interest from main dataframe
* Merge main dataframe with dataframe containing fMRI measures
* Recode missing values
* Remove or impute missing values
* Reduce the time series column to patient visits with measures of interest
* Deal with missing values in the diagnosis change column
* Identify and clean repeated entries in diagnosis change column
 
The clean dataset is saved as df_clean.csv in the Github repository.

## Exploratory Data Analysis

This analysis is in the eda.ipynb notebook.

The dataset contains baseline and time series measures for each variable. Each patient has a baseline diagnosis of either cognitively normal (CN), significant memory complaints (SMC), early mild cognitive impairment (EMCI), late mild cognitive impairment (LMCI), or Alzheimer’s Disease (AD). Demographic information at baseline for the different diagnoses were inspected and visualized.

The different variables of interest were also visualized and inspected. Variables that did not appear to show differences between AD and the other groups were flagged for removal. The rationale was that if a variable did not differ between AD and the other groups, it would not contain information that is useful in classifying patients with AD. Overall, the cognitive tests and volumetric brain measures appear the most useful, with some measures from DTI and PET imaging showing group differences as well. The presence of the APOE4 allele, especially when there are two copies present, appears useful as well.

There are a total of 331 patients out of 1382 patients (24% of sample) that entered the study without AD that subsequently converted to AD at some point. There are 330 patients with AD at the onset of the study.

The average person who converts to AD enters the study with a diagnosis of late MCI, is male, older on average with a university degree, is married and not hispanic/latino.

Differences on variables of interest were also investigated by comparing diagnosis group patients who convert to AD during the study with those that don’t. Three diagnosis groups were used: cognitively normal, early MCI, and late MCI. There was only one patient with SMC who converted, and therefore this diagnosis group was omitted from analysis.

## Generating a classification model:

Model evaluation is outlined in the model.ipynb notebook.

The central aim of the project is to develop a classification model that is able to identify persons without AD that are at high risk of developing it. To build the model, the first step is to define a feature set and to encode a binary target label that represents either patients who convert to AD at some point in the study or patients who don’t.
In order to retain as many observations as possible, the feature set used included:

* Demographic information: 
 * Years of education
 * Gender
 * Age at start of study 
* Cognitive assessments:
 * CDRSB, ADAS13, MMSE, and the difference score between the CDRSB and the ADAS13
* Structural MRI volumetric measures:
 * Volume of the left/right hippocampus and entorhinal cortex generated from a cross sectional template
 * Cortical thickness estimates for the left/right entorhinal cortex also generated from a cross sectional template
* Genetic information:
 * Number of APOE4 alleles
 
This feature set represented the data categories that showed promise in differentiating AD from other cognitive types while retaining the most data (the MOCA, for example, was only administered on about half the patient sample).

Converters were identified as patients that converted from either cognitively normal or MCI to AD at some point in the study. There was one patient with significant memory complaints that was dropped as well as six patients who at the baseline visit were diagnosed with AD.

The models were generated by including data points for each feature across all visits in the dataset. For converters, this means that visits before, at, and after conversion to AD were labeled as converted.

The classification models that were evaluated were:

* Logistic regression
* Random Forests
* XGBoost

These models encompass simple linear classification, as well as more modern approaches of bagging and boosting.

All models were evaluated using three metrics:

1. Accuracy score on the test data
2. Area under the ROC curve
3. Average precision

Hyperparameters were optimized using a 5-fold stratified gridsearch that preserved the proportion of convert/non-convert in each fold.

## Summary

The best performing model used the XGBoost classifier. This model had a high accuracy score of 92%, with a large area under the curve (0.975) and a fairly high average precision of 0.787. Importantly, the precision recall curve shows that it has high recall as well, indicating that there are few false negatives, patients that the classifier mislabeled as non-converts.

The use case of the model is to assist physicians in identifying patients at high risk for developing AD. This will allow early intervention and preventative therapies to by used by the patient to potentially decrease the likelihood of converting to AD.

## Next steps

The final model was trained on a limited set of features in order to maximize the observations during training. However, it may be that some of the omitted features have high influence in classifying converts from non-converts. Model evaluation should be performed on a reduced dataset that includes PET, fMRI and the MOCA, and feature importance looked at to assess whether there is need to collect additional data from the data category.

Second, the two top performing models also overfit the training data, potentially limiting the ability to generalize to the test data and other unseen data. In order to prevent overfitting, additional features such interactions between feature sets may be included, or a different score metric for the gridsearch cross validation to use.

Third, the model currently indicates whether a person is at risk for converting to AD at some point. It may be possible to forecast the timeframe of a conversion. This would not impact the amount of time between assessment and conversion to AD, but would give an indication of the urgency for preventative therapies that may be useful to hospitals or care givers that have limited resources.
