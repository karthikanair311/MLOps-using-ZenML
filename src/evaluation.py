import logging
from abc import ABC, abstractmethod
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

class Evaluation(ABC):
    """
    
    """
    @abstractmethod
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        pass

class MSE(Evaluation):
    """
    
    """
    def calculate_score(self, y_true:np.ndarray, y_pred: np.ndarray)-> float:
        try:
            logging.info("Calculate MSE")
            mse = mean_squared_error(y_true, y_pred)
            logging.info("MSE: {}".format(mse))
            return mse
        except Exception as e:
            logging.error("Error in calculating MSE:{}".format(e))
            raise e
        
class R2Score(Evaluation):
    """
    Evaluation strategy that uses R2 Score
    """
    def calculate_score(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        try:
            logging.info("Entered the calculate_score method of the R2Score class")
            r2 = r2_score(y_true, y_pred)
            logging.info("The r2 score value is: " + str(r2))
            return r2
        except Exception as e:
            logging.error(
                "Exception occurred in calculate_score method of the R2Score class. Exception message:  "
                + str(e)
            )
            raise e
        
class RMSE(Evaluation):
    """
    
    """
    def calculate_score(self, y_true:np.ndarray, y_pred: np.ndarray)-> float:
        try:
            logging.info("Calculate RMSE")
            rmse = mean_squared_error(y_true, y_pred, squared=False)
            logging.info("MSE: {}".format(rmse))
            return rmse
        except Exception as e:
            logging.error("Error in calculating RMSE:{}".format(e))
            raise e