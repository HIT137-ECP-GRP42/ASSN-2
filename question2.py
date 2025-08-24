'''
author: Alice Li

'''

import os
import pandas as pd

def process_file():
    try:
        temperature_folder = 'temperatures'
        dfs = []
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        for filename in os.listdir(temperature_folder):
            
            file_path = os.path.join(temperature_folder, filename)
            df = pd.read_csv(file_path)
            df_all = df.melt(
                id_vars=['STATION_NAME', 'STN_ID', 'LAT', 'LON'],
                value_vars=months,
                var_name='month_name',
                value_name='temperature'
            )
            df_all = df_all.dropna(subset=['temperature'])
            dfs.append(df_all)

        if dfs:
            temperatures_data = pd.concat(dfs, ignore_index=True)
            months_mapping = {m: i+1 for i, m in enumerate(months)}
            temperatures_data['month'] = temperatures_data['month_name'].map(months_mapping)
            temperatures_data.rename(columns={'STATION_NAME': 'station'}, inplace=True)
            return temperatures_data
        else:
            print("No  CSV files")
            return None
    except Exception as e:
        print(f"Error in processingfile: {e}")
        return None

def seasonal_average(temperatures_data):
    try:
        def get_season(month):
            if month in [12, 1, 2]:
                return 'Summer'
            elif month in [3, 4, 5]:
                return 'Autumn'
            elif month in [6, 7, 8]:
                return 'Winter'
            else:
                return 'Spring'

        temperatures_data['season'] = temperatures_data['month'].apply(get_season)
        seasons_averages = temperatures_data.groupby('season')['temperature'].mean().reindex(['Summer', 'Autumn', 'Winter', 'Spring'])

        with open('average_temp.txt', 'w') as f:
            for season, avg_temp in seasons_averages.items():
                f.write(f"{season}: {avg_temp:.1f}°C\n")
    except Exception as e:
        print(f"Error in executing seasonal_average: {e}")
        
def temperature_range(temperatures_data):
    try:
        temperatures_range = temperatures_data.groupby('station')['temperature'].agg(['max', 'min'])
        temperatures_range['range'] = temperatures_range['max'] - temperatures_range['min']
        max_range = temperatures_range['range'].max()
        stations_with_max_range = temperatures_range[temperatures_range['range'] == max_range]

        with open('largest_temperatures_range_station.txt', 'w') as f:
            for station, row in stations_with_max_range.iterrows():
                f.write(f"Station {station}: Range {row['range']:.1f}°C (Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n")
    except Exception as e:
        print(f"Error in executing temperature_range: {e}")

def temperature_stability(temperatures_data):
    try:
        temperatures_stability = temperatures_data.groupby('station')['temperature'].std()
        min_std = temperatures_stability.min()
        max_std = temperatures_stability.max()
        most_stable_stations = temperatures_stability[temperatures_stability == min_std]
        most_variable_stations = temperatures_stability[temperatures_stability == max_std]

        with open('temperature_stability_stations.txt', 'w') as f:
            for station, std in most_stable_stations.items():
                f.write(f"Most Stable: Station {station}: StdDev {std:.1f}°C\n")
            for station, std in most_variable_stations.items():
                f.write(f"Most Variable: Station {station}: StdDev {std:.1f}°C\n")
    except Exception as e:
        print(f"Error in executing temperature_stability: {e}")

def main():
   try:
    temperatures_data = process_file()
    if temperatures_data is not None:
        seasonal_average(temperatures_data)
        temperature_range(temperatures_data)
        temperature_stability(temperatures_data)
   except Exception as e:
        print(f"Error in main: {e}")
    



if __name__ == "__main__":
    main()
