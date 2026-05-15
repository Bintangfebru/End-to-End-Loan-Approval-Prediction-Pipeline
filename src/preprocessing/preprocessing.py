#Preprocessing pipeline
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
preprocessing = Pipeline([('imputer', SimpleImputer(strategy='median'))])
