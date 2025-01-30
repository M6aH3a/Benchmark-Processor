import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.ticker import MaxNLocator

class BenchmarkProcessor:
    def __init__(self, input_hml: str):
        self.input_hml = input_hml
        sns.set_style("darkgrid")
        sns.set_context("talk")
        sns.set_palette("Set2")

    def parse_hml_to_dataframe(self):
        with open(self.input_hml, "r") as file:
            lines = file.readlines()
        benchmarks = {}
        current_test = 0
        headers = None
        data = []
        for line in lines:
            if line.startswith("00,"):
                if headers and data:
                    df = self.create_benchmark_df(data, headers)
                    benchmarks[current_test] = df
                current_test += 1
                data = []
                headers = None
                continue
            if line.startswith("02,") and not headers:
                headers = [h.strip() for h in re.split(r",\s*", line.strip())][2:]
                continue
            if line.startswith("80,") and headers:
                values = [v.strip() for v in re.split(r",\s*", line.strip())]
                data.append(values[1:])
        if headers and data:
            df = self.create_benchmark_df(data, headers)
            benchmarks[current_test] = df
        print(f"Processed {len(benchmarks)} benchmarks.")
        return benchmarks

    def create_benchmark_df(self, data: list, headers: list):
        df = pd.DataFrame(data, columns=["Timestamp"] + headers)
        df["Timestamp"] = self.convert_timestamps(df["Timestamp"])
        return df

    def convert_timestamps(self, timestamps):
        parsed_times = pd.to_datetime(timestamps, dayfirst=True)
        start_time = parsed_times.min()
        return (parsed_times - start_time).dt.total_seconds()

    def draw_plot(self, df, metrics: list, title: str, output_pdf: PdfPages):
        plt.figure(figsize=(10, 6))
        ax = plt.gca()
        for metric in metrics:
            if metric in df.columns:
                sns.lineplot(x=df["Timestamp"], y=df[metric], label=metric, ax=ax)
        ax.set_xlabel("Time (seconds)")
        ax.set_ylabel(title)
        ax.set_title(f"{title} over time")
        ax.legend()
        ax.yaxis.set_major_locator(MaxNLocator(6))
        plt.tight_layout()
        output_pdf.savefig()
        plt.close()

    def generate_pdf_reports(self, benchmarks: dict):
        for test_id, df in benchmarks.items():
            filename = f"benchmark_{test_id}.pdf"
            with PdfPages(filename) as output_pdf:
                self.draw_plot(df, ["Framerate", "Framerate 1% Low", "Framerate 0.1% Low"], "Framerate", output_pdf)
                for metric in ["CPU usage", "GPU usage", "RAM usage \\ process", "Memory usage \\ process"]:
                    self.draw_plot(df, [metric], metric, output_pdf)
            print(f"Saved PDF: {filename}")
