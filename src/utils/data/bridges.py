# src/utils/data/bridges.py

# Полный граф связности (каждая сеть → все остальные)
BRIDGES = {
    'BASE': ['OPTIMISM', 'ARBITRUM', 'LINEA', 'ETHEREUM'],
    'OPTIMISM': ['BASE', 'ARBITRUM', 'LINEA', 'ETHEREUM'],
    'ARBITRUM': ['BASE', 'OPTIMISM', 'LINEA', 'ETHEREUM'],
    'LINEA': ['BASE', 'ARBITRUM', 'OPTIMISM', 'ETHEREUM'],
    'ETHEREUM': ['BASE', 'ARBITRUM', 'OPTIMISM', 'LINEA'],
}

# Ограничения мостов (какой мост какие цепочки поддерживает)
BRIDGE_ROUTES = {
    'RELAY': ['BASE', 'ARBITRUM', 'OPTIMISM', 'LINEA', 'ETHEREUM'],
    'ACROSS': ['ETHEREUM', 'BASE', 'ARBITRUM', 'OPTIMISM'],  # ← LINEA не поддерживается
}
