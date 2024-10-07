import pandas as pd

# pandas dictionarylerden oluşur

sozluk = dict(a=2, b=3, c=4, d=5)
sozluk['e'] = 11  # ekleme yaptık
seri = pd.Series(sozluk)
seri['e'] = 11  # ekleme yaptık
print(sozluk)
print(seri['a'])

recipe = {
    "id": 1,
    "name": "Classic Margherita Pizza",
    "ingredients": [
        "Pizza dough",
        "Tomato sauce",
        "Fresh mozzarella cheese",
        "Fresh basil leaves",
        "Olive oil",
        "Salt and pepper to taste"
    ],
    "instructions": [
        "Preheat the oven to 475°F (245°C).",
        "Roll out the pizza dough and spread tomato sauce evenly.",
        "Top with slices of fresh mozzarella and fresh basil leaves.",
        "Drizzle with olive oil and season with salt and pepper.",
        "Bake in the preheated oven for 12-15 minutes or until the crust is golden brown.",
        "Slice and serve hot."
    ],
    "prepTimeMinutes": 20,
    "cookTimeMinutes": 15,
    "servings": 4,
    "difficulty": "Easy",
    "cuisine": "Italian",
    "caloriesPerServing": 300,
    "tags": [
        "Pizza",
        "Italian"
    ],
    "userId": 166,
    "image": "https://cdn.dummyjson.com/recipe-images/1.webp",
    "rating": 4.6,
    "reviewCount": 98,
    "mealType": [
        "Dinner"
    ]
}

recipe_seri = pd.Series(recipe)
# print(recipe_seri)
print(recipe_seri['name'])
print(recipe_seri.iloc[2])  # pandasta kullanılan index location verme ifadesidir

print(recipe_seri.index)  # dict.keys()
print(recipe_seri.values)  # dict.values()

for i in recipe_seri:
    print(i)  # değerler gelir

# DATAFRAME = Serilerden oluşur,dict listeleri satırlara göre, iç içe dict yapısı sütunlara göre düzenlenir
# Her bir sütun veya satır bir seri olarak tutulur. Ancak okurken görebiliriz

liste = dict(
    c1=dict(a=4, b=5, c=6, d=7),
    c2=dict(a=1, b=2, c=5, e=7),
    c3=dict(c=4, f=5, g=6, e=7)
)

df = pd.DataFrame(liste)
print(df)
print(df['c1'])  # index yapısı sütun temellidir
print(df.loc['a'])  # satırlar için loc veya iloc kullanılır
print(df.iloc[0])

# Pandas İstatistik:
print(df.describe())  # Herbir sütunun istatistiki olarak hesaplamasını yapar
df.info()
print(df.value_counts()) # Üçünün de dolu olduğunu yazdırır
print(df['c1'].value_counts())

print(df.columns)
print(df.index)

