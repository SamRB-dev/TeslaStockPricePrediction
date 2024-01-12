import joblib
import warnings
warnings.filterwarnings('ignore')

def Prediction(Open: float, High: float, Low: float, Volume: float) -> list:
    model = joblib.load("stock-predictor-v2.job")
    prediction = model.predict([[Open, High, Low, Volume]])
    return prediction

print(Prediction(17.000000, 29.00, 10.540001, 1766300))