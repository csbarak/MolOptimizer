def make_it_rain(filename, features):
    import pandas
    import sklearn
    import pickle
    import os
    import numpy as np
    import pandas
    import time
    import sklearn
    from xgboost import XGBClassifier
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split
    PATH_OF_SCRIPT = r"<Add path to UPLOADS_Lasso_Regression_Manual_Prediction>"
    os.chdir(PATH_OF_SCRIPT)
    dataframe = pandas.read_csv('<Add path to UPLOADS_Lasso_Regression_Manual_Prediction\\>' + filename)
    X = dataframe[features]
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = pickle.load(open('<Add path to Web_Lasso_Regression_Manual_Training\\Lasso_Regression_Manual.pkl>', "rb"))
    predictions = model.predict(X_scaled)
    prediction = pandas.DataFrame(predictions, columns=['predictions']).to_csv(r'<Add path to Web_Lasso_Regression_Manual_Prediction\Results.csv>', header=True)


