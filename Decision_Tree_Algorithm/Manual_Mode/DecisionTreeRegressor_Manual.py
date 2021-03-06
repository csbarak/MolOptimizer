def make_it_train(filename,features,param_max_depth, param_min_samples_split,param_min_samples_leaf,param_min_weight_fraction_leaf):
    # Importing the required libraries
    import pandas
    import time
    import os
    import pickle
    import sklearn
    from xgboost import XGBClassifier
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    from sklearn import metrics
    from sklearn import linear_model
    from xgboost import XGBClassifier
    from sklearn.pipeline import Pipeline
    from sklearn.linear_model import Lasso
    from sklearn.preprocessing import StandardScaler
    from sklearn.feature_selection import SelectFromModel
    from sklearn.model_selection import train_test_split, GridSearchCV
    #
    # Reading the data
    #
    dataframe = pandas.read_csv('< Add complete path to UPLOADS_Decision_Tree_Regressor_Manual_Mode\\>' + filename)
    X = dataframe
    X = X.drop('BOND', axis=1)
    X = dataframe[features]
    #
    # This is the target variable
    #
    Y = dataframe['BOND']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)
    from sklearn.tree import DecisionTreeRegressor
    regressor = DecisionTreeRegressor(max_depth=param_max_depth, min_samples_split=param_min_samples_split, min_samples_leaf=param_min_samples_leaf, min_weight_fraction_leaf=param_min_weight_fraction_leaf)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    #
    # All the error metrics which we will display to the user
    #
    from sklearn import metrics
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    # Extracting top ten most influential features from the model
    # Writing the error metrics to the file
    #
    #
    MeanAbsoluteError=metrics.mean_absolute_error(y_test, y_pred)
    MeanSquaredError=metrics.mean_squared_error(y_test, y_pred)
    RootMeanSquaredError=np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    MeanAbsoluteErrorWrite = str(MeanAbsoluteError)
    MeanSquaredErrorWrite = str(MeanSquaredError)
    RootMeanSquaredErrorWrite = str(RootMeanSquaredError)
    print(MeanAbsoluteErrorWrite)
    print(MeanSquaredErrorWrite)
    print(RootMeanSquaredErrorWrite)
    with open('<Add complete path to Web_Decision_Tree_Regressor_Manual_Mode\Decision_Tree_Regressor_Manual.pkl>', 'wb') as file:
        pickle.dump(regressor, file)
    # Start of clean up job
    file = 'CustomModel_rmse.txt'
    location = "<Add complete path to Web_Decision_Tree_Regressor_Manual_Mode>"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    # End of clean up job
    txt_file = open("Add complete path to Web_Decision_Tree_Regressor_Manual_Mode\\CustomModel_rmse.txt>", "w")
    txt_file.write("The Mean Absolute Error is ")
    txt_file.write(MeanAbsoluteErrorWrite)
    txt_file.write("The Mean Squared Error is")
    txt_file.write(MeanSquaredErrorWrite)
    txt_file.write("The Root Mean Squared Error is")
    txt_file.write(RootMeanSquaredErrorWrite)

