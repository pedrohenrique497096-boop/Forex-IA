from strategies import run_all_strategies


def calculate_trade_levels(df, direction):

    price = float(df["close"].iloc[-1])

    if direction == "BUY":

        entry = round(price, 2)
        stop = round(price * 0.995, 2)

        take1 = round(price * 1.005, 2)
        take2 = round(price * 1.010, 2)
        take3 = round(price * 1.015, 2)

    elif direction == "SELL":

        entry = round(price, 2)
        stop = round(price * 1.005, 2)

        take1 = round(price * 0.995, 2)
        take2 = round(price * 0.990, 2)
        take3 = round(price * 0.985, 2)

    else:

        entry = "-"
        stop = "-"
        take1 = "-"
        take2 = "-"
        take3 = "-"

    return entry, stop, take1, take2, take3


def analyze_asset(asset, df):

    strategies = run_all_strategies(df)

    bullish_score = 0
    bearish_score = 0

    for s in strategies:

        if s["bias"] == "bullish":
            bullish_score += s["score"]

        if s["bias"] == "bearish":
            bearish_score += s["score"]

    total = bullish_score + bearish_score

    if total == 0:
        confidence = 0
    else:
        confidence = round(max(bullish_score, bearish_score) / total * 100, 2)

    if bullish_score > bearish_score:
        direction = "BUY"

    elif bearish_score > bullish_score:
        direction = "SELL"

    else:
        direction = "NEUTRAL"

    entry, stop, take1, take2, take3 = calculate_trade_levels(df, direction)

    result = {
        "asset": asset,
        "direction": direction,
        "confidence": confidence,
        "entry": entry,
        "stop": stop,
        "take1": take1,
        "take2": take2,
        "take3": take3,
        "summary": [s["reason"] for s in strategies]
    }

    return result
