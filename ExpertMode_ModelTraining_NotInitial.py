def make_it_rain(filename,Num_Features):
    import pandas
    import sklearn
    import numpy as np
    import matplotlib.pyplot as plt
    import os
    import pickle
    from xgboost import XGBRegressor
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import train_test_split
    # path of script. leave the "r" as it is.. its here to fix the "\" symbol
    PATH_OF_SCRIPT = r"< Add path to UPLOADS_EXPERTMODE_ModelTraining>"
    os.chdir(PATH_OF_SCRIPT)
    # Start of clean up job
    file = 'Expert_Mode_NotInitial.pkl'
    location = "<Add path to Web_Expert_Models_NotInitial>"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    # End of clean up job
    dataframe = pandas.read_csv('<Add path to UPLOADS_EXPERTMODE_ModelTraining_NotInitial\\>' + filename)
    with open("<Add path to Web_Expert_FeatureImportance\\TopFeatures.txt>") as f:
        mylist = f.read().splitlines()
    SelectedFeatures = mylist[0:Num_Features]
    X = dataframe
    X = X.drop('BOND',axis=1)
    X=X[SelectedFeatures]
    Y = dataframe['BOND']
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    Y_encoded = label_encoder.fit_transform(Y)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, Y_encoded, random_state=0)
    model = XGBRegressor(verbosity=2, epochs=100,max_depth=7)
    eval_metric = ["rmse", "mae"]
    model.fit(X_train, y_train, eval_metric=eval_metric)
    preds = model.predict(X_test)
    error_value=mean_squared_error(y_test, preds)
    value=str(error_value)
    with open('<Add path to Web_Expert_Models_NotInitial\Expert_Mode_NotInitial.pkl>', 'wb') as file:
        pickle.dump(model, file)
    # Start of clean up job
    file = 'CustomModel_rmse.txt'
    location = "<Add path to Web_Expert_Models_NotInitial>"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    # End of clean up job
    txt_file = open("<Add path to Web_Expert_Models_NotInitial\\CustomModel_rmse.txt>", "w")
    txt_file.write(value)


