import os
import json

def get_first_candidate():

    data_file = os.path.join(
        os.path.dirname(__file__),
        "..",
        "backend",
        "data",
        "raw",
        "candidates.jsonl"
    )

    with open(
        data_file,
        "r",
        encoding="utf-8"
    ) as f:

        candidate = json.loads(next(f))

    return candidate