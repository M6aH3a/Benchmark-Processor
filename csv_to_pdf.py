import pandas as pd
import matplotlib.pyplot as plt
import glob
from matplotlib.backends.backend_pdf import PdfPages

def plot_benchmark_data(csv_file, pdf_pages):
    df = pd.read_csv(csv_file)

    if "Timestamp" in df.columns:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

    metrics = [
        "Framerate", "CPU usage", "GPU usage",
        "RAM usage \\ process", "Memory usage \\ process"
    ]

    fig, axes = plt.subplots(len(metrics), 1, figsize=(10, 15), sharex=True)
    fig.suptitle(f"Performance Metrics - {csv_file}")

    for i, metric in enumerate(metrics):
        if metric in df.columns:
            ax = axes[i]
            ax.plot(df["Timestamp"], df[metric], label=metric, marker="o", linestyle="-")
            ax.set_ylabel(metric)
            ax.legend()
            ax.grid(True)

    plt.xticks(rotation=45)
    plt.xlabel("Time")
    pdf_pages.savefig(fig)
    plt.close(fig)
    print(f"Added to PDF: {csv_file}")

csv_files = glob.glob("benchmark_*.csv")
output_pdf = "performance_report.pdf"

with PdfPages(output_pdf) as pdf_pages:
    for csv_file in csv_files:
        plot_benchmark_data(csv_file, pdf_pages)

print(f"Saved all plots to {output_pdf}")
