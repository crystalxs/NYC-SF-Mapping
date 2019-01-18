# preprocess all files individually
# append them to one file

import pandas as pd
import numpy as np
from datetime import datetime
import glob, os
from s2sphere import CellId, LatLng

def file_slicing(file_path):
    data = pd.read_csv(file_path, sep=" ", header=None)
    data.columns = ["lat", "long", "occupied", "unixtime"]
    data['cab_name'] = pd.Series(file_name, index=data.index)
    data_sort = data.sort_values(by=['cab_name', 'unixtime'])

    data_sort['dt_ts'] = data_sort.apply(
    lambda row: datetime.utcfromtimestamp(int(row['unixtime'])).strftime('%Y-%m-%d %H:%M:%S'),
        axis = 1
    )
    data_sort = data_sort.reset_index(drop=True)
    for i in range(1, len(data_sort)):
        data_sort.loc[i, 'diff_occupied'] = data_sort.loc[i, 'occupied'] - data_sort.loc[i-1, 'occupied']

    data_sort['is_pickup'] = np.where(data_sort['diff_occupied']==1, True, False)
    data_sort['is_dropoff'] = np.where(data_sort['diff_occupied']==-1, True, False)
    data_sliced = data_sort[(data_sort['is_pickup']) | (data_sort['is_dropoff'])]
    data_sliced = data_sliced.reset_index(drop=True)
    data_sliced = data_sliced.drop(['diff_occupied','occupied','cab_name'], axis=1)
    return data_sliced

def LatLng_to_cellid(data_sliced, cell_level):
    data_sliced['cell_id'] = data_sliced.apply(
    lambda row: CellId.from_lat_lng(LatLng.from_degrees(float(row['lat']), float(row['long'])))\
            .parent(cell_level).to_token(),
    axis=1
    )
    return data_sliced

def collapse_pick_drop(data_sliced):
    assert (len(data_sliced)%2 == 0)
    data_start_end = pd.DataFrame()
    i = 0
    while i <= len(data_sliced) - 2:
        data_start_end.loc[i, 'Trip_Pickup_Datetime'] = data_sliced.loc[i, 'dt_ts']
        data_start_end.loc[i, 'Trip_Dropoff_Datetime'] = data_sliced.loc[i+1, 'dt_ts']
        data_start_end.loc[i, 'Start_Lon'] = data_sliced.loc[i, 'long']
        data_start_end.loc[i, 'Start_Lat'] = data_sliced.loc[i, 'lat']
        data_start_end.loc[i, 'End_Lon'] = data_sliced.loc[i+1, 'long']
        data_start_end.loc[i, 'End_Lat'] = data_sliced.loc[i+1, 'lat']
        i += 2
    data_start_end = data_start_end.reset_index(drop=True)
    assert sum(np.where(data_start_end['Trip_Dropoff_Datetime'] > data_start_end['Trip_Pickup_Datetime'], 0, 1)) == 0
    return data_start_end
    
