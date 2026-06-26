import joblib
import matplotlib.pyplot as plt

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    roc_auc_score,
    RocCurveDisplay
)

MODEL_PATH = "artifacts/best_model.pkl"
X_TEST_PATH = "artifacts/X_test.pkl"
Y_TEST_PATH = "artifacts/y_test.pkl"


def main():

    model = joblib.load(MODEL_PATH)
    X_test = joblib.load(X_TEST_PATH)
    y_test = joblib.load(Y_TEST_PATH)

    y_pred = model.predict(X_test)

    print("\nClassification Report\n")
    report = classification_report(y_test, y_pred)
    print(report)

    with open(
        "reports/classification_report.txt",
        "w"
    ) as f:
        f.write(report)

    cm = confusion_matrix(y_test, y_pred)

    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm
    )

    disp.plot()

    plt.savefig(
        "reports/confusion_matrix.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(X_test)[:, 1]

        roc_auc = roc_auc_score(
            y_test,
            probabilities
        )

        print(f"\nROC-AUC Score: {roc_auc:.4f}")

        RocCurveDisplay.from_predictions(
            y_test,
            probabilities
        )

        plt.savefig(
            "reports/roc_curve.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()


if __name__ == "__main__":
    main()