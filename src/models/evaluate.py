#Hasil Akhir

from sklearn.metrics import f1_score

y_train_pred = pipeline.predict(X_train)
train_score = f1_score(y_train, y_train_pred)
y_test_pred = pipeline.predict(X_test)
test_score = f1_score(y_test, y_test_pred)

print("Train F1:", train_score)
print("Test F1:", test_score)


from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
