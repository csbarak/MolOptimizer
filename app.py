"""
@author: D. Samuel Joshua Viswas
Developed at Akabavoy Research Laboratories, Department of Chemistry, Ben Gurion University of the Negev, under the supervision of Dr. Barak Akabayov

 ** Please kindly read the license file of MolOptimizer before starting to use MolOptimizer **.
Link to the release license of MolOptimizer

Link to the GitHub repository of MolOptimizer


"""
#Importing Required Libraries
import os
import flask
import json
import logging
import os
from flask import *
from flask import flash, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
from flask import send_from_directory, flash
from multiprocessing import Process
from flask import Flask, request
from flask import Flask, request
from multiprocessing import Process
# importing custom scripts which other sections of the project
import Mordred_Features_Script
import RDKit_Features_Script
import Feature_Correlation_Script
import Model_Training_Script
import Prediction_Script
import ExpertMode_ModelTraining_Initial
import ExpertMode_One
import ExpertMode_ModelTraining_NotInitial
import ExpertMode_Two
import ExpertMode_Prediction_Script
import Lasso_Regression_N1
import Lasso_Regression_N2
import Lasso_Regression_Prediction_Script
import MACS_Script
import DecisionTreeRegressor_1
import DecisionTreeRegressor_2
import Decision_Tree_Prediction_Script
import Lasso_Regression_Manual
import Lasso_Regression_Manual_Prediction
import DecisionTreeRegressor_Manual
import DecisionTreeRegressor_Manual_Prediction



from flask import Flask, request
from multiprocessing import Process
#set it to the directory where all the scripts are located
PATH_OF_SCRIPT = "<Add Directory Path>"

app = flask.Flask(__name__, template_folder='templates', static_url_path="/PICTURES", static_folder='PICTURES')
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = os.urandom(24)
app.config['MAX_CONTENT_LENGTH'] = None
app.config['UPLOAD_EXTENSIONS'] = ['.mol2', '.csv', '.sdf']
app.config['UPLOAD_PATH'] = '<Add complete path to UPLOADS_ALIGN Folder>'
app.config['MAX_CONTENT_LENGTH_1'] = None
app.config['UPLOAD_PATH_RDKIT'] = '<Add complete path to UPLOADS_FeatureExtraction_RDKIT folder>'
app.config['UPLOAD_PATH_MORDRED'] = '<Add complete path to UPLOADS_FeatureExtraction_MORDRED folder>'
app.config['UPLOAD_PATH_FEATURECORRELATION']='<Add complete path to UPLOADS_FeatureCorrelation folder>'
app.config['UPLOAD_PATH_MODELTRAINING']='<Add complete path to UPLOADS_Model_Training folder>'
app.config['UPLOAD_PATH_MODELPREDICTION']='<Add complete path to UPLOADS_Prediction folder>'
app.config['UPLOAD_PATH_EXPERTMODE_MODELTRAINING']='<Add complete path to UPLOADS_EXPERTMODE_ModelTraining folder>'
app.config['UPLOAD_PATH_EXPERTMODE_MODELTRAINING_NOTINITIAL']='<Add complete path to UPLOADS_EXPERTMODE_ModelTraining_NotInitial>'
app.config['UPLOAD_PATH_EXPERT_MODEL_PREDICTION']='<Add complete path to UPLOADS_Prediction folder>'
app.config['UPLOAD_PATH_DECISION_TREE_REGRESSOR_INITIAL']='<Add complete path to UPLOADS_Decision_Tree_Regressor>'
app.config['UPLOAD_PATH_DECISION_TREE_REGRESSOR_NOTINITIAL']='<Add complete path to UPLOADS_Decision_Tree_Regressor_NotInitial folder>'
app.config['UPLOAD_PATH_DECISION_TREE_PREDICTION']='<Add complete path to UPLOADS_Decision_Tree_Prediction folder>'
app.config['UPLOAD_LASSO_REGRESSION_INITIAL']='<Add complete path to UPLOADS_Lasso_Regression_Initial folder>'
app.config['UPLOAD_LASSO_REGRESSION_NOTINITIAL']='<Add complete path to UPLOADS_Lasso_Regression_NotInitial folder>'
app.config['UPLOAD_LASSO_REGRESSION_PREDICTION']='<Add complete path to UPLOADS_Lasso_Regression_Prediction folder>'
app.config['UPLOAD_PATH_LASSO_MODEL_MANUAL']='<Add complete path to UPLOADS_Lasso_Regression_Manual folder>'
app.config['UPLOAD_PATH_LASSO_MODEL_MANUAL_PREDICTION']='<Add complete path to UPLOADS_Lasso_Regression_Manual_Prediction folder>'
app.config['UPLOAD_PATH_DECISION_TREE_REGRESSOR_MODEL_MANUAL']='<Add complete path to UPLOADS_Decision_Tree_Regressor_Manual_Mode folder>'
app.config['UPLOAD_PATH_DECISION_TREE_REGRESSOR_MANUAL_PREDICTION']='<Add complete path to UPLOADS_Decision_Tree_Regressor_Manual_Prediction folder>'
"""
    --> This script restricts users to uploading only .mol2, .sdf and .csv files to the website
    --> If the uploaded file is not in the allowed extensions then ABORT Function Initiated
"""
# Rendering the Home Page
@app.route('/')
def index():
    return render_template('main.html')
