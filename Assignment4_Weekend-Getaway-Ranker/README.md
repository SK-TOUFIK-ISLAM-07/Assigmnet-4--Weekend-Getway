# Weekend Getaway Ranker

**Student Name:** Santanu Mondal  
**Student Code:** [BWU/BTD/22/067]  
---

## Project Overview

The **Weekend Getaway Ranker** is a recommendation engine for local travel destinations in India. It analyzes a comprehensive tourism dataset and ranks weekend getaway destinations based on multiple factors including distance from source city, Google review ratings, and popularity scores.

---

## Dataset Information

**Source**: India's Must-See Places Tourism Dataset  
**Location**: `data/raw/India_tourism.csv`
[LINK](https://www.kaggle.com/datasets/saketk511/travel-dataset-guide-to-indias-must-see-places)
### Dataset Columns Used:
- City, State, Zone
- Name (attraction name)
- Google review rating
- Establishment Year
- Time needed to visit (hours)
- Entrance Fee (INR)

---
---

## Technologies Used

- **Python 3.8+**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations and distance calculations
- **Tabulate**: Pretty-print results in table format
- **Logging**: Application monitoring and debugging

---

```
```
---

## Installation & Execution

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone <https://github.com/Santanu200407/Assignment3_Weekend-Getaway-Ranker>
cd Weekend-Getaway-Ranker
```
---
### Step 2: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Add Dataset

Download the dataset and place it in the `data/raw/` directory:
- File name: `India_tourism.csv`
- Path: `data/raw/India_tourism.csv`

**Note**: The `data/raw/` directory will be created automatically on first run.

### Step 5: Run the Application

#### Interactive Mode (Recommended)

```bash
cd src
python main.py
```

The application will:
1. Display a list of available cities
2. Prompt you to enter a source city name
3. Show top 5 weekend getaway recommendations
4. Save results to `outputs/recommendations_<cityname>.csv`

#### Command-Line Arguments Mode

```bash
cd src
python main.py --city "Kolkata" --max-distance 500 --top-n 5
```

**Arguments:**
- `--city`: Source city name (e.g., "Delhi", "Mumbai", "Kolkata")
- `--max-distance`: Maximum distance in kilometers (default: 500)
- `--top-n`: Number of recommendations to show (default: 5)

---

## Sample Outputs

The project includes sample outputs for three cities in `outputs/sample_recommendations/`:

### 1. Hyderabad

```
+--------+------------+----------------------------+-----------------+----------+--------------+---------+
|   Rank | City       | Place Name                 |   Distance (km) |   Rating |   Popularity |   Score |
+========+============+============================+=================+==========+==============+=========+
|      1 | Hampi      | Hampi Archaeological Ruins |          314.18 |      4.7 |       692.57 |    0.65 |
|      2 | Vijayawada | Kanaka Durga Temple        |          249.79 |      4.7 |       606.86 |    0.62 |
|      3 | Kurnool    | Belum Caves                |          179.62 |      4.4 |       692.29 |    0.61 |
|      4 | Aurangabad | Ajanta Caves               |          431.75 |      4.6 |       780.57 |    0.55 |
|      5 | Guntur     | Uppalapadu Bird Sanctuary  |          239.65 |      4.4 |       670.86 |    0.51 |
+--------+------------+----------------------------+-----------------+----------+--------------+---------+
```

### 2. Delhi

```
+--------+-------------+---------------------------+-----------------+----------+--------------+---------+
|   Rank | City        | Place Name                |   Distance (km) |   Rating |   Popularity |   Score |
+========+=============+===========================+=================+==========+==============+=========+
|      1 | Noida       | DLF Mall of India         |           19.8  |      4.6 |       680.29 |    0.77 |
|      2 | Meerut      | Augarnath Temple          |           63.62 |      4.8 |       618.86 |    0.74 |
|      3 | Agra        | Taj Mahal                 |          178.06 |      4.6 |       737.71 |    0.71 |
|      4 | Jaipur      | Amber Fort                |          235.29 |      4.6 |       737.71 |    0.66 |
|      5 | Jim Corbett | Jim Corbett National Park |          180.9  |      4.4 |       756.57 |    0.65 |
+--------+-------------+---------------------------+-----------------+----------+--------------+---------+
```

### 3. Kolkata

```
+--------+-------------+---------------------------------------+-----------------+----------+--------------+---------+
|   Rank | City        | Place Name                            |   Distance (km) |   Rating |   Popularity |   Score |
+========+=============+=======================================+=================+==========+==============+=========+
|      1 | Sundarbans  | Sundarbans National Park              |          109.12 |      4.4 |       799.43 |    0.65 |
|      2 | Bhubaneswar | Lingaraj Temple                       |          364.89 |      4.6 |       756.57 |    0.57 |
|      3 | Patna       | Takhat Shri Harimandir Ji Patna Sahib |          469.15 |      4.7 |       723.14 |    0.54 |
|      4 | Agartala    | Ujjayanta Palace                      |          329.88 |      4.5 |       704.29 |    0.43 |
|      5 | Ranchi      | Pahari Mandir                         |          324.27 |      4.6 |       594.86 |    0.42 |
+--------+-------------+---------------------------------------+-----------------+----------+--------------+---------+
```

---

## Configuration

All configuration parameters are centralized in `src/config.py`:

- **MAX_WEEKEND_DISTANCE_KM**: 500 (maximum distance for weekend trips)
- **WEIGHT_DISTANCE**: 0.40 (40% weight for distance)
- **WEIGHT_RATING**: 0.35 (35% weight for rating)
- **WEIGHT_POPULARITY**: 0.25 (25% weight for popularity)
- **TOP_N_RECOMMENDATIONS**: 5 (number of recommendations)

Modify these values to customize the recommendation behavior.

---



**Submission Date:** January 04, 2026
---

