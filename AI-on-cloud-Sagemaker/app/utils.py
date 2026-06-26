from datetime import datetime


def format_probability(probability):
    """
    Convert probability into percentage.
    Example:
    0.6125 -> 61.25%
    """

    return f"{probability * 100:.2f}%"


def format_timestamp(timestamp):
    """
    Format ISO timestamp into a readable form.
    """

    try:

        dt = datetime.fromisoformat(timestamp)

        return dt.strftime("%d-%m-%Y %I:%M:%S %p")

    except Exception:

        return timestamp


def risk_color(risk_level):
    """
    Return a color based on risk level.
    """

    colors = {

        "Low": "🟢",

        "Medium": "🟡",

        "High": "🔴"

    }

    return colors.get(risk_level, "⚪")


def prediction_icon(prediction):
    """
    Return an icon based on prediction.
    """

    if "stay" in prediction.lower():

        return "✅"

    return "⚠️"