#
# *************************** Molecular alignment section *************************************************
#
@app.route('/upload_files', methods=['POST'])
def upload_files():
    """
    This function is used to align molecules.
    """
    print("You are in the alignment section ")
    #
    # We need to remove the previously aligned mol2 file
    # This will ensure that the correct corresponding aligned file is served
    # Nick Named: 'Clean Up Job' referencing the legendary movie, John Wick
    # Required in every upload function
    # Start of clean up job
    file = 'aligned.sdf'
    location = "<Add complete path to UPLOADS_ALIGN Folder>"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    # End of clean up job
    uploaded_reffile = request.files['ref_file']
    print('uploaded_ref_file', uploaded_reffile)
    uploaded_ligdb_file=request.files['ligdb_file']
    filename_ref = secure_filename(uploaded_reffile.filename)
    filename_ligdb=secure_filename(uploaded_ligdb_file.filename)
    uploaded_reffile.save(os.path.join(app.config['UPLOAD_PATH'], filename_ref))
    uploaded_ligdb_file.save(os.path.join(app.config['UPLOAD_PATH'], filename_ligdb))
    # Passing the file to the alignment script
    MACS_Script.make_it_run(filename_ref,filename_ligdb)
    return render_template('main.html')
# Function to download the aligned molecules file
@app.route('/UPLOADS_ALIGN/aligned.sdf')
def download_file():
    return send_from_directory('UPLOADS_ALIGN', 'aligned.sdf')
#
# ******************************** End of Molecular alignment Section *****************************************
#
#
#
#
# ............................... RDKIT feature extraction section ............................................
@app.route('/feature_ext_RDKIT', methods=["GET", "POST"])
def feature_ext_RDKIT():
    """
    This function is for taking a file as input from the user and runs the RDKIT Feature Extraction
    script on it.
    """
    # Start of clean up job
    file = 'FeaturesExtracted_RDKIT.csv'
    location = "<Add complete path to UPLOADS_FeatureExtraction_RDKIT folder>"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    # End of clean up job
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_RDKIT'], filename))
        RDKit_Features_Script.make_it_run(filename)
    return render_template('main.html')
#
#
@app.route('/')
def come_back_1():
    """
    This makes the page refresh and the user can click on the download link to download the file
    """
    return redirect("main.html", code=302)
#
#
@app.route('/Web_Features_Extracted_RDKIT/FeaturesExtracted_RDKIT.csv')
def download_file_RDKIT():
    """
    Function to download the csv file which contains the extracted RDKIT features
    """
    return send_from_directory('Web_Features_Extracted_RDKIT', 'FeaturesExtracted_RDKIT.csv')
# ........................................ End of RDKIT feature extraction section ..............................
#
#
#
#
# ***************************************** MORDRED Feature Extraction Section *********************************
@app.route('/feature_ext_MORDRED', methods=["GET", "POST"])
def feature_ext_MORDRED():
    """
    This function is for taking a file as input from the user and runs the MORDRED Feature Extraction
    script on it.
    """
    # Start of clean up job
    file = 'FeaturesExtracted_MORDRED.csv'
    location = "<Add complete path to UPLOADS_FeatureExtraction_MORDRED folder>"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    # End of clean up job
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_MORDRED'], filename))
        Mordred_Features_Script.make_it_run(filename)
    return render_template('main.html')
#
#
@app.route('/')
def come_back_2():
    """
    This makes the page refresh and the user can click on the download link to download the file
    """
    return redirect("main.html", code=302)
