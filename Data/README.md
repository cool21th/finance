## Data Source

1. [pandas-datareader](https://pandas-datareader.readthedocs.io) : A separate package that allows you to connect to Google's Stock API(as well as others) 
and grab securities data and read it in as a DataFrame

        import pandas_datareader.data as web
        import datetime 
        start = datetime.datetime(2015,1,1)
        end = datetime.datetime(2017,1,1)

        facebook = web.DataReader('FB', 'google', start, end)

        facebook.head()

        from pandas_datareader.data import Options
        fb_options = Options('FB', 'google')

        options_df = fb_options.get_options_data(expiry=fb_options, expiry_dates[0])
        options_dv.head()


2. [Quandl](https://www.quandl.com/) : A company that offers a robust python API that allows you to grab data from a variety of sources(some free, som paid)

        import quandl
        mydata = quandl.get('EIA/PET_RWTC_D')
        # mydata = quandl.get('EIA/PET_RWTC_D', returns='numpy')
        
        import matplotlib.pyplot as plt
        # %matplotlib inline
        
        mydata.plot()
        
        
        real_estate = quandl.get('ZILLOW/C9_ZRIFAH')
        real_estate
        
        
        mydata = quandl.get("WIKI/AAPL")
        mydata.head()
        


3. Quantopian
    
    
4. AlphaVantage

5. Yahoo Finance(Shut down in 2017)

        Python library yfinance

