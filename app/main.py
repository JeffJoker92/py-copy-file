import os


def copy_file(command: str) -> None:

    try:

        formated_str = command.split(" ")
        first_file = str(formated_str[1])
        second_file = str(formated_str[2])

        if first_file == second_file:
            return

        if not os.path.isfile(first_file):
            return

        if len(formated_str) != 3 or formated_str != "cp":
            return

        with open(second_file, "w") as for_write, open(first_file, "r") as for_read:
            for_write.write(for_read.read())

    except IndexError:
        return
