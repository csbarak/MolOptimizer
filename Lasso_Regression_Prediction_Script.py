"""
This is the file which is responsible to generate csv file containing the predicted values
"""
def make_it_rain(filename,num_pred_features):
    import pandas
    import sklearn
    import pickle
    import os
    import numpy as np
    PATH_OF_SCRIPT = r"<Add path to UPLOADS_LASSO_REGRESSION_PREDICTION>"
    os.chdir(PATH_OF_SCRIPT)
    dataframe = pandas.read_csv('<Add path to UPLOADS_LASSO_REGRESSION_PREDICTION\\>' + filename)
    with open("<Add path to Web_Lasso_Regression_FeatureImportance\\TopFeatures.txt>") as f:
        mylist = f.read().splitlines()
    SelectedFeatures = mylist[0:num_pred_features]
    X = dataframe
    X=X[SelectedFeatures]
    model = pickle.load(open('<Add path to Web_Lasso_Regression_NotInitial\\Lasso_Regression_NotInitial.pkl>', "rb"))
    predictions = model.predict(X)
    pandas.DataFrame(predictions, columns=['predictions']).to_csv(r'<Add path to Web_Lasso_Regression_Results\Predicted_Results.csv>', header=True)


