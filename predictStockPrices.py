import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []

def read_data(filename):
    with open(filename, 'r') as csvFile:
        csvFileReader = csv.reader(csvFile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('/')[0]))
            prices.append(float(row[3]))
    return

def predict_stock_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates),1))

    svr_lin = SVR(kernel = "linear", C=1e3)
    svr_poly = SVR(kernel = "poly", C=1e3, degree=2)
    svr_rbf = SVR(kernel = "rbf", C=1e3, gamma = 0.1)

    svr_lin.fit(dates,prices)
    svr_poly.fit(dates,prices)
    svr_rbf.fit(dates,prices)

    plt.scatter(dates,prices, color="black", label = "Data")
    plt.plot(dates, svr_lin.predict(dates), color="red", label = "Linear Model")
    plt.plot(dates, svr_poly.predict(dates), color="green", label = "Polynomial Model")
    plt.plot(dates, svr_rbf.predict(dates), color="blue", label = "RBF Model")
    plt.xlabel('Dates')
    plt.ylabel('Prices')
    plt.title('Support Vector Regression')
    plt.legend()
    plt.show()

    return svr_lin.predict(x)[0], svr_poly.predict(x)[0], svr_rbf.predict(x)[0]

read_data('OracleStockPrices.csv')
predicted_prices = predict_stock_prices(dates, prices, 2)
print(predicted_prices)
