
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'
OUTPUT_DIR = PROJECT_ROOT / 'outputs'
SAMPLE_OUTPUT_DIR = OUTPUT_DIR / 'sample_recommendations'

for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, OUTPUT_DIR, SAMPLE_OUTPUT_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

DATASET_FILENAME = 'India_tourism.csv'
DATASET_PATH = RAW_DATA_DIR / DATASET_FILENAME

COL_SERIAL = 'Serial Number'
COL_ZONE = 'Zone'
COL_STATE = 'State'
COL_CITY = 'City'
COL_NAME = 'Name'  
COL_ESTABLISHMENT_YEAR = 'Establishment Year'
COL_TIME_NEEDED = 'time needed to visit in hrs'
COL_RATING = 'Google review rating'
COL_ENTRANCE_FEE = 'Entrance Fee in INR'


MAX_WEEKEND_DISTANCE_KM = 500  
WEIGHT_DISTANCE = 0.40
WEIGHT_RATING = 0.35
WEIGHT_POPULARITY = 0.25


MIN_RATING = 0.0
MAX_RATING = 5.0
TOP_N_RECOMMENDATIONS = 5


DECIMAL_PLACES = 2


REQUIRED_COLUMNS = [COL_CITY, COL_NAME, COL_RATING, COL_STATE]

