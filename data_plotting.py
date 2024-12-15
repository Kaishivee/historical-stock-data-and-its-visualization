import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, filename=None):
    """
    Создаёт график, отображающий цены закрытия, скользящие средние, RSI и MACD.
    Предоставляет возможность сохранения графика в файл.
    Параметр filename опционален; если он не указан, имя файла генерируется автоматически.
    """
    plt.figure(figsize=(10, 12))

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.subplot(3, 1, 1)
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.title(f"{ticker} Цена акций с течением времени")
            plt.xlabel("Дата")
            plt.ylabel("Цена")
            plt.legend()

            plt.subplot(3, 1, 2)
            plt.plot(dates, data['RSI'].values, label='RSI', color='orange')
            plt.axhline(70, linestyle='--', color='r', linewidth=0.5)
            plt.axhline(30, linestyle='--', color='g', linewidth=0.5)
            plt.title("RSI")
            plt.legend()

            plt.subplot(3, 1, 3)
            plt.plot(dates, data['MACD'].values, label='MACD', color='blue')
            plt.plot(dates, data['MACD_Signal'].values, label='MACD Signal', color='red')
            plt.title("MACD")
            plt.legend()
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.subplot(3, 1, 1)
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.title(f"{ticker} Цена акций с течением времени")
        plt.xlabel("Дата")
        plt.ylabel("Цена")
        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(data['Date'], data['RSI'], label='RSI', color='orange')
        plt.axhline(70, linestyle='--', color='r', linewidth=0.5)
        plt.axhline(30, linestyle='--', color='g', linewidth=0.5)
        plt.title("RSI")
        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(data['Date'], data['MACD'], label='MACD', color='blue')
        plt.plot(data['Date'], data['MACD_Signal'], label='MACD Signal', color='red')
        plt.title("MACD")
        plt.legend()

    if filename is None:
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.tight_layout()
    plt.savefig(filename)
    print(f"График сохранен как {filename}")