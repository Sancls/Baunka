import json
import os
file = "books.json"
def load_books():
    if not os.path.exists(file):
        return []
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
def save_books(books):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)
def add_book(books):
    print("\n--- Добавление книги ---")
    author = input("Введите автора: ").strip()
    title = input("Введите название книги: ").strip()
    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            print("Ошибка: Такая книга уже существует")
            return
    while True:
        try:
            rating = int(input("Введите оценку (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Оценка должна быть от 1 до 5.")
        except ValueError:
            print("Введите число.")

    date = input("Введите дату прочтения: ").strip()

    books.append({"author": author, "title": title, "rating": rating, "date": date})
    save_books(books)
    print("Книга успешно добавлена!")


def delete_book(books):
    if not books:
        print("Удалять нечего.")
        return
    print("\n--- Удаление книги ---")
    for idx, b in enumerate(books, 1):
        print(f"{idx}. {b['author']} - «{b['title']}»")

    try:
        num = int(input("Введите номер книги для удаления: ")) - 1
        if 0 <= num < len(books):
            removed = books.pop(num)
            save_books(books)
            print(f"Книга «{removed['title']}» удалена.")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Введите число.")
def main():
    books = load_books()
    while True:
        print("\n--- Меню ---")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "1":
            add_book(books)
        elif choice in ["2", "3", "4", "5"]:
            print("Этот функционал в разработке в другой ветке...")
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод, попробуйте снова.")
if __name__ == "__main__":
    main()