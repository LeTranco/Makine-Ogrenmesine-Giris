import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt

#Veri Setinin Eklenmesi
df = pd.read_csv(r"C:\Users\ahmet\Desktop\Ders\Makine Öğrenmesine Giriş\Ödev 1\veri.csv")

print(df.head())
print(df.info())

label_cols = ["gender", "family_history", "food_intake", 
              "previous_medications", "Insulin"]

for col in label_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

print(df.head())

X = df.drop("Insulin", axis=1)
y = df["Insulin"]

# Modelin Egitilmesi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42) #Train test split

scaler = StandardScaler() #Olceklendirme
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors = 3) #Model Olusturma
knn.fit(X_train, y_train) #fit fonksiyonu verimizi (samples + target) kullanarak knn algoritmasini egitir

#Sonuclarin Degerlendirilmesi
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Dogruluk:" , accuracy)

conf_matrix = confusion_matrix(y_test, y_pred)
print("confusion_matrix:")
print(conf_matrix)

#Hiperparametre Ayarlamasi
accuracy_values = []
k_values = []
for k in range (1, 100):
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_values.append(accuracy)
    k_values.append(k)

plt.figure()
plt.plot(k_values, accuracy_values, marker = "o", linestyle = "-")
plt.title("K degerine gore dogruluk")
plt.xlabel("K degeri")
plt.ylabel("Dogruluk")
plt.grid(True)

plt.show()
