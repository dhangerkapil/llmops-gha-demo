from promptflow import tool


@tool
def line_process(groundtruth: str, prediction: str):
    """
    This tool processes the prediction of a single line and returns the processed result.

    :param groundtruth: the groundtruth of a single line.
    :param prediction: the prediction of a single line.
    """

    # Add your line processing logic here
    return "Correct" if groundtruth.lower() == prediction.lower() else "Incorrect"
