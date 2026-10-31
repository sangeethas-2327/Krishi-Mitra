export interface CropItem {
  key: string;       // Normalized lowercase key for eligibility engine e.g. "arecanut", "paddy"
  name_en: string;
  name_kn: string;
}

export interface CropCategory {
  id: string;
  name_en: string;
  name_kn: string;
  crops: CropItem[];
}

export const CROP_CATEGORIES: CropCategory[] = [
  {
    id: "cereals_millets",
    name_en: "Cereals & Millets",
    name_kn: "ಧಾನ್ಯಗಳು & ಸಿರಿಧಾನ್ಯಗಳು",
    crops: [
      { key: "paddy", name_en: "Paddy / Rice", name_kn: "ಭತ್ತ / ಅಕ್ಕಿ" },
      { key: "ragi", name_en: "Finger Millet (Ragi)", name_kn: "ರಾಗಿ" },
      { key: "jowar", name_en: "Sorghum / Jowar", name_kn: "ಜೋಳ (ಬಿಳಿ ಜೋಳ)" },
      { key: "maize", name_en: "Maize / Corn", name_kn: "ಮೆಕ್ಕೆಜೋಳ" },
      { key: "wheat", name_en: "Wheat", name_kn: "ಗೋಧಿ" },
      { key: "bajra", name_en: "Pearl Millet (Bajra)", name_kn: "ಸಜ್ಜೆ" },
      { key: "foxtail_millet", name_en: "Foxtail Millet (Navane)", name_kn: "ನವಣೆ" },
      { key: "little_millet", name_en: "Little Millet (Same)", name_kn: "ಸಾಮೆ" },
      { key: "kodo_millet", name_en: "Kodo Millet (Haraka)", name_kn: "ಹಾರಕ" },
      { key: "barnyard_millet", name_en: "Barnyard Millet (Oodalu)", name_kn: "ಊದಲು" },
      { key: "proso_millet", name_en: "Proso Millet (Baragu)", name_kn: "ಬರಗು" }
    ]
  },
  {
    id: "pulses",
    name_en: "Pulses",
    name_kn: "ಬೇಳೆಕಾಳುಗಳು",
    crops: [
      { key: "redgram", name_en: "Redgram / Pigeon Pea (Tur)", name_kn: "ತೊಗರಿ" },
      { key: "greengram", name_en: "Greengram / Moong", name_kn: "ಹೆಸರು ಕಾಳು" },
      { key: "blackgram", name_en: "Blackgram / Urad", name_kn: "ಉದ್ದು" },
      { key: "chickpea", name_en: "Chickpea / Bengal Gram (Chana)", name_kn: "ಕಡಲೆ" },
      { key: "cowpea", name_en: "Cowpea (Alasande)", name_kn: "ಅಲಸಂದೆ" },
      { key: "horsegram", name_en: "Horsegram (Huruli)", name_kn: "ಹುರುಳಿ" },
      { key: "field_bean", name_en: "Field Bean (Avare)", name_kn: "ಅವರೆಕಾಳು" }
    ]
  },
  {
    id: "oilseeds",
    name_en: "Oilseeds",
    name_kn: "ಎಣ್ಣೆಕಾಳುಗಳು",
    crops: [
      { key: "groundnut", name_en: "Groundnut / Peanut", name_kn: "ಕಡಲೆಕಾಯಿ / ಶೇಂಗಾ" },
      { key: "sunflower", name_en: "Sunflower", name_kn: "ಸೂರ್ಯಕಾಂತಿ" },
      { key: "soybean", name_en: "Soybean", name_kn: "ಸೋಯಾಬೀನ್" },
      { key: "sesame", name_en: "Sesame / Til", name_kn: "ಎಳ್ಳು" },
      { key: "mustard", name_en: "Mustard", name_kn: "ಸಾಸಿವೆ" },
      { key: "castor", name_en: "Castor", name_kn: "ಹರಳು" },
      { key: "safflower", name_en: "Safflower (Kusube)", name_kn: "ಕುಸುಬೆ" },
      { key: "niger", name_en: "Niger Seed (Huchellu)", name_kn: "ಹುಚ್ಚೆಳ್ಳು" }
    ]
  },
  {
    id: "plantation_commercial",
    name_en: "Plantation & Commercial",
    name_kn: "ತೋಟಗಾರಿಕೆ & ವಾಣಿಜ್ಯ ಬೆಳೆಗಳು",
    crops: [
      { key: "arecanut", name_en: "Arecanut / Betel Nut", name_kn: "ಅಡಿಕೆ" },
      { key: "coconut", name_en: "Coconut", name_kn: "ತೆಂಗು / ಕೊಬ್ಬರಿ" },
      { key: "coffee", name_en: "Coffee (Arabica / Robusta)", name_kn: "ಕಾಫಿ" },
      { key: "sugarcane", name_en: "Sugarcane", name_kn: "ಕಬ್ಬು" },
      { key: "cotton", name_en: "Cotton", name_kn: "ಹತ್ತಿ" },
      { key: "cashew", name_en: "Cashew Nut", name_kn: "ಗೋಡಂಬಿ" },
      { key: "rubber", name_en: "Rubber", name_kn: "ರಬ್ಬರ್" },
      { key: "tea", name_en: "Tea", name_kn: "ಚಹಾ" },
      { key: "tobacco", name_en: "Tobacco", name_kn: "ತಂಬಾಕು" },
      { key: "betelvine", name_en: "Betel Vine", name_kn: "ವೀಳ್ಯದೆಲೆ" },
      { key: "cocoa", name_en: "Cocoa", name_kn: "ಕೋಕೋ" }
    ]
  },
  {
    id: "spices_condiments",
    name_en: "Spices & Condiments",
    name_kn: "ಮಸಾಲೆ ಬೆಳೆಗಳು",
    crops: [
      { key: "pepper", name_en: "Black Pepper", name_kn: "ಕಾಳುಮೆಣಸು" },
      { key: "cardamom", name_en: "Cardamom (Elaichi)", name_kn: "ಏಲಕ್ಕಿ" },
      { key: "ginger", name_en: "Ginger", name_kn: "ಶುಂಠಿ" },
      { key: "turmeric", name_en: "Turmeric", name_kn: "ಅರಿಶಿನ" },
      { key: "chili", name_en: "Dry Chili (Byadgi / Guntur)", name_kn: "ಒಣಮೆಣಸಿನಕಾಯಿ (ಬ್ಯಾಡಗಿ)" },
      { key: "garlic", name_en: "Garlic", name_kn: "ಬೆಳ್ಳುಳ್ಳಿ" },
      { key: "coriander_seed", name_en: "Coriander Seeds", name_kn: "ಕೊತ್ತಂಬರಿ ಬೀಜ / ಧನಿಯಾ" },
      { key: "cumin", name_en: "Cumin / Jeera", name_kn: "ಜೀರಿಗೆ" },
      { key: "clove", name_en: "Clove (Lavanga)", name_kn: "ಲವಂಗ" },
      { key: "nutmeg", name_en: "Nutmeg (Jayikayi)", name_kn: "ಜಾಯಿಕಾಯಿ" }
    ]
  },
  {
    id: "fruits",
    name_en: "Fruits",
    name_kn: "ಹಣ್ಣುಗಳು",
    crops: [
      { key: "banana", name_en: "Banana", name_kn: "ಬಾಳೆ" },
      { key: "mango", name_en: "Mango", name_kn: "ಮಾವಿನಹಣ್ಣು" },
      { key: "pomegranate", name_en: "Pomegranate", name_kn: "ದಾಳಿಂಬೆ" },
      { key: "papaya", name_en: "Papaya", name_kn: "ಪಪ್ಪಾಯಿ" },
      { key: "guava", name_en: "Guava", name_kn: "ಸೀಬೆಹಣ್ಣು" },
      { key: "grapes", name_en: "Grapes", name_kn: "ದ್ರಾಕ್ಷಿ" },
      { key: "citrus", name_en: "Citrus / Orange / Mosambi", name_kn: "ಕಿತ್ತಳೆ / ಮೂಸಂಬಿ" },
      { key: "sapota", name_en: "Sapota / Chiku", name_kn: "ಸಪೋಟ" },
      { key: "jackfruit", name_en: "Jackfruit", name_kn: "ಹಲಸಿನಹಣ್ಣು" },
      { key: "watermelon", name_en: "Watermelon", name_kn: "ಕಲ್ಲಂಗಡಿ" },
      { key: "pineapple", name_en: "Pineapple", name_kn: "ಅನಾನಸ್" }
    ]
  },
  {
    id: "vegetables",
    name_en: "Vegetables",
    name_kn: "ತರಕಾರಿಗಳು",
    crops: [
      { key: "onion", name_en: "Onion", name_kn: "ಈರುಳ್ಳಿ / ಉಳ್ಳಾಗಡ್ಡಿ" },
      { key: "tomato", name_en: "Tomato", name_kn: "ಟೊಮೇಟೊ" },
      { key: "potato", name_en: "Potato", name_kn: "ಆಲೂಗಡ್ಡೆ" },
      { key: "green_chili", name_en: "Green Chili", name_kn: "ಹಸಿಮೆಣಸಿನಕಾಯಿ" },
      { key: "cabbage", name_en: "Cabbage", name_kn: "ಎಲೆಕೋಸು" },
      { key: "cauliflower", name_en: "Cauliflower", name_kn: "ಹೂಕೋಸು" },
      { key: "brinjal", name_en: "Brinjal / Eggplant", name_kn: "ಬದನೆಕಾಯಿ" },
      { key: "okra", name_en: "Okra / Lady Finger", name_kn: "ಬೆಂಡೆಕಾಯಿ" },
      { key: "beans", name_en: "Beans", name_kn: "ಹುರುಳಿಕಾಯಿ / ಬೀನ್ಸ್" },
      { key: "drumstick", name_en: "Drumstick", name_kn: "ನುಗ್ಗೆಕಾಯಿ" },
      { key: "carrot", name_en: "Carrot", name_kn: "ಕ್ಯಾರೆಟ್" }
    ]
  },
  {
    id: "other_crops",
    name_en: "Other Crops",
    name_kn: "ಇತರ ಬೆಳೆಗಳು",
    crops: [
      { key: "fodder", name_en: "Fodder / Grass", name_kn: "ಮೇವು / ಹಸಿರು ಹುಲ್ಲು" },
      { key: "flowers", name_en: "Flowers (Jasmine, Rose, Marigold)", name_kn: "ಹೂವುಗಳು (ಮಲ್ಲಿಗೆ, ಸೇವಂತಿಗೆ, ಚೆಂಡುಹೂ)" },
      { key: "sericulture", name_en: "Sericulture / Mulberry", name_kn: "ರೇಷ್ಮೆ (ಹಿಪ್ಪುನೇರಳೆ)" },
      { key: "medicinal_plants", name_en: "Medicinal & Aromatic Plants", name_kn: "ಔಷಧೀಯ & ಸುಗಂಧ ಸಸ್ಯಗಳು" }
    ]
  }
];

export function findCropByKey(key: string): CropItem | undefined {
  const normKey = key.trim().toLowerCase();
  for (const cat of CROP_CATEGORIES) {
    const found = cat.crops.find((c) => c.key === normKey);
    if (found) return found;
  }
  return undefined;
}

