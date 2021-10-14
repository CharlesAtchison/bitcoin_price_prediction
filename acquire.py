import pandas as pd


def fetch_data_dict(df):
    ''' Fetches and formats a data_dict to put into project README.md
    returns two data dict.
    '''
    data_dict = {
        'Timestamp' : 'start tiem of time window (60s window), in Unix Time',
        'Open':'Open price at start time window',
        'High':'High price within the time window',
        'Low':'Low price within the time window',
        'Close':'Close price at the end of the time window',
        'Volume_(BTC)':'Volume of BTC transacted in this window',
        'Volume_(Currency)':'Volume of corresponding currency transacted in this window',
        'Weighted_Price' :'VWAP - Volume Weighted Average Price',
        'day_of_week' : 'Verbose name of the week',
        'month' : 'Month number and month name',
        'minute_price_diff' : 'Delta between the Close and Open',
        'price_delta' : 'Delta between the High and Low',
        'day_num' : 'The numeric number of the day of the month',
        'percent_change': 'Price difference / Open price represented as a percentage'
    }

    data_dict = pd.DataFrame([{'Feature': col, 
         'Datatype': f'{df[col].count()} non-null: {df[col].dtype}',
        'Definition' : data_dict[col]} for col in df.columns]).set_index('Feature').to_markdown()
    result = '### Data Dict\n\n' + data_dict
    return (result)