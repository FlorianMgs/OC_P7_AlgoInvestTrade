import csv
import os


def get_datasets() -> list:
    """
    :return: list of datasets paths
    """
    path = './data/datasets/'
    datasets = [path + file for file in os.listdir(path)]
    return datasets


def create_actions(path: str) -> list:
    """
    :param path: path to csv file containing actions
    :return: list of actions as tuples
    Filter actions: remove actions where price <= 0
                    remove duplicates
    """
    actions = []
    with open(path, newline='') as dataset_file:
        dataset = csv.DictReader(dataset_file)
        for row in dataset:
            if float(row["price"]) > 0 and float(row["roi"]) > 0:
                actions.append((row["name"], float(row["price"]), float(row["roi"])))
        else:
            return list(set(actions))

