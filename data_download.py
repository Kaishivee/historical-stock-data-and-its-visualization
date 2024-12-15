import pandas as pd
import yfinance as yf
import ta


def fetch_stock_data(ticker, period='1mo'):
    """
    Получает исторические данные об акциях для указанного тикера и временного периода. \
    Возвращает DataFrame с данными
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    """
    Добавляет в DataFrame колонку со скользящим средним, рассчитанным на основе цен закрытия.
    """
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """
    Вычисляет и выводит среднюю цену закрытия акций за заданный период.
    """
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия акций за период: {average_price:.2f}")


def notify_if_strong_fluctuations(data, threshold):
    """
    Анализирует данные и уведомляет пользователя, если цена акций колебалась более чем на заданный процент за период.
    """
    if 'Close' not in data or data['Close'].empty:
        print("Нет данных для анализа цен закрытия.")
        return False

    max_price = data['Close'].max()
    min_price = data['Close'].min()
    fluctuation = (max_price - min_price) / min_price * 100

    if fluctuation > threshold:
        print(f"Цена акций колебалась более чем на {threshold}% за период. Максимальная цена: {max_price:.2f}, Минимальная цена: {min_price:.2f}")
    else:
        print(f"Цена акций колебалась менее чем на {threshold}% за период. Максимальная цена: {max_price:.2f}, Минимальная цена: {min_price:.2f}")


def add_rsi(data, window=14):
    """
    Добавляет в DataFrame колонку с индикатором RSI.
    """
    data['RSI'] = ta.momentum.RSIIndicator(data['Close'], window=window).rsi()
    return data


def add_macd(data):
    """
    Добавляет в DataFrame колонки с индикатором MACD.
    """
    macd = ta.trend.MACD(data['Close'])
    data['MACD'] = macd.macd()
    data['MACD_Signal'] = macd.macd_signal()
    return data


def export_data_to_csv(data, filename='stock_data.csv'):
    """
    Экспортирует данные в CSV-файл.
    """
    data.to_csv(filename)