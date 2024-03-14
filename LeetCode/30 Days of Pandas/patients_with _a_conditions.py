import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    result = patients[patients['conditions'].str.contains(r'\bDIAB1\S*', regex=True)]
    return result[['patient_id', 'patient_name', 'conditions']]

# Example usage:
patients_data = {
    'patient_id': [1, 2, 3, 4, 5],
    'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'],
    'conditions': ['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201']
}
patients_df = pd.DataFrame(patients_data)
result_df = find_patients(patients_df)
print(result_df)