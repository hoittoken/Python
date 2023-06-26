## Проект №6 Сегментирование клиентов онлайн-магазина подарков 
в рамках обучения профессии Data Science от Skill Factory

## Предсказание продолжительность поездки на такси:

* [Короткое решение](https://github.com/hoittoken/Python/blob/master/Py/Projects/project_6/Project-6.ipynb)

* [Развернутое решение](https://github.com/hoittoken/Python/blob/master/Py/Projects/project_6/Project-6._Aubakirov.ipynb)

## Бизнес-задача

произвести сегментацию существующих клиентов, проинтерпретировать эти сегменты и определить стратегию взаимодействия с ними.

## Техническая задача

**Построить модель кластеризации** клиентов на основе их покупательской способности, частоты заказов и срока давности последней покупки, определить профиль каждого из кластеров.

## Основные цели

1. Произвести предобработку набора данных.

2. Провести разведывательный анализ данных и выявить основные закономерности.

3. Сформировать категории товаров и клиентов.

4. Построить несколько моделей машинного обучения, решающих задачу кластеризации клиентов, определить количество кластеров и проинтерпретировать их.

5. Спроектировать процесс предсказания категории интересов клиента и протестировать вашу модель на новых клиентах.


## Используемые файлы
[Датасет](https://drive.google.com/file/d/1Axlknf1Rd6T6UFRzWWZA_gBbfN2g9r3v/view?usp=sharing)

После проведения `DataCleaning`, и `EDA` определим оптимальное количество кластеров:

```Python
# k-mean - коэффициент силуэта
def get_silhouette(clust_num, data):
    """_функция вычисляющая коэффициент силуэта_
    """
    k_means = cluster.KMeans(n_clusters=clust_num, random_state=42)
    k_means.fit(data)
    silhouette = metrics.silhouette_score(data, k_means.predict(data))
    return silhouette

# словарь для записи результатов вычислений
results = {'silhouette':[], 'clusters':[]}

# вычислим коэф.силуэта для разного количества кластеров
for clust_num in range(3, 9):
    results['silhouette'].append(get_silhouette(clust_num, rfm_table_processed))
    results['clusters'].append(clust_num)
    
plot_df = pd.DataFrame(results)

sns.set_style("darkgrid")
sns.lineplot(x=plot_df['clusters'], y=plot_df['silhouette'], marker='o');
```
<img src=https://github.com/hoittoken/Python/blob/9c95aa3d8c74de49a890d1875161f0840b28aa3f/Py/Projects/project_6/clusters_1.png>

Вышли на 7 кластеров:

<img src=https://github.com/hoittoken/Python/blob/9c95aa3d8c74de49a890d1875161f0840b28aa3f/Py/Projects/project_6/rfm-1.png>

В рассматриваемых данных:

<img src=https://github.com/hoittoken/Python/blob/9c95aa3d8c74de49a890d1875161f0840b28aa3f/Py/Projects/project_6/clusters_2.png>