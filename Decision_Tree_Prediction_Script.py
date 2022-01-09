"""
This is the file which is responsible to generate csv file containing the predicted values
"""
def make_it_rain(filename,num_pred_features):
    import pandas
    import sklearn
    import pickle
    import os
    import numpy as np
    from sklearn import metrics
    from sklearn import linear_model
    from xgboost import XGBClassifier
    from sklearn.pipeline import Pipeline
    from sklearn.linear_model import Lasso
    from sklearn.preprocessing import StandardScaler
    from sklearn.feature_selection import SelectFromModel
    from sklearn.model_selection import train_test_split, GridSearchCV

    PATH_OF_SCRIPT = r"D:\\Samuel\\WebServer\\UPLOADS_Decision_Tree_Prediction"
    os.chdir(PATH_OF_SCRIPT)
    dataframe = pandas.read_csv('D:\\Samuel\\WebServer\\UPLOADS_Decision_Tree_Prediction\\' + filename)
    with open("D:\\Samuel\\WebServer\\Web_DecisionTree_FeatureImportance\\TopFeatures.txt") as f:
        mylist = f.read().splitlines()
    SelectedFeatures = mylist[0:num_pred_features]
    X = dataframe
    X=X[SelectedFeatures]
    model = pickle.load(open('D:\\Samuel\\WebServer\\Web_Decision_Tree_Regression_NotInitial\\Decision_Tree_Regressor_NotInitial.pkl', "rb"))
    predictions = model.predict(X)
    pandas.DataFrame(predictions, columns=['predictions']).to_csv(r'D:\Samuel\WebServer\Web_Decision_Tree_Regression_Results\Predicted_Results.csv', header=True)


