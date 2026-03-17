import pandas as pd
import numpy as np

def get_market_data(asset: str):

    # Simulação inicial de candles
    rows = 300

    data = {
        "open": np.random.uniform(100, 200, rows),
        "high": np.random.uniform(200, 250, rows),
        "low": np.random.uniform(90, 150, rows),
        "close": np.random.uniform(100, 200, rows),
        "volume": np.random.uniform(1000, 5000, rows),
    }

    df = pd.DataFrame(data)

    return df
