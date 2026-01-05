import numpy as np
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DistanceCalculator:
    EARTH_RADIUS_KM = 6371.0
    @staticmethod
    def haversine_distance(
        lat1: float, lon1: float, 
        lat2: float, lon2: float
    ) -> float:

        lat1_rad = np.radians(lat1)
        lon1_rad = np.radians(lon1)
        lat2_rad = np.radians(lat2)
        lon2_rad = np.radians(lon2)

        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
        
        a = (np.sin(dlat / 2) ** 2 + 
             np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2) ** 2)
        c = 2 * np.arcsin(np.sqrt(a))
        
        distance = DistanceCalculator.EARTH_RADIUS_KM * c
        
        return distance
    @staticmethod
    def calculate_distances_from_source(
        df: pd.DataFrame,
        source_lat: float,
        source_lon: float,
        lat_col: str = 'Latitude',
        lon_col: str = 'Longitude'
    ) -> pd.Series:

        distances = df.apply(
            lambda row: DistanceCalculator.haversine_distance(
                source_lat, source_lon,
                row[lat_col], row[lon_col]
            ),
            axis=1
        )
        
        return distances