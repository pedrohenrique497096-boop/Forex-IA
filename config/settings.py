# Ativos que a IA irá analisar
ASSETS = ["XAUUSD", "BTCUSD"]

# Timeframe padrão
TIMEFRAME = "M5"

# Confiança mínima para mostrar uma operação
MIN_CONFIDENCE = 75

# Histórico máximo salvo
MAX_HISTORY_RECORDS = 1000

# Pesos das estratégias
STRATEGY_WEIGHTS = {
    "trend": 1.2,
    "price_action": 1.1,
    "indicators": 1.0,
    "smc": 1.5,
    "ict": 1.4,
    "wyckoff": 1.0,
    "elliott": 0.9,
    "momentum": 1.1,
    "volatility": 1.0
}
