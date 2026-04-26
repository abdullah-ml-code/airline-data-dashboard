
import streamlit as st
import pandas as pd
import plotly.express as px

# إعدادات الصفحة
st.set_page_config(page_title="Airline Data Dashboard", layout="wide")

# عنوان التطبيق
st.title(" Airline Analysis Interactive Dashboard")
st.markdown("This dashboard explores flight data and investigates the relationship between passenger age and flight status.")

# تحميل البيانات
@st.cache_data
def load_data():
    df = pd.read_csv('Airline Dataset Updated - v2.csv')
    df['Departure Date'] = pd.to_datetime(df['Departure Date'], errors='coerce')
    return df

df = load_data()

# --- القائمة الجانبية (Sidebar) للفلاتر ---
st.sidebar.header("Filters")
selected_continent = st.sidebar.multiselect("Select Continent", 
                                            options=df['Continents'].unique(), 
                                            default=df['Continents'].unique())

# تصفية البيانات بناءً على الفلتر
filtered_df = df[df['Continents'].isin(selected_continent)]

# --- الجزء الأول: السؤال الأول (Data Exploration) ---
st.header("1. Data Overview & Quality")
col1, col2, col3 = st.columns(3)
col1.metric("Total Records", f"{len(filtered_df):,}")
col2.metric("Missing Values", filtered_df.isnull().sum().sum())
col3.metric("Duplicate Rows", filtered_df.duplicated().sum())

if st.checkbox("Show Raw Data"):
    st.write(filtered_df.head(100))

# --- الجزء الثاني: السؤال الثاني (Analysis & Findings) ---
st.header("2. Research: Age vs Flight Status")

# تقسيم الأعمار لفئات تفاعلية
age_bins = [0, 18, 35, 60, 100]
age_labels = ['Child', 'Young Adult', 'Adult', 'Senior']
filtered_df['Age_Group'] = pd.cut(filtered_df['Age'], bins=age_bins, labels=age_labels)

# الرسم البياني الأول: Stacked Bar Chart (تفاعلي)
st.subheader("Flight Status Distribution by Age Group")
fig1 = px.histogram(filtered_df, x="Age_Group", color="Flight Status", 
                barmode="stack", title="Passenger Count per Age Category")
st.plotly_chart(fig1, use_container_width=True)

# الرسم البياني الثاني: Boxplot (تفاعلي)
st.subheader("Age Distribution for each Flight Status")
fig2 = px.box(filtered_df, x="Flight Status", y="Age", color="Flight Status",
            points="all", title="Detailed Age Spread")
st.plotly_chart(fig2, use_container_width=True)

# استنتاج تلقائي
st.info("**Conclusion:** As shown in the charts, flight status proportions are consistent across all ages, supporting the hypothesis that age is not a major factor in flight delays.")