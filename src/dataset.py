import kagglehub
import os
import shutil


def download_dataset_from_kagglehub(dataset: str, path: str) -> None:
    """
    Downloads a dataset from Kaggle.

    Args:
        dataset (str): The handle of the Kaggle dataset to download.
        path (str): The local directory path where the dataset should be downloaded.

    Raises:
        Exception: If any error occurs during the download process.

    Returns:
        None
    """
    try:
        dataset_path = kagglehub.dataset_download(
          handle=dataset
        )

        os.makedirs(path, exist_ok=True)

        for file_name in os.listdir(dataset_path):
            full_file_name = os.path.join(dataset_path, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, path)

        print(f"Dataset {dataset} downloaded successfully.")
    except Exception as e:
        print(f"Error downloading dataset: {e}")
        raise e
