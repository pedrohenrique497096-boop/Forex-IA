import json
import os
from datetime import datetime


def save_history(result):

    file = "history.json"

    if os.path.exists(file):

        with open(file, "r") as f:
            try:
                data = json.load(f)
            except:
                data = []

    else:
        data = []

    result["timestamp"] = str(datetime.now())

    data.append(result)

    with open(file, "w") as f:
        json.dump(data, f, indent=2)
