import pandas as pd

def run_simulation(initial_id, initial_ar, alpha, delta, iterations):
    data = []

    id_val = initial_id
    ar_val = initial_ar

    misalignment = id_val - ar_val
    fatigue = abs(misalignment)

    data.append([1, id_val, ar_val, misalignment, fatigue])

    for i in range(2, int(iterations) + 1):

        ar_val = ar_val + alpha * (id_val - ar_val)
        id_val = id_val + delta

        misalignment = id_val - ar_val
        fatigue += abs(misalignment)

        data.append([i, id_val, ar_val, misalignment, fatigue])

    return pd.DataFrame(data, columns=[
        "Iteration", "ID", "AR", "Misalignment", "Fatigue"
    ])