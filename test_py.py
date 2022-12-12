import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)

try:
    data = pd.read_csv('real_estate_data.csv', sep='\t')
except FileNotFoundError:
    data = pd.read_csv(
        'https://code.s3.yandex.net/datasets/real_estate_data.csv', sep='\t')

data = data.rename(columns={'cityCenters_nearest': 'city_center_dist',
                            'parks_around3000': 'parks_around_3k',
                            'ponds_around3000': 'ponds_around_3k'})

ceiling_median = round(data['ceiling_height'].median(), 2)
data['ceiling_height'] = data['ceiling_height'].fillna(ceiling_median)
# print(f'Медианная высота потолков: {ceiling_median} м.')

'''
def floors_total_fill(row):
    # Процедура присвоения этажности здания пустым строкам
    # по данным из сводной таблицы floors_total_by_floor

    if pd.isna(row['floors_total']):
        return floors_total_by_floor.iloc[row['floor']].values[0]
    return row['floors_total']


data['floors_total'] = data.apply(floors_total_fill, axis=1)
'''

data.insert(loc=22,
            column='city_center_dist_km',
            value=data['city_center_dist'] / 1000
            )

print(data['city_center_dist_km'].head())

# Округлим расстояние до центра города
data['city_center_dist_km'] = (data['city_center_dist_km']
                               .astype('int64', errors='ignore')
                               )

print(data['city_center_dist_km'].head())
