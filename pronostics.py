import choix
import numpy as np

def pronostics(match, matrix):
    t1 = match[0]
    t2 = match[1]
    prob1 = matrix.at[t1, t2]
    prob2 = matrix.at[t2, t1]
    p1 = int(prob1 * 1000) / 10
    p2 = int(prob2 * 1000) / 10
    print(f"{t1} {p1}% -- {t2} {p2}%")
    return (prob1, prob2)


def get_prob(t1, t2, teams, params, DBG=False):
    idx1 = np.where(teams == t1)[0][0]
    idx2 = np.where(teams == t2)[0][0]

    if DBG:
        print(t1, idx1, teams[idx1], params[idx1])
        print(t2, idx2, teams[idx2], params[idx2])

    prob_1_wins, prob_2_wins = choix.probabilities([idx1, idx2], params)
    if DBG:
        print(f"Prob({t1} wins over {t2}): {prob_1_wins:.2f}")
        print(f"Prob({t2} wins over {t1}): {prob_2_wins:.2f}")

    return prob_1_wins
