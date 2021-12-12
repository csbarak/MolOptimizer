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






*@author: D. Samuel Joshua Viswas*
        


## Motivation: 

MolOptimizer was developed to be used by researchers working in the field of Small Fragment based inhibitors and is intended to be helpful
in optimization of ligand databases. 

## Description:
![alt_text](https://img.shields.io/badge/-FLASK-lightgrey?style=flat-square)	![alt_text](https://img.shields.io/badge/-PYTHON-blue?style=flat-square) 		![alt_text](https://img.shields.io/badge/-HTML-orange?style=flat-square) 
![alt_text](https://img.shields.io/badge/-CSS-informational?style=flat-square)
![alt_text](https://img.shields.io/badge/-ANGULARJS-red?style=flat-square)

MolOptimizer is a flask based web package which can be used for Alignment of large ligand datasets, extracting large volume of Chemical Descriptors
and training Machine Learning models to predict binding scores. 

## Table of contents
* Setting up MolOptimizer
* How to run MolOptimizer
* Features of MolOptimizer
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

Once the folders are created in the directory and the paths to the folders added in the scripts, MolOptimizer can be run.


### How to run MolOptimizer
Kindly download the YAML file containing the anaconda environment required for MolOptimizer. This will enable to use RDKit and Mordred libraries along with the Machine Learning Algorithms. Once in the provided anaconda environment, please use the following command,
```
flask run 
```
MolOptimizer will start running on your local host. Copy past the URL generated in the Command Prompt/terminal in your web browser and you should see the
template of MolOptimizer displayed as shown below. 

------------------------------------------------------------------------------------------------------------------- 
!!!!     IMPORTANT   !!!!

PLEASE KINDLY NOTE THE FOLLOWING, 
 
1. MIT License under which Chosen is released is included in the main.html script where Chosen is used. No Modifications/Upgradations have been made to Chosen. 

It is used in this project without any changes made to Chosen.

Link to GitHub Repository of Chosen:  https://github.com/harvesthq/chosen
Link to Chosen License Statement: https://github.com/harvesthq/chosen/blob/master/LICENSE.md


2. MIT License under which RDKit Tethered Minimization code is released is included in the MACS_Script.py file.

Link to RDKit Tethered Minimization GitHub Repository: https://github.com/Discngine/rdkit_tethered_minimization
Link to RDKit Tethered Minimization License File: https://github.com/Discngine/rdkit_tethered_minimization/blob/master/LICENSE
	
3. BSD 3-Clause "New" or "Revised" License under which RDKit software is released and is used in feature extraction section of MolOptimizer is included in the file RDKit_Features_Script.py

Link to GitHub Repository of RDKit: https://github.com/rdkit/rdkit
Link to RDKit License statement: https://github.com/rdkit/rdkit/blob/master/license.txt





MolOptimizer Released under license: MIT License 

MIT License

Copyright (c) 2021 Barak Akabayov 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


############################################


   

Information for users
** Please kindly make sure to add the full paths to each of the folders in the scripts --

Debuging

-->If the front end of MolOptimizer is not responding, check the terminal for any error messages. 
--> Please do make sure that you are running in the environment provided by MolOptimizer
--> Kindly make sure that while entering the complete paths in the scripts that you use '\\'. Feel free to change it depending on the platform in which you are running.

- - -
MIT License

Copyright (c) 2021 Barak Akabayov
