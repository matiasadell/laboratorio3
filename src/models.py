from sklearn.ensemble import RandomForestClassifier

class FraudRandomForest:
    def __init__(self, n_estimators=100, max_depth=6):
        # El modelo vive dentro de la clase
        self.clf = RandomForestClassifier(
            n_estimators=n_estimators, 
            max_depth=max_depth, 
            random_state=42
        )
    
    def fit(self, X, y):
        """Entrena el modelo"""
        self.clf.fit(X, y)
        
    def predict(self, X):
        """Predice clases (0 o 1)"""
        return self.clf.predict(X)
    
    def predict_proba(self, X):
        """Predice probabilidades (útil para AUC)"""
        return self.clf.predict_proba(X)