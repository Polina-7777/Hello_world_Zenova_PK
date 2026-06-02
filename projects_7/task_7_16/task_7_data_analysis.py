import psycopg2
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Patch

# Отключаем предупреждения Pandas о переходе на SQLAlchemy
warnings.filterwarnings("ignore", category=UserWarning)

# -----------------------------------------------------------------------------
# БЛОК 1: ПОДКЛЮЧЕНИЕ И ИЗВЛЕЧЕНИЕ ДАННЫХ
# -----------------------------------------------------------------------------
try:
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres",
        password="student",
        database="student_task"
    )
    print("✓ Подключение установлено")

    # Выгружаем таблицы для объединения в Pandas
    df_prices = pd.read_sql("SELECT * FROM prices;", connection)
    df_products = pd.read_sql("SELECT * FROM products;", connection)

    # Автоматическое определение названий колонок при нестыковках в БД
    prod_id_col_prices = 'product_id' if 'product_id' in df_prices.columns else 'id'
    prod_id_col_products = 'product_id' if 'product_id' in df_products.columns else 'id'
    name_col = 'product_name' if 'product_name' in df_products.columns else 'name'

    # Приведение к единому стандарту имен
    df_prices = df_prices.rename(columns={prod_id_col_prices: 'product_id'})
    df_products = df_products.rename(columns={prod_id_col_products: 'product_id', name_col: 'product_name'})

    # Объединяем данные
    df = pd.merge(df_prices, df_products, on='product_id')
    print(f"✓ Данные загружены. Всего записей о ценах: {len(df)}")

except Exception as error:
    print(f"Ошибка подключения или запроса: {error}")
    raise SystemExit
finally:
    if 'connection' in locals() and connection:
        connection.close()
        print("✓ Соединение с БД закрыто\n")

# -----------------------------------------------------------------------------
# БЛОК 2: ПОДГОТОВКА ДАННЫХ ДЛЯ ГРАФИКОВ
# -----------------------------------------------------------------------------
# Агрегируем метрики по категориям для графиков 1 и 2
df_category = df.groupby('category')['price'].agg(
    avg_price='mean',
    total_records='count'
).reset_index().sort_values('avg_price', ascending=False)

# Данные для круговой диаграммы (распределение уникальных товаров по категориям)
df_unique_products = df.drop_duplicates(subset=['product_id'])
df_pie_data = df_unique_products['category'].value_counts().reset_index()
df_pie_data.columns = ['category', 'product_count']

# Цветовой порог для ценников (например, подсветим категории со средней ценой выше 15 000 руб.)
PRICE_THRESHOLD = 15000
bar_colors = ["#d9534f" if p > PRICE_THRESHOLD else "#4a90d9" for p in df_category["avg_price"]]

# Подписи для легенды круговой диаграммы
pie_labels = [f"{row.category} ({row.product_count} тов.)" for row in df_pie_data.itertuples()]

# -----------------------------------------------------------------------------
# БЛОК 3: ПОСТРОЕНИЕ ДАШБОРДА (GridSpec)
# -----------------------------------------------------------------------------
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
    "figure.dpi": 130,
})

fig = plt.figure(figsize=(16, 10))
fig.suptitle("Анализ прайс-листа и структуры товаров", fontsize=15, fontweight="bold", y=1.01)

# Сетка 2x3
gs = gridspec.GridSpec(2, 3, figure=fig,
                       height_ratios=[5, 4],
                       width_ratios=[2, 1, 2],
                       hspace=0.45, wspace=0.35)

ax1 = fig.add_subplot(gs[0, 0:2])  # Строка 0, колонки 0 и 1
ax2 = fig.add_subplot(gs[0, 2])  # Строка 0, колонка 2
ax3 = fig.add_subplot(gs[1, 0])  # Строка 1, колонка 0
ax4 = fig.add_subplot(gs[1, 1:3])  # Строка 1, колонки 1 и 2

# ── ГРАФИК 1: Средняя стоимость товаров по категориям ──
bars1 = ax1.barh(df_category["category"], df_category["avg_price"], color=bar_colors, edgecolor="white", height=0.6)

