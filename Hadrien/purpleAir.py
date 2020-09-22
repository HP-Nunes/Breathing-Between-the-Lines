import glob
import pandas as pd
import datetime

class cleanup:

    def __init__(self, filepath): # init(self) is the first method that needs to be passed as the class' argument
        self.filepath = filepath
        
        self.wrangle_from_many_csv()
        
    def wrangle_from_many_csv(self):
        files = glob.glob(self.filepath + '/*.csv') # Filepath needs to be inputted as a string
        print(files)

        for i, f in enumerate (files,dataframe,file_name): 
            # we have a undertermined number of csv files in our repo from i (n=0) to f (n=n)
            df = pd.DataFrame()
            dataframe = df

            file_name = 'fname'
            if i == 0:
                dataframe = pd.read_csv(f)
                dataframe[file_name] = f # Save the csv filename to a dataframe field
        else:
            tmp = pd.read_csv(f)
            tmp[file_name] = f
            
    
        dataframe['location'] = dataframe.fname.str.split(filepath).str[1].str.split('(').str[0]
        
        # Split Latitude and Longitude into separate fields
        dataframe['Longitude'] = dataframe.fname.str.split(')').str[1].str.split('-').str[1]
        dataframe['Latitude'] = dataframe.fname.str.split(')').str[1].str.split('-').str[0].str.replace(r'(', '')
        dataframe['Latitude'] = dataframe['Latitude'].astype(float)
        dataframe['Longitude'] = dataframe['Longitude'].astype(float) * -1
        
        # Sensor location type
        dataframe['location_type'] = dataframe.fname.str.split('(').str[1].str.replace(r')', '') # purpleAir has outdoor and indoor sensors,
                                                         # therefore it's good to have an option to filter between those types

        # Fix & format the time fields
        dataframe['date'] = dataframe.created_at.str.split(' ').str[0]
        dataframe['hour'] = dataframe.created_at.str.split(' ').str[1].str.replace(r'UTC', '')
        dataframe['dateTime'] = pd.to_datetime(dataframe['date'] + ' ' + dataframe['hour'])
        dataframe = dataframe.sort_values(by='dateTime')
        dataframe.set_index(['dateTime'], inplace = True)

        dataframe = dataframe.loc[datetime.date(year=2020,month=1,day=1):datetime.date(year=2020,month=5,day=31)]

        # Convert UTC to PST
        dataframe.index = dataframe.index.tz_localize('UTC').tz_convert('US/Pacific')


        # Drop unwanted fields
        dataframe= dataframe.drop(['Unnamed: 9','fname','created_at'],axis=1)

        # Drop "undefined location types, i.e. only retain locations confirmed interior/outside"
        dataframe = dataframe[dataframe.location_type != 'undefined ']
        dataframe = dataframe.reset_index()
        print(dataframe.dtypes)
        print(len(dataframe))
        
        return dataframe.head()
    
    if __name__ == "__wrangle_from_many_csv__":
        wrangle_from_many_csv()