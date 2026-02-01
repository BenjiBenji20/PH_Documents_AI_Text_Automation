from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class ProcessorType(str, Enum):
    FRONT = "front"
    REAR = "rear"
    BOTH = "both"

class FrontNationalIDData(BaseModel):
    """Data extracted from the front of PH National ID"""
    unique_id_number: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    birth_date: Optional[str] = None
    complete_address: Optional[str] = None

class RearNationalIDData(BaseModel):
    """Data extracted from the rear of PH National ID"""
    issued_date: Optional[str] = None
    sex: Optional[str] = None
    blood_type: Optional[str] = None
    marital_status: Optional[str] = None
    place_of_birth: Optional[str] = None

class NationalIDResponse(BaseModel):
    """Complete response containing both front and rear data"""
    success: bool
    message: str
    processor_used: ProcessorType
    front_data: Optional[FrontNationalIDData] = None
    rear_data: Optional[RearNationalIDData] = None
    raw_text: Optional[str] = None  # For debugging purposes

class ErrorResponse(BaseModel):
    """Error response model"""
    success: bool = False
    message: str
    error_detail: Optional[str] = None
    