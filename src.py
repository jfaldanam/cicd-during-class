import argparse
import pickle

import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

MODEL_PATH = "model.pkl"
IRIS_CLASSES = ["setosa", "versicolor", "virginica"]


def train():
    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"Test accuracy: {acc:.4f}")

    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved to {MODEL_PATH}")


def predict(features: list[float]):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    X = np.array(features).reshape(1, -1)
    prediction = int(model.predict(X)[0])
    probabilities = model.predict_proba(X)[0]

    print(f"Prediction : {prediction} ({IRIS_CLASSES[prediction]})")
    for cls, prob in zip(IRIS_CLASSES, probabilities):
        print(f"  {cls}: {prob:.4f}")


def main():
    parser = argparse.ArgumentParser(description="Iris MLOps CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("train", help="Train the model and save it to disk")

    predict_parser = subparsers.add_parser("predict", help="Run inference on input features")
    predict_parser.add_argument(
        "--features",
        type=float,
        nargs=4,
        required=True,
        metavar=("SEPAL_LEN", "SEPAL_WID", "PETAL_LEN", "PETAL_WID"),
        help="Four Iris feature values",
    )

    args = parser.parse_args()

    if args.command == "train":
        train()
    elif args.command == "predict":
        predict(args.features)


if __name__ == "__main__":
    main()
