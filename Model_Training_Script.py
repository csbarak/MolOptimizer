def make_it_train(filename, features,param_learning_rate,param_max_depth,param_lambda,param_alpha,param_rate_drop):
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
    PATH_OF_SCRIPT = r"D:\\Samuel\\WebServer\\UPLOADS_Model_Training"
    os.chdir(PATH_OF_SCRIPT)
    # Start of clean up job
    file = 'Your_model.pkl'
    location = "D:\\Samuel\\WebServer\\UPLOADS_Model_Training"
    path = os.path.join(location, file)
    if os.path.exists(path):
        os.remove(path)
    # End of clean up job
    dataframe = pandas.read_csv('D:\\Samuel\\WebServer\\UPLOADS_Model_Training\\' + filename)
    print("I have read the csv file")
    X = dataframe[features]
    Y = dataframe['BOND']
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    Y_encoded = label_encoder.fit_transform(Y)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, Y_encoded, random_state=0)
    model = XGBRegressor(verbosity=2,
                         booster='gbtree',
                         learning_rate=int(param_learning_rate),
                         max_depth=int(param_max_depth),
                         reg_lambda=int(param_lambda),
                         reg_alpha=int(param_alpha),
                         rate_drop=int(param_rate_drop),
                         objective='reg:squarederror',
                         eval_metric='rmse')
    eval_metric = ["rmse"]
    model.fit(X_train, y_train, eval_metric=eval_metric)
    with open('D:\Samuel\WebServer\Web_Models\Your_model.pkl', 'wb') as file:
        pickle.dump(model, file)



