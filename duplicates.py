import argparse
import os
import timeit
from collections import defaultdict


def parser_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "directory_path",
        help="The path to directory")
    return parser.parse_args()


def get_all_files(directory_path):
    all_files = defaultdict(list)
    for root, dirs, file_names in os.walk(directory_path):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            combining_name_size = (file_name, file_size)
            all_files[combining_name_size].append(file_path)
    return all_files


def search_duplicates(all_files):
    duplicates = {}
    for combining_name_size, file_paths in all_files.items():
        if (len(file_paths) > 1):
            duplicates.update({combining_name_size: file_paths})
    return duplicates


def print_the_result(duplicates, search_time):
    print('\nДубликаты:')
    for combining_name_size, file_paths in duplicates.items():
        file_name = combining_name_size[0]
        file_size = combining_name_size[1]
        print('\nФайл: {}'.format(file_name))
        print('Размер: {}'.format(file_size))
        for number, file_path in enumerate(file_paths, start=1):
            print('{}{}. {}'.format('\t', number, file_path))
    print('\nНайдено {} файла(ов).'.format(len(duplicates)))
    print('На поиск ушло {} секунды.'.format(round(search_time, 2)))


if __name__ == '__main__':
    arguments = parser_arguments()
    start_time = timeit.default_timer()
    all_files = get_all_files(arguments.directory_path)
    duplicates = search_duplicates(all_files)
    search_time = timeit.default_timer()-start_time
    print_the_result(duplicates, search_time)
