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
    print("You are in Decision Tree Regressor Manual Mode Prediction")
    PATH_OF_SCRIPT = r"<Add complete path to UPLOADS_Decision_Tree_Regressor_Manual_Prediction>"
    os.chdir(PATH_OF_SCRIPT)
    dataframe = pandas.read_csv('< Add complete path to UPLOADS_Decision_Tree_Regressor_Manual_Prediction\\>' + filename)
    X = dataframe[features]
    model = pickle.load(open('<Add complete path to Web_Decision_Tree_Regressor_Manual_Mode\\Decision_Tree_Regressor_Manual.pkl>', "rb"))
    predictions = model.predict(X)
    prediction = pandas.DataFrame(predictions, columns=['predictions']).to_csv(r'<Add complete path to Web_Decision_Tree_Regressor_Manual_Prediction\Results.csv>', header=True)


