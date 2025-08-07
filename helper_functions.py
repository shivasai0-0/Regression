import pandas as pd

def Stats_fn(df:pd.DataFrame)->pd.DataFrame:
    """ Stats:df.describe
        skewness->absolute skewness>1
        IQR/std-> 1< and 3>
        outliers->(max-min)/std >6
        long left tail or long right tail->(min,max)/mean>2
        max outliers->Q3+1.5*IQR<max
        min outliers->Q1-1.5*IQR>min     """
    df=df.select_dtypes(include="number")
    Stats=df.describe()
    IQR=Stats.iloc[6]-Stats.iloc[4]
    return pd.DataFrame({"skewness":df.skew().abs()>1,
        "IQR/std":(IQR/Stats.loc["std"]).between(1,3,inclusive="neither"),
        "outliers":(Stats.iloc[7]-Stats.iloc[3])/Stats.iloc[2]>6,
        "long right tail":(Stats.loc["max"]/Stats.loc["mean"])>2,
        "long left tail":(Stats.loc["min"]/Stats.loc["mean"])>2,
        "max outliers":(Stats.iloc[6]+1.5*IQR)<Stats.loc["max"],
        "min outliers":Stats.iloc[4]-1.5*(IQR)>Stats.loc["min"]})