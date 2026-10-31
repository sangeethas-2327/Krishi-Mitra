from typing import Optional, List, Dict, Any, Union
from datetime import datetime, timezone
from pydantic import BaseModel, Field

class Location(BaseModel):
    state: Optional[str] = "Karnataka"
    district: Optional[str] = None
    taluk: Optional[str] = None
    village: Optional[str] = None

class LandArea(BaseModel):
    value: Optional[float] = None
    unit: Optional[str] = "acre"
    value_acres: Optional[float] = None

class IrrigationInfo(BaseModel):
    has_irrigation: Optional[bool] = None
    source: Optional[str] = None  # borewell, open_well, canal, river, rainfed
    type: Optional[str] = None    # drip, sprinkler, flood, none

class FieldMetadata(BaseModel):
    field_name: str
    value: Any = None
    confidence: float = 0.0
    confirmation_status: str = "unconfirmed"  # confirmed, unconfirmed, needs_clarification, disputed
    source: str = "default"  # user_explicit, inferred, default, user_edit
    last_updated: Optional[str] = None
    previous_values: List[Any] = Field(default_factory=list)

class FarmerProfile(BaseModel):
    location: Location = Field(default_factory=Location)
    land_area: LandArea = Field(default_factory=LandArea)
    crops: List[str] = Field(default_factory=list)
    ownership: Optional[str] = None  # owned, tenant, leased, sharecropper, joint_owned
    season: Optional[str] = None     # kharif, rabi, summer, annual, perennial
    irrigation: IrrigationInfo = Field(default_factory=IrrigationInfo)
    assistance_needs: List[str] = Field(default_factory=list)
    additional_details: Dict[str, Any] = Field(default_factory=dict)
    
    # Audit, provenance, and confidence tracking
    field_confidence: Dict[str, float] = Field(default_factory=dict)
    confirmed_fields: List[str] = Field(default_factory=list)
    unknown_fields: List[str] = Field(default_factory=lambda: [
        "location.district",
        "land_area.value_acres",
        "crops",
        "ownership",
        "assistance_needs"
    ])
    conflict_fields: Dict[str, List[Any]] = Field(default_factory=dict)
    fields_metadata: Dict[str, FieldMetadata] = Field(default_factory=dict)

    def set_field_value(
        self,
        field_name: str,
        value: Any,
        confidence: float = 0.95,
        source: str = "user_explicit",
        status: str = "confirmed"
    ) -> None:
        """
        Helper method to record field updates with provenance and history tracking.
        Detects conflicts when an existing confirmed value differs significantly.
        """
        now_str = datetime.now(timezone.utc).isoformat()
        current_meta = self.fields_metadata.get(field_name)

        if current_meta:
            # Check for conflict
            if current_meta.value is not None and current_meta.value != value:
                if field_name not in self.conflict_fields:
                    self.conflict_fields[field_name] = []
                self.conflict_fields[field_name].append({
                    "old_value": current_meta.value,
                    "new_value": value,
                    "timestamp": now_str,
                    "source": source
                })
                current_meta.previous_values.append(current_meta.value)
            current_meta.value = value
            current_meta.confidence = confidence
            current_meta.source = source
            current_meta.confirmation_status = status
            current_meta.last_updated = now_str
        else:
            self.fields_metadata[field_name] = FieldMetadata(
                field_name=field_name,
                value=value,
                confidence=confidence,
                confirmation_status=status,
                source=source,
                last_updated=now_str,
                previous_values=[]
            )

        self.field_confidence[field_name] = confidence
        if status == "confirmed" and field_name not in self.confirmed_fields:
            self.confirmed_fields.append(field_name)
        if field_name in self.unknown_fields:
            self.unknown_fields.remove(field_name)

class FarmerProfileUpdate(BaseModel):
    location: Optional[Dict[str, Optional[str]]] = None
    land_area: Optional[Dict[str, Any]] = None
    crops: Optional[List[str]] = None
    ownership: Optional[str] = None
    season: Optional[str] = None
    irrigation: Optional[Dict[str, Any]] = None
    assistance_needs: Optional[List[str]] = None
    additional_details: Optional[Dict[str, Any]] = None

class ExtractedFarmerInfo(BaseModel):
    district: Optional[str] = None
    taluk: Optional[str] = None
    village: Optional[str] = None
    land_area: Optional[float] = None
    land_unit: Optional[str] = "acre"
    land_area_acres: Optional[float] = None
    crops: Optional[List[str]] = Field(default_factory=list)
    ownership: Optional[str] = None
    season: Optional[str] = None
    irrigation_source: Optional[str] = None
    has_irrigation: Optional[bool] = None
    assistance_needs: Optional[List[str]] = Field(default_factory=list)
    is_correction: bool = False
    corrected_fields: List[str] = Field(default_factory=list)
    raw_notes: Optional[str] = None
