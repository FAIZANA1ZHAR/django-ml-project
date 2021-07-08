# Customer Churn Prediction Model 

## Problem statement :: make web application which will predict the customer churn with good accuracy 

### Model Building 

#### Contents Cover in this project 
 1. loading data 
 2. Data visualization
   > ploting graphs for colums 
   > datatypes of each colum 
   > no of colums 
   > no of rows 
 3. data cleaning 
   > removing null values 
   > detecting outliers 
   > symetry of data
   > 5 number summary 
 4. understanding bussiness model 
   > we have to look each attribute and its importance for model trainning 
   > In this data set the colums we dont need : 
     * area code 
     * serial number
     * state
  5. pre-processing 
     > null value row removed 
     > unnecessory colums droped 
     > data skewness
     > changed bool type colums to 0 and 1
     > arranged the data for processing 
   6. training data
     > 80 prcent data is used for taining model
   7  testing data 
      > 20 percent data is used for testing 
   8  results 
      > confusion matrix for each model 
      > roc curve 
      
      
   8. the results   
      
   **name**	    |         **score**	  |   **confusion matrix**	          |   **percentage**

 
0.	Nearest_Neighbor	  |    0.88     | [[445, 20],[39, 30]]	           88.9513  1
1.	Linear_SVM	        |    0.870    | 	[[465, 0], [69, 0]]	               87.0 78652
2.	Polynomial_SVM	    |    0.870	  |   [[465, 0], [69, 0]]	                8 7.078652
3.	RBF_SVM	            |    0.87078  |  [[465, 0], [69, 0]]	               87 .078652
4.	Gaussian_Pro	      |    0.92134	| [[457, 8], [34, 35]]	            92. 134831
5.	Gradient_Boost	    |    0.906	  |  [[440, 25], [25, 44]]	            90.636704
6.	Extra_Trees     	  |    0.934457 | 	[[460, 5], [30, 39]]	            93.445693
7.	Neural_Net	        |    0.917603 |	[[457, 8], [36, 33]]	              91.760300 
8.	AdaBoost	          |    0.902622 | [[452, 13], [39, 30]]	              90.262172
9.	Naive_Bayes	        |    0.867041 |	[[425, 40], [31, 38]]	              86.704120
10. QDA	              |    0.855805 | [[423, 42], [35, 34]]	              85.58054
11. RandomForestClassifier 	0.955056|	[[465, 0], [24, 45]]	              95.505 618
12. DecisionTreeClassifier	0.876404	| [[426, 39], [27, 42]]	              87.640449
13.	SGD	              |    0.80898  | [[412, 53], [49, 20]]               80.89886


9 pickle 
 > we use pickle for model deployment 
 
 
 ### Django and mongodb 
 1. Django
   > use pickle file for model
   > fetch datafrom frontend fed to model live data of customer
   > prepare data for prediction 
   > send prediction back to frontend 
 2. frontend 
  > html
  > bootstrap
 3.  mongodb 
  > store the prediction for future use 
  
  
  
  
  for any query feel free to ask at faziazhar1@gmail.com
  
  ### thank you
   
