import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os

st.set_page_config(page_title="Data Analysis", layout="wide")

catFile = "categories.json"

if "categories" not in st.session_state:
    st.session_state.categories = {
        "Category Pending": []
    }
if os.path.exists(catFile):
    with open (catFile, "r") as f:
        st.session_state.categories = json.load(f)

def saveCategories():
    with open(catFile, "w") as f:
        json.dump(st.session_state.categories, f)

def categorizeTransaction(df):
    df["Category"] = "Category Pending"
    for category, keywords in st.session_state.categories.items():
        if category == "Category Pending" or not keywords:
            continue
        
        lowerKeywords = [keyword.lower().strip() for keyword in keywords]
        for idx, row in df.iterrows():
            details = row["Description"].lower()
            if details in lowerKeywords:
                df.at[idx,"Category"] = category
    return df

def loadTransactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip() for col in df.columns]
        df["Amount"] = df["Amount"].replace(',', '').astype(float)
        df["Date"] = pd.to_datetime(df["Date"], format='%Y-%m-%d')
        return categorizeTransaction(df)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def addKeyword(category, keyword):
    keyword = keyword.strip()
    if keyword and keyword not in st.session_state.categories[category]:
        st.session_state.categories[category].append(keyword)
        saveCategories()
        return True
    return False

def main():
    st.title("Data Analysis Dashboard")
    
    uploadFile = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploadFile is not None:
        df = loadTransactions(uploadFile)
        if df is not None:
            spending = df[df["Amount"] < 0]
            income = df[df["Amount"] > 0]

            st.session_state.spending = spending.copy()

            tab1, tab2 = st.tabs(["Expenses", "Income"])
            with tab1:
                newCat = st.text_input("Add a new category")
                addButton = st.button("Add Category")
                if addButton and newCat:
                    if newCat not in st.session_state.categories:
                        st.session_state.categories[newCat] = []
                        saveCategories()
                        st.rerun()
                st.subheader("your spending")
                editedDf = st.data_editor(
                    st.session_state.spending[["Date", "Description", "Amount", "Category"]],
                    column_config={
                        "Date": st.column_config.DateColumn("Date", format="YY-MM-DD"),
                        "Description": st.column_config.TextColumn("Description"),
                        "Amount": st.column_config.NumberColumn("Amount", format="%.2f USD"),
                        "Category": st.column_config.SelectboxColumn("Category",options=list(st.session_state.categories.keys()))
                    },
                    hide_index=True,
                    use_container_width=True,
                    key="category_editor"
                )
                saveButton = st.button("Save Changes", type="primary")
                if saveButton:
                    for idx, row in editedDf.iterrows():
                        newCat = row["Category"]
                        if newCat == st.session_state.spending.at[idx,"Category"]:
                            continue
                        details = row["Description"]
                        st.session_state.spending.at[idx,"Category"] = newCat
                        addKeyword(newCat, details)
                
                st.subheader("Spending by Category")
                categoryCounts = st.session_state.spending.groupby("Category")["Amount"].sum().reset_index()
                categoryCounts = categoryCounts.sort_values(by="Amount", ascending=False)
                categoryCounts["Amount"] = categoryCounts["Amount"].abs()
                
                st.dataframe(categoryCounts, column_config={"Amount": st.column_config.NumberColumn("Amount", format="%.2f USD")}, use_container_width=True, hide_index=True)

                fig = px.pie(
                    categoryCounts, 
                    values='Amount', 
                    names='Category', 
                    title='Spending by Category')
                
                st.plotly_chart(fig, use_container_width=True)
                st.subheader("Total Spending")
                st.write("Total Spending: ", spending["Amount"].sum())
                
            with tab2:
                st.subheader("your income")
                payment = income["Amount"].sum()
                st.metric("Payments", f"{payment:.2f} USD")
main()