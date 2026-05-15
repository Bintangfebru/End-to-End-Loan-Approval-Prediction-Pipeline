# split DATA

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV
)
X = df[fitur_pilihan]
y = df["status_pinjaman"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,  stratify=y, random_state=42)
