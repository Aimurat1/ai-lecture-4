# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Travel request entity for travel planning system."""

from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class TravelPreferences(BaseModel):
    """Travel preferences and requirements."""
    accommodation_type: str = "hotel"  # hotel, vacation_rental, hostel, resort
    dining_style: str = "mixed"  # fine_dining, casual, local, mixed
    activity_level: str = "moderate"  # relaxed, moderate, active, adventure
    transportation_preference: str = "flexible"  # car, public_transport, walking, flexible
    special_interests: List[str] = Field(default_factory=list)  # museums, nightlife, nature, etc.
    accessibility_needs: List[str] = Field(default_factory=list)
    dietary_restrictions: List[str] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)


class TravelParty(BaseModel):
    """Information about the travel party."""
    adults: int = 1
    children: int = 0
    children_ages: List[int] = Field(default_factory=list)
    seniors: int = 0
    special_occasions: List[str] = Field(default_factory=list)  # birthday, anniversary, etc.
    model_config = ConfigDict(from_attributes=True)


class TravelRequest(BaseModel):
    """Represents a travel planning request."""
    
    request_id: str
    destination: str
    start_date: str  # ISO format date string
    end_date: str    # ISO format date string
    duration_days: int
    budget_total: float
    budget_currency: str = "USD"
    
    travel_party: TravelParty
    preferences: TravelPreferences
    
    # Additional context
    departure_location: Optional[str] = None
    trip_purpose: str = "leisure"  # leisure, business, family, romantic, adventure
    flexibility: str = "moderate"  # strict, moderate, flexible
    
    # User's specific requests or questions
    specific_requests: List[str] = Field(default_factory=list)
    priority_areas: List[str] = Field(default_factory=list)  # accommodation, dining, attractions, etc.
    
    model_config = ConfigDict(from_attributes=True)

    def to_json(self) -> str:
        """Converts the TravelRequest object to a JSON string."""
        return self.model_dump_json(indent=4)

    @staticmethod
    def get_sample_request() -> "TravelRequest":
        """Returns a sample travel request for testing."""
        return TravelRequest(
            request_id="TR001",
            destination="Orlando, Florida",
            start_date="2025-03-15",
            end_date="2025-03-20",
            duration_days=5,
            budget_total=3000.0,
            budget_currency="USD",
            travel_party=TravelParty(
                adults=2,
                children=2,
                children_ages=[8, 12],
                special_occasions=["birthday celebration"]
            ),
            preferences=TravelPreferences(
                accommodation_type="hotel",
                dining_style="family_friendly",
                activity_level="moderate",
                special_interests=["theme_parks", "family_activities", "good_food"],
                dietary_restrictions=["vegetarian_options_needed"]
            ),
            departure_location="Atlanta, Georgia",
            trip_purpose="family",
            specific_requests=[
                "Need family-friendly hotels near theme parks",
                "Looking for character dining experiences",
                "Want to visit Universal and Disney World"
            ],
            priority_areas=["attractions", "accommodation", "dining"]
        ) 