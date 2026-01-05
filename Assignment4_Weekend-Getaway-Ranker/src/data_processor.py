import pandas as pd
import numpy as np
import logging
import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataProcessor: 
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.processed_df = None
    
    def clean_data(self) -> pd.DataFrame:
        logger.info("Starting data cleaning process")
        
        df = self.df.copy()
        
        initial_count = len(df)
        

        if config.COL_CITY in df.columns:
            df[config.COL_CITY] = df[config.COL_CITY].str.strip().str.title()
        
        if config.COL_NAME in df.columns:
            df[config.COL_NAME] = df[config.COL_NAME].str.strip()
        
        df = self._handle_missing_values(df)
        
        df = self._normalize_ratings(df)
        
        df = self._create_popularity_score(df)
        
        df = self._add_coordinates(df)
        
        self.processed_df = df
        logger.info(f"Data cleaning complete. Records: {initial_count} → {len(df)}")
        
        return df
    
    def _handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        critical_cols = [config.COL_CITY, config.COL_NAME]
        df = df.dropna(subset=critical_cols)

        if config.COL_RATING in df.columns:
            median_rating = df[config.COL_RATING].median()
            df[config.COL_RATING].fillna(median_rating, inplace=True)

        if config.COL_ENTRANCE_FEE in df.columns:
            df[config.COL_ENTRANCE_FEE].fillna(0, inplace=True)
        
        if config.COL_TIME_NEEDED in df.columns:
            median_time = df[config.COL_TIME_NEEDED].median()
            df[config.COL_TIME_NEEDED].fillna(median_time, inplace=True)
        
        return df
    
    def _normalize_ratings(self, df: pd.DataFrame) -> pd.DataFrame:
      
        if config.COL_RATING in df.columns:
            df[config.COL_RATING] = pd.to_numeric(df[config.COL_RATING], errors='coerce')

            median_rating = df[config.COL_RATING].median()
            df[config.COL_RATING].fillna(median_rating, inplace=True)

            df[config.COL_RATING] = df[config.COL_RATING].clip(
                lower=config.MIN_RATING,
                upper=config.MAX_RATING
            )
        else:
            df[config.COL_RATING] = 3.5
            logger.warning("Rating column not found. Using default value of 3.5")
        
        return df
    
    def _create_popularity_score(self, df: pd.DataFrame) -> pd.DataFrame:
        df['Popularity_Score'] = 0

        if config.COL_RATING in df.columns:
            df['Popularity_Score'] += (df[config.COL_RATING] / 5.0) * 600

        if config.COL_TIME_NEEDED in df.columns:
            time_numeric = pd.to_numeric(df[config.COL_TIME_NEEDED], errors='coerce').fillna(2)
            max_time = time_numeric.max()
            if max_time > 0:
                df['Popularity_Score'] += (time_numeric / max_time) * 300
        
        if config.COL_ENTRANCE_FEE in df.columns:
            fee_numeric = pd.to_numeric(df[config.COL_ENTRANCE_FEE], errors='coerce').fillna(0)
            df['Popularity_Score'] += (fee_numeric > 0).astype(int) * 100
        
        logger.info("Created popularity scores based on rating, time needed, and entrance fee")
        
        return df
    
    def _add_coordinates(self, df: pd.DataFrame) -> pd.DataFrame:     
        def get_coordinates(city_name):
            city = str(city_name).strip().title()
            if city in config.CITY_COORDINATES:
                return config.CITY_COORDINATES[city]
            return (None, None)
        df[['Latitude', 'Longitude']] = df[config.COL_CITY].apply(
            lambda x: pd.Series(get_coordinates(x))
        )

        missing_coords = df[df['Latitude'].isnull()].shape[0]
        if missing_coords > 0:
            logger.warning(f"{missing_coords} places have cities without coordinates")
            df = df.dropna(subset=['Latitude', 'Longitude'])
        
        logger.info(f"Added coordinates for {len(df)} places")
        
        return df
    
    def save_processed_data(self, filename: str = 'processed_travel_data.csv'):
        
        if self.processed_df is None:
            raise ValueError("No processed data available.")
        
        output_path = config.PROCESSED_DATA_DIR / filename
        self.processed_df.to_csv(output_path, index=False)
        logger.info(f"Processed data saved to {output_path}")