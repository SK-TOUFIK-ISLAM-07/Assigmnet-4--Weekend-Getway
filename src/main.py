import argparse
import sys
import logging
from tabulate import tabulate
import config
from data_loader import DataLoader
from data_processor import DataProcessor
from ranking_engine import RankingEngine

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description='Weekend Getaway Ranker - Find your perfect weekend destination'
    )
    parser.add_argument(
        '--city',
        type=str,
        help='Source city name'
    )
    parser.add_argument(
        '--max-distance',
        type=float,
        default=config.MAX_WEEKEND_DISTANCE_KM,
        help=f'Maximum distance in km (default: {config.MAX_WEEKEND_DISTANCE_KM})'
    )
    parser.add_argument(
        '--top-n',
        type=int,
        default=config.TOP_N_RECOMMENDATIONS,
        help=f'Number of recommendations (default: {config.TOP_N_RECOMMENDATIONS})'
    )
    
    args = parser.parse_args()
    
    try:
        logger.info("=" * 60)
        logger.info("Weekend Getaway Ranker - Starting")
        logger.info("=" * 60)
        
        data_loader = DataLoader()
        df = data_loader.load_data()
        
        if not data_loader.validate_data():
            logger.error("Data validation failed")
            sys.exit(1)
        
        processor = DataProcessor(df)
        processed_df = processor.clean_data()
        
        processor.save_processed_data()
        
        engine = RankingEngine(processed_df)
        
        source_city = args.city
        if not source_city:
            print("\nAvailable cities (sample):")
            available_cities = [city for city in config.CITY_COORDINATES.keys() 
                              if city in processed_df[config.COL_CITY].unique()][:30]
            
            for i, city in enumerate(available_cities[:20], 1):
                print(f"{i}. {city}")
            print("...")
            
            source_city = input("\nEnter source city name: ").strip()
        
        print(f"\n{'=' * 60}")
        print(f"Finding weekend getaways from {source_city}...")
        print(f"{'=' * 60}\n")
        
        recommendations = engine.get_recommendations(
            source_city=source_city,
            max_distance=args.max_distance,
            top_n=args.top_n
        )
        
        if recommendations.empty:
            print(f"No destinations found within {args.max_distance}km.")
            return

        print(f"Input City: {source_city.title()}")
        print()

        table_data = []
        for _, row in recommendations.iterrows():
            table_data.append([
                int(row['Rank']),
                row['City'],
                row['Place_Name'],
                f"{row['Distance_km']:.2f}",
                f"{row['Rating']:.2f}",
                f"{row['Popularity']:.2f}",
                f"{row['Score']:.2f}"
            ])
        
        headers = ['Rank', 'City', 'Place Name', 'Distance (km)', 'Rating', 'Popularity', 'Score']
        
        print(tabulate(table_data, headers=headers, tablefmt='grid'))
        
        output_file = config.OUTPUT_DIR / f"recommendations_{source_city.lower().replace(' ', '_')}.csv"
        recommendations.to_csv(output_file, index=False)
        print(f"\nResults saved to: {output_file}")
        
        logger.info("Application completed successfully")
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()