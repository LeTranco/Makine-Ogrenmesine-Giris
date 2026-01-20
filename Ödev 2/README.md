# Akıllı Ev Enerji Tüketimi Tahmini

Bu projenin amacı, bir akıllı ev veri setinden yola çıkarak 'Sıcaklık' gibi enerji tüketimini etkileyebilecek özelliklerden yola çıkarak evin tükettiği enerji seviyesinin ortalamanın üzerinde olup olmadığını tahmin etmektir.

## Projede Kullanılan Teknolojiler

#### 1-Python 
#### 2-Pandas
#### 3-Scikit-learn
#### 4-Matplotlib
#### 5-CSV veri seti

## Kodun Çalışma Mantığı

### 1-Gerekli Kütüphanelerin Eklenmesi
Veri işleme ve analizi için 'pandas', çok boyutlu diziler ve matematiksel işlemler için 'numpy' gibi projede kullanılmış kütüphaneler içeri aktarılır.

### 2-Veri Setinin Yüklenmesi ve Temizlenmesi
CSV dosyası okunur ve veri setindeki boş değer içeren tüm satırlar silinir.

### 3-Veri Setindeki Gerekli Sütunların Sayısallaştırılması
Örnek olarak modellerin çalışmasına uygun olması amacıyla 'summary' sütunundaki verilerin sayısallaştırılması gerekmektedir. Bu bağlamda 'LabelEncoder' yöntemi kullanılmıştır.

### 4-Pivot Tablosunun Amacı ve Kullanılması
Karmaşık ve çok satırlı bir veriyi anlamlı hale getirmek için pivot tablosu oluşturulur. Örneğin bu projede 'Saatlik ortalama', 'Sıcaklık Ortalaması', 'Nem Ortalaması' ve 'Rüzgar Hızı Ortalaması' olacak şekilde 4 pivot değer kullanılmıştır.

### 5-Üretilen Değerlerin Ana Tabloyla Birşetirilmesi
Pivot tablolarında ürettiğimiz 'Akıllı Bilgiler' modelin okuyabileceği ana veri setine yazdırılır. Bu işlem yapılmazsa oluşturulan pivot tabloları sadece grafik çizdirmeye yarar, modelin tahmin gücüne hiçbir katkı sağlamaz.

### 6-Modelin Hazırlanması ve Verinin Bölünmesi
Hedef değişken belirlenir ve ardından özellikler seçilir. Sonrasında eksik veriler silinip ölçeklendirme işlemi uygulanır. Son olarak elimizdeki veri %80 eğitim, %20 test olacak şekilde bölünür.

### 7-Modellerin Eğitilmesi
Bu aşamada 'Logistic Regression', 'KNN Classification' ve 'Random Forest' modelleri eğitilir. Sonucunda ise doğruluk oranları yazdırılır.

<img width="272" height="21" alt="image" src="https://github.com/user-attachments/assets/e8680329-732f-4e1a-9c10-fc263c39a767" />

'Logistic Regression', diğer modellere kıyasla %75 doğruluk oranıyla en az doğruluk oranına sahiptir.

<img width="273" height="19" alt="image" src="https://github.com/user-attachments/assets/40541c16-c16b-4fa4-be04-dfe7cd8b75e0" />

'KNN Classification' ise %82 doğruluk oranıyla 2. sırada yer almıştır.

<img width="230" height="15" alt="image" src="https://github.com/user-attachments/assets/d9363d05-2647-431d-a640-3145dd4a878a" />

'Random Forest' modeli, %84 doğruluk oranıyla en başarılı model olarak bulunmuştur.

### 8-Özellik-Önem Grafiğinin Çizilmesi
'Random Forest' modelinin özelliklere verdiği önem puanına bakılarak 'Özellik-Önem' grafiği çizilir.

<img width="993" height="594" alt="image" src="https://github.com/user-attachments/assets/fbfd47b7-309c-43e7-a09b-dc00364945ee" />

## Örnek Görseller

### Neme Göre Enerji Tüketimi
<img width="754" height="438" alt="image" src="https://github.com/user-attachments/assets/f10f79bc-9c2f-4518-b3b0-fbd6c87c73c1" />

### Saatlik Ortalama Enerji Tüketimi
<img width="754" height="438" alt="image" src="https://github.com/user-attachments/assets/3b8bf2b1-18a4-4a6c-a9be-0d3de9f97be9" />

# Katılım Sertifikalarım
<img width="1319" height="933" alt="image" src="https://github.com/user-attachments/assets/a98d4e8e-d23a-4b66-bcf7-0a6a667e5968" /> <img width="1321" height="933" alt="image" src="https://github.com/user-attachments/assets/a93e3080-b1ab-4dd8-9258-dac3d8a3c79a" />


