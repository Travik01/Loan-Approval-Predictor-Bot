# Loan Approval Predictor Bot

A Telegram bot that predicts whether a bank loan will be approved based on the applicant's profile. The model is trained on a Kaggle loan dataset using Linear Discriminant Analysis (LDA).

---

## Overview

The bot guides the user through a step-by-step questionnaire covering gender, marital status, dependents, self-employment status, applicant income, co-applicant income, loan amount, and loan term. After collecting all answers, it runs an LDA classifier and returns a prediction: approved or denied.

**Model accuracy:** ~78.4%

---

## Features

- Interactive Telegram questionnaire with keyboard buttons
- Real-time loan approval prediction
- Based on Linear Discriminant Analysis (LDA)
- Trained on Kaggle loan dataset
- Conversational flow with emoji support

---

## Dataset

Download the loan dataset from Kaggle and place it as `данные.csv` in the project root.

Recommended source: [Loan Prediction Dataset](https://www.kaggle.com/datasets/altruistsecond/loan-prediction) or similar loan dataset containing:

| Column | Description |
|--------|-------------|
| Gender | Male / Female |
| Married | Yes / No |
| Dependents | 0, 1, 2, 3+ |
| Self_Employed | Yes / No |
| ApplicantIncome | Primary applicant income |
| CoapplicantIncome | Co-applicant income |
| LoanAmount | Requested loan amount |
| Loan_Amount_Term | Repayment period (days) |
| Credit_History | Credit history record |
| Loan_Status | Target variable (Y / N) |

---

## Installation

```bash
pip install aiogram pandas numpy scikit-learn emoji
```

## Setup

1. **Download the dataset** from Kaggle and save it as `данные.csv` in the project folder.
2. **Get a Telegram bot token** from [@BotFather](https://t.me/BotFather).
3. **Replace the token** in the code:

```python
bot = Bot(token='YOUR_TOKEN', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
```

4. **Update the CSV path** to match your system:

```python
data = pd.read_csv(r"path/to/данные.csv")
```

## Run

```bash
python bot.py
```

Open your bot in Telegram and send `/start`.

---

## Bot Flow

```
/start → "начать" → gender (male/female) → married (yes/no)
        → dependents (0/1/2/3) → self-employed (✅/❌)
        → applicant income → co-applicant income → loan amount → loan term (days)
        → prediction: "вам одобрят кредит" / "вам не одобрят кредит"
```

---

## Model Details

| Parameter | Value |
|-----------|-------|
| Algorithm | Linear Discriminant Analysis |
| Test split | 20% |
| Accuracy | ~78.4% |
| Features | 8 (gender, married, dependents, self-employed, income, co-income, loan amount, loan term) |

### Data Preprocessing
- Categorical features encoded numerically (Male = 1, Female = 0, etc.)
- Loan amounts and incomes scaled by dividing by 92 (currency conversion heuristic)
- `Loan_ID`, `Education`, `Property_Area` columns dropped
- Missing or invalid values replaced with 0

---

## Project Structure

```
loan-approval-bot/
├── bot.py             # Main bot code (data loading, model, Telegram handlers)
├── данные.csv         # Kaggle loan dataset
└── README.md
```

## Requirements

Python ≥ 3.9, aiogram ≥ 3.0, pandas, numpy, scikit-learn, emoji

## License

MIT

---

# Loan Approval Predictor Bot

Telegram-бот для предсказания одобрения кредита на основе профиля заёмщика. Модель обучена на датасете Kaggle методом линейного дискриминантного анализа (LDA).

---

## Обзор

Бот проводит пользователя через пошаговый опрос: пол, семейное положение, количество иждивенцев, самозанятость, доход заёмщика, совместный доход, сумма займа и срок выплаты. После сбора ответов запускается классификатор LDA и возвращается прогноз — одобрен кредит или нет.

**Точность модели:** ~78.4%

---

## Возможности

- Интерактивный опрос через кнопки Telegram
- Предсказание одобрения кредита в реальном времени
- Модель — Linear Discriminant Analysis (LDA)
- Обучение на датасете Kaggle
- Поддержка эмодзи в интерфейсе

---

## Датасет

Скачайте датасет о кредитах с Kaggle и сохраните как `данные.csv` в корне проекта.

Рекомендуемый источник: [Loan Prediction Dataset](https://www.kaggle.com/datasets/altruistsecond/loan-prediction) или аналогичный датасет со следующими полями:

| Столбец | Описание |
|--------|----------|
| Gender | Пол (Male / Female) |
| Married | Семейное положение (Yes / No) |
| Dependents | Количество иждивенцев (0, 1, 2, 3+) |
| Self_Employed | Самозанятость (Yes / No) |
| ApplicantIncome | Доход основного заёмщика |
| CoapplicantIncome | Доход созаёмщика |
| LoanAmount | Сумма займа |
| Loan_Amount_Term | Срок выплаты (дни) |
| Credit_History | Кредитная история |
| Loan_Status | Целевая переменная (Y / N) |

---

## Установка

```bash
pip install aiogram pandas numpy scikit-learn emoji
```

## Настройка

1. **Скачайте датасет** с Kaggle и сохраните как `данные.csv` в папке проекта.
2. **Получите токен Telegram-бота** у [@BotFather](https://t.me/BotFather).
3. **Замените токен** в коде:

```python
bot = Bot(token='ВАШ_ТОКЕН', default=DefaultBotProperties(parse_mode=ParseMode.HTML))
```

4. **Обновите путь к CSV**:

```python
data = pd.read_csv(r"путь/к/данные.csv")
```

## Запуск

```bash
python bot.py
```

Откройте бота в Telegram и отправьте `/start`.

---

## Сценарий работы бота

```
/start → "начать" → пол (male/female) → семейное положение (yes/no)
        → иждивенцы (0/1/2/3) → самозанятость (✅/❌)
        → доход → совместный доход → сумма займа → срок (дни)
        → результат: "вам одобрят кредит" / "вам не одобрят кредит"
```

---

## Детали модели

| Параметр | Значение |
|-----------|----------|
| Алгоритм | Linear Discriminant Analysis |
| Размер тестовой выборки | 20% |
| Точность | ~78.4% |
| Признаки | 8 (пол, брак, иждивенцы, самозанятость, доход, совместный доход, сумма, срок) |

### Предобработка данных
- Категориальные признаки закодированы числами (Male = 1, Female = 0 и т. д.)
- Суммы займа и доходы делятся на 92 (эвристика конвертации валюты)
- Столбцы `Loan_ID`, `Education`, `Property_Area` удалены
- Пропущенные или некорректные значения заменены на 0

---

## Структура проекта

```
loan-approval-bot/
├── bot.py             # Основной код (загрузка данных, модель, обработчики Telegram)
├── данные.csv         # Датасет Kaggle
└── README.md
```

## Зависимости

Python ≥ 3.9, aiogram ≥ 3.0, pandas, numpy, scikit-learn, emoji

## Лицензия

MIT
