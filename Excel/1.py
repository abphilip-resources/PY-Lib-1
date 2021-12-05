import pandas as pd
from openpyxl.workbook import Workbook
loc = 'C:/Users/allen/Downloads/Resources/' \
      'Python/Lib/L1/Excel/data/1'                                # Location of the directory
      

# Converting to Pandas Dataframe
print(pd.read_excel(f'{loc}/ReadExcel.xlsx'),'\n\n')              # Print the excel file
print(pd.read_csv(f'{loc}/ReadText.txt', delimiter='\t'))         # Print the text file

# Dataframe Modification
df = pd.read_csv(f'{loc}/ReadCSV.csv', header=None)               # Read the csv file
df.columns = ['First', 'Last', 'Address', 
              'City', 'State', 'Zip', 'Income']                   # Rename the columns
df.to_excel(f'{loc}/WriteExcel.xlsx', index=False)                # Write the csv file to excel
df['Tax'] = df['Income'].apply(
      lambda x: .15 if x in range(0,5000)
           else .20 if x in range(5000,15000)
           else .25
)                                                                 # Create Tax column to df and calculate tax
df['Pay'] = df['Income'] * df['Tax']                              # Calculate tax to be paid

# Data Output
print('\n\nCSV data handling\n')
print(df[['Last', 'Zip']],'\n\n')                                 # Print the last name and zip code columns
print(df['City'][0:4],'\n\n')                                     # Print the first 4 cities
print(df.iloc[1,1],'\n\n')                                        # Print the second row, second column
print(df.loc[(df['First']=='John') &                              # Print the rows where first name is John 
     (df['City']=='Riverside')],'\n\n')                           # And city is Riverside
print(df[['Income', 'Tax', 'Pay']],'\n\n')                        # Print Income related information

# Dataframe Modification
df.drop(columns=['Address'], inplace=True)                        # Deleting unnecessary column
df['Rich'] = False                                                # New column created
df.loc[df['Income']>17500, 'Rich'] = True                         # Column added with conditional values

# Data Output
print(df,'\n\n')                                                  # Print all values
print(df.groupby(['Rich']).mean().sort_values('Tax'),'\n\n')      # Grouped by wealth, averaged and sorted by tax 
print(df.set_index('Zip').loc[8074],'\n\n')                       # Details of person with zip = 8074
print(df.First.str.split(expand=True))                            # Replacing first name with the first word