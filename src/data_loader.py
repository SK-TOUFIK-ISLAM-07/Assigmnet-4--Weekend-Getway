import pandas as pd
import logging
from pathlib import Path
from typing import Optional
import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataLoader: 
    def __init__(self, dataset_path: Optional[Path] = None):
        self.dataset_path = dataset_path or config.DATASET_PATH
        self.df = None
    
    def load_data(self) -> pd.DataFrame:
        try:
            logger.info(f"Loading dataset from {self.dataset_path}")
            
            if not self.dataset_path.exists():
                raise FileNotFoundError(
                    f"Dataset not found at {self.dataset_path}. "
                    f"Please download from Kaggle and place in {config.RAW_DATA_DIR}"
                )
            
            self.df = pd.read_csv(self.dataset_path, encoding='utf-8')
            logger.info(f"Successfully loaded {len(self.df)} records")
            logger.info(f"Available columns: {list(self.df.columns)}")
            
            return self.df
            
        except Exception as e:
            logger.error(f"Error loading dataset: {str(e)}")
            raise

    
    def validate_data(self) -> bool:
        if self.df is None:
            raise ValueError("No data loaded")
        
        missing_cols = set(config.REQUIRED_COLUMNS) - set(self.df.columns)
        
        if missing_cols:
            logger.error(f"Missing required columns: {missing_cols}")
            logger.info(f"Available columns: {list(self.df.columns)}")
            return False
        
        logger.info("Data validation passed")
        return True
    
    def get_data_info(self) -> dict:
        if self.df is None:
            return {}
        
        return {
            'total_records': len(self.df),
            'total_cities': self.df[config.COL_CITY].nunique() if config.COL_CITY in self.df.columns else 0,
            'total_places': len(self.df),
            'columns': list(self.df.columns),
            'missing_values': self.df.isnull().sum().to_dict()
        }