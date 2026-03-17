import pandas as pd
import ta


def analyze_trend(df: pd.DataFrame):

    ema50 = ta.trend.ema_indicator(df["close"], window=50)
    ema200 = ta.trend.ema_indicator(df["close"], window=200)

    if ema50.iloc[-1] > ema200.iloc[-1]:
        return {
            "name": "Trend",
            "bias": "bullish",
            "score": 12,
            "reason": "EMA50 acima da EMA200 indicando tendência de alta"
        }

    else:
        return {
            "name": "Trend",
            "bias": "bearish",
            "score": 12,
            "reason": "EMA50 abaixo da EMA200 indicando tendência de baixa"
        }


def analyze_rsi(df: pd.DataFrame):

    rsi = ta.momentum.rsi(df["close"], window=14)

    if rsi.iloc[-1] < 30:

        return {
            "name": "RSI",
            "bias": "bullish",
            "score": 8,
            "reason": "RSI em sobrevenda"
        }

    elif rsi.iloc[-1] > 70:

        return {
            "name": "RSI",
            "bias": "bearish",
            "score": 8,
            "reason": "RSI em sobrecompra"
        }

    else:

        return {
            "name": "RSI",
            "bias": "neutral",
            "score": 3,
            "reason": "RSI neutro"
        }


def analyze_macd(df: pd.DataFrame):

    macd = ta.trend.macd(df["close"])
    macd_signal = ta.trend.macd_signal(df["close"])

    if macd.iloc[-1] > macd_signal.iloc[-1]:

        return {
            "name": "MACD",
            "bias": "bullish",
            "score": 7,
            "reason": "MACD cruzamento positivo"
        }

    else:

        return {
            "name": "MACD",
            "bias": "bearish",
            "score": 7,
            "reason": "MACD cruzamento negativo"
        }


def analyze_price_action(df: pd.DataFrame):

    last = df.iloc[-1]
    prev = df.iloc[-2]

    if last["close"] > prev["high"]:

        return {
            "name": "Price Action",
            "bias": "bullish",
            "score": 10,
            "reason": "Rompimento do candle anterior"
        }

    elif last["close"] < prev["low"]:

        return {
            "name": "Price Action",
            "bias": "bearish",
            "score": 10,
            "reason": "Rompimento de baixa do candle anterior"
        }

    else:

        return {
            "name": "Price Action",
            "bias": "neutral",
            "score": 4,
            "reason": "Mercado lateral"
        }


def run_all_strategies(df):

    results = []

    results.append(analyze_trend(df))
    results.append(analyze_rsi(df))
    results.append(analyze_macd(df))
    results.append(analyze_price_action(df))

    return results
