import argparse
import os
import timeit


def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "directory_path",
        help="The path to directory")
    return parser.parse_args()


def search_duplicates(directory_path):
    duplicates = {}
    file_paths = []
    directory_paths = []
    for root, directories, files in os.walk(directory_path):
        directory_paths.append(root)
        for file in files:
            if file in duplicates:
                continue
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_paths.append(file_path)
            for again_root, again_directories, again_files in os.walk(directory_path):
                    if again_root in directory_paths:
                        continue
                    for again_file in again_files:
                        if again_file in duplicates:
                            continue
                        again_file_path = os.path.join(again_root, again_file)
                        again_file_size = os.path.getsize(again_file_path)
                        if (again_file == file and
                                again_file_size == file_size and
                                again_file_path != file_path):
                                    file_paths.append(again_file_path)
            if (len(file_paths) > 1):
                duplicates.update({file: file_paths.copy()})
            file_paths.clear()
    return duplicates


def print_the_result(duplicates, search_time):
    print('\nДубликаты:')
    for file_name, file_paths in duplicates.items():
        print('{} {}'.format('\n', file_name))
        for number, file_path in enumerate(file_paths, start=1):
            print('{}{}. {}'.format('\t', number, file_path))
    print('\nНайдено {} файла(ов).'.format(len(duplicates)))
    print('На поиск ушло {} секунды.'.format(round(search_time, 2)))


if __name__ == '__main__':
    arguments = parser_arguments()
    start_time = timeit.default_timer()
    duplicates = search_duplicates(arguments.directory_path)
    search_time = timeit.default_timer()-start_time
    print_the_result(duplicates, search_time)
