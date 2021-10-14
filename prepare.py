import pandas as pd

def prep_bitcoin_data(df):
    df = df.ffill()
    df['day_of_week'] = df.index.day_name()
    df['day_of_week_num'] = df.index.dayofweek
    df['month'] = df.index.strftime('%m_%b')
    df['month_num'] = df.index.month
    df['price_diff'] = df.Close - df.Open
    df['price_delta'] = df.High - df.Low
    df['day_num'] = df.index.day
    df['avg_price'] = (df.Open + df.Close) / 2 

    # Calculated from open
    df['percent_change'] = (df.price_diff / df.Open) * 100
    return df

def time_split(df, train_size = .5, validate_size = .3):
    '''Splits time series data based on percentages and returns train, validate, test THE
    DATAFRAME MUST BE CHRONOLOGICALLY SORTED!'''
    t_size = int(len(df) * train_size)
    v_size = int(len(df) * validate_size)
    end = t_size + v_size
    return df[0:t_size], df[t_size:end], df[end:len(df)+1]

