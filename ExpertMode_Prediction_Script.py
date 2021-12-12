
def make_it_rain(filename,num_pred_features):
    import pandas
    import sklearn
    import pickle
    import os
    import numpy as np
    PATH_OF_SCRIPT = r"<Add path to UPLOADS_Prediction>"
    os.chdir(PATH_OF_SCRIPT)
    dataframe = pandas.read_csv('<Add path to UPLOADS_Prediction\\>' + filename)
    with open("<Add path to Web_Expert_FeatureImportance\\TopFeatures.txt>") as f:
        mylist = f.read().splitlines()
    SelectedFeatures = mylist[0:num_pred_features]
    X = dataframe
    X=X[SelectedFeatures]
    model = pickle.load(open('<Add path to Web_Expert_Models_NotInitial\\Expert_Mode_NotInitial.pkl>', "rb"))
    predictions = model.predict(X)
    prediction = pandas.DataFrame(predictions, columns=['predictions']).to_csv(r'<Add path to Web_Expert_Results\Predicted_Results.csv>', header=True)