CITY_COORDINATES = {
    'Mumbai': (19.0760, 72.8777),
    'Delhi': (28.6139, 77.2090),
    'Bangalore': (12.9716, 77.5946),
    'Chennai': (13.0827, 80.2707),
    'Kolkata': (22.5726, 88.3639),
    'Hyderabad': (17.3850, 78.4867),
    'Pune': (18.5204, 73.8567),
    'Ahmedabad': (23.0225, 72.5714),
    'Jaipur': (26.9124, 75.7873),
    'Surat': (21.1702, 72.8311),
    'Lucknow': (26.8467, 80.9462),
    'Kanpur': (26.4499, 80.3319),
    'Nagpur': (21.1458, 79.0882),
    'Indore': (22.7196, 75.8577),
    'Thane': (19.2183, 72.9781),
    'Bhopal': (23.2599, 77.4126),
    'Visakhapatnam': (17.6868, 83.2185),
    'Pimpri-Chinchwad': (18.6298, 73.7997),
    'Patna': (25.5941, 85.1376),
    'Vadodara': (22.3072, 73.1812),
    'Ghaziabad': (28.6692, 77.4538),
    'Ludhiana': (30.9010, 75.8573),
    'Agra': (27.1767, 78.0081),
    'Nashik': (19.9975, 73.7898),
    'Faridabad': (28.4089, 77.3178),
    'Meerut': (28.9845, 77.7064),
    'Rajkot': (22.3039, 70.8022),
    'Kalyan-Dombivali': (19.2403, 73.1305),
    'Vasai-Virar': (19.4612, 72.7964),
    'Varanasi': (25.3176, 82.9739),
    'Srinagar': (34.0837, 74.7973),
    'Aurangabad': (19.8762, 75.3433),
    'Dhanbad': (23.7957, 86.4304),
    'Amritsar': (31.6340, 74.8723),
    'Navi Mumbai': (19.0330, 73.0297),
    'Allahabad': (25.4358, 81.8463),
    'Ranchi': (23.3441, 85.3096),
    'Howrah': (22.5958, 88.2636),
    'Coimbatore': (11.0168, 76.9558),
    'Jabalpur': (23.1815, 79.9864),
    'Gwalior': (26.2183, 78.1828),
    'Vijayawada': (16.5062, 80.6480),
    'Jodhpur': (26.2389, 73.0243),
    'Madurai': (9.9252, 78.1198),
    'Raipur': (21.2514, 81.6296),
    'Kota': (25.2138, 75.8648),
    'Chandigarh': (30.7333, 76.7794),
    'Guwahati': (26.1445, 91.7362),
    'Solapur': (17.6599, 75.9064),
    'Hubli-Dharwad': (15.3647, 75.1240),
    'Mysore': (12.2958, 76.6394),
    'Tiruchirappalli': (10.7905, 78.7047),
    'Bareilly': (28.3670, 79.4304),
    'Aligarh': (27.8974, 78.0880),
    'Tiruppur': (11.1085, 77.3411),
    'Moradabad': (28.8389, 78.7378),
    'Jalandhar': (31.3260, 75.5762),
    'Bhubaneswar': (20.2961, 85.8245),
    'Salem': (11.6643, 78.1460),
    'Warangal': (17.9689, 79.5941),
    'Mira-Bhayandar': (19.2952, 72.8544),
    'Thiruvananthapuram': (8.5241, 76.9366),
    'Bhiwandi': (19.3009, 73.0643),
    'Saharanpur': (29.9680, 77.5460),
    'Guntur': (16.3067, 80.4365),
    'Amravati': (20.9374, 77.7796),
    'Bikaner': (28.0229, 73.3119),
    'Noida': (28.5355, 77.3910),
    'Jamshedpur': (22.8046, 86.2029),
    'Bhilai': (21.2167, 81.4333),
    'Cuttack': (20.4625, 85.8828),
    'Firozabad': (27.1591, 78.3957),
    'Kochi': (9.9312, 76.2673),
    'Bhavnagar': (21.7645, 72.1519),
    'Dehradun': (30.3165, 78.0322),
    'Durgapur': (23.5204, 87.3119),
    'Asansol': (23.6739, 86.9524),
    'Nanded': (19.1383, 77.3210),
    'Kolhapur': (16.7050, 74.2433),
    'Ajmer': (26.4499, 74.6399),
    'Akola': (20.7002, 77.0082),
    'Gulbarga': (17.3297, 76.8343),
    'Jamnagar': (22.4707, 70.0577),
    'Ujjain': (23.1765, 75.7885),
    'Loni': (28.7523, 77.2860),
    'Siliguri': (26.7271, 88.3953),
    'Jhansi': (25.4484, 78.5685),
    'Ulhasnagar': (19.2183, 73.1382),
    'Jammu': (32.7266, 74.8570),
    'Sangli-Miraj & Kupwad': (16.8524, 74.5815),
    'Mangalore': (12.9141, 74.8560),
    'Erode': (11.3410, 77.7172),
    'Belgaum': (15.8497, 74.4977),
    'Ambattur': (13.1143, 80.1548),
    'Tirunelveli': (8.7139, 77.7567),
    'Malegaon': (20.5579, 74.5287),
    'Gaya': (24.7955, 85.0002),
    'Jalgaon': (21.0077, 75.5626),
    'Udaipur': (24.5854, 73.7125),
    'Maheshtala': (22.5093, 88.2477),
    'Tirupati': (13.6288, 79.4192),
    'Davanagere': (14.4644, 75.9217),
    'Kozhikode': (11.2588, 75.7804),
    'Akbarpur': (26.4297, 82.5347),
    'Kurnool': (15.8281, 78.0373),
    'Bokaro': (23.6693, 86.1511),
    'Rajahmundry': (17.0005, 81.8040),
    'Ballari': (15.1394, 76.9214),
    'Agartala': (23.8315, 91.2868),
    'Bhagalpur': (25.2425, 86.9842),
    'Latur': (18.3983, 76.5604),
    'Dhule': (20.9042, 74.7749),
    'Korba': (22.3595, 82.7501),
    'Bhilwara': (25.3407, 74.6269),
    'Brahmapur': (19.3150, 84.7941),
    'Agra': (27.1767, 78.0081),
    'Goa': (15.2993, 74.1240),
    'Shimla': (31.1048, 77.1734),
    'Manali': (32.2396, 77.1887),
    'Ooty': (11.4102, 76.6950),
    'Darjeeling': (27.0360, 88.2627),
    'Rishikesh': (30.0869, 78.2676),
    'Haridwar': (29.9457, 78.1642),
    'Mussoorie': (30.4598, 78.0644),
    'Nainital': (29.3803, 79.4636),
    'Mount Abu': (24.5926, 72.7156),
    'Kodaikanal': (10.2381, 77.4892),
    'Coorg': (12.3375, 75.8069),
    'Munnar': (10.0889, 77.0595),
    'Pondicherry': (11.9416, 79.8083),
    'Gangtok': (27.3389, 88.6065),
    'Leh': (34.1526, 77.5771),
    'Ladakh': (34.1526, 77.5771),
    'Khajuraho': (24.8318, 79.9199),
    'Hampi': (15.3350, 76.4600),
    'Mahabaleshwar': (17.9244, 73.6479),
    'Lonavala': (18.7537, 73.4057),
    'Khandala': (18.7500, 73.3833),
    'Alibaug': (18.6414, 72.8722),
    'Matheran': (18.9833, 73.2667),
    'Panchgani': (17.9244, 73.8031),
    'Igatpuri': (19.6958, 73.5631),
    'Jim Corbett': (29.5308, 78.7466),
    'Ranthambore': (26.0173, 76.5026),
    'Kaziranga': (26.5775, 93.1711),
    'Sundarbans': (21.9497, 89.1833),
    'Andaman': (11.7401, 92.6586),
    'Lakshadweep': (10.5667, 72.6417),
    'Daman': (20.4140, 72.8328),
    'Diu': (20.7144, 70.9872),
    'Puducherry': (11.9416, 79.8083),
    'Port Blair': (11.6234, 92.7265),
}
