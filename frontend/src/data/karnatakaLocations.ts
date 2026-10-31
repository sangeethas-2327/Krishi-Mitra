export interface LocationItem {
  id: string;
  name_en: string;
  name_kn: string;
}

export interface TalukData {
  id: string;
  name_en: string;
  name_kn: string;
  villages: LocationItem[];
}

export interface DistrictData {
  id: string;
  name_en: string;
  name_kn: string;
  taluks: TalukData[];
}

export const KARNATAKA_DISTRICTS: DistrictData[] = [
  {
    id: "shivamogga",
    name_en: "Shivamogga",
    name_kn: "ಶಿವಮೊಗ್ಗ",
    taluks: [
      {
        id: "thirthahalli",
        name_en: "Thirthahalli",
        name_kn: "ತೀರ್ಥಹಳ್ಳಿ",
        villages: [
          { id: "agumbe", name_en: "Agumbe", name_kn: "ಆಗುಂಬೆ" },
          { id: "megaravalli", name_en: "Megaravalli", name_kn: "ಮೇಗರವಳ್ಳಿ" },
          { id: "konandur", name_en: "Konandur", name_kn: "ಕೋಣಂದೂರು" },
          { id: "salur", name_en: "Salur", name_kn: "ಸಾಲೂರು" },
          { id: "muttur", name_en: "Muttur", name_kn: "ಮುತ್ತೂರು" },
          { id: "bejavalli", name_en: "Bejavalli", name_kn: "ಬೇಜವಳ್ಳಿ" },
          { id: "kudumallige", name_en: "Kudumallige", name_kn: "ಕುಡುಮಲ್ಲಿಗೆ" },
          { id: "mandagadde_th", name_en: "Mandagadde", name_kn: "ಮಂಡಗದ್ದೆ" }
        ]
      },
      {
        id: "shivamogga_t",
        name_en: "Shivamogga",
        name_kn: "ಶಿವಮೊಗ್ಗ",
        villages: [
          { id: "holalur", name_en: "Holalur", name_kn: "ಹೊಳಲೂರು" },
          { id: "harnahalli", name_en: "Harnahalli", name_kn: "ಹಾರ್ನಹಳ್ಳಿ" },
          { id: "kumsi", name_en: "Kumsi", name_kn: "ಕುಂಸಿ" },
          { id: "ayanoor", name_en: "Ayanur", name_kn: "ಅಯನೂರು" },
          { id: "gajanur", name_en: "Gajanur", name_kn: "ಗಜನೂರು" },
          { id: "abbalagere", name_en: "Abbalagere", name_kn: "ಅಬ್ಬಲಗೆರೆ" }
        ]
      },
      {
        id: "bhadravathi",
        name_en: "Bhadravathi",
        name_kn: "ಭದ್ರಾವತಿ",
        villages: [
          { id: "holehonnur", name_en: "Holehonnur", name_kn: "ಹೊಳೆಹೊನ್ನೂರು" },
          { id: "kudligere", name_en: "Kudligere", name_kn: "ಕುಡ್ಲಿಗೆರೆ" },
          { id: "barandur", name_en: "Barandur", name_kn: "ಬಾರಂದೂರು" },
          { id: "donabagatta", name_en: "Donabagatta", name_kn: "ದೋಣಬಘಟ್ಟ" }
        ]
      },
      {
        id: "sagara",
        name_en: "Sagara",
        name_kn: "ಸಾಗರ",
        villages: [
          { id: "jog", name_en: "Jog Falls", name_kn: "ಜೋಗ್ ಜಲಪಾತ" },
          { id: "anandapura", name_en: "Anandapura", name_kn: "ಆನಂದಪುರ" },
          { id: "talaguppa", name_en: "Talaguppa", name_kn: "ತಾಳಗುಪ್ಪ" },
          { id: "kargal", name_en: "Kargal", name_kn: "ಕಾರ್ಗಲ್" },
          { id: "avina", name_en: "Avinahalli", name_kn: "ಅವಿನಹಳ್ಳಿ" },
          { id: "keladi", name_en: "Keladi", name_kn: "ಕೆಳದಿ" }
        ]
      },
      {
        id: "shikaripura",
        name_en: "Shikaripura",
        name_kn: "ಶಿಕಾರಿಪುರ",
        villages: [
          { id: "shiralkoppa", name_en: "Shiralkoppa", name_kn: "ಶಿರಾಳಕೊಪ್ಪ" },
          { id: "hittaladahalli", name_en: "Hittaladahalli", name_kn: "ಹಿತ್ತಲದಹಳ್ಳಿ" },
          { id: "salur_sk", name_en: "Salur", name_kn: "ಸಾಲೂರು" },
          { id: "togarsi", name_en: "Togarsi", name_kn: "ತೋಗರ್ಸಿ" }
        ]
      },
      {
        id: "soraba",
        name_en: "Soraba",
        name_kn: "ಸೊರಬ",
        villages: [
          { id: "anavatty", name_en: "Anavatti", name_kn: "ಆನವಟ್ಟಿ" },
          { id: "chandragutti", name_en: "Chandragutti", name_kn: "ಚಂದ್ರಗುತ್ತಿ" },
          { id: "ulavi", name_en: "Ulavi", name_kn: "ಉಳವಿ" },
          { id: "jade", name_en: "Jade", name_kn: "ಜಡೆ" }
        ]
      },
      {
        id: "hosanagara",
        name_en: "Hosanagara",
        name_kn: "ಹೊಸನಗರ",
        villages: [
          { id: "nagara", name_en: "Nagara", name_kn: "ನಗರ" },
          { id: "ripponpet", name_en: "Ripponpet", name_kn: "ರಿಪ್ಪನ್‌ಪೇಟೆ" },
          { id: "marakutuka", name_en: "Marakutuka", name_kn: "ಮಾರಕುಟುಕ" },
          { id: "kodur", name_en: "Kodur", name_kn: "ಕೋದೂರು" }
        ]
      }
    ]
  },
  {
    id: "hassan",
    name_en: "Hassan",
    name_kn: "ಹಾಸನ",
    taluks: [
      {
        id: "hassan_t",
        name_en: "Hassan",
        name_kn: "ಹಾಸನ",
        villages: [
          { id: "dudda", name_en: "Dudda", name_kn: "ದುದ್ದ" },
          { id: "shantigrama", name_en: "Shantigrama", name_kn: "ಶಾಂತಿಗ್ರಾಮ" },
          { id: "kattaya", name_en: "Kattaya", name_kn: "ಕಟ್ಟಾಯ" }
        ]
      },
      {
        id: "sakleshpur",
        name_en: "Sakleshpur",
        name_kn: "ಸಕಲೇಶಪುರ",
        villages: [
          { id: "yeslur", name_en: "Yeslur", name_kn: "ಯೆಸಳೂರು" },
          { id: "hanbal", name_en: "Hanbal", name_kn: "ಹಾನ್ಬಾಳ್" },
          { id: "heggadde", name_en: "Heggadde", name_kn: "ಹೆಗ್ಗದ್ದೆ" },
          { id: "shukravarasante", name_en: "Shukravarasante", name_kn: "ಶುಕ್ರವಾರಸಂತೆ" }
        ]
      },
      {
        id: "belur",
        name_en: "Belur",
        name_kn: "ಬೇಲೂರು",
        villages: [
          { id: "halebeedu", name_en: "Halebeedu", name_kn: "ಹಳೇಬೀಡು" },
          { id: "arehalli", name_en: "Arehalli", name_kn: "ಅರೆಹಳ್ಳಿ" },
          { id: "hagare", name_en: "Hagare", name_kn: "ಹಗರೆ" }
        ]
      },
      {
        id: "alur",
        name_en: "Alur",
        name_kn: "ಆಲೂರು",
        villages: [
          { id: "kanthur", name_en: "Kanthur", name_kn: "ಕಣ್ತೂರು" },
          { id: "palya", name_en: "Palya", name_kn: "ಪಾಳ್ಯ" }
        ]
      },
      {
        id: "arkalgud",
        name_en: "Arkalgud",
        name_kn: "ಅರಕಲಗೂಡು",
        villages: [
          { id: "konanur", name_en: "Konanur", name_kn: "ಕೊಣನೂರು" },
          { id: "ramanathapura", name_en: "Ramanathapura", name_kn: "ರಾಮನಾಥಪುರ" }
        ]
      },
      {
        id: "arsikere",
        name_en: "Arsikere",
        name_kn: "ಅರಸೀಕೆರೆ",
        villages: [
          { id: "banavara", name_en: "Banavara", name_kn: "ಬಾಣಾವರ" },
          { id: "kandikere", name_en: "Kandikere", name_kn: "ಕಂಡಿಕೆರೆ" }
        ]
      },
      {
        id: "channarayapatna",
        name_en: "Channarayapatna",
        name_kn: "ಚನ್ನರಾಯಪಟ್ಟಣ",
        villages: [
          { id: "shravanabelagola", name_en: "Shravanabelagola", name_kn: "ಶ್ರವಣಬೆಳಗೊಳ" },
          { id: "hirisave", name_en: "Hirisave", name_kn: "ಹಿರಿಸಾವೆ" }
        ]
      },
      {
        id: "holenarasipura",
        name_en: "Holenarasipura",
        name_kn: "ಹೊಳೆನರಸೀಪುರ",
        villages: [
          { id: "hallimysuru", name_en: "Halli Mysuru", name_kn: "ಹಳ್ಳಿ ಮೈಸೂರು" },
          { id: "kerekodi", name_en: "Kerekodi", name_kn: "ಕೆರೆಕೋಡಿ" }
        ]
      }
    ]
  },
  {
    id: "mandya",
    name_en: "Mandya",
    name_kn: "ಮಂಡ್ಯ",
    taluks: [
      {
        id: "mandya_t",
        name_en: "Mandya",
        name_kn: "ಮಂಡ್ಯ",
        villages: [
          { id: "keragodu", name_en: "Keragodu", name_kn: "ಕೆರೆಗೋಡು" },
          { id: "dudda_m", name_en: "Dudda", name_kn: "ದುದ್ದ" },
          { id: "basaralu", name_en: "Basaralu", name_kn: "ಬಸರಾಳು" }
        ]
      },
      {
        id: "maddur",
        name_en: "Maddur",
        name_kn: "ಮದ್ದೂರು",
        villages: [
          { id: "besagarahalli", name_en: "Besagarahalli", name_kn: "ಬೆಸಗರಹಳ್ಳಿ" },
          { id: "koppam", name_en: "Koppa", name_kn: "ಕೊಪ್ಪ" }
        ]
      },
      {
        id: "malavalli",
        name_en: "Malavalli",
        name_kn: "ಮಳವಳ್ಳಿ",
        villages: [
          { id: "halagur", name_en: "Halagur", name_kn: "ಹಲಗೂರು" },
          { id: "kikkeri", name_en: "Kikkeri", name_kn: "ಕಿಕ್ಕೇರಿ" }
        ]
      },
      {
        id: "pandavapura",
        name_en: "Pandavapura",
        name_kn: "ಪಾಂಡವಪುರ",
        villages: [
          { id: "melukote", name_en: "Melukote", name_kn: "ಮೇಲುಕೋಟೆ" },
          { id: "kyathanahalli", name_en: "Kyathanahalli", name_kn: "ಕ್ಯಾತನಹಳ್ಳಿ" }
        ]
      },
      {
        id: "srirangapatna",
        name_en: "Srirangapatna",
        name_kn: "ಶ್ರೀರಂಗಪಟ್ಟಣ",
        villages: [
          { id: "aralakuppe", name_en: "Aralakuppe", name_kn: "ಅರಳಕುಪ್ಪೆ" },
          { id: "palahalli", name_en: "Palahalli", name_kn: "ಪಾಲಹಳ್ಳಿ" }
        ]
      },
      {
        id: "kr_pete",
        name_en: "K.R. Pete",
        name_kn: "ಕೆ.ಆರ್. ಪೇಟೆ",
        villages: [
          { id: "santhebachahalli", name_en: "Santhebachahalli", name_kn: "ಸಂತೆಬಾಚಹಳ್ಳಿ" }
        ]
      },
      {
        id: "nagamangala",
        name_en: "Nagamangala",
        name_kn: "ನಾಗಮಂಗಲ",
        villages: [
          { id: "bellur", name_en: "Bellur", name_kn: "ಬೆಳ್ಳೂರು" },
          { id: "bindiganavile", name_en: "Bindiganavile", name_kn: "ಬಿಂದಿಗನವಿಲೆ" }
        ]
      }
    ]
  },
  {
    id: "mysuru",
    name_en: "Mysuru",
    name_kn: "ಮೈಸೂರು",
    taluks: [
      {
        id: "mysuru_t",
        name_en: "Mysuru",
        name_kn: "ಮೈಸೂರು",
        villages: [
          { id: "varuna", name_en: "Varuna", name_kn: "ವರುಣಾ" },
          { id: "jayapura", name_en: "Jayapura", name_kn: "ಜಯಪುರ" },
          { id: "kadakola", name_en: "Kadakola", name_kn: "ಕಡಕೋಳ" }
        ]
      },
      {
        id: "hunsur",
        name_en: "Hunsur",
        name_kn: "ಹುಣಸೂರು",
        villages: [
          { id: "bilikere", name_en: "Bilikere", name_kn: "ಬಿಳಿಕೆರೆ" },
          { id: "hanagodu", name_en: "Hanagodu", name_kn: "ಹನಗೋಡು" }
        ]
      },
      {
        id: "nanjangud",
        name_en: "Nanjangud",
        name_kn: "ನಂಜನಗೂಡು",
        villages: [
          { id: "hadinaru", name_en: "Hadinaru", name_kn: "ಹದಿನಾರು" },
          { id: "kallamballa", name_en: "Kallamballa", name_kn: "ಕಲ್ಲಂಬಳ್ಳ" }
        ]
      },
      {
        id: "heggadadevankote",
        name_en: "H.D. Kote",
        name_kn: "ಹೆಚ್.ಡಿ. ಕೋಟೆ",
        villages: [
          { id: "antharasanthe", name_en: "Antharasanthe", name_kn: "ಅಂತರಸಂತೆ" }
        ]
      },
      {
        id: "kr_nagar",
        name_en: "K.R. Nagar",
        name_kn: "ಕೆ.ಆರ್. ನಗರ",
        villages: [
          { id: "saligrama", name_en: "Saligrama", name_kn: "ಸಾಲಿಗ್ರಾಮ" },
          { id: "mirle", name_en: "Mirle", name_kn: "ಮಿರ್ಲೆ" }
        ]
      },
      {
        id: "periyapatna",
        name_en: "Periyapatna",
        name_kn: "ಪಿರಿಯಾಪಟ್ಟಣ",
        villages: [
          { id: "bettadapura", name_en: "Bettadapura", name_kn: "ಬೆಟ್ಟದಪುರ" },
          { id: "kikkeri_p", name_en: "Kikkeri", name_kn: "ಕಿಕ್ಕೇರಿ" }
        ]
      },
      {
        id: "t_narasipura",
        name_en: "T. Narasipura",
        name_kn: "ಟಿ. ನರಸೀಪುರ",
        villages: [
          { id: "mugur", name_en: "Mugur", name_kn: "ಮುಗೂರು" },
          { id: "sosale", name_en: "Sosale", name_kn: "ಸೋಸಲೆ" }
        ]
      },
      {
        id: "saragur",
        name_en: "Saragur",
        name_kn: "ಸರಗೂರು",
        villages: [
          { id: "mullur", name_en: "Mullur", name_kn: "ಮುಳ್ಳೂರು" }
        ]
      }
    ]
  },
  {
    id: "chikkamagaluru",
    name_en: "Chikkamagaluru",
    name_kn: "ಚಿಕ್ಕಮಗಳೂರು",
    taluks: [
      {
        id: "chikkamagaluru_t",
        name_en: "Chikkamagaluru",
        name_kn: "ಚಿಕ್ಕಮಗಳೂರು",
        villages: [
          { id: "aldur", name_en: "Aldur", name_kn: "ಅಲ್ದೂರು" },
          { id: "vastare", name_en: "Vastare", name_kn: "ವಸ್ತಾರೆ" },
          { id: "avathi", name_en: "Avathi", name_kn: "ಆವತಿ" }
        ]
      },
      {
        id: "mudigere",
        name_en: "Mudigere",
        name_kn: "ಮೂಡಿಗೆರೆ",
        villages: [
          { id: "kalasa", name_en: "Kalasa", name_kn: "ಕಳಸ" },
          { id: "kottigehara", name_en: "Kottigehara", name_kn: "ಕೊಟ್ಟಿಗೆಹಾರ" },
          { id: "gonibeedu", name_en: "Gonibeedu", name_kn: "ಗೋಣಿಬೀಡು" }
        ]
      },
      {
        id: "koppa",
        name_en: "Koppa",
        name_kn: "ಕೊಪ್ಪ",
        villages: [
          { id: "hariharapura", name_en: "Hariharapura", name_kn: "ಹರಿಹರಪುರ" },
          { id: "jayapura_k", name_en: "Jayapura", name_kn: "ಜಯಪುರ" }
        ]
      },
      {
        id: "sringeri",
        name_en: "Sringeri",
        name_kn: "ಶೃಂಗೇರಿ",
        villages: [
          { id: "kigga", name_en: "Kigga", name_kn: "ಕಿಗ್ಗ" },
          { id: "menase", name_en: "Menase", name_kn: "ಮೆಣಸೆ" }
        ]
      },
      {
        id: "narasimharajapura",
        name_en: "N.R. Pura",
        name_kn: "ಎನ್.ಆರ್. ಪುರ",
        villages: [
          { id: "balehonnur", name_en: "Balehonnur", name_kn: "ಬಾಳೆಹೊನ್ನೂರು" }
        ]
      },
      {
        id: "tarikere",
        name_en: "Tarikere",
        name_kn: "ತರೀಕೆರೆ",
        villages: [
          { id: "ajjumpura", name_en: "Ajjampura", name_kn: "ಅಜ್ಜಂಪುರ" },
          { id: "lingadahalli", name_en: "Lingadahalli", name_kn: "ಲಿಂಗದಹಳ್ಳಿ" }
        ]
      },
      {
        id: "kadavur",
        name_en: "Kadur",
        name_kn: "ಕಡೂರು",
        villages: [
          { id: "birur", name_en: "Birur", name_kn: "ಬೀರೂರು" },
          { id: "sakrepatna", name_en: "Sakrepatna", name_kn: "ಸಖರಾಯಪಟ್ಟಣ" }
        ]
      }
    ]
  },
  {
    id: "dakshina_kannada",
    name_en: "Dakshina Kannada",
    name_kn: "ದಕ್ಷಿಣ ಕನ್ನಡ",
    taluks: [
      {
        id: "mangalore_t",
        name_en: "Mangaluru",
        name_kn: "ಮಂಗಳೂರು",
        villages: [
          { id: "surathkal", name_en: "Surathkal", name_kn: "ಸುರತ್ಕಲ್" },
          { id: "gurupura", name_en: "Gurupura", name_kn: "ಗುರುಪುರ" }
        ]
      },
      {
        id: "bantwal",
        name_en: "Bantwal",
        name_kn: "ಬಂಟ್ವಾಳ",
        villages: [
          { id: "panemangalore", name_en: "Panemangalore", name_kn: "ಪಾಣೆಮಂಗಳೂರು" },
          { id: "vittla", name_en: "Vittla", name_kn: "ವಿಟ್ಲ" }
        ]
      },
      {
        id: "puttur",
        name_en: "Puttur",
        name_kn: "ಪುತ್ತೂರು",
        villages: [
          { id: "uppinangady", name_en: "Uppinangady", name_kn: "ಉಪ್ಪಿನಂಗಡಿ" },
          { id: "panaje", name_en: "Panaje", name_kn: "ಪಣಾಜೆ" }
        ]
      },
      {
        id: "belthangady",
        name_en: "Belthangady",
        name_kn: "ಬೆಳ್ತಂಗಡಿ",
        villages: [
          { id: "dharmasthala", name_en: "Dharmasthala", name_kn: "ಧರ್ಮಸ್ಥಳ" },
          { id: "ujire", name_en: "Ujire", name_kn: "ಉಜಿರೆ" }
        ]
      },
      {
        id: "sullia",
        name_en: "Sullia",
        name_kn: "ಸುಳ್ಯ",
        villages: [
          { id: "subrahmanya", name_en: "Subrahmanya", name_kn: "ಸುಬ್ರಹ್ಮಣ್ಯ" },
          { id: "bellare", name_en: "Bellare", name_kn: "ಬೆಳ್ಳಾರೆ" }
        ]
      },
      {
        id: "moodbidri",
        name_en: "Moodbidri",
        name_kn: "ಮೂಡುಬಿದಿರೆ",
        villages: [
          { id: "alangar", name_en: "Alangar", name_kn: "ಅಲಂಗಾರ್" }
        ]
      },
      {
        id: "kadaba",
        name_en: "Kadaba",
        name_kn: "ಕಡಬ",
        villages: [
          { id: "mardhala", name_en: "Mardhala", name_kn: "ಮರ್ದಾಳ" }
        ]
      }
    ]
  },
  {
    id: "udupi",
    name_en: "Udupi",
    name_kn: "ಉಡುಪಿ",
    taluks: [
      {
        id: "udupi_t",
        name_en: "Udupi",
        name_kn: "ಉಡುಪಿ",
        villages: [
          { id: "malpe", name_en: "Malpe", name_kn: "ಮಲ್ಪೆ" },
          { id: "santhekatte", name_en: "Santhekatte", name_kn: "ಸಂತೆಕಟ್ಟೆ" }
        ]
      },
      {
        id: "kundapura",
        name_en: "Kundapura",
        name_kn: "ಕುಂದಾಪುರ",
        villages: [
          { id: "gangolli", name_en: "Gangolli", name_kn: "ಗಂಗೊಳ್ಳಿ" },
          { id: "kollur", name_en: "Kollur", name_kn: "ಕೊಲ್ಲೂರು" },
          { id: "shankaranarayana", name_en: "Shankaranarayana", name_kn: "ಶಂಕರನಾರಾಯಣ" }
        ]
      },
      {
        id: "karkala",
        name_en: "Karkala",
        name_kn: "ಕಾರ್ಕಳ",
        villages: [
          { id: "belman", name_en: "Belman", name_kn: "ಬೆಲ್ಮಣ್" },
          { id: "hebri_k", name_en: "Hebri", name_kn: "ಹೆಬ್ರಿ" },
          { id: "bajagoli", name_en: "Bajagoli", name_kn: "ಬಜಗೋಳಿ" }
        ]
      },
      {
        id: "byndoor",
        name_en: "Byndoor",
        name_kn: "ಬೈಂದೂರು",
        villages: [
          { id: "shirur", name_en: "Shirur", name_kn: "ಶಿರೂರು" }
        ]
      },
      {
        id: "brahmavara",
        name_en: "Brahmavara",
        name_kn: "ಬ್ರಹ್ಮಾವರ",
        villages: [
          { id: "barkur", name_en: "Barkur", name_kn: "ಬಾರಕೂರು" }
        ]
      },
      {
        id: "kaup",
        name_en: "Kaup",
        name_kn: "ಕಾಪು",
        villages: [
          { id: "shirva", name_en: "Shirva", name_kn: "ಶಿರ್ವ" },
          { id: "katapadi", name_en: "Katapadi", name_kn: "ಕಟಪಾಡಿ" }
        ]
      },
      {
        id: "hebri",
        name_en: "Hebri",
        name_kn: "ಹೆಬ್ರಿ",
        villages: [
          { id: "seetanadi", name_en: "Seetanadi", name_kn: "ಸೀತಾನದಿ" }
        ]
      }
    ]
  },
  {
    id: "uttara_kannada",
    name_en: "Uttara Kannada",
    name_kn: "ಉತ್ತರ ಕನ್ನಡ",
    taluks: [
      {
        id: "karwar",
        name_en: "Karwar",
        name_kn: "ಕಾರವಾರ",
        villages: [
          { id: "sadashivgad", name_en: "Sadashivgad", name_kn: "ಸದಾಶಿವಗಡ" }
        ]
      },
      {
        id: "sirsi",
        name_en: "Sirsi",
        name_kn: "ಶಿರಸಿ",
        villages: [
          { id: "banavasi", name_en: "Banavasi", name_kn: "ಬನವಾಸಿ" },
          { id: "sampkhanda", name_en: "Sampkhanda", name_kn: "ಸಂಪಖಂಡ" }
        ]
      },
      {
        id: "siddapur",
        name_en: "Siddapur",
        name_kn: "ಸಿದ್ಧಾಪುರ",
        villages: [
          { id: "kolsirsi", name_en: "Kolsirsi", name_kn: "ಕೋಲಶಿರಸಿ" }
        ]
      },
      {
        id: "kumta",
        name_en: "Kumta",
        name_kn: "ಕುಮಟಾ",
        villages: [
          { id: "gokarna", name_en: "Gokarna", name_kn: "ಗೋಕರ್ಣ" },
          { id: "mirjan", name_en: "Mirjan", name_kn: "ಮಿರ್ಜಾನ್" }
        ]
      },
      {
        id: "ankola",
        name_en: "Ankola",
        name_kn: "ಅಂಕೋಲಾ",
        villages: [
          { id: "belekere", name_en: "Belekere", name_kn: "ಬೆಲೆಕೇರಿ" }
        ]
      },
      {
        id: "bhatkal",
        name_en: "Bhatkal",
        name_kn: "ಭಟ್ಕಳ",
        villages: [
          { id: "murudeshwar", name_en: "Murudeshwar", name_kn: "ಮುರುಡೇಶ್ವರ" }
        ]
      },
      {
        id: "honavar",
        name_en: "Honavar",
        name_kn: "ಹೊನ್ನಾವರ",
        villages: [
          { id: "manki", name_en: "Manki", name_kn: "ಮಂಕಿ" }
        ]
      },
      {
        id: "yellapur",
        name_en: "Yellapur",
        name_kn: "ಯಲ್ಲಾಪುರ",
        villages: [
          { id: "manchikere", name_en: "Manchikere", name_kn: "ಮಂಚಿಕೇರಿ" }
        ]
      },
      {
        id: "dandeli",
        name_en: "Dandeli",
        name_kn: "ದಾಂಡೇಲಿ",
        villages: [
          { id: "ambikanagar", name_en: "Ambikanagar", name_kn: "ಅಂಬಿಕಾನಗರ" }
        ]
      },
      {
        id: "haliyal",
        name_en: "Haliyal",
        name_kn: "ಹಳಿಯಾಳ",
        villages: [
          { id: "tergaon", name_en: "Tergaon", name_kn: "ತೆರಗಾಂವ್" }
        ]
      },
      {
        id: "joida",
        name_en: "Joida",
        name_kn: "ಜೋಯಿಡಾ",
        villages: [
          { id: "ramnagar_j", name_en: "Ramnagar", name_kn: "ರಾಮನಗರ" }
        ]
      },
      {
        id: "mundgod",
        name_en: "Mundgod",
        name_kn: "ಮುಂಡಗೋಡು",
        villages: [
          { id: "indoorkatti", name_en: "Indoorkatti", name_kn: "ಇಂದೂರಕಟ್ಟಿ" }
        ]
      }
    ]
  },
  {
    id: "belagavi",
    name_en: "Belagavi",
    name_kn: "ಬೆಳಗಾವಿ",
    taluks: [
      { id: "belagavi_t", name_en: "Belagavi", name_kn: "ಬೆಳಗಾವಿ", villages: [] },
      { id: "gokak", name_en: "Gokak", name_kn: "ಗೋಕಾಕ್", villages: [] },
      { id: "chikkodi", name_en: "Chikkodi", name_kn: "ಚಿಕ್ಕೋಡಿ", villages: [] },
      { id: "athani", name_en: "Athani", name_kn: "ಅಥಣಿ", villages: [] },
      { id: "bailhongal", name_en: "Bailhongal", name_kn: "ಬೈಲಹೊಂಗಲ", villages: [] },
      { id: "saundatti", name_en: "Saundatti", name_kn: "ಸವದತ್ತಿ", villages: [] },
      { id: "ramdurg", name_en: "Ramdurg", name_kn: "ರಾಮದುರ್ಗ", villages: [] },
      { id: "hukkeri", name_en: "Hukkeri", name_kn: "ಹುಕ್ಕೇರಿ", villages: [] },
      { id: "khanapur", name_en: "Khanapur", name_kn: "ಖಾನಾಪುರ", villages: [] },
      { id: "raibag", name_en: "Raibag", name_kn: "ರಾಯಭಾಗ", villages: [] },
      { id: "nipani", name_en: "Nipani", name_kn: "ನಿಪ್ಪಾಣಿ", villages: [] },
      { id: "kagwad", name_en: "Kagwad", name_kn: "ಕಾಗವಾಡ", villages: [] },
      { id: "mudalgi", name_en: "Mudalgi", name_kn: "ಮೂಡಲಗಿ", villages: [] },
      { id: "kittur", name_en: "Kittur", name_kn: "ಕಿತ್ತೂರು", villages: [] }
    ]
  },
  {
    id: "bagalkote",
    name_en: "Bagalkote",
    name_kn: "ಬಾಗಲಕೋಟೆ",
    taluks: [
      { id: "bagalkote_t", name_en: "Bagalkote", name_kn: "ಬಾಗಲಕೋಟೆ", villages: [] },
      { id: "badami", name_en: "Badami", name_kn: "ಬಾದಾಮಿ", villages: [] },
      { id: "hungund", name_en: "Hungund", name_kn: "ಹುನಗುಂದ", villages: [] },
      { id: "jamkhandi", name_en: "Jamkhandi", name_kn: "ಜಮಖಂಡಿ", villages: [] },
      { id: "mudhol", name_en: "Mudhol", name_kn: "ಮುಧೋಳ", villages: [] },
      { id: "bilagi", name_en: "Bilagi", name_kn: "ಬೀಳಗಿ", villages: [] },
      { id: "ilkal", name_en: "Ilkal", name_kn: "ಇಳಕಲ್", villages: [] },
      { id: "rabkavi_banhatti", name_en: "Rabkavi Banhatti", name_kn: "ರಬಕವಿ ಬನಹಟ್ಟಿ", villages: [] },
      { id: "guledgudda", name_en: "Guledgudda", name_kn: "ಗುಳೇದಗುಡ್ಡ", villages: [] }
    ]
  },
  {
    id: "vijayapura",
    name_en: "Vijayapura",
    name_kn: "ವಿಜಯಪುರ",
    taluks: [
      { id: "vijayapura_t", name_en: "Vijayapura", name_kn: "ವಿಜಯಪುರ", villages: [] },
      { id: "basavana_bagewadi", name_en: "Basavana Bagewadi", name_kn: "ಬಸವನ ಬಾಗೇವಾಡಿ", villages: [] },
      { id: "indi", name_en: "Indi", name_kn: "ಇಂಡಿ", villages: [] },
      { id: "muddebihal", name_en: "Muddebihal", name_kn: "ಮುದ್ದೇಬಿಹಾಳ", villages: [] },
      { id: "sindagi", name_en: "Sindagi", name_kn: "ಸಿಂದಗಿ", villages: [] },
      { id: "talikoti", name_en: "Talikoti", name_kn: "ತಾಳಿಕೋಟೆ", villages: [] },
      { id: "chadchan", name_en: "Chadchan", name_kn: "ಚಡಚಣ", villages: [] },
      { id: "kolhar", name_en: "Kolhar", name_kn: "ಕೊಲ್ಹಾರ", villages: [] },
      { id: "nidagundi", name_en: "Nidagundi", name_kn: "ನಿಡಗುಂದಿ", villages: [] },
      { id: "devara_hippargi", name_en: "Devara Hippargi", name_kn: "ದೇವರ ಹಿಪ್ಪರಗಿ", villages: [] }
    ]
  },
  {
    id: "kalaburagi",
    name_en: "Kalaburagi",
    name_kn: "ಕಲಬುರಗಿ",
    taluks: [
      { id: "kalaburagi_t", name_en: "Kalaburagi", name_kn: "ಕಲಬುರಗಿ", villages: [] },
      { id: "afzalpur", name_en: "Afzalpur", name_kn: "ಅಫ್ಜಲಪುರ", villages: [] },
      { id: "aland", name_en: "Aland", name_kn: "ಆಳಂದ", villages: [] },
      { id: "chincholi", name_en: "Chincholi", name_kn: "ಚಿಂಚೋಳಿ", villages: [] },
      { id: "chitapur", name_en: "Chitapur", name_kn: "ಚಿತ್ತಾಪುರ", villages: [] },
      { id: "jewargi", name_en: "Jewargi", name_kn: "ಜೇವರ್ಗಿ", villages: [] },
      { id: "sedam", name_en: "Sedam", name_kn: "ಸೇಡಂ", villages: [] },
      { id: "kamalapur", name_en: "Kamalapur", name_kn: "ಕಮಲಾಪುರ", villages: [] },
      { id: "shahabad", name_en: "Shahabad", name_kn: "ಶಹಾಬಾದ್", villages: [] },
      { id: "yadrami", name_en: "Yadrami", name_kn: "ಯಡ್ರಾಮಿ", villages: [] },
      { id: "kalagi", name_en: "Kalagi", name_kn: "ಕಾಳಗಿ", villages: [] }
    ]
  },
  {
    id: "bidar",
    name_en: "Bidar",
    name_kn: "ಬೀದರ್",
    taluks: [
      { id: "bidar_t", name_en: "Bidar", name_kn: "ಬೀದರ್", villages: [] },
      { id: "basavakalyan", name_en: "Basavakalyan", name_kn: "ಬಸವಕಲ್ಯಾಣ", villages: [] },
      { id: "bhalki", name_en: "Bhalki", name_kn: "ಭಾಲ್ಕಿ", villages: [] },
      { id: "homnabad", name_en: "Humnabad", name_kn: "ಹುಮ್ನಾಬಾದ್", villages: [] },
      { id: "aurad", name_en: "Aurad", name_kn: "ಔರಾದ್", villages: [] },
      { id: "hulsoor", name_en: "Hulsoor", name_kn: "ಹುಲಸೂರು", villages: [] },
      { id: "chitguppa", name_en: "Chitguppa", name_kn: "ಚಿಟಗುಪ್ಪ", villages: [] },
      { id: "kamalnagar", name_en: "Kamalnagar", name_kn: "ಕಮಲನಗರ", villages: [] }
    ]
  },
  {
    id: "raichur",
    name_en: "Raichur",
    name_kn: "ರಾಯಚೂರು",
    taluks: [
      { id: "raichur_t", name_en: "Raichur", name_kn: "ರಾಯಚೂರು", villages: [] },
      { id: "manvi", name_en: "Manvi", name_kn: "ಮಾನ್ವಿ", villages: [] },
      { id: "sindhanur", name_en: "Sindhanur", name_kn: "ಸಿಂಧನೂರು", villages: [] },
      { id: "devadurga", name_en: "Devadurga", name_kn: "ದೇವದುರ್ಗ", villages: [] },
      { id: "lingasugur", name_en: "Lingasugur", name_kn: "ಲಿಂಗಸುಗೂರು", villages: [] },
      { id: "maski", name_en: "Maski", name_kn: "ಮಸ್ಕಿ", villages: [] },
      { id: "sirwar", name_en: "Sirwar", name_kn: "ಸಿರವಾರ", villages: [] }
    ]
  },
  {
    id: "koppal",
    name_en: "Koppal",
    name_kn: "ಕೊಪ್ಪಳ",
    taluks: [
      { id: "koppal_t", name_en: "Koppal", name_kn: "ಕೊಪ್ಪಳ", villages: [] },
      { id: "gangavathi", name_en: "Gangavathi", name_kn: "ಗಂಗಾವತಿ", villages: [] },
      { id: "kushtagi", name_en: "Kushtagi", name_kn: "ಕುಷ್ಟಗಿ", villages: [] },
      { id: "yelburga", name_en: "Yelburga", name_kn: "ಯಲಬುರ್ಗಾ", villages: [] },
      { id: "kanakagiri", name_en: "Kanakagiri", name_kn: "ಕನಕಗಿರಿ", villages: [] },
      { id: "karatagi", name_en: "Karatagi", name_kn: "ಕಾರಟಗಿ", villages: [] },
      { id: "kukanur", name_en: "Kukanur", name_kn: "ಕುಕನೂರು", villages: [] }
    ]
  },
  {
    id: "gadag",
    name_en: "Gadag",
    name_kn: "ಗದಗ",
    taluks: [
      { id: "gadag_t", name_en: "Gadag", name_kn: "ಗದಗ", villages: [] },
      { id: "ron", name_en: "Ron", name_kn: "ರೋಣ", villages: [] },
      { id: "shirhatti", name_en: "Shirhatti", name_kn: "ಶಿರಾಹಟ್ಟಿ", villages: [] },
      { id: "nargund", name_en: "Nargund", name_kn: "ನರಗುಂದ", villages: [] },
      { id: "mundargi", name_en: "Mundargi", name_kn: "ಮುಂಡರಗಿ", villages: [] },
      { id: "gajendragad", name_en: "Gajendragad", name_kn: "ಗಜೇಂದ್ರಗಡ", villages: [] },
      { id: "laxmeshwar", name_en: "Laxmeshwar", name_kn: "ಲಕ್ಷ್ಮೇಶ್ವರ", villages: [] }
    ]
  },
  {
    id: "dharwad",
    name_en: "Dharwad",
    name_kn: "ಧಾರವಾಡ",
    taluks: [
      { id: "dharwad_t", name_en: "Dharwad", name_kn: "ಧಾರವಾಡ", villages: [] },
      { id: "hubballi_urban", name_en: "Hubballi Urban", name_kn: "ಹುಬ್ಬಳ್ಳಿ ನಗರ", villages: [] },
      { id: "hubballi_rural", name_en: "Hubballi Rural", name_kn: "ಹುಬ್ಬಳ್ಳಿ ಗ್ರಾಮೀಣ", villages: [] },
      { id: "kalghatgi", name_en: "Kalghatgi", name_kn: "ಕಲಘಟಗಿ", villages: [] },
      { id: "navalgund", name_en: "Navalgund", name_kn: "ನವಲಗುಂದ", villages: [] },
      { id: "kundgol", name_en: "Kundgol", name_kn: "ಕುಂದಗೋಳ", villages: [] },
      { id: "alnavar", name_en: "Alnavar", name_kn: "ಅಳ್ನಾವರ", villages: [] },
      { id: "annigeri", name_en: "Annigeri", name_kn: "ಅಣ್ಣಿಗೇರಿ", villages: [] }
    ]
  },
  {
    id: "haveri",
    name_en: "Haveri",
    name_kn: "ಹಾವೇರಿ",
    taluks: [
      { id: "haveri_t", name_en: "Haveri", name_kn: "ಹಾವೇರಿ", villages: [] },
      { id: "byadgi", name_en: "Byadgi", name_kn: "ಬ್ಯಾಡಗಿ", villages: [] },
      { id: "ranibennur", name_en: "Ranebennur", name_kn: "ರಾಣೆಬೆನ್ನೂರು", villages: [] },
      { id: "hirekerur", name_en: "Hirekerur", name_kn: "ಹಿರೇಕೆರೂರು", villages: [] },
      { id: "shiggaon", name_en: "Shiggaon", name_kn: "ಶಿಗ್ಗಾಂವಿ", villages: [] },
      { id: "hangal", name_en: "Hangal", name_kn: "ಹಾನಗಲ್", villages: [] },
      { id: "savanur", name_en: "Savanur", name_kn: "ಸವಣೂರು", villages: [] },
      { id: "rattihalli", name_en: "Rattihalli", name_kn: "ರಟ್ಟಿಹಳ್ಳಿ", villages: [] }
    ]
  },
  {
    id: "davanagere",
    name_en: "Davanagere",
    name_kn: "ದಾವಣಗೆರೆ",
    taluks: [
      { id: "davanagere_t", name_en: "Davanagere", name_kn: "ದಾವಣಗೆರೆ", villages: [] },
      { id: "harihara", name_en: "Harihara", name_kn: "ಹರಿಹರ", villages: [] },
      { id: "honnali", name_en: "Honnali", name_kn: "ಹೊನ್ನಾಳಿ", villages: [] },
      { id: "channagiri", name_en: "Channagiri", name_kn: "ಚನ್ನಗಿರಿ", villages: [] },
      { id: "jagalur", name_en: "Jagalur", name_kn: "ಜಗಳೂರು", villages: [] },
      { id: "nyamathi", name_en: "Nyamathi", name_kn: "ನ್ಯಾಮತಿ", villages: [] }
    ]
  },
  {
    id: "chitradurga",
    name_en: "Chitradurga",
    name_kn: "ಚಿತ್ರದುರ್ಗ",
    taluks: [
      { id: "chitradurga_t", name_en: "Chitradurga", name_kn: "ಚಿತ್ರದುರ್ಗ", villages: [] },
      { id: "challakere", name_en: "Challakere", name_kn: "ಚಳ್ಳಕೆರೆ", villages: [] },
      { id: "hiriyur", name_en: "Hiriyur", name_kn: "ಹಿರಿಯೂರು", villages: [] },
      { id: "holalkere", name_en: "Holalkere", name_kn: "ಹೊಳಲ್ಕೆರೆ", villages: [] },
      { id: "hosadurga", name_en: "Hosadurga", name_kn: "ಹೊಸದುರ್ಗ", villages: [] },
      { id: "molakalmuru", name_en: "Molakalmuru", name_kn: "ಮೊಳಕಾಲ್ಮೂರು", villages: [] }
    ]
  },
  {
    id: "tumakuru",
    name_en: "Tumakuru",
    name_kn: "ತುಮಕೂರು",
    taluks: [
      { id: "tumakuru_t", name_en: "Tumakuru", name_kn: "ತುಮಕೂರು", villages: [] },
      { id: "gubbi", name_en: "Gubbi", name_kn: "ಗುಬ್ಬಿ", villages: [] },
      { id: "kunigal", name_en: "Kunigal", name_kn: "ಕುಣಿಗಲ್", villages: [] },
      { id: "sira", name_en: "Sira", name_kn: "ಶಿರಾ", villages: [] },
      { id: "tiptur", name_en: "Tiptur", name_kn: "ತಿಪಟೂರು", villages: [] },
      { id: "chikkanayakanahalli", name_en: "C.N. Halli", name_kn: "ಚಿ.ನಾ. ಹಳ್ಳಿ", villages: [] },
      { id: "madhugiri", name_en: "Madhugiri", name_kn: "ಮಧುಗಿರಿ", villages: [] },
      { id: "pavagada", name_en: "Pavagada", name_kn: "ಪಾವಗಡ", villages: [] },
      { id: "koratagere", name_en: "Koratagere", name_kn: "ಕೊರಟಗೆರೆ", villages: [] },
      { id: "turuvekere", name_en: "Turuvekere", name_kn: "ತುರುವೇಕೆರೆ", villages: [] }
    ]
  },
  {
    id: "bengaluru_urban",
    name_en: "Bengaluru Urban",
    name_kn: "ಬೆಂಗಳೂರು ನಗರ",
    taluks: [
      { id: "bengaluru_north", name_en: "Bengaluru North", name_kn: "ಬೆಂಗಳೂರು ಉತ್ತರ", villages: [] },
      { id: "bengaluru_south", name_en: "Bengaluru South", name_kn: "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ", villages: [] },
      { id: "bengaluru_east", name_en: "Bengaluru East", name_kn: "ಬೆಂಗಳೂರು ಪೂರ್ವ", villages: [] },
      { id: "anekal", name_en: "Anekal", name_kn: "ಆನೇಕಲ್", villages: [] },
      { id: "yelahankan", name_en: "Yelahanka", name_kn: "ಯಲಹಂಕ", villages: [] }
    ]
  },
  {
    id: "bengaluru_rural",
    name_en: "Bengaluru Rural",
    name_kn: "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ",
    taluks: [
      { id: "devanahalli", name_en: "Devanahalli", name_kn: "ದೇವನಹಳ್ಳಿ", villages: [] },
      { id: "doddaballapur", name_en: "Doddaballapur", name_kn: "ದೊಡ್ಡಬಳ್ಳಾಪುರ", villages: [] },
      { id: "hosakote", name_en: "Hosakote", name_kn: "ಹೊಸಕೋಟೆ", villages: [] },
      { id: "nelamangala", name_en: "Nelamangala", name_kn: "ನೆಲಮಂಗಲ", villages: [] }
    ]
  },
  {
    id: "ramanagara",
    name_en: "Ramanagara",
    name_kn: "ರಾಮನಗರ",
    taluks: [
      { id: "ramanagara_t", name_en: "Ramanagara", name_kn: "ರಾಮನಗರ", villages: [] },
      { id: "channapatna", name_en: "Channapatna", name_kn: "ಚನ್ನಪಟ್ಟಣ", villages: [] },
      { id: "magadi", name_en: "Magadi", name_kn: "ಮಾಗಡಿ", villages: [] },
      { id: "kanakapura", name_en: "Kanakapura", name_kn: "ಕನಕಪುರ", villages: [] },
      { id: "harohalli", name_en: "Harohalli", name_kn: "ಹಾರೋಹಳ್ಳಿ", villages: [] }
    ]
  },
  {
    id: "kolar",
    name_en: "Kolar",
    name_kn: "ಕೋಲಾರ",
    taluks: [
      { id: "kolar_t", name_en: "Kolar", name_kn: "ಕೋಲಾರ", villages: [] },
      { id: "bangalpet", name_en: "Bangarapet", name_kn: "ಬಂಗಾರಪೇಟೆ", villages: [] },
      { id: "malur", name_en: "Malur", name_kn: "ಮಾಲೂರು", villages: [] },
      { id: "mulbagal", name_en: "Mulbagal", name_kn: "ಮುಳಬಾಗಿಲು", villages: [] },
      { id: "srinivaspur", name_en: "Srinivaspur", name_kn: "ಶ್ರೀನಿವಾಸಪುರ", villages: [] },
      { id: "kgf", name_en: "K.G.F.", name_kn: "ಕೆ.ಜಿ.ಎಫ್.", villages: [] }
    ]
  },
  {
    id: "chikkaballapur",
    name_en: "Chikkaballapur",
    name_kn: "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
    taluks: [
      { id: "chikkaballapur_t", name_en: "Chikkaballapur", name_kn: "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", villages: [] },
      { id: "bagepalli", name_en: "Bagepalli", name_kn: "ಬಾಗೇಪಲ್ಲಿ", villages: [] },
      { id: "chintamani", name_en: "Chintamani", name_kn: "ಚಿಂತಾಮಣಿ", villages: [] },
      { id: "gauribidanur", name_en: "Gauribidanur", name_kn: "ಗೌರಿಬಿದನೂರು", villages: [] },
      { id: "sidlaghatta", name_en: "Sidlaghatta", name_kn: "ಶಿಡ್ಲಘಟ್ಟ", villages: [] },
      { id: "gudibande", name_en: "Gudibande", name_kn: "ಗುಡಿಬಂಡೆ", villages: [] },
      { id: "manchenahalli", name_en: "Manchenahalli", name_kn: "ಮಂಚೇನಹಳ್ಳಿ", villages: [] }
    ]
  },
  {
    id: "chamarajanagar",
    name_en: "Chamarajanagar",
    name_kn: "ಚಾಮರಾಜನಗರ",
    taluks: [
      { id: "chamarajanagar_t", name_en: "Chamarajanagar", name_kn: "ಚಾಮರಾಜನಗರ", villages: [] },
      { id: "gundlupet", name_en: "Gundlupet", name_kn: "ಗುಂಡ್ಲುಪೇಟೆ", villages: [] },
      { id: "kollegal", name_en: "Kollegal", name_kn: "ಕೊಳ್ಳೇಗಾಲ", villages: [] },
      { id: "yelandur", name_en: "Yelandur", name_kn: "ಯಳಂದೂರು", villages: [] },
      { id: "hanur", name_en: "Hanur", name_kn: "ಹನೂರು", villages: [] }
    ]
  },
  {
    id: "kodagu",
    name_en: "Kodagu",
    name_kn: "ಕೊಡಗು",
    taluks: [
      { id: "madikeri", name_en: "Madikeri", name_kn: "ಮಡಿಕೇರಿ", villages: [] },
      { id: "virajpet", name_en: "Virajpet", name_kn: "ವಿರಾಜಪೇಟೆ", villages: [] },
      { id: "somwarpet", name_en: "Somwarpet", name_kn: "ಸೋಮವಾರಪೇಟೆ", villages: [] },
      { id: "kushalnagar", name_en: "Kushalnagar", name_kn: "ಕುಶಾಲನಗರ", villages: [] },
      { id: "ponnampet", name_en: "Ponnampet", name_kn: "ಪೊನ್ನಂಪೇಟೆ", villages: [] }
    ]
  },
  {
    id: "ballari",
    name_en: "Ballari",
    name_kn: "ಬಳ್ಳಾರಿ",
    taluks: [
      { id: "ballari_t", name_en: "Ballari", name_kn: "ಬಳ್ಳಾರಿ", villages: [] },
      { id: "siruguppa", name_en: "Siruguppa", name_kn: "ಸಿರುಗುಪ್ಪ", villages: [] },
      { id: "sandur", name_en: "Sandur", name_kn: "ಸಂಡೂರು", villages: [] },
      { id: "kampli", name_en: "Kampli", name_kn: "ಕಂಪ್ಲಿ", villages: [] },
      { id: "kurugodu", name_en: "Kurugodu", name_kn: "ಕುರುಗೋಡು", villages: [] }
    ]
  },
  {
    id: "vijayanagara",
    name_en: "Vijayanagara",
    name_kn: "ವಿಜಯನಗರ",
    taluks: [
      { id: "hosapete", name_en: "Hosapete", name_kn: "ಹೊಸಪೇಟೆ", villages: [] },
      { id: "kudligi", name_en: "Kudligi", name_kn: "ಕೂಡ್ಲಿಗಿ", villages: [] },
      { id: "hagaribommanahalli", name_en: "H.B. Halli", name_kn: "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", villages: [] },
      { id: "harapanahalli", name_en: "Harapanahalli", name_kn: "ಹರಪನಹಳ್ಳಿ", villages: [] },
      { id: "hadagali", name_en: "Hoovina Hadagali", name_kn: "ಹೂವಿನ ಹಡಗಲಿ", villages: [] },
      { id: "kotturu", name_en: "Kotturu", name_kn: "ಕೊಟ್ಟೂರು", villages: [] }
    ]
  },
  {
    id: "yadgir",
    name_en: "Yadgir",
    name_kn: "ಯಾದಗಿರಿ",
    taluks: [
      { id: "yadgir_t", name_en: "Yadgir", name_kn: "ಯಾದಗಿರಿ", villages: [] },
      { id: "shahapur", name_en: "Shahapur", name_kn: "ಶಹಾಪುರ", villages: [] },
      { id: "shorapur", name_en: "Shorapur", name_kn: "ಶೋರಾಪುರ", villages: [] },
      { id: "hunsagi", name_en: "Hunsagi", name_kn: "ಹುಣಸಗಿ", villages: [] },
      { id: "vadagera", name_en: "Vadagera", name_kn: "ವಡಗೇರಾ", villages: [] },
      { id: "gurmitkal", name_en: "Gurmitkal", name_kn: "ಗುರ್ಮಿಟ್ಕಲ್", villages: [] }
    ]
  }
];

