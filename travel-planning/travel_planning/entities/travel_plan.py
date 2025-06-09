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

"""Travel plan entity for travel planning system."""

from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field, ConfigDict


class AccommodationRecommendation(BaseModel):
    """Accommodation recommendation details."""
    name: str
    type: str  # hotel, vacation_rental, resort, etc.
    location: str
    price_per_night: float
    total_cost: float
    rating: Optional[float] = None
    amenities: List[str] = Field(default_factory=list)
    booking_url: Optional[str] = None
    reasons: List[str] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)


class AttractionRecommendation(BaseModel):
    """Attraction or activity recommendation."""
    name: str
    type: str  # theme_park, museum, tour, etc.
    location: str
    price_per_person: Optional[float] = None
    duration: Optional[str] = None
    age_suitability: List[str] = Field(default_factory=list)
    booking_required: bool = False
    booking_url: Optional[str] = None
    reasons: List[str] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)


class DiningRecommendation(BaseModel):
    """Restaurant or dining recommendation."""
    name: str
    cuisine_type: str
    location: str
    price_range: str  # $, $$, $$$, $$$$
    meal_type: List[str] = Field(default_factory=list)  # breakfast, lunch, dinner
    dietary_accommodations: List[str] = Field(default_factory=list)
    reservation_required: bool = False
    booking_url: Optional[str] = None
    reasons: List[str] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)


class TransportationOption(BaseModel):
    """Transportation option details."""
    type: str  # flight, car_rental, train, etc.
    provider: Optional[str] = None
    route: str
    price: Optional[float] = None
    duration: Optional[str] = None
    booking_url: Optional[str] = None
    reasons: List[str] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)


class BudgetBreakdown(BaseModel):
    """Budget allocation and breakdown."""
    total_budget: float
    accommodation_cost: float
    transportation_cost: float
    dining_cost: float
    attractions_cost: float
    miscellaneous_cost: float
    savings_opportunities: List[str] = Field(default_factory=list)
    budget_tips: List[str] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)


class DayItinerary(BaseModel):
    """Daily itinerary details."""
    day: int
    date: str
    theme: Optional[str] = None
    morning_activities: List[str] = Field(default_factory=list)
    afternoon_activities: List[str] = Field(default_factory=list)
    evening_activities: List[str] = Field(default_factory=list)
    dining_suggestions: List[str] = Field(default_factory=list)
    transportation_notes: List[str] = Field(default_factory=list)
    estimated_cost: Optional[float] = None
    model_config = ConfigDict(from_attributes=True)


class TravelPlan(BaseModel):
    """Complete travel plan with all recommendations."""
    
    plan_id: str
    request_id: str
    destination: str
    travel_dates: str
    
    # Main recommendations
    accommodation: AccommodationRecommendation
    attractions: List[AttractionRecommendation]
    dining: List[DiningRecommendation]
    transportation: TransportationOption
    budget: BudgetBreakdown
    
    # Detailed itinerary
    daily_itinerary: List[DayItinerary]
    
    # Additional information
    packing_suggestions: List[str] = Field(default_factory=list)
    local_tips: List[str] = Field(default_factory=list)
    emergency_contacts: List[str] = Field(default_factory=list)
    weather_considerations: List[str] = Field(default_factory=list)
    
    # Metadata
    created_at: str
    specialist_sources: List[str] = Field(default_factory=list)
    confidence_score: Optional[float] = None
    
    model_config = ConfigDict(from_attributes=True)

    def to_json(self) -> str:
        """Converts the TravelPlan object to a JSON string."""
        return self.model_dump_json(indent=4)

    def get_summary(self) -> str:
        """Returns a brief summary of the travel plan."""
        return f"""
Travel Plan Summary:
- Destination: {self.destination}
- Dates: {self.travel_dates}
- Accommodation: {self.accommodation.name} (${self.accommodation.total_cost})
- Top Attractions: {', '.join([a.name for a in self.attractions[:3]])}
- Total Budget: ${self.budget.total_budget}
- Daily Itinerary: {len(self.daily_itinerary)} days planned
        """.strip() 