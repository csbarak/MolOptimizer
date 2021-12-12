# ###############################################  Lasso Regression ####################

@app.route('/Lasso_Regression_Initial', methods=["GET", "POST"])
def Lasso_Regression_Initial():
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
    Lasso_Regression_1.make_it_rain(filename)
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
def Lasso_Regression_RecommendedFeatures():
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
    DecisionTreeRegressor_2.make_it_rain(filename, num_features)
    return ('', 204)


@app.route('/Web_Lasso_Regression_NotInitial/CustomModel_rmse.txt')
def View_RMSE_Lasso_Regression_NotInitial():
    return send_from_directory('Web_Lasso_Regression_NotInitial', 'CustomModel_rmse.txt')
"""
Now we predict the scores
"""
# ---------------------*********************************************************************************************-------------
#
# *******************************************************************************************************************************
@app.route('/Decision_Tree_Prediction', methods=["GET", "POST"])
def Lasso_Regression_Prediction():
    """
    This function is save user uploaded csv file in a designated folder and pass it on to the
    'Prediction Script'. Which will then open the model (saved in pkl format) and pass on the
    data from the csv file after scaling it as 'X' variable to predict the target variable (binding score)
    """
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_LASSO_REGRESSION_PREDICTION'], filename))
        num_pred_features = int(request.form.get('NumPredFeatures'))
        Lasso_Regression_Prediction_Script.make_it_rain(filename, num_pred_features)
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