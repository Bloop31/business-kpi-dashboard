import matplotlib.pyplot as plt
def plot_monthly_revenue(data):
    plt.figure()
    data.plot(marker='o')
    plt.title('Monthly Revenue Trend')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.grid()
    plt.show()
    
def plot_top_product(data):
    plt.figure()
    data.plot(kind='bar')
    plt.title("Top 5 Products")
    plt.xlabel("Product")
    plt.ylabel("Revenue")
    plt.grid()
    plt.show()

def plot_region_sales(data):
    plt.figure()
    data.plot(kind='bar')
    plt.title("Region-wise-sales")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.grid()
    plt.show()
    