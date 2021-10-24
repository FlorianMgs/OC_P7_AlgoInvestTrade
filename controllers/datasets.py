import csv
import os


def get_datasets() -> list:
    """
    :return: list of datasets paths
    """
    path = './data/datasets/'
    datasets = [path + file for file in os.listdir(path)]
    print(datasets)
    return datasets


def create_actions(path: str) -> list:
    """
    :param path: path to csv file containing actions
    :return: list of actions as tuples
    """
    actions = []
    with open(path, newline='') as dataset_file:
        dataset = csv.DictReader(dataset_file)
        for row in dataset:
            actions.append((row["name"], float(row["price"]), float(row["roi"])))

    for action in actions:
        print(action)
    return actions

