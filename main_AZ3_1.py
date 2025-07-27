import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import re

def parse_divan_prices():
    # Настройка Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Инициализация драйвера
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Переход на страницу диванов
        url = "https://www.divan.ru/category/divany"
        driver.get(url)
        
        # Ждем загрузки страницы
        time.sleep(3)
        
        # Список для хранения цен
        prices = []
        
        # Поиск всех элементов с ценами
        price_elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid='price']")
        
        print(f"Найдено цен: {len(price_elements)}")
        
        for price_element in price_elements:
            try:
                price_text = price_element.text.strip()
                # Извлекаем только цифры из цены
                price = re.sub(r'[^\d]', '', price_text)
                if price:  # Добавляем только если цена не пустая
                    prices.append(price)
                    
            except Exception as e:
                print(f"Ошибка при парсинге цены: {e}")
                continue
        
        # Создание DataFrame
        data = {
            'Цена (руб)': prices
        }
        
        df = pd.DataFrame(data)
        
        # Сохранение в CSV
        filename = 'divan_prices.csv'
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        
        print(f"Данные сохранены в файл: {filename}")
        print(f"Всего спарсено товаров: {len(df)}")
        print("\nПервые 5 товаров:")
        print(df.head())
        
        return df
        
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return None
        
    finally:
        driver.quit()

if __name__ == "__main__":
    print("Начинаем парсинг цен на диваны с divan.ru...")
    result = parse_divan_prices()
    
    if result is not None:
        print("\nПарсинг завершен успешно!")
    else:
        print("\nОшибка при парсинге!")
