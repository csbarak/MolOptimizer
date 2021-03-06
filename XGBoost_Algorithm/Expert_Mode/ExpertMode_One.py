
def make_it_rain(filename):
    import pandas
    import sklearn
    import numpy as np
    import matplotlib.pyplot as plt
    import os
    import pickle
    import xgboost as xgb
    from sklearn.model_selection import GridSearchCV
    from xgboost import XGBRegressor
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.preprocessing import LabelEncoder
    # path of script. leave the "r" as it is.. its here to fix the "\" symbol
    dataframe = pandas.read_csv('<Add path to UPLOADS_EXPERTMODE_ModelTraining\\>' + filename)
    def algorithm_pipeline(X_train_data, X_test_data, y_train_data, y_test_data,
                           model, param_grid, cv=10, scoring_fit='neg_mean_squared_error',
                           do_probabilities=False):
        gs = GridSearchCV(
            estimator=model,
            param_grid=param_grid,
            cv=cv,
            n_jobs=-1,
            scoring=scoring_fit,
            verbose=2
        )
        fitted_model = gs.fit(X_train_data, y_train_data)

        if do_probabilities:
            pred = fitted_model.predict_proba(X_test_data)
        else:
            pred = fitted_model.predict(X_test_data)

        return fitted_model, pred

    X = dataframe
    X = X.drop('BOND', axis=1)
    Y = dataframe['BOND']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)
    model = xgb.XGBRegressor()
    param_grid = {
        'n_estimator': [350, 650, 950],
        'colsample_bytree': [0.25,0.65 ,0.8],
        'max_depth': [8, 11, 14],
        'reg_alpha': [0.75, 1.4, 1.6],
        'reg_lambda': [0.43, 0.65, 1.3],
        'subsample': [0.6, 0.85, 0.9]
    }
    model, pred = algorithm_pipeline(X_train, X_test, y_train, y_test, model, param_grid, cv=5)
    sample = model.best_params_
    colsample_value = sample['colsample_bytree']
    maxdepth_value = sample['max_depth']
    nestimators_value = sample['n_estimator']
    regalpha_value = sample['reg_alpha']
    reglambda_value = sample['reg_lambda']
    subsample_value = sample['subsample']
    model1 = XGBRegressor(verbosity=2,
                          colsample_bytree=colsample_value,
                          max_depth=maxdepth_value,
                          objective='reg:squarederror',
                          n_estimators=nestimators_value,
                          reg_alpha=regalpha_value,
                          reg_lambda=reglambda_value,
                          subsample=subsample_value)
    model1.fit(X_train, y_train)
    features = dataframe.drop('BOND', axis=1).columns
    importances = model1.feature_importances_
    indices = np.argsort(importances)
    important_feature = []
    for i in range(len(indices)):
        for i in indices:
            important_feature.append(features[i])
    top_important_features = important_feature[0:10]
    arr = np.array(top_important_features)
    # Start of clean up job
    file = 'TopFeatures.txt'
    location = "<Add path to Web_Expert_FeatureImportance>"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    # End of clean up job
    with open("<Add path to Web_Expert_FeatureImportance\\TopFeatures.txt>", "w") as txt_file:
        for line in arr:
            txt_file.write("".join(line) + "\n")  # works with any number of elements in a line