for bar in bars1:
    val = bar.get_width()
    ax1.text(val + (val * 0.01), bar.get_y() + bar.get_height() / 2, f"{val:.2f} ₽", va="center", fontsize=9)

# Линия общей средней цены по всей базе
overall_avg_price = df['price'].mean()
ax1.axvline(overall_avg_price, color="darkorange", linestyle="--", linewidth=1.3,
            label=f"Общая средняя: {overall_avg_price:.2f} ₽")

ax1.set_xlabel("Средняя цена в рублях")
ax1.set_title("Рейтинг категорий по средней стоимости", fontweight="bold", pad=8)
legend_patches = [
    Patch(facecolor="#d9534f", label=f"Премиум (≥ {PRICE_THRESHOLD} ₽)"),
    Patch(facecolor="#4a90d9", label="Масс-маркет"),
]
ax1.legend(handles=legend_patches, fontsize=8, loc="lower right")

# --- ДОБАВЛЕНИЕ BOXPLOT ---
# Допустим, у нас есть одна из осей (например, ax2)
# Сравниваем распределение цен по категориям
df.boxplot(column='price', by='category', ax=ax2, grid=False, vert=True, patch_artist=True)

# Настройка оформления
ax2.set_title("Распределение цен по категориям", fontweight="bold")
ax2.set_xlabel("Категория товара")
ax2.set_ylabel("Цена (₽)")
plt.suptitle("") # Убираем стандартный заголовок pandas, который может мешать

# ── ГРАФИК 3: Доля уникальных товаров в ассортименте ──
pie_colors = ["#7b68ee", "#4a90d9", "#2ecc71", "#f0ad4e", "#e74c3c"]
wedges, texts, autotexts = ax3.pie(
    df_pie_data["product_count"],
    labels=None,
    autopct="%1.0f%%",
    colors=pie_colors[:len(df_pie_data)],
    startangle=90,
    wedgeprops={"edgecolor": "white", "linewidth": 1.5},
    pctdistance=0.7
)

for autotext in autotexts:
    autotext.set_fontsize(10)
    autotext.set_fontweight("bold")

ax3.set_title("Структура ассортимента\n(доля уникальных товаров)", fontweight="bold", pad=8)
ax3.legend(wedges, pie_labels, loc="lower center", bbox_to_anchor=(0.5, -0.25), fontsize=8, frameon=False)

# ── ГРАФИК 4: Гистограмма распределения цен на продукцию ──
# Строим гистограмму распределения цен
n, bins, patches = ax4.hist(df['price'], bins=15, color="#f0ad4e", edgecolor="white", alpha=0.85)

# Добавляем вертикальную черту медианы
median_price = df['price'].median()
ax4.axvline(median_price, color="crimson", linestyle="--", linewidth=1.5, label=f"Медианная цена: {median_price:.2f} ₽")

ax4.set_xlabel("Стоимость товаров (₽)")
ax4.set_ylabel("Количество позиций")
ax4.set_title("Общее распределение стоимости товаров", fontweight="bold", pad=8)
ax4.legend(fontsize=8)

# Блок со сводными метриками в углу гистограммы
stats_text = (
    f"Всего ценников: {len(df)}\n"
    f"Средняя цена: {overall_avg_price:.2f} ₽\n"
    f"Станд. откл.: {df['price'].std():.2f} ₽"
)
ax4.text(0.97, 0.95, stats_text, transform=ax4.transAxes, va="top", ha="right", fontsize=8,
         bbox={"boxstyle": "round,pad=0.4", "facecolor": "lightyellow", "edgecolor": "lightgray", "alpha": 0.8})

# -----------------------------------------------------------------------------
# БЛОК 4: СОХРАНЕНИЕ РЕЗУЛЬТАТА
# -----------------------------------------------------------------------------
OUTPUT_FILE = "product_analytics_dashboard.png"
plt.savefig(OUTPUT_FILE, bbox_inches="tight", dpi=150)
print(f"✓ Аналитический дашборд успешно сохранён в файл: {OUTPUT_FILE}")
plt.show()