#
#
@app.route('/Web_Features_Extracted_MORDRED/FeaturesExtracted_MORDRED.csv')
def download_file_MORDRED():
    """
    Function to download the csv file which contains the extracted MORDRED features
    """
    return send_from_directory('Web_Features_Extracted_MORDRED', 'FeaturesExtracted_MORDRED.csv')
#******************************************* End of MORDRED feature extraction section *************************
#
#

#
#
# ------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# ******************************************** EXPERT MODE *******************************
@app.route('/Expert_Training_Model_Initial', methods=["GET", "POST"])
def Expert_Training_Model_Initial():
    """
    This function is for taking a file as input from the user saves it in the designated folder
     and passes it on to the training the model script along with the feature names
     the user has selected.
    """
    # Clean up job for the model generated is present in the script

    # This is to get multiple feature names in the form of a list
    print("You are in Expert Initial")
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        # This saves the uploaded csv file in the designated folder
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_EXPERTMODE_MODELTRAINING'], filename))
        # Pass the parameters to the boosting model
    ExpertMode_One.make_it_rain(filename)
    return ('', 204)
#
#
#
@app.route('/Web_Expert_FeatureImportance/TopFeatures.txt')
def download_file_RecommendedFeatures():
    return send_from_directory('Web_Expert_FeatureImportance', 'TopFeatures.txt')

@app.route('/Expert_Training_Model_NotInitial', methods=["GET", "POST"])
def Expert_Training_Model_NotInitial():
    """
    This function is for taking a file as input from the user saves it in the designated folder
     and passes it on to the training the model script along with the feature names
     the user has selected.
    """
    print("You are in Expert Not Initial")
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        # This saves the uploaded csv file in the designated folder
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_EXPERTMODE_MODELTRAINING_NOTINITIAL'], filename))
    num_features = int(request.form.get('NumFeatures'))
    ExpertMode_Two.make_it_rain(filename,num_features)
    return ('', 204)

@app.route('/Web_Expert_Models_NotInitial/CustomModel_rmse.txt')
def View_RMSE():
    return send_from_directory('Web_Expert_Models_NotInitial', 'CustomModel_rmse.txt')
"""
Now we predict the scores
"""
# ---------------------*********************************************************************************************-------------
#
# ******************************************************************************************************
@app.route('/Expert_Model_Prediction', methods=["GET", "POST"])
def Expert_Model_Prediction():
    """
    This function is save user uploaded csv file in a designated folder and pass it on to the
    'Prediction Script'. Which will then open the model (saved in pkl format) and pass on the
    data from the csv file to predict the target variable (binding score)
    """
    print("You are in Expert Prediction Section")
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_EXPERT_MODEL_PREDICTION'], filename))
    num_pred_features = int(request.form.get('NumPredFeatures'))
    print('this is the filename',filename)
    print('this is the num_pred_features',num_pred_features)
    ExpertMode_Prediction_Script.make_it_rain(filename,num_pred_features)
    return ('', 204)
#
#
@app.route('/Web_Expert_Results/Predicted_Results.csv')
def download_Expert_Results():
    return send_from_directory('Web_Expert_Results', 'Predicted_Results.csv')
# ---------------------------------------------------***********************************************************-----------------
#
#
#
#
#
# ******************************************** End of EXPERT MODE ************************
# --------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------
#
#
#
# .....................################################ MANUAL MODE ############################################################
# ....................################################                ################################################
# ....................##############################                    ####################################
"""
        About:              This section is for the MANUAL MODE (XGBoost) of the website. 
      
"""
# ******************************* Training the model section ********************************************
@app.route('/Training_Model', methods=["GET", "POST"])
def Training_Model():
    """
    This function is for taking a file as input from the user saves it in the designated folder
     and passes it on to the training the model script along with the feature names
     the user has selected.
    """
    # Clean up job for the model generated is present in the script
    learning_rate = float(request.form['param_learning_rate'])
    max_depth=float(request.form['param_max_depth'])
    reg_lambda=float(request.form['param_lambda'])
    alpha=float(request.form['param_alpha'])
    droprate=float(request.form['param_rate_drop'])
    # This is to get multiple feature names in the form of a list
    features=request.form.getlist('model_training_options')
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        # This saves the uploaded csv file in the designated folder
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_MODELTRAINING'], filename))
        # Pass the parameters to the boosting model
        Model_Training_Script.make_it_train(filename,features,learning_rate,max_depth,reg_lambda,alpha,droprate)
    return render_template('main.html')
#
#
@app.route('/')
def come_back_4():
    """
    This makes the page refresh and the user can click on the download link to download the file
    """
    return redirect("main.html", code=302)
