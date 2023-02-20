import pandas as pd

OUTPUT_PATH = './data/five_three_eight_rankings/'

def five_three_eight_api_url(year):
    """Get URL for 538 yearly ratings."""
    return 'https://projects.fivethirtyeight.com/march-madness-api/' + str(year) + '/fivethirtyeight_ncaa_forecasts.csv'


def download():
    """Download 538 college rankings."""

    for year in [2016, 2017, 2018, 2019, 2020, 2021, 2022]:
        url = five_three_eight_api_url(year)
        df = pd.read_csv(url)
        df.to_csv(OUTPUT_PATH+str(year)+'.csv', index=False)


if __name__ == "__main__":
    download()