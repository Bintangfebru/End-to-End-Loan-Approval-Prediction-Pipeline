best_model = RandomForestClassifier(
    **study.best_params,
    random_state=42,
    n_jobs=-1
)

pipeline = Pipeline([
    ('preprocessing', preprocessing),
    ('model', best_model)
])

pipeline.fit(X_train, y_train)