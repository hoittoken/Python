***
# Стажировка в моторике 2023

## Sprint-2. Новые данные. Пробный прогон на протезе.

Стажировка проводится компанией моторика в кооперации с [SkillFactory.](https://skillfactory.ru/)

## Задача: Получить рабочую модель для прогона на протезе

## Варианты решений:

* ## [**baseline**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%202/Read%20data%20and%20Inference.ipynb "От организаторов"): Базовый скрипт от организаторов.

* ## [**Super_light_version**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%202/_super%20short%20solution%20Mike_A.ipynb "Для практической пробы"): Облегчённая версия (без визуализации). Всего 9 блоков кода.

* ## [**Light_version**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%202/_Read%20data%20and%20Inference%20Mike_A.ipynb "Подготовка к Q&A сессии"): Полное решение. Визуализации, обоснования принятия решений.

***
## Обзор данных:

Для обучения и тестов имеем данный собранные с двух пилотов:

| **Pilot_1** | **Pilot_2** |
| - | - |
| [**gestures_train.csv**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%202/gestures_train.csv "Выполнены по протоколу (повторяющийся паттерн)") | [**gestures_train_2.csv**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%202/gestures_train_2.csv "Выполнены по протоколу (повторяющийся паттерн)") |
| [**gestures_test.csv**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%202/gestures_test.csv "Выполнены по протоколу (повторяющийся паттерн)") | [**gestures_test_2.csv**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%202/gestures_test_2.csv "Выполнены по протоколу (повторяющийся паттерн)") |
| [**free_movements.csv**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%202/free_movements.csv "Свободные жесты (без повторяющихся паттернов)") | [**free_movements.csv**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%202/free_movements_2.csv "Свободные жесты (без повторяющихся паттернов)") |

*Fig_1. Разницы в силе сжатия/разжатия палцев для обоих пилотов, на тренировочных данных*
<img src=Fig_1.png>

|**Активных датчиков:**| |
| - | - |
|первый пилот: |16|
|второй пилот: |16|


|**Пассивных датчиков:**| |
| - | - |
|первый пилот: |34|
|второй пилот: |34|

Номера этих датчиков совпадают: `True`

*Fig_2. Повторяющиеся паттерны жестов для обоих пилотов на тренировочных данных:*
<img src=Fig_2.png>

*Fig_3. **Желаемая** схема модели принятия решения*
<img src=Fig_3.png>

*Fig_4. **Построенная** схема модели принятия решения*
<img src=Fig_4.png>

## Блок препроцессинга

В качестве предпроцессинга реализовано добавление 1 предикта (флажкового типа где 0 - нет признака движения, 1 - есть признак движения) к вектору показаний датчиков.

Флаг 1/0 выдаётся `sklearn.linear_model.RidgeClassifier()` обученной на данных по изменения в показаний датчиков за 1 шаг.

```python
def get_diff(array, step=1, threshold=500):
    """_вычислятель изменений датчиков
        за step - шагов,
        с отсечением всего что ниже threshold - уровня_
    """
    new_array = np.zeros(array.shape[0])
    for i in np.arange(array.shape[0]):
        if i == 0:
            pass
        else:
            new_array[i] = np.sum(abs(array[i-step] - array[i]))
    new_array[new_array < threshold] = 0
    new_array[new_array > 0] = 1
    return new_array

X_all_diff = get_diff(X_all)  

from sklearn.linear_model import RidgeClassifier

ridge = RidgeClassifier().fit(X_all, X_all_diff)
X_all_class = ridge.predict(X_all)

X_new = np.insert(X_all, -1, X_all_class, axis=1)

```

## Блок модели

сс

## Блок постпроцессинга

сс