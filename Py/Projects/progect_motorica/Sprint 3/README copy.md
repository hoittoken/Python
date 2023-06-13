***
# Стажировка в моторике 2023

## **Sprint-3**. Финальная попытка.

Стажировка проводится компанией моторика в кооперации с [SkillFactory.](https://skillfactory.ru/)

## **Задача**: Получить рабочую модель для прогона на протезе

## Варианты решений:

* ### [**baseline**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%203/Read%20data%20and%20Inference.ipynb "От организаторов"): Базовый скрипт от организаторов.

* ### [**Super_light_version**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%203/_super%20short%20solution%20Mike_A_palm_readable.ipynb "Для практической пробы"): Облегчённая версия (без визуализации). Всего 9 блоков кода.

* ### [**Light_version**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%203/light_ver_sprint_3_Aubakirov.ipynb "Подготовка к Q&A сессии"): Полное решение. Визуализации, обоснования принятия решений.

## 0. Содержание:

1. [Обзор данных](#1-обзор-данных)
2. [Блок предпроцессинга](#2-блок-предпроцессинга)
3. [Блок модели](#3-блок-модели)
4. [Блок постпроцессинга](#4-блок-постпроцессинга)
5. [Зависимость метрик от данных для обучения](#5-зависимость-метрик-от-данных-для-обучения-моделей)
6. [Финальный сет. Гипотезы. Вопросы](#6-финальный-сет-гипотезы-вопросы)

***
## **1. Обзор данных**:

В спринте 3 данные представлены в `.palm` разрешении.

Стоит отдельно сказать, что данные между спринтами в рамках одного пилота объединять нельзя.
Только данные за 3 спринт можно объединять между монтажами.
Особенности данных 3 спринта:
- наличие наводки на сигнал, тк при записи данных ноутбук, на который писались данные, был включен в сеть;
- датчик на 8 каналов из-за чего 12 каналов первого порядка, вместо 16 (в спринтах 1 и 2).

| **Pilot_1_mount1** | **Pilot_1_mount2** |
| - | - |
| [**sprint3_pilote1_mount1_gestures.palm**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%203/sprint3_pilote1_mount1_gestures.palm.protocol.csv "Первый монтаж") | [**sprint3_pilote1_mount2_gestures.palm**](https://github.com/hoittoken/Python/blob/master/Py/Projects/progect_motorica/Sprint%203/sprint3_pilote1_mount2_gestures.palm.protocol.csv "Второй монтаж") |


*Fig_1. Разница в видк данных для разных монтажей*
<img src=Figure 0.png>

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

## 2. Блок предпроцессинга

[наверх](#0-содержание)

В качестве предпроцессинга реализовано добавление 1 признака (флажкового типа, где 0 - нет признака движения, 1 - есть признак движения) к вектору показаний датчиков.

Флаг 1/0 выдаётся `sklearn.linear_model.RidgeClassifier()` обученной на данных по изменения в показаний датчиков за 1 шаг.

```python
def get_diff(array, step=1, threshold=500):
    """_вычислятель изменений датчиков
        за step - шагов,
        с отсечением всего что ниже threshold - уровня
        theresold выбран в районе 90 квантиля_
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

## 3. Блок модели

[наверх](#0-содержание)

Рассматриваются 3 варианта моделей:

**Вариант_1:** Стек на `DecisionTreeRegressor()` и  `LassoLars()` на `VotingRegressor()`

```python
from sklearn.multioutput import MultiOutputRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LassoLars
from sklearn.ensemble import VotingRegressor

estimators = [
    ('dt', DecisionTreeRegressor()),
    ('ll', LassoLars())
]
model_vr_1 = MultiOutputRegressor(VotingRegressor(estimators=estimators))
model_vr_1.fit(np.insert(X_train, -1, ridge.predict(X_train), axis=1), y_train)
```


**Вариант_2:** Бустер `xgboost.XGBRegressor()` оптимизированный `optun`'ой

```python
import xgboost as xgb

# параметры оптимизированы optun'ой
params = {'learning_rate': 0.06329973864656831,
 'max_depth': 6,
 'subsample': 0.9814063371832862,
 'colsample_bytree': 0.41087811860602663,
 'min_child_weight': 8}

model_xgb_1 = xgb.XGBRegressor(**params)
model_xgb_1.fit(np.insert(X_train, -1, ridge.predict(X_train), axis=1), y_train)
```


**Вариант_3:** Бустер `lightgbm.LGBMRegressor()` оптимизированный `optun`'ой (+`MultiOutputRegressor()` для multi-target регрессии`)

```python
from sklearn.multioutput import MultiOutputRegressor
import lightgbm as lgb

# параметры оптимизированы optun'ой
params = {'learning_rate': 0.07118878873086158,
 'num_leaves': 78,
 'max_depth': 159,
 'min_data_in_leaf': 1423}

model_lgb_1 = MultiOutputRegressor(lgb.LGBMRegressor(**params))
model_lgb_1.fit(np.insert(X_train, -1, ridge.predict(X_train), axis=1), y_train)
```
## 4. Блок постпроцессинга

[наверх](#0-содержание)

В качестве постпроцессинга используется дискретизация полученных предсказаний на `100/step` - уровней (по умолчанию 20 уровней по 5 единиц в каждом)

```python
def postprocessing(array, step=5):
    """_дискретизация выходных сигналов по 100/step количеству уровней
        по умолчанию step=5 -> 20 уровней сигналов_
    """
    array[array < 0] = 0
    array = np.round(array / step, 0).astype(int) * step
    return array
```

и сглаживатель пиков организованный на очереди длинной = 3.

```python
dq = collections.deque(maxlen=3)

def commands(dq):
    """_сглаживатель пиков по 2-м предыдущим шагам_
    """
    if len(dq) < 2:
        return np.zeros(6)
    else:
        # если нет разницы межды настоящим и пред-предыдущим значением
        if (dq[-1] == dq[0]).any():
            # перепишем значение находящееся между ними
            dq[1][dq[-1] == dq[0]] = dq[0][dq[-1] == dq[0]] 
    return dq[-1]
```

## 5. Зависимость метрик от данных для обучения моделей

[наверх](#0-содержание)

Рассматривалось 3 варианта данных для обучения:

**Вариант_1:** учим модель на протокольных жестах

<img src=Fig_5.png>

| Finger | `mse` on test| `mse` on free_movements |
| - | - | - |
|ENC0 | 98.16 | 137.83 |
|ENC1 | 61.84 | 320.22 |
|ENC2 | 77.11 | 470.57 |
|ENC3 | 71.45 | 391.35 |
|ENC4 | 298.68 | 659.92 |

Сильно не попадаем во free_movements

**Вариант_2:** учим модель на свободных жестах

<img src=Fig_6.png>

| Finger | `mse` on test| `mse` on free_movements |
| - | - | - |
|ENC0 | 435.05 | 46.28 |
|ENC1 | 464.52 | 37.22 |
|ENC2 | 392.00 | 39.49 |
|ENC3 | 447.47 | 49.36 |
|ENC4 | 687.42 | 180.44 |

Сильно не попадаем в протокольные жесты

**Вариант_3:** учим модель на объединённых данных

<img src=Fig_7.png>

| Finger | `mse` on test| `mse` on free_movements |
| - | - | - |
|ENC0 | 112.61 | 82.66 |
|ENC1 | 129.75 | 57.68 |
|ENC2 | 135.72 | 82.03 |
|ENC3 | 127.19 | 88.21 |
|ENC4 | 359.71 | 298.05 |

Терпимо ошибаемся и в протокольных жестах и в free_movements

### **Вывод** - будем учить на всёх доступных данных

## 6. Финальный сет. Гипотезы. Вопросы

[наверх](#0-содержание)

### Финальный сет:

* Данные для моделирования - последовательно соединённые данные 2-х пилотов (train протокольных жестов и free_movements), дополнительно нарезанные `sklearn.model_selection.TimeSeriesSplit`
* Подготовлены к работе **3 модели** (`VotingRegressor`, `XGBRegressor`, `LGBMRegressor`)
* Предпроцессинг - **добавляем 1 фичу** (которая является флагом действия/бездействия)
* Постпроцессинг:
* * **дискретизация таргетов** на заданное количество диапазонов (по умолчанию 20 диапазон, по 5 единиц в каждом) 
* * **сглаживатель пиков** по предыдущим показаниям с шагом 3 и 4 (по умолчанию шаг 3) даёт задержку между предсказанием и выводом на протез в 1 временной шаг

*Fig_8. Финальные предсказания модели для `gestures_test`*

<img src=Fig_8.png>

*Fig_9. Укрупнённый фрагмент для ENC2, ENC3 `gestures_test`, диапазон [6700:7070]*

<img src=Fig_9.png>


**Вопросы к организатарам:**

1. Как подаётся NOGO (при отсутствии изменений сигналов датчиков выше заданного порога?)

2. Насколько гладкий сигнал должен быть на выходе (чтобы протез не испытывал “биение”?)

3. Как протез должен реагировать на пики (резкие изменения показаний датчиков?)

4. Как протез сейчас реагирует на `free_movements` (это же быстрые "мельтешения" пальцев)


[Презентация на docs.google.com](https://docs.google.com/presentation/d/1a2s7xupdbl6BUUNC2blYWt_eawKg4N_LzyKeon0On4M/edit?usp=sharing) 