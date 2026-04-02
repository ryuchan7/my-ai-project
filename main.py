import os
import warnings
import pandas as pd
from sklearn.feature_selection import mutual_info_classif

# --- FIX: Prevent the 'joblib'/'wmic' error ---
os.environ["LOKY_MAX_CPU_COUNT"] = "4" 
warnings.filterwarnings("ignore")

# 1. Create the Dataset
data = {
    'Student_ID': range(1, 11),
    'Hours_Studied': [2, 8, 12, 15, 18, 25, 30, 35, 40, 48],
    'Passed_Exam': ['No', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'aYes', 'Yes']
}
df = pd.DataFrame(data)

# 2. Prepare Data for Scikit-Learn
# mutual_info_classif requires:
# - X (Feature) to be 2D (DataFrame or list of lists)
# - y (Target) to be encoded as numbers (0 and 1)
X = df[['Hours_Studied']]
y = df['Passed_Exam'].apply(lambda x: 1 if x == 'Yes' else 0)

# 3. Calculate Information Gain (Mutual Information)
# discrete_features=False tells the function to treat 'Hours_Studied' as continuous
mi_score = mutual_info_classif(X, y, discrete_features=False, random_state=42)

# 4. Print Results
print("-" * 30)
print("INFORMATION GAIN RESULTS")
print("-" * 30)
print(f"Manual Calculation (Split > 16): 0.257")
print(f"Python (mutual_info_classif):    {mi_score[0]:.4f}")
print("-" * 30)