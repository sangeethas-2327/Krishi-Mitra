export interface Location {
  state?: string | null;
  district?: string | null;
  taluk?: string | null;
  village?: string | null;
}

export interface LandArea {
  value?: number | null;
  unit?: string | null;
  value_acres?: number | null;
}

export interface IrrigationInfo {
  has_irrigation?: boolean | null;
  source?: string | null;
  type?: string | null;
}

export interface FieldMetadata {
  field_name: string;
  value: any;
  confidence: number;
  confirmation_status: 'confirmed' | 'unconfirmed' | 'needs_clarification' | 'disputed';
  source: string;
  last_updated?: string | null;
  previous_values: any[];
}

export interface FarmerProfile {
  location: Location;
  land_area: LandArea;
  crops: string[];
  ownership?: string | null;
  season?: string | null;
  irrigation?: IrrigationInfo;
  assistance_needs: string[];
  additional_details: Record<string, any>;
  field_confidence: Record<string, number>;
  confirmed_fields: string[];
  unknown_fields: string[];
  conflict_fields?: Record<string, any[]>;
  fields_metadata?: Record<string, FieldMetadata>;
}

export type CriterionStatus = 'SATISFIED' | 'NOT_SATISFIED' | 'UNKNOWN' | 'NEEDS_VERIFICATION';

export type SchemeStatus = 
  | 'POTENTIALLY_SUITABLE' 
  | 'NOT_SUITABLE_BASED_ON_KNOWN_RULES' 
  | 'INSUFFICIENT_INFORMATION' 
  | 'REQUIRES_OFFICIAL_VERIFICATION';

export interface EligibilityRule {
  rule_id: string;
  description: string;
  description_kn?: string;
  field: string;
  operator: string;
  expected_value: any;
  is_mandatory: boolean;
  source_reference?: string;
  verification_status: string;
  clarification_question?: string;
  clarification_question_kn?: string;
  why_needed?: string;
  why_needed_kn?: string;
  sub_rules?: EligibilityRule[];
  logical_operator?: string;
}

export interface RuleEvaluationResult {
  rule_id: string;
  description: string;
  description_kn?: string;
  field: string;
  status: CriterionStatus;
  expected_value: any;
  actual_value: any;
  is_mandatory: boolean;
  source_reference?: string;
  reason: string;
  reason_kn?: string;
  clarification_question?: string;
  clarification_question_kn?: string;
  why_needed?: string;
  why_needed_kn?: string;
  sub_evaluations?: RuleEvaluationResult[];
}

export interface SchemeRecord {
  id: string;
  name: string;
  name_kn?: string;
  official_abbreviation?: string;
  government_level?: string;
  scheme_type: 'real' | 'demonstration';
  category: string;
  category_kn?: string;
  assistance_type?: string;
  status_label?: string;
  status_label_kn?: string;
  description: string;
  description_kn?: string;
  benefits: string[];
  benefits_kn?: string[];
  eligibility_rules: EligibilityRule[];
  required_documents: string[];
  required_documents_kn?: string[];
  optional_documents?: string[];
  optional_documents_kn?: string[];
  application_steps: string[];
  application_steps_kn?: string[];
  official_source_url?: string | null;
  issuing_authority?: string | null;
  verification_authority?: string | null;
  last_verified_at?: string | null;
  verification_status: string;
  applicable_locations: string[];
  supported_crops: string[];
  notes: string[];
  notes_kn?: string[];
}

export interface SchemeMatchResult {
  scheme: SchemeRecord;
  evaluation_status: SchemeStatus;
  score: number;
  satisfied_rules: RuleEvaluationResult[];
  unsatisfied_rules: RuleEvaluationResult[];
  unknown_rules: RuleEvaluationResult[];
  needs_verification_rules: RuleEvaluationResult[];
  match_reason: string;
  match_reason_kn?: string;
  next_clarification_question?: string;
  next_clarification_question_kn?: string;
}

export interface ChecklistItem {
  item_id: string;
  title: string;
  title_kn?: string;
  category: string;
  is_mandatory: boolean;
  is_completed: boolean;
  evidence_found?: string | null;
  help_text?: string | null;
  help_text_kn?: string | null;
}

