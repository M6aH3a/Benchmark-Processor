from hml_process import BenchmarkProcessor

input_hml = "HardwareMonitoring.hml"

processor = BenchmarkProcessor(input_hml)
benchmarks = processor.parse_hml_to_dataframe()
processor.generate_pdf_reports(benchmarks)