#
#
#
# ############################### End of Training the model section #########################################
#
#
#
#
# ********************************* Prediction Score Section ***********************************************
@app.route('/Model_Prediction', methods=["GET", "POST"])
def Model_Prediction():
    """
     This function is save user uploaded csv file in a designated folder and pass it on to the
    Prediction Script. Which will then open the model (saved in pkl format) and pass on the
    data from the csv file to predict the target variable (binding score)
    """
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    features_pred=request.form.getlist('model_predicting_options')
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_MODELPREDICTION'], filename))
        Prediction_Script.make_it_rain(filename,features_pred)
    flash("Your Prediction Result")
    return render_template('main.html')


@app.route('/')
def come_back_5():
    """
    This makes the page refresh and the user can click on the download link to download the file
    """
    return redirect("main.html", code=302)
#
#
@app.route('/Web_Results/Results.csv')
def download_file_Results():
    return send_from_directory('Web_Results', 'Results.csv')
#
#
#
# *******************************************    End of Prediction Score Section *****************************************
# .....................################################                ############################################
# ....................################################                ################################################
# ....................############################## !!! END OF MANUAL MODE !!!   ####################################
#
#
#
#
#
#
#
# ............................................... Lasso Regression Section ...............................
# ###############################################  Lasso Regression ####################
# ###############################################  Lasso Regression ####################
#
#
@app.route('/Lasso_Regression_Initial', methods=["GET", "POST"])
def Lasso_Regression_Initial():
    """
    This function is for taking a file as input from the user saves it in the designated folder
     and passes it on to the training the model script along with the feature names
     the user has selected.
    """
    print("You are in Lasso Initial")
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        # This saves the uploaded csv file in the designated folder
        uploaded_file.save(os.path.join(app.config['UPLOAD_LASSO_REGRESSION_INITIAL'], filename))
        # Pass the parameters to the boosting model
    Lasso_Regression_N1.make_it_rain(filename)
    return ('', 204)
#
#
#
#
#
@app.route('/Web_Lasso_Regression_Initial/CustomModel_rmse.txt')
def View_RMSE_LassoRegression_Initial():
    return send_from_directory('Web_Lasso_Regression_Initial','CustomModel_rmse.txt')


@app.route('/Web_Lasso_Regression_FeatureImportance/TopFeatures.txt')
def download_Lasso_Regression_RecommendedFeatures():
    return send_from_directory('Web_Lasso_Regression_FeatureImportance', 'TopFeatures.txt')


@app.route('/Lasso_Regression_NotInitial', methods=["GET", "POST"])
def Lasso_Regression_NotInitial():
    """
    This function is for taking a file as input from the user saves it in the designated folder
     and passes it on to the training the model script along with the feature names
     the user has selected.
    """
    print("You are in Lasso Regression Not Initial")
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        # This saves the uploaded csv file in the designated folder
        uploaded_file.save(os.path.join(app.config['UPLOAD_LASSO_REGRESSION_NOTINITIAL'], filename))
    num_features = int(request.form.get('NumFeatures'))
    Lasso_Regression_N2.make_it_rain(filename,num_features)
    return ('', 204)

@app.route('/Web_Lasso_Regression_NotInitial/CustomModel_rmse.txt')
def View_Lasso_Regression_NotInitial_RMSE():
    return send_from_directory('Web_Lasso_Regression_NotInitial', 'CustomModel_rmse.txt')

"""
Now we predict the scores
"""
# ---------------------*********************************************************************************************-------------
#
# *******************************************************************************************************************************
@app.route('/Lasso_Regression_Prediction', methods=["GET", "POST"])
def Lasso_Regression_Prediction():
    """
    This function is save user uploaded csv file in a designated folder and pass it on to the
    Prediction Script. Which will then open the model (saved in pkl format) and pass on the
    data from the csv file to predict the target variable (binding score)
    """
    print("You are in Lasso Regression Prediction Section")
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_LASSO_REGRESSION_PREDICTION'], filename))
        num_pred_features = int(request.form.get('NumPredFeatures'))
        Lasso_Regression_Prediction_Script.make_it_rain(filename, num_pred_features)
    flash("Your prediction result is ready ")
    return ('', 204)
#
#
#
#
@app.route('/Web_Lasso_Regression_Results/Predicted_Results.csv')
def Lasso_Regression_Prediction_Download():
    return send_from_directory('Web_Lasso_Regression_Results', 'Predicted_Results.csv')
