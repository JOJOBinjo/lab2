import re
import requests

# Регулярное выражение
DOMAIN_REGEX = re.compile(
    r"(?<![A-Za-z0-9-])(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}(?![A-Za-z0-9-])"
)


def find_domains(text: str):
    return DOMAIN_REGEX.findall(text)

def search_in_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as file:
        text = file.read()
    return find_domains(text)

def search_on_web(url: str):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return find_domains(response.text)

def main():
    print("=== Поиск синтаксически корректных доменных имен ===")
    print("1 — Проверка пользовательского ввода")
    print("2 — Поиск в файле")
    print("3 — Поиск на веб-странице")

    choice = input("Выберите режим работы: ")

    if choice == "1":
        text = input("Введите текст: ")
        domains = find_domains(text)
        if domains:
            print("Найденные домены:", domains)
        else:
            print("Домены е айдены")

    elif choice == "2":
        filepath = input("Введите путь к файлу: ")
        try:
            domains = search_in_file(filepath)
            if domains:
                print("Найденные домены:", domains)
            else:
                print("Домены е айдены")
        except FileNotFoundError:
            print("Ошибка: файл не найден")

    elif choice == "3":
        url = input("Введите URL: ")
        try:
            domains = search_on_web(url)
            if domains:
                print("Найденные домены:", domains)
            else:
                print("Домены е айдены")
        except Exception as e:
            print("Ошибка при загрузке страницы:", e)

    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()