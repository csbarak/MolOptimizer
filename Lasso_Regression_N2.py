def make_it_rain(filename,Num_Features):
    import time
    import pandas
    import pickle
    import sklearn
    import os
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import metrics
    from sklearn import linear_model
    from xgboost import XGBClassifier
    from sklearn.pipeline import Pipeline
    from sklearn.linear_model import Lasso
    from sklearn.preprocessing import StandardScaler
    from sklearn.feature_selection import SelectFromModel
    from sklearn.model_selection import train_test_split, GridSearchCV
    # path of script. leave the "r" as it is.. its here to fix the "\" symbol
    PATH_OF_SCRIPT = r"<Add path to UPLOADS_Lasso_Regression_NotInitial>"
    os.chdir(PATH_OF_SCRIPT)
    # Start of clean up job
    file = 'Lasso_Regression_NotInitial.pkl'
    location = "<Add path to Web_Lasso_Regression_NotInitial>"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    # End of clean up job
    with open("<Add path to Web_Lasso_Regression_FeatureImportance\\TopFeatures.txt>") as f:
        mylist = f.read().splitlines()
    SelectedFeatures = mylist[0:Num_Features]

    dataframe = pandas.read_csv('<Add path to UPLOADS_Lasso_Regression_NotInitial\\>' + filename)
    X = dataframe
    X = X.drop('BOND', axis=1)
    X = X[SelectedFeatures]
    Y = dataframe['BOND']
    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', Lasso())
    ])
    search = GridSearchCV(pipeline, {'model__alpha': np.arange(0.1, 10, 0.5)}, cv=5,
                          scoring="neg_mean_squared_error", verbose=3)
    search.fit(X_train, y_train)
    optimum_alpha = search.best_params_.get('model__alpha')
    clf = linear_model.Lasso(alpha=optimum_alpha)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    with open('<Add path to Web_Lasso_Regression_NotInitial\Lasso_Regression_NotInitial.pkl>', 'wb') as file:
        pickle.dump(clf, file)
    MeanAbsoluteError = metrics.mean_absolute_error(y_test, y_pred)
    MeanSquaredError = metrics.mean_squared_error(y_test, y_pred)
    RootMeanSquaredError = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
    MeanAbsoluteErrorWrite = str(MeanAbsoluteError)
    MeanSquaredErrorWrite = str(MeanSquaredError)
    RootMeanSquaredErrorWrite = str(RootMeanSquaredError)
    txt_file = open("<Add path to Web_Lasso_Regression_NotInitial\\CustomModel_rmse.txt>", "w")
    txt_file.write("The Mean Absolute Error is ")
    txt_file.write(MeanAbsoluteErrorWrite)
    txt_file.write("The Mean Squared Error is")
    txt_file.write(MeanSquaredErrorWrite)
    txt_file.write("The Root Mean Squared Error is")
    txt_file.write(RootMeanSquaredErrorWrite)