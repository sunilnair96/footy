import pandas as pd
import os

def join_player_files(year):
    # Define base path relative to the script location
    base_path = os.path.join(os.path.dirname(__file__), '../../data')
    draftguru_file = os.path.join(base_path, f"AflPlayersDraftGuru{year}.xlsx")
    footywire_file = os.path.join(base_path, f"AflPlayersFootywire{year}.xlsx")
    output_file = os.path.join(base_path, f"AflPlayers{year}.xlsx")
    exception_file = os.path.join(base_path, f"ExceptionPlayers{year}.xlsx")

    # Load the Excel files
    df_draftguru = pd.read_excel(draftguru_file)
    df_footywire = pd.read_excel(footywire_file)
    
    # Convert DOB and Date of Birth columns to datetime format for consistent comparison
    df_draftguru['DOB'] = pd.to_datetime(df_draftguru['DOB'], errors='coerce', dayfirst=True)
    df_footywire['Date of Birth'] = pd.to_datetime(df_footywire['Date of Birth'], format='%d %b %Y', errors='coerce')
    
    # Select required columns and split Position in footywire file
    df_footywire[['PrimaryPos', 'DualPos']] = df_footywire['Position'].str.split(' ', n=1, expand=True)
    df_footywire = df_footywire[['Team', 'No', 'Name', 'Date of Birth', 'PrimaryPos', 'DualPos']]
    
    # Merge dataframes on 'Team' and 'Date of Birth' (footywire) / 'DOB' (draftguru) columns
    merged_df = df_footywire.merge(
        df_draftguru[['Team', 'DOB', 'No']],
        left_on=['Team', 'Date of Birth'],
        right_on=['Team', 'DOB'],
        how='left',
        suffixes=('', '_draftguru')
    )
    
    print (df_footywire.head(50))
    print (df_draftguru.head(50))
    # Update 'No' in df_footywire only if there is a match in draftguru
    df_footywire['No'] = merged_df['No_draftguru'].combine_first(df_footywire['No'])
    print (df_footywire.head(50))

    # Merge the two files on 'Team' and 'No'
    df_merged = pd.merge(df_draftguru, df_footywire, on=['Team', 'No'], how='outer', indicator=True)
    
    # Separate exceptions for players only in one of the files
    draftguru_only = df_merged[df_merged['_merge'] == 'left_only']
    footywire_only = df_merged[df_merged['_merge'] == 'right_only']
    
    # Add error messages for exceptions
    draftguru_only['error_message'] = 'Player exists in AflPlayersDraftGuru but not in AflPlayersFootywire'
    footywire_only['error_message'] = 'Player exists in AflPlayersFootywire but not in AflPlayersDraftGuru'
    print (draftguru_only.columns)
    print(footywire_only.columns)  

    # Prepare the exceptions file
    exceptions = pd.concat([draftguru_only[['Team', 'No', 'Player', 'error_message']],
                            footywire_only[['Team', 'No', 'Name', 'error_message']]], ignore_index=True)
    
    # Filter only matched records
    df_result = df_merged[df_merged['_merge'] == 'both'].drop(columns=['_merge'])
    
    # Save the joined result and exceptions to Excel
    df_result.to_excel(output_file, index=False)
    exceptions.to_excel(exception_file, index=False)

    print(f"Output saved to {output_file}")
    print(f"Exceptions saved to {exception_file}")

join_player_files(2022)
