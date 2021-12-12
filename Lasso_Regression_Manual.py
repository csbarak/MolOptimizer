def make_it_rain(filename,features ,param_alpha):
    # Importing the required libraries
    import pandas
    import time
    import sklearn
    from xgboost import XGBClassifier
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    import pickle
    import pandas
    import time
    import os
    import pickle
    import sklearn
    #
    # Reading the data
    #
    dataframe = pandas.read_csv('<Add path to UPLOADS_Lasso_Regression_Manual' + filename)
    X = dataframe
    X = X.drop('BOND', axis=1)
    X = dataframe[features]
    # This is the target variable
    #
    Y = dataframe['BOND']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)
    from sklearn import linear_model
    clf = linear_model.Lasso(alpha=param_alpha)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    #
    # All the error metrics which we will display to the user
    #
    from sklearn import metrics
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    MeanAbsoluteError=metrics.mean_absolute_error(y_test, y_pred)
    MeanAbsoluteErrorWrite=str(MeanAbsoluteError)
    MeanSquaredError=metrics.mean_squared_error(y_test, y_pred)
    MeanSquaredErrorWrite=str(MeanSquaredError)
    RootMeanSquaredError=np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    RootMeanSquaredErrorWrite=str(RootMeanSquaredError)
    with open('<Add path to Web_Lasso_Regression_Manual_Training\Lasso_Regression_Manual.pkl>', 'wb') as file:
        pickle.dump(clf, file)
    # Start of clean up job
    file = 'CustomModel_rmse.txt'
    location = "<Add path to Web_Lasso_Regression_Manual_Training>"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    # End of clean up job
    txt_file = open("<Add path to Web_Lasso_Regression_Manual_Training\\CustomModel_rmse.txt>", "w")
    txt_file.write("The Mean Absolute Error is ")
    txt_file.write(MeanAbsoluteErrorWrite)
    txt_file.write("The Mean Squared Error is")
    txt_file.write(MeanSquaredErrorWrite)
    txt_file.write("The Root Mean Squared Error is")
    txt_file.write(RootMeanSquaredErrorWrite)

