# Anti-Duplicator

The program searches for duplicate files in the specified folder.

# Quickstart

Example of script launch on Linux and Windows, Python 3.5:

```bash
$ python duplicates.py directory_path
```

The program displays in the console the names and size of the files that have duplicates, and also the paths to duplicates.

```bash
Дубликаты:

Файл: 197700.jpg
Размер: 839287
        1. d:\image\197700.jpg
        2. d:\image\image_1920x1080\197700.jpg

Файл: 198066.jpg
Размер: 1296998
        1. d:\image\198066.jpg
        2. d:\image\image_1920x1080\198066.jpg

Файл: 198200.jpg
Размер: 879772
        1. d:\image\198200.jpg
        2. d:\image\image_1920x1080\198200.jpg

Найдено 3 файла(ов).
На поиск ушло 0.01 секунды.
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