# ---------------------------------------------------***********************************************************-----------------
#

# .............................................End of lasso Regression Section .....................
#
#
# *************************************** Lasso Regression Manual Mode ***********************************
#   ####################################################################################################
#                   ###############################################################################
#                                   #############################################
# ******************************* Training the model section ********************************************
@app.route('/Lasso_Training_Model_Manual', methods=["GET", "POST"])
def Lasso_Training_Model_Manual():
    """
    This function is for taking a file as input from the user saves it in the designated folder
     and passes it on to the training the model script along with the feature names
     the user has selected.
    """
    alpha = float(request.form['param_lasso_alpha'])
    # This is to get multiple feature names in the form of a list
    features = request.form.getlist('lasso_model_training_options')
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        # This saves the uploaded csv file in the designated folder
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_LASSO_MODEL_MANUAL'], filename))
        # Pass the parameters to the boosting model
        Lasso_Regression_Manual.make_it_rain(filename, features,alpha)
    return render_template('main.html')
#
#
@app.route('/')
def come_back_34():
    """
    This makes the page refresh and the user can click on the download link to download the file
    """
    return redirect("main.html", code=302)
#
#
#
# ############################### End of Training the model section #########################################
#
#
#
#
# ********************************* Prediction Score Section ***********************************************
@app.route('/Lasso_Manual_Model_Prediction', methods=["GET", "POST"])
def Lasso_Manual_Model_Prediction():
    """
    This function is save user uploaded csv file in a designated folder and pass it on to the
    'Prediction Script'. Which will then open the model (saved in pkl format) and pass on the
    data from the csv file to predict the target variable (binding score)
    """
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    features_pred = request.form.getlist('lasso_model_predicting_options')
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_LASSO_MODEL_MANUAL_PREDICTION'], filename))
        Lasso_Regression_Manual_Prediction.make_it_rain(filename, features_pred)
    return render_template('main.html')


@app.route('/')
def come_back_45():
    """
    This makes the page refresh and the user can click on the download link to download the file
    """
    return redirect("main.html", code=302)
#
#
#
#
@app.route('/Web_Lasso_Regression_Manual_Prediction/Results.csv')
def download_file_Lasso_Manual_Results():
    return send_from_directory('Web_Lasso_Regression_Manual_Prediction', 'Results.csv')
#
#
#
# *******************************************    End of Prediction Score Section *****************************************
# .....................################################                ############################################
# ....................################################                ################################################
# ....................############################## !!! END OF LASSO REGRESSION MANUAL MODE !!!   ####################################
#
#
#
#*********************************************************************************************************
# ###############################################  Decission Tree Regressor ####################
#
#
@app.route('/DecisionTreeRegressor_Initial', methods=["GET", "POST"])
def DecisionTreeRegressor_Initial():
    """
    This function is for taking a file as input from the user saves it in the designated folder
     and passes it on to the training the model script along with the feature names
     the user has selected.
    """
    print("You are in Decision Tree Regressor Expert Mode")
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        # This saves the uploaded csv file in the designated folder
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_DECISION_TREE_REGRESSOR_INITIAL'], filename))
        # Pass the parameters to the boosting model
    DecisionTreeRegressor_1.make_it_rain(filename)
    return ('', 204)
#
#
#
#
#
@app.route('/Web_DecisionTree_FeatureImportance/TopFeatures.txt')
def download_Decision_Tree_RecommendedFeatures():
    return send_from_directory('Web_DecisionTree_FeatureImportance', 'TopFeatures.txt')

@app.route('/Web_Decision_Tree_Regression_Initial/CustomModel_rmse.txt')
def View_RMSE_DecisionTree_Initial():
    return send_from_directory('Web_Decision_Tree_Regression_Initial','CustomModel_rmse.txt')


@app.route('/DecisionTreeRegressor_NotInitial', methods=["GET", "POST"])
def DecisionTreeRegressor_NotInitial():
    """
    This function is for taking a file as input from the user saves it in the designated folder
     and passes it on to the training the model script along with the feature names
     the user has selected.
    """
    print("You are in Decision Tree Regressor Not Initial")
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        # This saves the uploaded csv file in the designated folder
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_DECISION_TREE_REGRESSOR_NOTINITIAL'], filename))
    num_features = int(request.form.get('NumFeatures'))
    DecisionTreeRegressor_2.make_it_rain(filename, num_features)
    return ('', 204)


