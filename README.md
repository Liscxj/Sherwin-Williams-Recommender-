# SWRS - Sherwin-Williams Recommender System 🎨
- May 5 2026
- DSC 4900 - Data Science Project/Portfolio
- Belmont University
- Author: Lis Caxaj

# Table of Contents 🗒️
---
  * Introduction
  * Overview of Advanced Topics
  * Gathering and Cleaning Data
    * Dataset Description
    * Data Cleaning
  * Database Creation
    * Combining Datasets
  * Building out the Recommender System
    * Feature Engineering and K-Means Clustering
  * Website Creation Using Flask
  * Navigating Through the Website
  * Conclusion

## Introduction 💬
This project focuses on building a paint recommendation system that helps customers select appropriate Sherwin-Williams paint products using structured product data, feature engineering, and clustering techniques to better organize and differentiate similar products. By combining multiple datasets and applying user-driven filters, the system identifies the most relevant options. The final Flask web application delivers tailored paint recommendations with key attributes, simplifying the selection process.

## Advanced Topics 💡
- **Feature Engineering (0.5 points):** Created structured features from PDS and Paint Grades Guide data (durability, coverage, appearance). Built a composite score (QSum) for ranking, cleaned numeric fields (VOC, dry time, coverage), and encoded categorical variables (type, price tier) for clustering.
- **Database Creation (1 point):** Constructed a custom database by extracting and organizing product attributes from publicly available Sherwin-Williams data sources into structured CSV files.
- **Combining Datasets (0.5 points):** Combined multiple datasets by merging product, quality, and sheen data using Product_ID to create a unified dataset for analysis.
- **Website Using Flask (1 point):** Developed a Flask web application that allows users to input preferences and receive personalized paint recommendations based on filtering and ranking logic.
- **K-Means Clustering (1 point):** Applied K-means clustering to group similar paint products based on engineered features, and labeled clusters to create interpretable product categories.


## Gathering and Cleaning Data 📚
---
 **Gathering Data**
 
My data was sourced from the Sherwin-Williams website, where Product Data Sheets (PDS) are readily available for all paint products. My secondary source of data was sourced from the Sherwin-Williams Paint Grades Guide.

Sherwin-Williams PDS Link: https://www.sherwin-williams.com/painting-contractors/products/data-sheets?msockid=0af8c3a5954466053fa3d76c94ea67ce

Key Variables:
- **Product_ID:** unique primary key assigned to all paints
- **Product_Name:** paint product name
- **Interior:** classification of paint suitable for interior use 
- **Exterior:** classification of paint suitable for exterior use
- **VOC_Value:** volatile organic compound value of paint
- **Recoat_Dry_Time:** dry time for a recoat job
- **Coverage_Min:** minimum coverage value of paint
- **Coverage_Max:** maximum coverage value pf paint
- **Cleanup:** refers to the removal of paint based on it being alkyd or latex-based (paint thinner/ water cleanup)
- **Price_Tier:** price tier of paint
- **Type:** classification of wall, trim, or ceiling paint
- **Description:** short description of paint
- **Sheen:** level of shine on a paint
- **Appearance:** appearence of paint
- **Easy_Clean:** categorizes how easy it is to clean the dirty surface of a paint 
- **Durability:** categorizes how durable a paint is in terms of wear and damage
- **Mold_&_Mildew:** categorizes how resistant a paint is to mold and mildew
- **Coverage:** ranks the coat coverage of a paint 
- **Application:** ranks how silky and smooth the application of a paint is
- **QSum:** numerically sums up all individual categorical aspects pulled from the paint grade guide for every paint
- **Base:** classifies if light, dark, very dark, or vibrant accent colors can be mixed in a paint
- **Surface:** classifies what type of surface the paint can be applied to

<img width="657" height="838" alt="PDS Example" src="https://github.com/user-attachments/assets/198dae40-1309-4c0b-93a2-79e07dd3c009" />

## Data Cleaning 🧹

## Database Creation

**Combining Datasets**

## Building out the Recommender System 🛠️

**Feature Engineering & K-Means Clustering**

## Website Creation Using Flask 💻

## Navigating Through the Website

## Conclusion

