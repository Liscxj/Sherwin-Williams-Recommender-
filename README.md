# SWRS - Sherwin-Williams Recommender System 🎨
- March 19 2026
- DSC 4900 - Data Science Project/Portfolio
- Belmont University
- Author: Lis Caxaj

# Table of Contents
---
  * Introduction
  * Overview of Advanced Topics
  * Gathering and Cleaning Data
    * Dataset Description
    * Data Cleaning
  * Database Creation
  * Building out the Recommender System
  * Website Creation Using Flask
  * Navigating Through the Website
  * Conclusion

## Introduction 
This project focuses on building a paint recommendation system that helps customers select appropriate Sherwin-Williams paint products using structured product data, feature engineering, and clustering techniques to better organize and differentiate similar products. By combining multiple datasets and applying user-driven filters, the system identifies the most relevant options. The final Flask web application delivers tailored paint recommendations with key attributes, simplifying the selection process.

## Advanced Topics
- Feature Engineering (0.5 points): Created structured features from raw attributes (Durability, Coverage, Appearance, etc) from both the PDS and Paint Grades Guide. Built a composite score (Qsum) to aid in ranking products. Cleaned and converted numeric fields in reference to VOC values, dry time, and coverage ranges. Categorical variables (paint type and price tier) were converted into numerical format using one-hot encoding, allowing them to be used in clustering and modeling.
- Database Creation (1 point): Constructed a custom database by extracting and organizing product attributes from publicly available Sherwin-Williams data sources into structured CSV files.
- Combining Datasets (0.5 points): Combined multiple datasets by merging product, quality, and sheen data using Product_ID to create a unified dataset for analysis.
- Website Using Flask (1 point): Developed a Flask web application that allows users to input preferences and receive personalized paint recommendations based on filtering and ranking logic.
- K-Means Clustering (1 point): Applied K-means clustering to group similar paint products based on engineered features, and labeled clusters to create interpretable product categories.