@app.route('/Web_Decision_Tree_Regression_NotInitial/CustomModel_rmse.txt')
def View_RMSE_DecisionTree_NotInitial():
    return send_from_directory('Web_Decision_Tree_Regression_NotInitial', 'CustomModel_rmse.txt')
"""
Now we predict the scores
"""
# ---------------------*********************************************************************************************-------------
#
# *******************************************************************************************************************************
@app.route('/Decision_Tree_Prediction', methods=["GET", "POST"])
def Decision_Tree_Prediction():
    """
    This function is save user uploaded csv file in a designated folder and pass it on to the
    Prediction Script. Which will then open the model (saved in pkl format) and pass on the
    data from the csv file to predict the target variable (binding score)
    """
    print("You are in DecisionTree Prediction Section")
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_DECISION_TREE_PREDICTION'], filename))
        num_pred_features = int(request.form.get('NumPredFeatures'))
        Decision_Tree_Prediction_Script.make_it_rain(filename, num_pred_features)
    return ('', 204)
#
#
#
#
@app.route('/Web_Decision_Tree_Regression_Results/Predicted_Results.csv')
def Decision_Tree_Prediction_Download():
    return send_from_directory('Web_Decision_Tree_Regression_Results', 'Predicted_Results.csv')
# ---------------------------------------------------***********************************************************-----------------
#
#
#
#
#
#
#
# ################################################ End of Decision Tree Regressor ###############
#
#
# *************************************** DECISION TREE REGRESSOR Manual Mode ***********************************
#   ####################################################################################################
#                   ###############################################################################
#                                   #############################################
# ******************************* Training the model section ********************************************
@app.route('/DECISION_TREE_MANUAL_Training', methods=["GET", "POST"])
def DECISION_TREE_MANUAL_Training():
    """
    This function is for taking a file as input from the user saves it in the designated folder
     and passes it on to the training the model script along with the feature names
     the user has selected.
    """
    # Clean up job for the model generated is present in the script
    print("You are in Decision Tree Regressor Manual Mode")
    max_depth = float(request.form['param_max_depth'])
    min_samples_split = float(request.form['param_min_samples_split'])
    min_samples_leaf = float(request.form['param_min_samples_leaf'])
    min_weight_fraction_leaf = float(request.form['param_min_weight_fraction_leaf'])
    # This is to get multiple feature names in the form of a list
    features = request.form.getlist('decision_Tree_Manual_model_training_options')
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        # This saves the uploaded csv file in the designated folder
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_DECISION_TREE_REGRESSOR_MODEL_MANUAL'], filename))
        # Pass the parameters to the boosting model
        DecisionTreeRegressor_Manual.make_it_train(filename,features,max_depth,min_samples_split,min_samples_leaf,min_weight_fraction_leaf)
    return render_template('main.html')
#
#
@app.route('/')
def come_back_54():
    """
    This makes the page refresh and the user can click on the download link to download the file
    """
    return redirect("main.html", code=302)
#
#
#
# ############################### End of Training the model section #########################################
#
#
#
#
# ********************************* Prediction Score Section ***********************************************
@app.route('/Decision_Tree_Manual_Prediction', methods=["GET", "POST"])
def Decision_Tree_Manual_Prediction():
    """
     This function is save user uploaded csv file in a designated folder and pass it on to the
    Prediction Script. Which will then open the model (saved in pkl format) and pass on the
    data from the csv file to predict the target variable (binding score)
    """
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    features_pred = request.form.getlist('decision_tree_predicting_options')
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH_DECISION_TREE_REGRESSOR_MANUAL_PREDICTION'], filename))
        DecisionTreeRegressor_Manual_Prediction.make_it_rain(filename, features_pred)
    flash("Your Prediction Result")
    return render_template('main.html')


@app.route('/')
def come_back_65():
    """
    This makes the page refresh and the user can click on the download link to download the file
    """
    return redirect("main.html", code=302)
#
#
@app.route('/Web_Decision_Tree_Regressor_Manual_Prediction/Results.csv')
def download_file_Decision_Tree_Manual_Results():
    """
    Function to download the csv file which contains the extracted MORDRED features
    """
    return send_from_directory('Web_Decision_Tree_Regressor_Manual_Prediction', 'Results.csv')
#
#
#
# *******************************************    End of Prediction Score Section *****************************************
# .....................################################                ############################################
# ....................################################                ################################################
# ....................############################## !!! END OF DECISION TREE REGRESSOR MANUAL MODE !!!   ####################################
#
#
#
# Feel free to modify the parameters below
if __name__ == '__main__':
    app.run(threaded=True, processes=3)