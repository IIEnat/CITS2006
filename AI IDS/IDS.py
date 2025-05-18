import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
)


INPUT_CSV = 'big_dataset.csv'
df = pd.read_csv(INPUT_CSV)

X = df.drop(columns=['class'])
y = df['class']


numeric_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_cols = ['service', 'flag', 'protocol_type']

numeric_transformer = StandardScaler()

cat_transformer = OneHotEncoder(handle_unknown='ignore')


preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_cols),
        ('cat', cat_transformer, categorical_cols)
    ]
)

clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)


accuracy  = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall    = recall_score(y_test, y_pred, zero_division=0)
f1        = f1_score(y_test, y_pred, zero_division=0)
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

total   = len(y_test)
correct = tp + tn


print(f"Accuracy : {accuracy:.4f} → {correct} out of {total} packets correctly classified")
print(f"Precision: {precision:.4f} → {tp} of {tp + fp} predicted anomalous were actually anomalous")
print(f"Recall   : {recall:.4f} → {tp} of {tp + fn} actual anomalous packets were correctly detected")
print(f"F1 Score : {f1:.4f} → harmonic mean of precision and recall")
print(f"Counts   : TP={tp}, TN={tn}, FP={fp}, FN={fn}")
