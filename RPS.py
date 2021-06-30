def player(prev_play, opponent_history=[]):
    if prev_play == "":
        return "P"
    opponent_history.append(prev_play)

    column_dict = {"P": 0, "R": 1, "S": 2, 0: "P", 1: "R", 2: "S"}

    winning_matches = {
        "R": "P",
        "P": "S",
        "S": "R",
    }

    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    row_dict = {
        "RPP": 0,
        "RPR": 1,
        "RPS": 2,
        "RRP": 3,
        "RRR": 4,
        "RRS": 5,
        "RSP": 6,
        "RSR": 7,
        "RSS": 8,
        "PPP": 9,
        "PPR": 10,
        "PPS": 11,
        "PRP": 12,
        "PRR": 13,
        "PRS": 14,
        "PSP": 15,
        "PSR": 16,
        "PSS": 17,
        "SPP": 18,
        "SPR": 19,
        "SPS": 20,
        "SRP": 21,
        "SRR": 22,
        "SRS": 23,
        "SSP": 24,
        "SSR": 25,
        "SSS": 26,
    }

    if len(opponent_history) < 4:
        return "P"

    for index, play in enumerate(opponent_history):
        if index + 3 == len(opponent_history):
            break
        trio = play + opponent_history[index + 1] + opponent_history[index + 2]
        next = opponent_history[index + 3]
        matrix[row_dict[trio]][column_dict[next]] += 1

    for rowI, row in enumerate(matrix):
        for elI, el in enumerate(row):
            if el > 0:
                matrix[rowI][elI] = el / len(opponent_history)

    prev_trio = opponent_history[-3] + opponent_history[-2] + opponent_history[-1]
    current_row_i = row_dict[prev_trio]
    current_row = matrix[current_row_i]
    max_prob_i = current_row.index(max(current_row))
    guess = winning_matches[column_dict[max_prob_i]]
    return guess
