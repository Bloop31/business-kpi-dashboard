import tkinter as tk
from tkinter import filedialog,messagebox
import utils
from kpi_calculator import KPICalculator
import charts

class Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.title("Business KPI Dashboard")
        self.root.geometry("1000x500")
        self.df=None
        self.kpi=None
        self.create_ui()

    def create_ui(self):
        title=tk.Label(self.root,text="Business KPI Dashboard",font=("Arial",20))
        title.pack(pady=10)

        upload_btn=tk.Button(self.root,text="Upload CSV",font=("Arial",14),command=self.upload_file)
        upload_btn.pack(pady=10)

        self.output=tk.Text(self.root,height=15,width=70)
        self.output.pack()

        chart_btn1 = tk.Button(
            self.root,
            text="Monthly Revenue Chart",
            command=self.show_monthly_charts
        )
        chart_btn1.pack(pady=5)
        chart_btn2 = tk.Button(
            self.root,
            text="Top Products Chart",
            command=self.show_products_charts
        )
        chart_btn2.pack(pady=5)
        chart_btn3 = tk.Button(
            self.root,
            text="Region Sales Chart",
            command=self.show_region_charts
        )
        chart_btn3.pack(pady=5)
    
    def upload_file(self):
        file_path=filedialog.askopenfilename()
        if not file_path:
            return 
        try:
            self.df=utils.load_csv(file_path)
            self.kpi=KPICalculator(self.df)
            self.show_kpi()
        except Exception as e:
            messagebox.showerror("Error",str(e))

    def show_kpi(self):
        self.output.delete("1.0",tk.END)
        result=f"""Total Revenue: {self.kpi.total_revenue():,.2f}

Total Customers: {self.kpi.total_customers()}

Retention Rate: {self.kpi.retention_rate():.2f} %

Growth Rate: {self.kpi.growth_rate():.2f} %

"""
        self.output.insert(tk.END,result)

    def show_monthly_charts(self):
        if self.kpi:
            charts.plot_monthly_revenue(self.kpi.monthly_revenue())

    def show_products_charts(self):
        if self.kpi:
            charts.plot_top_product(self.kpi.top_products())
    def show_region_charts(self):
        if self.kpi:
            charts.plot_region_sales(self.kpi.region_sales())
    
root=tk.Tk()
app=Dashboard(root)
root.mainloop()