import psycopg2
import pandas as pd
import warnings

# Скрываем предупреждения Pandas касательно SQLAlchemy connections
warnings.filterwarnings("ignore", category=UserWarning)

try:
    # 1. Подключение к контейнеру PostgreSQL
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres",
        password="student",
        database="student_task"
    )
    print("✓ Содержимое базы успешно запрошено")

    # Выгружаем таблицы целиком, чтобы проверить их структуру в Pandas
    df_prices = pd.read_sql("SELECT * FROM prices;", connection)
    df_products = pd.read_sql("SELECT * FROM products;", connection)

    # Автоматически определяем, как называются ключевые колонки
    # Ищем идентификатор продукта (обычно 'product_id' или 'id')
    prod_id_col_prices = 'product_id' if 'product_id' in df_prices.columns else 'id'
    prod_id_col_products = 'product_id' if 'product_id' in df_products.columns else 'id'

    # Ищем колонку с названием товара (обычно 'product_name' или 'name')
    name_col = 'product_name' if 'product_name' in df_products.columns else 'name'

    # Переименовываем для стандартизации, если имена колонок отличаются
    df_prices = df_prices.rename(columns={prod_id_col_prices: 'product_id'})
    df_products = df_products.rename(columns={prod_id_col_products: 'product_id', name_col: 'product_name'})

    # 2. Объединяем таблицы (аналог SQL JOIN) средствами Pandas
    df = pd.merge(df_prices, df_products, on='product_id')
    print("✓ Данные успешно объединены в DataFrame\n")

    # 3. Расчет базовых показателей для столбца price
    print("=== 3. Основные показатели стоимости ===")
    mean_price = df['price'].mean()
    median_price = df['price'].median()
    std_price = df['price'].std()
    min_price = df['price'].min()
    max_price = df['price'].max()

    print(f"Среднее значение:       {mean_price:.2f} руб.")
    print(f"Медиана:                {median_price:.2f} руб.")
    print(f"Стандартное отклонение: {std_price:.2f} руб.")
    print(f"Минимальная цена:       {min_price:.2f} руб.")
    print(f"Максимальная цена:      {max_price:.2f} руб.\n")

    # 4. Расчет квартилей, IQR и вывод товаров дороже Q3
    print("=== 4. Квартильный анализ и дорогие товары ===")
    q1 = df['price'].quantile(0.25)
    q2 = df['price'].quantile(0.50)
    q3 = df['price'].quantile(0.75)
    iqr = q3 - q1

    print(f"Первый квартиль (Q1):   {q1:.2f} руб.")
    print(f"Второй квартиль (Q2):   {q2:.2f} руб.")
    print(f"Третий квартиль (Q3):   {q3:.2f} руб.")
    print(f"Межквартильный размах:  {iqr:.2f} руб.\n")

    expensive_products = df[df['price'] > q3][['product_name', 'category', 'price']].drop_duplicates()
    print(f"Список товаров с ценой выше Q3 ({q3:.2f} руб.):")
    print(expensive_products.to_string(index=False))
    print("\n")

    # 5. Группировка по полю category
    print("=== 5. Анализ стоимости по категориям ===")
    by_category = df.groupby('category')['price'].agg(
        count='count',
        mean='mean',
        median='median',
        std='std'
    ).round(2).sort_values('mean', ascending=False)

    by_category.columns = ['Кол-во записей', 'Средняя цена (руб.)', 'Медиана (руб.)', 'Ст. отклонение']
    print(by_category)
    print("\n")

    # 6. Анализ разброса цен для каждого товара
    print("=== 6. Топ-5 товаров с наибольшим разбросом цен ===")
    by_product = df.groupby('product_name')['price'].agg(
        min_price='min',
        max_price='max'
    )
    by_product['price_range'] = by_product['max_price'] - by_product['min_price']

    top_5_range = by_product.sort_values('price_range', ascending=False).head(5)
    top_5_range = top_5_range.join(df[['product_name', 'category']].drop_duplicates().set_index('product_name'))

    top_5_range.columns = ['Мин. цена (руб.)', 'Макс. цена (руб.)', 'Разброс (руб.)', 'Категория']
    print(top_5_range[['Категория', 'Мин. цена (руб.)', 'Макс. цена (руб.)', 'Разброс (руб.)']])

except Exception as error:
    print(f"Ошибка при работе с базой данных или анализом: {error}")

finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("\n✓ Соединение с базой данных закрыто")