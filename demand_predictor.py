from typing import Dict, Any, List
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class DemandPredictor:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        
    def prepare_data(self, data: Dict[str, Any]) -> np.ndarray:
        """Prepare and preprocess data for demand prediction."""
        try:
            # Extract features and target
            X = []
            y = []
            
            df = pd.DataFrame(data)
            for i in range(len(df)):
                if i > 0:
                    feature = [df['price'][i-1], df['volume'][i-1]]
                    label = df['demand'][i]
                    X.append(feature)
                    y.append(label)
                    
            return np.array(X), np.array(y)
        except Exception as e:
            self.logger.error(f"Error preparing data: {str(e)}")
            raise

    def train_model(self, features: np.ndarray, labels: np.ndarray) -> LinearRegression:
        """Train a linear regression model for demand prediction."""
        try:
            X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
            
            model = LinearRegression()
            model.fit(X_train, y_train)
            
            # Validate the model
            score = model.score(X_test, y_test)
            self.logger.info(f"Model trained with a score of {score:.2f}")
            
            return model
        except Exception as e:
            self.logger.error(f"Error training model: {str(e)}")
            raise

    def predict_demand(self, model: LinearRegression, input_features: List[List[float]]) -> np.ndarray:
        """Predict demand using a trained model."""
        try:
            return model.predict(input_features)
        except Exception as e:
            self.logger.error(f"Error making predictions: {str(e)}")
            raise