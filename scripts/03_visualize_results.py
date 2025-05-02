import argparse
import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_hist(df, col, out_dir):
    plt.figure()
    df[col].hist(bins=30)
    plt.title(f"Distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(out_dir, f"{col}_hist.png"))
    plt.close()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--in", dest="inp", type=str, default="outputs/tree_stats.csv")
    p.add_argument("--outdir", type=str, default="outputs/figures")
    args = p.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    df = pd.read_csv(args.inp)
    for metric in ["height", "diameter", "avg_degree", "avg_path_length"]:
        plot_hist(df, metric, args.outdir)

if __name__ == "__main__":
    main()
