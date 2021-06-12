# DataQuality
tavlab@iiitd.ac.in

## Background
Data is expanding at an unimaginable rate, and with this development comes the responsibility of the quality of data. Data Quality refers to the relevance of the information present and helps in various operations like decision making and planning in a particular organization. Mostly data quality is measured on an ad-hoc basis, and hence none of the developed concepts provided any practical application. 
## Methods and Findings
The current empirical study was undertaken to formulate a concrete automated data quality platform to assess the quality of incoming dataset and generate a quality label, score and comprehensive report. The proposed system quantifies and qualifies the provided data and evaluates them at subjective and objective levels. We utilize various datasets from healthdata.gov, opendata.nhs and **Demographics and Health Surveys (DHS) Program** to observe the variations in the quality score and formulate a label using Principal Component Analysis. The results of the current empirical study revealed a metric that encompasses nine quality “ingredients”, namely **provenance, dataset characteristics, uniformity, metadata coupling, percentage of missing cells and duplicate rows, skewness of data, the ratio of categorical columns, and correlation** between these columns. 
## Conclusion
Judging various datasets based on this metric proved that due to the growing technological upgradations in data collection and processing, there is a constant gradient increase in the quality of data. The study also validates the metric by using modified **Mutation Testing** approaches to show that the metric completely captures the essence of any incoming dataset. The value of the quality label instills confidence in the user in deploying the data for his/her respective practical application.

## Guidelines
1. Results folder contains the dataset utulized for the traning of the model which further gives us the component loadings for each ingredient. 
2. These component loadings are used to formulate the Data Quality Label.
3. The DQ Label is used to test the model on the DHS India datasets to observe trends and quantify the quality of data. 
4. Elaborate explantion is available in the "DataQualityFramework.ppt". 
