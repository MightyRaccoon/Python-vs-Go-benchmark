from datetime import datetime, timedelta
from typing import Dict, Union

import numpy as np


def generate_row(index: int) -> Dict[str, Union[int, float, str, datetime]]:

    base_date = datetime.fromisoformat("2021-10-10 00:00:00")
    reindex = index % 86400
    creation_diff = np.random.uniform(
        low=0,
        high=86400
    )

    center_latitude = 52.3112
    center_longitude = 13.2417

    return {

        "order_id": index,
        "row_created_at": str(base_date + timedelta(seconds=creation_diff)),

        "pickup_latitude": center_latitude + np.random.uniform(-1, 1),
        "pickup_longitude": center_longitude + np.random.uniform(-1, 1),

        "customer_latitude": center_latitude + np.random.uniform(-1, 1),
        "customer_longitude": center_longitude + np.random.uniform(-1, 1),
    }