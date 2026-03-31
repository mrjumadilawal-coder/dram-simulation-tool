import matplotlib.pyplot as plt


def plot_simulation(df):
    fig, ax = plt.subplots()

    ax.plot(df["Iteration"], df["ID"], label="ID")
    ax.plot(df["Iteration"], df["AR"], label="AR")
    ax.plot(df["Iteration"], df["Fatigue"], linestyle="--", label="Fatigue")

    ax.set_xlabel("Iteration")
    ax.set_ylabel("Value")
    ax.legend()
    ax.grid(True)

    return fig