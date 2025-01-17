import argparse
import os
from datetime import datetime

from dataset import download_dataset_from_kagglehub
from process import write_raw_data_to_parquet

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str)
    parser.add_argument("--dataset_path", type=str)

    args = parser.parse_args()

    download_dataset_from_kagglehub(args.dataset, args.dataset_path)

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    output_parquet = f"amazon-sales-{current_datetime}.parquet"

    data_source_uri = os.path.join(args.dataset_path, "Amazon Sale Report.csv")
    data_output_uri = os.path.join(args.dataset_path, output_parquet)

    write_raw_data_to_parquet(data_source_uri, data_output_uri)
