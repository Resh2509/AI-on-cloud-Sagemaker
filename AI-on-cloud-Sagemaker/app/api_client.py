import requests

# FastAPI URL
BASE_URL = "http://127.0.0.1:8000"


def predict_customer(customer_data):
    """
    Send customer data to FastAPI
    """

    try:

        response = requests.post(
            f"{BASE_URL}/predict",
            json=customer_data,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:

        return {
            "error": "Unable to connect to FastAPI server."
        }

    except requests.exceptions.Timeout:

        return {
            "error": "Request timed out."
        }

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }


def get_prediction_history():
    """
    Fetch prediction history from FastAPI
    """

    try:

        response = requests.get(
            f"{BASE_URL}/history",
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:

        return []

    except requests.exceptions.Timeout:

        return []

    except requests.exceptions.RequestException:

        return []