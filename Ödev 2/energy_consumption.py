# Gerekli kütüphanelerin eklenmesi
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score, classification_report 
from sklearn.preprocessing import LabelEncoder, StandardScaler 

# Veri setinin yüklenmesi ve temizlenmesi
df = pd.read_csv('Smart Home Dataset.csv', low_memory=False) 
df = df.dropna() 

# 'time' sütununun sayısallaştırıp oluşan sayısal zaman verisinin okunulabilir tarih formatına çevrilmesi
df['time'] = pd.to_numeric(df['time'], errors='coerce') 
df['datetime'] = pd.to_datetime(df['time'], unit='s') 
df['hour'] = df['datetime'].dt.hour 

# Hava durumuyla ilgili sütunların listelenip verilerin sayısallaştırılması
w_cols = ['temperature', 'humidity', 'visibility', 'windSpeed', 'pressure', 'cloudCover', 'windBearing', 'dewPoint', 'precipProbability']
for col in w_cols: 
    df[col] = pd.to_numeric(df[col], errors='coerce') 

# 'summary' sütununun sayısallaştırılması
le = LabelEncoder() 
df['summary_encoded'] = le.fit_transform(df['summary'].astype(str)) 

# Her saat, sıcaklık, nem ve rüzgar hızı için ortalama enerji tüketimini hesaplayan bir pivot tablo oluşturulması
p_hour = df.pivot_table(index='hour', values='use [kW]') 
p_hour.columns = ['hourAvg']
p_temp = df.pivot_table(index='temperature', values='use [kW]') 
p_temp.columns = ['temperatureAvg'] 
p_humid = df.pivot_table(index='humidity', values='use [kW]') 
p_humid.columns = ['humidityAvg']
p_wind = df.pivot_table(index='windSpeed', values='use [kW]') 
p_wind.columns = ['windSpeedAvg'] 

# Saatlik, sıcaklık, nem ve rüzgar hızı ortalamalarının ana tabloyla birleştirilmesi
df = df.merge(p_hour, on='hour', how='left') 
df = df.merge(p_temp, on='temperature', how='left') 
df = df.merge(p_humid, on='humidity', how='left') 
df = df.merge(p_wind, on='windSpeed', how='left')

# Öğrenilen ortalama bilgilerinin 4 ayrı grafikte düzenli bir şekilde gösterilmesi
fig, axes = plt.subplots(2, 2, figsize=(15, 10)) 
fig.suptitle('Energy Consumption Analysis of Pivot Variables', fontsize=16) 

sns.lineplot(ax=axes[0, 0], x=p_hour.index, y=p_hour['hourAvg'], marker='o', color='blue') 
axes[0, 0].set_title('Average Hourly Consumption')
axes[0, 0].set_ylabel('Avarage kW') 
sns.scatterplot(ax=axes[0, 1], x=p_temp.index, y=p_temp['temperatureAvg'], color='blue', alpha=0.5) 
axes[0, 1].set_title('Average Consumption Based on Temperature') 
sns.lineplot(ax=axes[1, 0], x=p_humid.index, y=p_humid['humidityAvg'], color='blue') 
axes[1, 0].set_title('Average Consumption Based on Humidity') 
sns.lineplot(ax=axes[1, 1], x=p_wind.index, y=p_wind['windSpeedAvg'], color='blue') 
axes[1, 1].set_title('Average Consumption Based on Wind Speed') 

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
plt.show() 

# Modelin hazırlanması
y = (df['use [kW]'] > df['use [kW]'].mean()).astype(int) 
features = ['hour', 'summary_encoded', 'temperature', 'humidity', 'visibility', 'windSpeed', 'pressure', 'cloudCover', 'windBearing', 'dewPoint', 'precipProbability', 'hourAvg', 'temperatureAvg', 'humidityAvg', 'windSpeedAvg']
X = df[features].fillna(0) 
scaler = StandardScaler() 
X_sc = scaler.fit_transform(X) 

# Verinin %80'i eğitim, %20'si test olacak şekilde bölünmesi
X_train, X_test, y_train, y_test = train_test_split(X_sc, y, test_size=0.2, random_state=42) 

# Sırayla modellerin eğitilmesi, test verilerinin üzerinde tahmin yapılması ve doğruluk oranlarının atanması
models = {
    "Logistic Regression": LogisticRegression(max_iter=7000),
    "KNN Classification": KNeighborsClassifier(n_neighbors=5), 
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42) 
}

print(" Model Sonuclari ") 
for name, model in models.items(): 
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds) 
    print(f"\n{name} Basari Orani: %{acc*100:.0f}") 
    print(classification_report(y_test, preds)) 

# Hangi özelliğin ne kadar önemli olduğunu Random Forest modelinin özelliklere verdiği önem puanına göre görselleştirilmesi
rf_importance = models["Random Forest"].feature_importances_ 
fea_imp_df = pd.DataFrame({'Feature': features, 'Importance': rf_importance}).sort_values(by='Importance', ascending=False) 

plt.figure(figsize=(10, 6)) 
sns.barplot(x='Importance', y='Feature', data=fea_imp_df, hue='Feature', palette='magma', legend=False) 
plt.title('Importance-Feature Graph') 
plt.grid(axis='x', linestyle='--', alpha=0.6) 
plt.tight_layout() 
plt.show() 