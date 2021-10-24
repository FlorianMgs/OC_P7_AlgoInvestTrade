from controllers.datasets import get_datasets, create_actions


def dataset_selection() -> list:
    """
    :return: list of tuples corresponding to chosen dataset of actions
    """

    datasets = get_datasets()

    """
    Create data selection menu from datasets list
    """
    data_selection_menu = ""
    for i, dataset in enumerate(datasets):
        data_selection_menu = data_selection_menu + f"{i} - {dataset.split('/')[-1]}\n"

    while True:
        user_input = input("--- AgloInvest&Trade ---\n\n" +
                           data_selection_menu +
                           "b - Back\n\n"
                           "> "
                           )

        """
        if user input is an index of datasets, return corresponding list of actions.
        else, quit or continue
        """
        try:
            i = int(user_input)
            if 0 <= i < len(datasets):
                return create_actions(datasets[i])
        except ValueError:
            if user_input == "b":
                break



