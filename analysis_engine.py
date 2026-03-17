from strategies import run_all_strategies


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

    result = {
        "asset": asset,
        "direction": direction,
        "confidence": confidence,
        "summary": [s["reason"] for s in strategies]
    }

    return result
