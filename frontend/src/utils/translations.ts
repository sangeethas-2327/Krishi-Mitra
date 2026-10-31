export interface TranslationBundle {
  appName: string;
  tagline: string;
  startSpeaking: string;
  stopSpeaking: string;
  recording: string;
  processingAudio: string;
  typeMessagePlaceholder: string;
  send: string;
  clearSession: string;
  farmerProfileTitle: string;
  extractedDetails: string;
  confirmed: string;
  unknown: string;
  needsClarification: string;
  district: string;
  taluk: string;
  village: string;
  landArea: string;
  crops: string;
  ownership: string;
  season: string;
  irrigation: string;
  needs: string;
  recommendedSchemes: string;
  allSchemes: string;
  realSchemeBadge: string;
  demoSchemeBadge: string;
  satisfied: string;
  unsatisfied: string;
  rulesRequiringCheck: string;
  viewDetails: string;
  close: string;
  benefits: string;
  documentsRequired: string;
  applicationSteps: string;
  officialSource: string;
  disclaimerText: string;
  readAloud: string;
  editProfile: string;
  saveChanges: string;
  demoModeNotice: string;
  readinessTitle: string;
  readyToApply: string;
  pendingSteps: string;
  compareSchemes: string;
  compareTitle: string;
  comparisonMatrix: string;
  whyNeeded: string;
  sourceProvenance: string;
  userStated: string;
  inferred: string;
  userEdited: string;
  mandatoryDocs: string;
  optionalDocs: string;
  prerequisitesTitle: string;
  closeComparison: string;
  navDiscover: string;
  navVoiceStudio: string;
  navMyFarm: string;
  navSchemes: string;
  navJourney: string;
  heroHeadline: string;
  heroSubtitle: string;
  startConversation: string;
  exploreSchemes: string;
  livingCompanion: string;
}

