# MolOptimizer
![alt_text](https://img.shields.io/badge/OPTIMIZATION-Fragement%20Screening-yellow?style=for-the-badge)
![alt text](https://img.shields.io/badge/LICENSE-MIT-informational?style=for-the-badge)
![alt_text](https://img.shields.io/badge/Version-1.00-yellowgreen?style=for-the-badge)

Flask based package useful for optimization of fragment screening datasets


Developed at Akabavoy Research Laboratories, Department of Chemistry, Ben Gurion University of the Negev.
Under the supervision of *Dr. Barak Akabayov*

![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/BGU_logo.PNG)        
Visit Dept. of Chemistry@BGU: https://in.bgu.ac.il/teva/chem/eng/Pages/default.aspx 


![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/lab_logo.png)

Please visit  our lab website: https://akabayov-lab.org/ 







        


>## Motivation: 

>MolOptimizer was developed to be used by researchers working in the field of Small Fragment based inhibitors and is intended to be helpful
in optimization of ligand databases. 

## Description:
![alt_text](https://img.shields.io/badge/-FLASK-lightgrey?style=flat-square)	![alt_text](https://img.shields.io/badge/-PYTHON-blue?style=flat-square) 		![alt_text](https://img.shields.io/badge/-HTML-orange?style=flat-square) 
![alt_text](https://img.shields.io/badge/-CSS-informational?style=flat-square)
![alt_text](https://img.shields.io/badge/-ANGULARJS-red?style=flat-square)

MolOptimizer is a flask based web package which can be used for Alignment of large ligand datasets, extracting large volume of Chemical Descriptors
and training Machine Learning models to predict binding scores. 

## Table of contents
* Setting up MolOptimizer
* Features of MolOptimizer
	* Molecules Alignment Section
	* Feature Extraction Section
	* Expert Mode 
	* Manual Mode 
* How to run MolOptimizer and use it's various sections
	* Alignment Section
	* Feature Extraction Section
	* [Expert Mode] Extreme Gradient Boosting
	* [Manual Mode] Extreme Gradient Boosting
	* [Expert Mode] Lasso Regression
	* [Manual Mode] Lasso Regression
	* [Expert Mode] Decision Tree Regressor
	* [Manual Mode] Decision Tree Regressor
* Note to user
* Credits
* License
* Conclusion & Future Improvements

### Setting up MolOptimizer

App.py acts as the main runner script for MolOptimizer. 
Mentioned below is the list of folders which have to be created to before running MolOptimizer.

List of folders which the user has to create
| Folders which need to be created 	  		| Folders which need to be created         |
| ------------------------------------------------- | --------------------------------------------- |
| PICTURES								      		|	Web_Decision_Tree_Regression_Initial        |
| templates (where main.html is located)      		| Web_Decision_Tree_Regression_NotInitial       |
| UPLOADS_ALIGN							            | Web_Decision_Tree_Regression_Results	        |
| UPLOADS_Decision_Tree_Prediction		      		| Web_Decision_Tree_Regressor_Manual_Mode       |
| UPLOADS_Decision_Tree_Regressor	    	  		| Web_Decision_Tree_Regressor_Manual_Prediction |
| UPLOADS_Decision_Tree_Regressor_Manual_Mode 		| Web_DecisionTree_FeatureImportance		    |
| UPLOADS_Decision_Tree_Regressor_Manual_Prediction	| Web_Expert_FeatureImportance 			  		|
| UPLOADS_Decision_Tree_Regressor_NotInitial	    | Web_Expert_Models								|
| UPLOADS_EXPERTMODE_ModelTraining					| Web_Expert_Models_NotInitial					|
| UPLOADS_EXPERTMODE_ModelTraining_NotInitial		| Web_Expert_Results							|
| UPLOADS_FeatureCorrelation						| Web_FeatureImportance							|
| UPLOADS_FeatureExtraction_Mordred					| Web_Features_Extracted_Mordred				|
| UPLOADS_FeatureExtraction_RDKIT					| Web_Features_Extracted_RDKIT					|
| UPLOADS_Lasso_Regression_Initial					| Web_Lasso_Regression_Download					|
| UPLOADS_Lasso_Regression_Manual					| Web_Lasso_Regression_FeatureImportance		|
| UPLOADS_Lasso_Regression_Manual_Prediction		| Web_Lasso_Regression_Initial					|
| UPLOADS_Lasso_Regression_NotInitial				| Web_Lasso_Regression_Manual_Prediction		|
| UPLOADS_Lasso_Regression_Prediction				| Web_Lasso_Regression_Manual_Training			|
| UPLOADS_Model_Training							| Web_Lasso_Regression_NotInitial				|
| UPLOADS_Prediction								| Web_Lasso_Regression_Results					|
| Web_Models										| Web_Results									|

In all of the scripts provided with MolOptimizer please kindly add the fullpaths to the mentioned required folders. 

Once the folders are created in the directory and the paths to the folders added in the scripts, MolOptimizer is ready to be run.

### Features of MolOptimizer

#### Molecules Alignment Section 				![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/alignment.PNG)
	
In this section, a ligand database(in .SDF file format) can be aligned with a reference molecule(in .SDF file format) using RDKit Most Common Substructure module.
The parameters for alignment can be edited according to the user requirements through MCS_Script.py file. For MolOptimizer the default parameters of MCS module 
have been used.

#### Feature Extraction Section					![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/Feature_Extraction.png)

##### Extraction of chemical descriptors can be done using RDKit and Mordred open source cheminformatics libraries.
 User can choose the either of the two libraries for feature extraction and upload files in .MOL2 format.
 Extracted features can be then downloaded in .csv format. 

#### Expert Mode
   MolOptimizer offers Machine Learning Algorithms in two flavours, Expert Mode and Manual Mode. In Expert Mode, the Machine Learning algorithms trains on the
   optimial parameters for the dataset and recommends the top ten most influential features to the user in ascending order. The user can then opt to train machine 
   learning model with the recommended features and use this model to predict the binding scores. 

#### Manual Mode
   In case the model in Expert Mode gives a high RMSD error rate. User has the option to manually enter the hyper parameters for the models and select the features
   from a drop down menu to train the models. 
 
---

### How to run MolOptimizer
Kindly download the YAML file('MolOptimizer_env.yml') containing the anaconda environment required for MolOptimizer. This will enable to use RDKit and Mordred libraries along with the Machine Learning Algorithms. Once in the provided anaconda environment, please use the following command,
```
flask run 
```
MolOptimizer will start running on your local host as shown below, 
![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/Flask_Message.JPG)
Copy past the URL generated in the Command Prompt/terminal in your web browser and you should see the
webpage of MolOptimizer displayed as shown below. 

* Using Alignment Section
  ![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/Molecules_Alignment_Section_png.png)
  Please upload your files in SDF format for this section. Upload the reference molecule and then the ligand database. Since MolOptimizer is running on local host, feel free to upload any file size. The execution time depends on the hardware of the local host.  
 * Using Feature Extraction Section
 ![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/Feature_Extraction_Section_png_2.png)
 Please upload multi-molecule(only) .MOL2 files to either RDKit or Mordred Sections for extraction of chemical descriptors. 
 
 * Using Expert Mode - XGBoost
 
   ![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/XGBoost_EM_png.png)
   
   
   In Expert Mode, user can upload csv file containing chemical descriptor values of molecules along with the binding scores under the column 'BOND'. The model iteraters through    a dictionary of parameters to find the optimal parameters for the dataset. User is encouraged to change the parameters dictionary found in the script 'ExpertMode_One.py'. On    clicking submit, uses GridSearchCV and uses the recommended parameters to train the model on the dataset. The progress of training of the model can be seen through the          loading of icon the browser and also through the command prompt/terminal in which MolOptimizer is running. 
   
   ![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/Recommended_Features.JPG)
   
   *Only* after the browser completes the training process should the user right-click on the pop up dialog box which appears on the screen to see the recommended features.
   The following section is displayed after closing the dialogue box, 
   
   ![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/XGBoost_EM_2.JPG)
   
   
   After re-uploading the csv files, kindly the features to train the model with and click submit. The progress of training of the model can be noted through the loading icon on    the browser and also from the terminal. Once the training is completed user is requested to click on the following pop up box if the user wishes to see the RMSD error value      of the model. 
   
   ![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/xg_em2_RMSD.JPG) 
   
   User can then upload files containing only the chemical descriptors and get the prediction of binding scores from the trained model.
 
 * Using Manual Mode - XGBoost
   
   ![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/xgboost_mm_png_2.png)
   In Manual mode of XGBoost user can enter the hyper-parameters and select the features on which the model trains. Once the training of the model is completed, user selects the    features (the same features on which the model is trained on) for prediction. Once the page refreshes, user can click on the download button and a csv file containing the        predicted binding scores is downloaded. (The progress of training of the model can be noted by the loading icon in the browser)

Kind note to the user: Expert Mode and Manual Mode of all the rest of the algorithms follows the same procedure as mentioned for XGBoost Expert and Manual Mode.

* Using Expert Mode - Lasso Regression
  ![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/laso_em.JPG)
  
  For Expert Mode of Lasso Regression, the entire section is displayed. The user is requested to follow training of the model with the same procedure as mentioned for XGBoost     Expert Mode section
 
* Using Manual Mode - Lasso Regression

 ![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/LASO_MM.JPG)

* Using Expert Mode - Decision Tree Regressor

![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/em_dt.JPG)

* Using Manual Mode - Decision Tree Regressor
![alt_text](https://github.com/csbarak/MolOptimizer/blob/main/dt_mm.JPG)

* Note to user
	* MolOptimizer looks best on Chrome
	* Kindly delete uploaded and generated files from folders after running MolOptimizer so that MolOptimizer does not read from previous files.
	* If XGBoost Expert Mode model throws an error please select higher number of recommended features to train from. 
	* Please kindly make sure to add the full paths to each of the folders in the relevant scripts (mainly 'app.py' file)
	* Debuging
		* If the front end of MolOptimizer is not responding, check the terminal for any error messages. 
		* Please do make sure that you are running in the environment provided by MolOptimizer
   		* Kindly make sure that while entering the complete paths in the scripts that you use '\\'. Feel free to change it depending on the platform in which you are                       running.

* Credits

  Thanks to my supervisor Dr. Barak Akabayov and all the amazing members of the group. 
  
  * Link to GitHub Repository of Chosen:  https://github.com/harvesthq/chosen
  * Link to Chosen License Statement: https://github.com/harvesthq/chosen/blob/master/LICENSE.md
  * Link to RDKit Tethered Minimization GitHub Repository: https://github.com/Discngine/rdkit_tethered_minimization
  * Link to RDKit Tethered Minimization License File: https://github.com/Discngine/rdkit_tethered_minimization/blob/master/LICENSE
  * Link to Mordred GitHub Repository: https://github.com/mordred-descriptor/mordred
  * Link to Mordred License Statement: https://github.com/mordred-descriptor/mordred/blob/develop/LICENSE
 
* License

  MolOptimizer uses Chosen, RDKit, RDKit Tetherd Minimization and Mordred libraries in its program without any modifications. The license statements for all of the mentioned     programs is kept 'as is' in the script files. 
  
  MolOptimizer is released under MIT License.

- - -
MIT License

Copyright (c) 2021 Barak Akabayov
