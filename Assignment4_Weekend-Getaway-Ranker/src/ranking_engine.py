import pandas as pd
import numpy as np
import logging
from typing import Optional
import config
from distance_calculator import DistanceCalculator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RankingEngine:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.distance_calc = DistanceCalculator()
    
    def get_recommendations(
        self,
        source_city: str,
        max_distance: float = config.MAX_WEEKEND_DISTANCE_KM,
        top_n: int = config.TOP_N_RECOMMENDATIONS
    ) -> pd.DataFrame:
        source_city_clean = source_city.strip().title()
        
        if source_city_clean not in config.CITY_COORDINATES:
            available_cities = [city for city in config.CITY_COORDINATES.keys() if city in self.df[config.COL_CITY].unique()][:30]
            raise ValueError(
                f"Source city '{source_city}' not found. "
                f"Available cities include: {', '.join(available_cities[:20])}..."
            )
        
        source_lat, source_lon = config.CITY_COORDINATES[source_city_clean]
        
        logger.info(f"Finding recommendations from {source_city_clean}")
        destinations = self.df[
            self.df[config.COL_CITY].str.lower() != source_city_clean.lower()
        ].copy()
        
        if destinations.empty:
            logger.warning(f"No destinations found for {source_city_clean}")
            return pd.DataFrame()

        destinations['Distance_km'] = self.distance_calc.calculate_distances_from_source(
            destinations,
            source_lat,
            source_lon,
            'Latitude',
            'Longitude'
        )

        destinations = destinations[destinations['Distance_km'] <= max_distance]
        
        if destinations.empty:
            logger.warning(
                f"No destinations found within {max_distance}km of {source_city_clean}"
            )
            return pd.DataFrame()

        city_recommendations = self._aggregate_by_city(destinations)

        city_recommendations = self._calculate_scores(city_recommendations)

        recommendations = city_recommendations.nsmallest(top_n, 'Rank')

        output = self._format_output(recommendations)
        
        logger.info(f"Found {len(recommendations)} recommendations")
        
        return output
    
    def _aggregate_by_city(self, df: pd.DataFrame) -> pd.DataFrame:
        idx = df.groupby(config.COL_CITY)[config.COL_RATING].idxmax()
        city_best_places = df.loc[idx].copy()
        min_distances = df.groupby(config.COL_CITY)['Distance_km'].min()
        city_best_places['Distance_km'] = city_best_places[config.COL_CITY].map(min_distances)

        max_popularity = df.groupby(config.COL_CITY)['Popularity_Score'].max()
        city_best_places['Popularity_Score'] = city_best_places[config.COL_CITY].map(max_popularity)

        required_cols = [config.COL_CITY, config.COL_NAME, config.COL_RATING, 
                        config.COL_STATE, 'Distance_km', 'Popularity_Score', 
                        'Latitude', 'Longitude']
        
        return city_best_places[required_cols].reset_index(drop=True)
    
    def _calculate_scores(self, df: pd.DataFrame) -> pd.DataFrame:

        max_dist = df['Distance_km'].max()
        min_dist = df['Distance_km'].min()
        
        if max_dist == min_dist:
            df['Distance_Score'] = 1.0
        else:
            df['Distance_Score'] = 1 - (
                (df['Distance_km'] - min_dist) / (max_dist - min_dist)
            )

        max_rating = df[config.COL_RATING].max()
        min_rating = df[config.COL_RATING].min()
        
        if max_rating == min_rating:
            df['Rating_Score'] = 1.0
        else:
            df['Rating_Score'] = (
                (df[config.COL_RATING] - min_rating) / (max_rating - min_rating)
            )

        max_pop = df['Popularity_Score'].max()
        min_pop = df['Popularity_Score'].min()
        
        if max_pop == min_pop:
            df['Popularity_Score_Norm'] = 1.0
        else:
            df['Popularity_Score_Norm'] = (
                (df['Popularity_Score'] - min_pop) / (max_pop - min_pop)
            )

        df['Final_Score'] = (
            df['Distance_Score'] * config.WEIGHT_DISTANCE +
            df['Rating_Score'] * config.WEIGHT_RATING +
            df['Popularity_Score_Norm'] * config.WEIGHT_POPULARITY
        )

        df['Rank'] = df['Final_Score'].rank(ascending=False, method='first').astype(int)
        
        return df
    
    def _format_output(self, df: pd.DataFrame) -> pd.DataFrame:

        
        output = pd.DataFrame({
            'Rank': df['Rank'],
            'City': df[config.COL_CITY],
            'Place_Name': df[config.COL_NAME],
            'Distance_km': df['Distance_km'].round(config.DECIMAL_PLACES),
            'Rating': df[config.COL_RATING].round(config.DECIMAL_PLACES),
            'Popularity': df['Popularity_Score'].round(config.DECIMAL_PLACES),
            'Score': df['Final_Score'].round(config.DECIMAL_PLACES)
        })
        
        return output.sort_values('Rank').reset_index(drop=True)