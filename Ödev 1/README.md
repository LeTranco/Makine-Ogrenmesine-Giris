# KNN Algoritması İle İnsulin Tahmini

Bu proje, verilen bir CSV veri seti üzerinde KNN algoritması kullanılarak insülin doz tahmini / sınıflandırması yapmayı amaçlar.
Model, çeşitli sağlık parametrelerini kullanarak hastanın hangi insülin sınıfına ait olduğunu tahmin etmeye çalışır.

## Projede Kullanılan Teknolojiler:

#### 1-Python 3.x
#### 2-Pandas
#### 3-Scikit-learn
#### 4-Matplotlib
#### 5-CSV veri seti

## Neden KNN Algoritması?
Her ne kadar KNN algoritması için ölçeklendirme zorunlu olsa da doğrudan veriye bakarak analiz yapıp tahmin edebilmesi, tamamen veri dağılımına duyarlı olup hiçbir varsayım yapmaması, kategori ve sayısal özellikleri sorunsuz kullanabilmesi ve standartlaşmış bir veri üzerinden (yüksek glukoz + düşük fiziksel aktivite + yüksek BMI) karmaşık kombinasyonları yakalayabilir olması yüzünden insülin tahmini için KNN algoritması tercih edilmiştir. 

## Modelin Çalışma Mantığı:

### 1-Veri Setinin Yüklenmesi:
CSV dosyası Pandas ile okunur, ilk 5 satır ve veri tipi bilgileri görüntülenir.

### 2-Kategorileri Değişkenlerinin Düzenlenmesi:
Değişkenler "LabelEncoder" ile sayısal forma dönüştürülür.(gender, family_history, food_intake, previous_medications, Insulin (hedef değişken))

### 3-Veri Bölme:
Verinin %70’i eğitim, %30’u test için ayrılır.

### 4-Ölçeklendirme:
KNN mesafe hesabına dayandığından ölçeklendirme çok önemlidir. "StandardScaler()" ile eğitim/test verisi normalize edilir.

### 5-Modelin Eğitilmesi:
Model ilk olarak "k=3" ile eğitilir. Doğruluk oranı ve karışıklık matrisi hesaplanır.

### 6-Hiperparamete Optimizasyonu:
1–100 arasındaki k değerleri denenir, her biri için doğruluk hesaplanır ve grafik çizilir. Bu grafik, en uygun komşu sayısının belirlenmesini sağlar.

## Model Performansı:
Bütün işlemlerden sonra model %70 başarı oranı göstermektedir. Karışıklık matrisini hesaplamaktadır. Seçebileceğimiz her bir k değeri için grafik çizmektedir.

<img width="1317" height="1101" alt="image" src="https://github.com/user-attachments/assets/e9d4d96e-9093-4717-aff8-c6822425e7db" />

## Örnek Çıktılar:
Çıktı 1: <img width="198" height="13" alt="image" src="https://github.com/user-attachments/assets/0e05882e-e30f-402b-969a-575e88fb8e39" />

Çıktı 2: <img width="633" height="544" alt="image" src="https://github.com/user-attachments/assets/0e7f6d59-63d7-4ea2-b892-d13078fd9ca3" />

