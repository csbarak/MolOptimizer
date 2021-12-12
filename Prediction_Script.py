"""
This is the file which is responsible to generate csv file containing the predicted values
"""
def make_it_rain(filename, features):
    import pandas
    import sklearn
    import pickle
    import os
    import numpy as np
    PATH_OF_SCRIPT = r"D:\\Samuel\\WebServer\\UPLOADS_Prediction"
    os.chdir(PATH_OF_SCRIPT)
    dataframe = pandas.read_csv('D:\\Samuel\\WebServer\\UPLOADS_Prediction\\' + filename)
    X = dataframe[features]
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    model = pickle.load(open('D:\\Samuel\\WebServer\\Web_Models\\Your_model.pkl', "rb"))
    predictions = model.predict(X_scaled)
    prediction = pandas.DataFrame(predictions, columns=['predictions']).to_csv(r'D:\Samuel\WebServer\Web_Results\Results.csv', header=True)


