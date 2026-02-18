import pandas as pd

class KPICalculator:
    def __init__(self,df):
        self.df=df.copy()
        self.df['date']=pd.to_datetime(self.df['date'])
        self.df['revenue']=self.df['quantity']*self.df['price']

    def total_revenue(self):
        return self.df['revenue'].sum()
    
    def total_customers(self):
        return self.df['customer_id'].nunique()
        
    def monthly_revenue(self):
        return(
            self.df.groupby(self.df['date'].dt.to_period('M'))['revenue'].sum()
        )
    
    def top_products(self):
        return(
            self.df.groupby('product')['revenue'].sum().sort_values(ascending=False).head(5)

        )
    
    def region_sales(self):
        return (self.df.groupby('region')['revenue']).sum()
    
    def retention_rate(self):
        counts=self.df['customer_id'].value_counts()
        retained=counts[counts>1].count()
        total=counts.count()
        return (retained/total)*100
    
    def growth_rate(self):
        monthly=self.monthly_revenue()
        if len(monthly)<2:
            return 0
        first=monthly.iloc[0]
        last=monthly.iloc[-1]

        return (last-first/last)*100