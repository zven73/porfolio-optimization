import pandas as pd
import numpy as np

class monte_carlo_simulator:
    def __init__(self, mc, risk_function, return_function, numberOfPortfolios):
        self.__numberOfPortfolios = numberOfPortfolios
        self.__risk_function = risk_function
        self.__return_function = return_function
        self.__mc = mc

    def progressBar(iterable, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        total = len(iterable)

        # Progress Bar Printing Function
    def print_progress(iteration, total, prefix='', suffix='', decimals=1, bar_length=100):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            bar_length  - Optional  : character length of bar (Int)
        """
        str_format = "{0:." + str(decimals) + "f}"
        percents = str_format.format(100 * (iteration / float(total)))
        filled_length = int(round(bar_length * iteration / float(total)))
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        print('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),

    def generate_portfolios(self, returns, covariance, risk_free_rate):
        
        portfolios_allocations_df = pd.DataFrame({'Symbol':returns.index,'MeanReturn':returns.values})
        extra_data = pd.DataFrame({'Symbol':['Return','Risk','SharpeRatio'], 'MeanReturn':[0,0,0]})
        portfolios_allocations_df = portfolios_allocations_df.append(extra_data, ignore_index=True)        

        portfolio_size = len(returns.index)
        np.random.seed(0)

        #Adding equal allocation so I can assess how good/bad it is
        equal_allocations = self.get_equal_allocations(portfolio_size)
        portfolio_id = 'EqualAllocationPortfolio'
        self.compute_portfolio_risk_return_sharpe_ratio(portfolio_id, equal_allocations, portfolios_allocations_df, returns, covariance, risk_free_rate) 

        #Generating portfolios
        number_of_steps = 1000
        print('Generating portfolios. Number of steps: ', number_of_steps)
        counter_to_print =  int(self.__numberOfPortfolios / number_of_steps)
        for i in range(self.__numberOfPortfolios):
            portfolio_id = 'Portfolio_'+str(i)
            allocations = self.get_random_allocations(portfolio_size)
            self.compute_portfolio_risk_return_sharpe_ratio(portfolio_id, allocations, portfolios_allocations_df,returns, covariance, risk_free_rate)
            
            #printing approx <number of steps>x
            if (i%counter_to_print==0):
                #print('Completed Generating '+ str(i) +' Portfolios. ' + str((i + 1) / self.__numberOfPortfolios * 100), '%')
                monte_carlo_simulator.print_progress(i, self.__numberOfPortfolios, prefix='Progress:', suffix='Complete', bar_length=50)

        return portfolios_allocations_df

    def compute_portfolio_risk_return_sharpe_ratio(self, portfolio_id, allocations, portfolios_allocations_df, returns, covariance, risk_free_rate):
    
        #Calculate expected returns of portfolio
        expected_returns = self.__return_function(returns, allocations)
        #Calculate risk of portfolio
        risk = self.__risk_function(allocations,covariance)
        #Calculate Sharpe ratio of portfolio
        sharpe_ratio = self.__mc.calculate_sharpe_ratio(risk, expected_returns, risk_free_rate)
        
        portfolio_data = allocations
        portfolio_data = np.append(portfolio_data,expected_returns)
        portfolio_data = np.append(portfolio_data,risk)
        portfolio_data = np.append(portfolio_data,sharpe_ratio)
        #add data to the dataframe            
        portfolios_allocations_df[portfolio_id] = portfolio_data

    def get_equal_allocations(self, portfolio_size):
        n = float(1/portfolio_size)
        allocations = np.repeat(n, portfolio_size)
        return allocations

    def get_random_allocations(self, portfolio_size):
        
        allocations = np.random.rand(portfolio_size)
        allocations /= sum(allocations)
        return allocations

