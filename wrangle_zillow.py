from imports import *
# set columnns display format
pd.set_option('display.max_columns', None)
# default pandas decimal number display format
pd.options.display.float_format = '{:20,.3f}'.format

# from our acquire.py:
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
def new_zillow_data():
    '''
    This function reads the Zillow data from the mySQL database into a df.
    '''
    # Create SQL query.
    sql_query = '''
    SELECT 
    prop.*,
    pred.logerror,
    pred.transactiondate,
    air.airconditioningdesc,
    arch.architecturalstyledesc,
    build.buildingclassdesc,
    heat.heatingorsystemdesc,
    landuse.propertylandusedesc,
    story.storydesc,
    construct.typeconstructiondesc
FROM
    properties_2017 prop
        INNER JOIN
    (SELECT 
        parcelid, logerror, MAX(transactiondate) AS transactiondate
    FROM
        predictions_2017
    GROUP BY parcelid , logerror) pred USING (parcelid)
        LEFT JOIN
    airconditioningtype air USING (airconditioningtypeid)
        LEFT JOIN
    architecturalstyletype arch USING (architecturalstyletypeid)
        LEFT JOIN
    buildingclasstype build USING (buildingclasstypeid)
        LEFT JOIN
    heatingorsystemtype heat USING (heatingorsystemtypeid)
        LEFT JOIN
    propertylandusetype landuse USING (propertylandusetypeid)
        LEFT JOIN
    storytype story USING (storytypeid)
        LEFT JOIN
    typeconstructiontype construct USING (typeconstructiontypeid)
WHERE
    prop.latitude IS NOT NULL
        AND prop.longitude IS NOT NULL
        AND transactiondate <= '2017-12-31';
    '''
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('zillow'))
    df = df.drop(columns='id')
    return df

def get_zillow_data():
    '''
    This function reads in zillow data from Zillow database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('zillow_data.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('zillow_data.csv', index_col=0)
        df = df.drop(columns='id')
    else:
        
        # Read fresh data from db into a DataFrame.
        df = new_zillow_data()
        
        # Write DataFrame to a csv file.
        df.to_csv('zillow_data.csv')
        
    return df

def nulls_by_col(df):
    num_rows_missing = df.isnull().sum()
    rows = df.shape[0]
    pct_miss = num_rows_missing / rows * 100
    cols_missing = pd.DataFrame({'num_rows_missing': num_rows_missing, 'percent_rows_missing': pct_miss})
    return cols_missing.sort_values(by='num_rows_missing', ascending=False)

def handle_missing_values(df, prop_required_columns, prop_required_row):
    threshold = int(round(prop_required_columns * len(df.index), 0))
    df = df.dropna(axis=1, thresh=threshold) #1, or ‘columns’ : Drop columns which contain missing value
    threshold = int(round(prop_required_row * len(df.columns), 0))
    df = df.dropna(axis=0, thresh=threshold) #0, or ‘index’ : Drop rows which contain missing values.
    return df

def split(df):
    '''
    This function drops the customer_id column and then splits a dataframe into 
    train, validate, and test in order to explore the data and to create and validate models. 
    It takes in a dataframe and contains an integer for setting a seed for replication. 
    Test is 20% of the original dataset. The remaining 80% of the dataset is 
    divided between valiidate and train, with validate being .30*.80= 24% of 
    the original dataset, and train being .70*.80= 56% of the original dataset. 
    The function returns, train, validate and test dataframes. 
    '''
    train, test = train_test_split(df, test_size = .2, random_state=123)   
    train, validate = train_test_split(train, test_size=.3, random_state=123)
    
    return train, validate, test