export const translations: Record<'kn' | 'en', TranslationBundle> = {
  kn: {
    appName: "ಕೃಷಿ ಮಿತ್ರ",
    tagline: "ನಿಮ್ಮ ಕೃಷಿ. ನಿಮ್ಮ ಧ್ವನಿ. ನಿಮ್ಮ ಅವಕಾಶಗಳು.",
    livingCompanion: "ದ ಲಿವಿಂಗ್ ಫಾರ್ಮ್ ಕಂಪ್ಯಾನಿಯನ್",
    navDiscover: "ಮುಖ್ಯಪುಟ",
    navVoiceStudio: "ಧ್ವನಿ ಸ್ಟುಡಿಯೋ",
    navMyFarm: "ನನ್ನ ಕೃಷಿ",
    navSchemes: "ಯೋಜನಾ ಜ್ಞಾನ",
    navJourney: "ಅರ್ಜಿ ಪಯಣ",
    heroHeadline: "ನಿಮ್ಮ ಕೃಷಿಗೆ, ನಿಮ್ಮ ಧ್ವನಿಯಲ್ಲಿ ಸಹಾಯ",
    heroSubtitle: "ನೈಸರ್ಗಿಕವಾಗಿ ಮಾತನಾಡಿ. ಸೂಕ್ತ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳನ್ನು ಕಂಡುಕೊಳ್ಳಿ. ನಿಮ್ಮ ಮುಂದಿನ ಹೆಜ್ಜೆಯನ್ನು ಸುಲಭವಾಗಿ ತಿಳಿಯಿರಿ.",
    startConversation: "ಧ್ವನಿ ಸಂಭಾಷಣೆ ಪ್ರಾರಂಭಿಸಿ",
    exploreSchemes: "ಯೋಜನೆಗಳನ್ನು ಅನ್ವೇಷಿಸಿ",
    startSpeaking: "ಮಾತನಾಡಲು ಒತ್ತಿ",
    stopSpeaking: "ನಿಲ್ಲಿಸಿ",
    recording: "ಕೇಳಿಸಿಕೊಳ್ಳುತ್ತಿದ್ದೇವೆ...",
    processingAudio: "ಧ್ವನಿಯನ್ನು ಪರಿವರ್ತಿಸಲಾಗುತ್ತಿದೆ...",
    typeMessagePlaceholder: "ಇಲ್ಲಿ ಸಂದೇಶ ಟೈಪ್ ಮಾಡಿ ಅಥವಾ ಮೈಕ್ ಬಳಸಿ...",
    send: "ಕಳುಹಿಸಿ",
    clearSession: "ಹೊಸ ಸಂಭಾಷಣೆ",
    farmerProfileTitle: "ನಿಮ್ಮ ಕೃಷಿ ವಿವರಗಳು (ರೈತರ ಪ್ರೊಫೈಲ್)",
    extractedDetails: "ದೃಢೀಕರಿಸಿದ ಮಾಹಿತಿ",
    confirmed: "ದೃಢೀಕರಿಸಲಾಗಿದೆ",
    unknown: "ಮಾಹಿತಿ ಅಗತ್ಯವಿದೆ",
    needsClarification: "ಸ್ಪಷ್ಟೀಕರಣ ಬೇಕು",
    district: "ಜಿಲ್ಲೆ",
    taluk: "ತಾಲೂಕು",
    village: "ಗ್ರಾಮ",
    landArea: "ಭೂಮಿ ವಿಸ್ತೀರ್ಣ",
    crops: "ಬೆಳೆಗಳು",
    ownership: "ಭೂಮಿ ಹಕ್ಕು",
    season: "ಹಂಗಾಮು",
    irrigation: "ನೀರಾವರಿ ಸೌಲಭ್ಯ",
    needs: "ಅಗತ್ಯವಿರುವ ನೆರವು",
    recommendedSchemes: "ನಿಮಗೆ ಸರಿಹೊಂದುವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
    allSchemes: "ಎಲ್ಲಾ ಯೋಜನೆಗಳು",
    realSchemeBadge: "ಅಧಿಕೃತ ಸರ್ಕಾರಿ ಯೋಜನೆ",
    demoSchemeBadge: "ಪ್ರಾಯೋಗಿಕ ಪ್ರದರ್ಶನ (ಡೆಮೊ)",
    satisfied: "ಪೂರೈಸಿದ ಷರತ್ತುಗಳು",
    unsatisfied: "ಹೊಂದಿಕೆಯಾಗದ ಷರತ್ತುಗಳು",
    rulesRequiringCheck: "ಪರಿಶೀಲಿಸಬೇಕಾದ ಅಂಶಗಳು",
    viewDetails: "ವಿವರ ಮತ್ತು ಅರ್ಜಿ ಮಾರ್ಗದರ್ಶಿ",
    close: "ಮುಚ್ಚಿ",
    benefits: "ಯೋಜನೆಯ ಪ್ರಯೋಜನಗಳು",
    documentsRequired: "ಅಗತ್ಯ ದಾಖಲೆಗಳು",
    applicationSteps: "ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಹಂತಗಳು",
    officialSource: "ಅಧಿಕೃತ ಪೋರ್ಟಲ್",
    disclaimerText: "ಗಮನಿಸಿ: ಇದು ಪ್ರಾಥಮಿಕ ಅರ್ಹತಾ ಮಾರ್ಗದರ್ಶಿಯಾಗಿದೆ. ಅಂತಿಮ ಅನುಮೋದನೆ ಸಂಬಂಧಪಟ್ಟ ಕೃಷಿ ಇಲಾಖೆಯ ಅಧಿಕೃತ ಪರಿಶೀಲನೆಗೆ ಒಳಪಟ್ಟಿರುತ್ತದೆ.",
    readAloud: "ಕೇಳಿ (ಧ್ವನಿ)",
    editProfile: "ವಿವರ ತಿದ್ದುಪಡಿ",
    saveChanges: "ಉಳಿಸಿ",
    demoModeNotice: "ಡೆಮೊ ಮೋಡ್: ಸರ್ವರ್ ನೇರ ಎಪಿಐ ರಹಿತವಾಗಿಯೂ ನೈಜ ನಿಯಮಗಳ ಮೂಲಕ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ.",
    readinessTitle: "ಅರ್ಜಿ ಸಿದ್ಧತಾ ಪಟ್ಟಿ",
    readyToApply: "ಸಿದ್ಧವಿರುವ ದಾಖಲೆಗಳು",
    pendingSteps: "ಬಾಕಿ ಇರುವ ಕ್ರಮಗಳು",
    compareSchemes: "ಯೋಜನೆಗಳ ಹೋಲಿಕೆ",
    compareTitle: "ಸರ್ಕಾರಿ ಮತ್ತು ಪ್ರಾಯೋಗಿಕ ಯೋಜನೆಗಳ ಸಮಗ್ರ ಹೋಲಿಕೆ",
    comparisonMatrix: "ಹೋಲಿಕಾ ಕೋಷ್ಟಕ",
    whyNeeded: "ಯಾತಕ್ಕಾಗಿ ಈ ಮಾಹಿತಿ ಬೇಕು?",
    sourceProvenance: "ಮಾಹಿತಿಯ ಮೂಲ",
    userStated: "ರೈತರು ತಿಳಿಸಿದ್ದು",
    inferred: "ಸ್ವಯಂ ಗುರುತಿಸಿದ್ದು",
    userEdited: "ತಿದ್ದಿ ನಮೂದಿಸಿದ್ದು",
    mandatoryDocs: "ಕಡ್ಡಾಯ ದಾಖಲೆಗಳು",
    optionalDocs: "ಐಚ್ಛಿಕ ದಾಖಲೆಗಳು",
    prerequisitesTitle: "ಪೂರ್ವಭಾವಿ ಅರ್ಹತಾ ಕ್ರಮಗಳು",
    closeComparison: "ಹೋಲಿಕೆ ಮುಚ್ಚಿ"
  },
  en: {
    appName: "Krishi Mitra",
    tagline: "Your farm. Your voice. Your opportunities.",
    startSpeaking: "Tap to Speak",
    stopSpeaking: "Stop Recording",
    recording: "Listening...",
    processingAudio: "Processing audio...",
    typeMessagePlaceholder: "Type in Kannada or English, or use the microphone...",
    send: "Send",
    clearSession: "Reset Session",
    farmerProfileTitle: "Your Agricultural Profile",
    extractedDetails: "Extracted Information",
    confirmed: "Confirmed",
    unknown: "Missing / Needed",
    needsClarification: "Needs Clarification",
    district: "District",
    taluk: "Taluk",
    village: "Village",
    landArea: "Land Area",
    crops: "Crops",
    ownership: "Ownership",
    season: "Season",
    irrigation: "Irrigation Facilities",
    needs: "Assistance Need",
    recommendedSchemes: "Recommended Government Schemes",
    allSchemes: "All Schemes",
    realSchemeBadge: "Official Government Scheme",
    demoSchemeBadge: "Demonstration Only (Demo)",
    satisfied: "Satisfied Conditions",
    unsatisfied: "Unsatisfied Conditions",
    rulesRequiringCheck: "Needs Verification",
    viewDetails: "View Details & Guidance",
    close: "Close",
    benefits: "Scheme Benefits",
    documentsRequired: "Required Documents",
    applicationSteps: "Application Process",
    officialSource: "Official Portal",
    disclaimerText: "Notice: Recommendations are preliminary. Final official approval rests with the designated government authority.",
    readAloud: "Listen",
    editProfile: "Edit Profile",
    saveChanges: "Save Changes",
    demoModeNotice: "Demo Mode: Operating with verified eligibility checks & offline speech fallback.",
    readinessTitle: "Application Readiness Checklist",
    readyToApply: "Ready / Confirmed",
    pendingSteps: "Pending Actions",
    compareSchemes: "Compare Schemes",
    compareTitle: "Side-by-Side Scheme Comparison",
    comparisonMatrix: "Comparison Matrix",
    whyNeeded: "Why is this required?",
    sourceProvenance: "Data Source",
    userStated: "Farmer Stated",
    inferred: "Inferred",
    userEdited: "User Edited",
    mandatoryDocs: "Mandatory Documents",
    optionalDocs: "Optional Documents",
    prerequisitesTitle: "Prerequisites & Verification",
    closeComparison: "Close Comparison",
    livingCompanion: "The Living Farm Companion",
    navDiscover: "Discover",
    navVoiceStudio: "Voice Studio",
    navMyFarm: "My Farm",
    navSchemes: "Scheme Intelligence",
    navJourney: "Application Journey",
    heroHeadline: "Support for your farming, in your own voice.",
    heroSubtitle: "Talk naturally in Kannada. Discover relevant government schemes. Understand your next step clearly.",
    startConversation: "Open Voice Studio",
    exploreSchemes: "Explore Schemes"
  }
};
