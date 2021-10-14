import pandas as pd

def prep_bitcoin_data(df):
    df = df.ffill()
    df['day_of_week'] = df.index.day_name()
    df['month'] = df.index.strftime('%m_%b')
    df['minute_price_diff'] = df.Close - df.Open
    df['price_delta'] = df.High - df.Low
    df['day_num'] = df.index.day

    # Calculated from open
    df['percent_change'] = (df.minute_price_diff / df.Open) * 100
    return df

