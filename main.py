meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "bir şakaya karşılık cevap",
    "SHEESH": "onaylamamak",
    "AGGRO": "agresifleşmek/sinirlenmek",
    "SIGMA": "topluluk kurallarına uymayan, kendi yolunda giden, çok havalı ve yalnız kurt takılan karakterleri tanımlamak için kullanılan bir meme",
    "BRUH":"Hayal kırıklığına uğranıldığında, utanç verici veya çok saçma bir durumla karşılaşıldığında "Ciddi misin?", "Hadi canım" anlamında söylenen tepki",
    "RIZZ": "birini etkileme, tavlama yeteneği veya karizma anlamına gelen KELİME',
}

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Bu kelime sözlükte yok :(")
