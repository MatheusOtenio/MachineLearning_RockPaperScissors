import random
from collections import Counter

from RPS_game import play

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])  # Aleatório no começo para evitar leitura fácil

    # Previsão baseada nos últimos 5 movimentos do oponente
    last_moves = "".join(opponent_history[-5:])
    
    # Dicionário para contar padrões e prever o próximo movimento do oponente
    patterns = {}
    for i in range(len(opponent_history) - 5):
        seq = "".join(opponent_history[i:i+5])
        next_move = opponent_history[i+5] if i+5 < len(opponent_history) else None
        if next_move:
            patterns[seq] = patterns.get(seq, Counter())
            patterns[seq][next_move] += 1

    # Se já vimos esse padrão antes, prever o próximo movimento do oponente
    if last_moves in patterns:
        predicted = patterns[last_moves].most_common(1)[0][0]
    else:
        predicted = random.choice(["R", "P", "S"])

    # Jogada que vence o movimento previsto
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[predicted]
