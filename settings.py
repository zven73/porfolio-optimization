import numpy as np
import datetime as dt
from calculator import risk_return_calculator
import time

class settings:

    PriceEvent = 'Adj Close'
    ReturnType = 'Geometric'
    Optimisersettings = {}
    OptimiserType = 'OLS'
    CompaniesUrl = 'https://en.wikipedia.org/wiki/NASDAQ-100'#'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    NumberOfPortfolios = 10000
    API = 'yahoo'
    YearsToGoBack = 3
    RiskFreeRate = 0
    CompanyFetchMode = "PreFixed" #Auto

    #MyCompanies = ['AAPL', 'AMD', 'MSFT', 'MSFT', 'AMZN', 'NEM', 'MA', 'PYPL', 'T', 'LI', 'OGZPY', 'ALRS', 'TCS', 'YNDX', 'WDC']
    #MyCompanies = ['HON', 'T', 'ARCC', 'WFC', 'LMT', 'MRK', 'MDT', 'PFE', 'WELL', 'RTX', 'NEM', 'NOC', 'CSCO',
    #               'DIS', 'EA', 'F', 'FB', 'FDX', 'GE', 'GM', 'GOOGL', 'HPE', 'INTC', 'MA', 'MCD', 'MSFT', 'MU', 'NEM',
    #               'NFLX', 'NVDA', 'PFE', 'PYPL', 'QCOM', 'T', 'TSLA', 'TWTR', 'V', 'WMT']

    MyCompanies = ['AAPL', 'AMZN', 'NEM', 'MSFT', 'AMD', 'MA', 'PYPL', 'T', 'NVDA']

    # MyCompanies = ['HON',
    #  'T',
    #  'ARCC',
    #  'WFC',
    #  'LMT',
    #  'MRK',
    #  'MDT',
    #  'PFE',
    #  'WELL',
    #  'RTX',
    #  'NEM',
    #  'NOC',
    #  'MA',
    #  'CSCO',
    #  'UNM',
    #  'MSFT',
    #  'GD',
    #  'INTC',
    #  'RIO',
    #  'AAPL',
    #  'PYPL',
    #  'LRCX',
    #  'MRNA',
    #  'VALE',
    #  'TSM',
    #  'STT',
    #  'HBAN',
    #  'FTI',
    #  'SNPS',
    #  'ALL',
    #  'SBSW',
    #  'OGN',
    #  'GOOGL']

    #MyCompanies = ['AAL', 'AAPL', 'ABBV', 'ADBE', 'AMD', 'AMZN', 'ATVI', 'AVGO', 'BA', 'BABA', 'BIDU', 'BIIB', 'CSCO',
    #               'DIS', 'EA', 'F', 'FB', 'FDX', 'GE', 'GM', 'GOOGL', 'HPE', 'INTC', 'MA', 'MCD', 'MSFT', 'MU', 'NEM',
    #               'NFLX', 'NVDA', 'PFE', 'PYPL', 'QCOM', 'T', 'TSLA', 'TWTR', 'V', 'WMT']

    #MyCompanies = ['AAPL', 'AMD', 'AMZN', 'MSFT', 'NEM', 'TSLA', 'WMT', 'PYPL']

    #MyCompanies = ['INTC', 'AAPL', 'NVDA', 'T', 'AMD', 'AMZN', 'FB', 'GOOGL', 'MCD', 'MSFT', 'CSCO', 'EA', 'PYPL', 'QCOM', 'WMT', 'V', 'MA']
    #MyCompanies = ['INTC', 'AAPL', 'NVDA', 'T', 'AMD', 'FB', 'MCD', 'MSFT', 'CSCO', 'EA', 'PYPL', 'QCOM', 'WMT', 'V', 'MA']

    #MyCompanies = ['AAPL', 'AMD', 'AMZN', 'MSFT', 'NEM', 'NFLX', 'PYPL']

    #MyCompanies = ['AAPL', 'ABBV', 'ADBE', 'AMD', 'AMZN', 'AVGO', 'GOOGL', 'MA', 'MSFT', 'NEM', 'NFLX', 'PFE', 'PYPL', 'T', 'V']
    #MyCompanies = ['AAL', 'AAPL', 'ABBV', 'ABT', 'ADBE', 'ADBE', 'AMD', 'AMZN', 'ATVI', 'AVGO', 'BA', 'BABA', 'BIDU',
    #               'BIIB', 'BMY', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'EA', 'F', 'FB', 'FDX', 'GE', 'GM', 'GOOG', 'HPQ',
    #               'IBM', 'INTC', 'JNJ', 'KHC', 'KO', 'MA', 'MCD', 'MSFT', 'MU', 'NEM', 'NFLX', 'NKE', 'NVDA', 'PFE',
    #               'PG', 'PYPL', 'QCOM', 'SBUX', 'T', 'TGT', 'TSLA', 'TWTR', 'UBER', 'V', 'VTRS', 'WMT', 'XOM']

    #MyCompanies = ['AMD', 'AMZN', 'WMT', 'MA', 'AAPL', 'EA', 'PYPL']

    timestr = time.strftime("%Y%m%d-%H%M%S")
    extension = ".xlsx"
    plot_extension = ".pdf"
    PortfolioOptimisationPath = timestr + extension

    RiskFunction = risk_return_calculator.calculate_portfolio_risk
    ReturnFunction = risk_return_calculator.calculate_portfolio_expectedreturns
    AssetsExpectedReturnsFunction = risk_return_calculator.calculate_assets_expectedreturns
    AssetsCovarianceFunction = risk_return_calculator.calculate_assets_covariance
    DailyAssetsReturnsFunction = risk_return_calculator.calculate_daily_asset_returns

    @staticmethod
    def get_my_targets():
        return np.arange(0, 1.5, 0.05)

    @staticmethod
    def get_end_date():
        return dt.date.today()

    @staticmethod
    def get_start_date(end_date):
        return end_date - dt.timedelta(days=settings.YearsToGoBack*365)