export interface SchemeReadinessChecklist {
  scheme_id: string;
  scheme_name: string;
  scheme_name_kn?: string;
  scheme_type: string;
  official_source_url?: string | null;
  completion_percentage: number;
  mandatory_ready_count: number;
  mandatory_total_count: number;
  items: ChecklistItem[];
  next_steps: string[];
  next_steps_kn: string[];
  disclaimer: string;
  disclaimer_kn: string;
}

export interface SchemeComparisonItem {
  scheme_id: string;
  name: string;
  name_kn?: string;
  government_level?: string;
  scheme_type: string;
  category: string;
  category_kn?: string;
  assistance_type?: string;
  purpose: string;
  purpose_kn?: string;
  target_beneficiaries: string;
  target_beneficiaries_kn?: string;
  key_eligibility: string[];
  key_eligibility_kn: string[];
  benefits_summary: string[];
  benefits_summary_kn: string[];
  required_documents: string[];
  required_documents_kn: string[];
  application_mode: string;
  application_mode_kn?: string;
  official_url?: string | null;
  verification_status: string;
  status_label?: string | null;
  status_label_kn?: string | null;
  application_steps?: string[];
  application_steps_kn?: string[];
  issuing_authority?: string | null;
  verification_authority?: string | null;
}

export interface SchemeComparisonResponse {
  schemes: SchemeComparisonItem[];
  comparison_matrix: Record<string, Record<string, any>>;
  disclaimer: string;
  disclaimer_kn: string;
}

export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  content_kn?: string;
  content_en?: string;
  audio_url?: string;
  audio_base64?: string;
  voice_provider?: string;
  created_at: string;
  isError?: boolean;
  retryText?: string;
  llm_provider?: string;
}

export interface ChatResponse {
  session_id: string;
  response_text: string;
  response_text_kn?: string;
  response_text_en?: string;
  audio_url?: string;
  audio_base64?: string;
  voice_provider?: string;
  updated_profile: FarmerProfile;
  next_question?: string;
  next_question_kn?: string;
  conversation_status: string;
  recommendations: SchemeMatchResult[];
  source_references: string[];
  uncertainty_notes: string[];
  llm_provider?: string;
  is_fallback?: boolean;
  explained_schemes?: string[];
}

export interface HourlyForecastItem {
  time: string;
  temperature: number;
  weather_code: number;
  weather_desc: string;
  weather_desc_kn: string;
  precipitation_prob: number;
  is_day: boolean;
}

export interface DailyForecastItem {
  date: string;
  day_name: string;
  day_name_kn: string;
  min_temp: number;
  max_temp: number;
  weather_code: number;
  weather_desc: string;
  weather_desc_kn: string;
  precipitation_prob: number;
}

export interface AgronomicInsight {
  alert_level: 'optimal' | 'advisory' | 'warning';
  title: string;
  title_kn: string;
  advice: string;
  advice_kn: string;
}

export interface FarmWeatherResponse {
  location_name: string;
  location_name_kn: string;
  precision_level: 'village' | 'taluk' | 'district' | 'state_default';
  precision_label: string;
  precision_label_kn: string;
  latitude: number;
  longitude: number;
  current_temp: number;
  feels_like: number;
  humidity: number;
  wind_speed: number;
  wind_direction: string;
  wind_direction_kn: string;
  precipitation: number;
  precipitation_prob: number;
  cloud_cover: number;
  weather_code: number;
  weather_desc: string;
  weather_desc_kn: string;
  is_day: boolean;
  today_min_temp: number;
  today_max_temp: number;
  hourly_forecast: HourlyForecastItem[];
  daily_forecast: DailyForecastItem[];
  agronomic_insight: AgronomicInsight;
  fetched_at: string;
  is_cached?: boolean;
}

export interface MandiPriceItem {
  commodity: string;
  commodity_kn: string;
  variety: string;
  market: string;
  market_kn: string;
  district: string;
  district_kn: string;
  min_price: number;
  max_price: number;
  modal_price: number;
  unit: string;
  price_date: string;
  trend: 'rising' | 'falling' | 'stable' | string;
  msp?: number | null;
}

export interface MandiPricesResponse {
  source: string;
  last_updated: string;
  filter_district?: string | null;
  filter_commodity?: string | null;
  total_records: number;
  prices: MandiPriceItem[];
}
