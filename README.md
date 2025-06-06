💰 Automated Personal Finance App

An interactive, automated personal finance dashboard built with Python, Streamlit, Pandas, Plotly, Matplotlib, and JSON. This app helps you track, visualize, and categorize your expenses and income for smarter financial decisions.
🚀 Features

    📂 Automatic Categorization of transactions using a JSON-based ruleset

    📊 Interactive Dashboards powered by Plotly and Matplotlib

    🧮 Summary Statistics: Total income, expenses, and net savings

    📅 Monthly and Category-wise Trends

    🧾 Upload CSV or Excel files of bank statements

    📉 Visual insights into spending habits over time

🛠️ Tech Stack
Tool	Purpose
Python	Core logic and data processing
Pandas	Data manipulation and cleaning
JSON	Rules-based categorization system
Streamlit	Interactive web UI
Plotly	Dynamic visualizations
Matplotlib	Static summary charts
🧱 Project Structure

finance-app/
├── app.py                  # Main Streamlit app
├── categorizer.py          # Categorization logic using JSON
├── utils.py                # Helper functions
├── sample_data.csv         # Sample bank transaction data
├── categories.json         # Rules for transaction categorization
├── requirements.txt        # Python dependencies
└── README.md

📝 How to Use

    Clone the repository

git clone https://github.com/yourusername/finance-app.git
cd finance-app

Install dependencies
It's recommended to use a virtual environment.

pip install -r requirements.txt

Add your transaction data
Upload your .csv or .xlsx bank statement. Ensure it includes at least:

    Date

    Description

    Amount

Customize categories (optional)
Edit categories.json to add your own transaction classification rules.

Run the app

    streamlit run app.py

🔍 Categorization Logic

The app uses a JSON file (categories.json) to classify transactions based on keywords:

{
  "Groceries": ["walmart", "aldi", "grocery"],
  "Utilities": ["electric", "water", "internet"],
  "Dining": ["restaurant", "cafe", "starbucks"],
  "Salary": ["payroll", "direct deposit"]
}

Each transaction is matched against the keywords in the description field.
📈 Example Visualizations

    Category Breakdown Pie Chart

    Monthly Spending Line Chart

    Income vs. Expense Bar Chart

    Top 10 Expense Items

All visualizations are interactive using Plotly and customizable via the Streamlit sidebar.
✅ To Do

Add recurring expense prediction

Export categorized data

Add budgeting and alerts

    Multi-currency support

📄 License

MIT License
🙌 Contributing

Contributions are welcome! Please open an issue or submit a pull request for bugs, feature suggestions, or improvements.
