import psycopg2

try:
    # Устанавливаем соединение с PostgreSQL
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres",
        password="student",
        database="student_task"
    )
    cursor = connection.cursor()

    # 1. Выполняем запрос на выборку цен в диапазоне от 1000 до 50000
    # Используем логику из Снимок экрана 2026-05-14 124227.png
    query = "SELECT * FROM prices WHERE price BETWEEN 1000 AND 50000;"
    cursor.execute(query)

    # 2. Извлекаем все подходящие записи
    prices_data = cursor.fetchall()

    print(f"Записи из таблицы prices (от 1000 до 50000):")
    for item in prices_data:
        # Предполагаем, что в таблице prices структура: id, product_id, price
        print(f"Товар ID: {item[1]} | Цена: {item[2]}")

    # Не забываем закрыть курсор
    cursor.close()

except Exception as error:
    print(f"Ошибка при подключении или выполнении запроса: {error}")

finally:
    # Обязательное закрытие соединения с базой данных
    if 'connection' in locals() and connection:
        connection.close()
        print("\nСоединение с базой данных закрыто.")