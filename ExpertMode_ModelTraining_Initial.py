def make_it_rain(filename):
    import pandas
    import sklearn
    import numpy as np
    import matplotlib.pyplot as plt
    import os
    import pickle
    from xgboost import XGBRegressor
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import make_scorer, mean_squared_error
    # path of script. leave the "r" as it is.. its here to fix the "\" symbol
    PATH_OF_SCRIPT = r" <Add complete path to UPLOADS_EXPERTMODE_ModelTraining>"
    os.chdir(PATH_OF_SCRIPT)
    # Start of clean up job
    file = 'Expert_Mode_Initial.pkl'
    location = "<Add complete path to Web_Expert_Models>"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    # End of clean up job
    dataframe = pandas.read_csv('< Add complete path to UPLOADS_EXPERTMODE_ModelTraining\\>' + filename)
    X = dataframe
    X = X.drop('BOND', axis=1)
    Y = dataframe['BOND']
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    Y_encoded = label_encoder.fit_transform(Y)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, Y_encoded, random_state=0)
    model = XGBRegressor(objective='reg:linear',verbosity=2, epochs=100,max_depth=7)
    eval_metric = ["rmse", "mae"]
    model.fit(X_train, y_train,eval_metric=eval_metric)
    preds = model.predict(X_test)
    print('Mean Square error ', mean_squared_error(y_test, preds))
    arr=np.array(np.asanyarray(X.columns[0:])[np.argsort(model.feature_importances_)][9::-1])
    # Start of clean up job
    file = 'TopFeatures.txt'
    location = "< Add complete path to Web_Expert_FeatureImportance>"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    # End of clean up job
    with open("<Add complete path to Web_Expert_FeatureImportance\\TopFeatures.txt>", "w") as txt_file:
        for line in arr:
            txt_file.write("".join(line) + "\n")  # works with any number of elements in a line
    with open('<Add complete path to Web_Expert_Models\Expert_Mode_Initial.pkl>', 'wb') as file:
        pickle.dump(model,file)

