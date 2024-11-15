import pandas as pd
import os

def join_player_files(year):
    # Define file paths

    # Define base path relative to the script location
    base_path = os.path.join(os.path.dirname(__file__), '../../data')

    footywire_file = os.path.join(base_path, f"AflPlayersFootywire{year}.xlsx")

    # Load the Excel files
    df_footywire = pd.read_excel(footywire_file)
# Check if 'Position' column exists and handle missing or NaN values
    if 'Position' in df_footywire.columns:
        # Replace NaN with empty string to handle missing Position data
        df_footywire['Position'] = df_footywire['Position'].fillna('')
        # Split Position into PrimaryPos and DualPos, using None for single-word values
        df_footywire[['PrimaryPos', 'DualPos']] = df_footywire['Position'].str.split(' ', n=1, expand=True)
    else:
        print(f"'Position' column not found in {footywire_file}")
        df_footywire['PrimaryPos'], df_footywire['DualPos'] = None, None

    
    print (df_footywire.head(5))
    # Merge the two files on 'Team' and 'No'

# Call the function with the desired year
print("begin")
join_player_files(2022)
