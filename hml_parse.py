import re
import pandas as pd

def parse_hml_to_csv(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    current_test = 0
    headers = None
    data = []
    test_files = []

    for line in lines:
        if line.startswith("00,"):
            if headers and data:
                save_to_csv(data, headers, current_test)
                test_files.append(f"benchmark_{current_test}.csv")

            current_test += 1
            data = []
            headers = None
            continue

        if line.startswith("02,") and not headers:
            cleaned_line = line.strip()
            split_headers = re.split(r",\s*", cleaned_line)
            headers = [h.strip() for h in split_headers][2:]
            continue

        if line.startswith("80,") and headers:
            values = re.split(r",\s*", line.strip())
            data.append(values[1:])

    if headers and data:
        save_to_csv(data, headers, current_test)
        test_files.append(f"benchmark_{current_test}.csv")

    print(f"Processed {current_test} benchmarks.")
    return test_files


def save_to_csv(data, headers, test_number):
    dataframe = pd.DataFrame(data, columns=["Timestamp"] + headers)
    output_file = f"benchmark_{test_number}.csv"
    dataframe.to_csv(output_file, index=False, encoding="utf-8")
    print(f"Saved file: {output_file}")


input_file = "HardwareMonitoring.hml"
parse_hml_to_csv(input_file)
