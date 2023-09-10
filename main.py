import pie_comparison, matplotlib.pyplot as plt, numpy as np

gl = np.array([])
winratel = np.array([])

for i in range(1, 30):
    games_called, winrate = pie_comparison.predict(i/1000)
    games_won = games_called*winrate
    print(f"Called: {games_called}, Winrate: {winrate}, Aggregate Won: {games_won}")

