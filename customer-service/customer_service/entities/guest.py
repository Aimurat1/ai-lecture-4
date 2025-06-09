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
"""Guest entity module for amusement park."""

from typing import List, Dict, Optional, Any
from pydantic import BaseModel, Field, ConfigDict


class Address(BaseModel):
    """Represents a guest's address."""
    street: str
    city: str
    state: str
    zip: str
    model_config = ConfigDict(from_attributes=True)


class Attraction(BaseModel):
    """Represents an attraction experience in visit history."""
    attraction_name: str
    ride_count: int
    last_ride_time: str
    rating: Optional[int] = None  # 1-5 stars
    model_config = ConfigDict(from_attributes=True)


class Purchase(BaseModel):
    """Represents a guest's purchase."""
    date: str
    items: List[Dict[str, Any]]  # Food, merchandise, photos
    total_amount: float
    location: str  # Where in park purchased
    model_config = ConfigDict(from_attributes=True)


class Visit(BaseModel):
    """Represents a guest's park visit."""
    date: str
    ticket_type: str
    attractions_visited: List[Attraction]
    purchases: List[Purchase]
    total_spent: float
    visit_duration_hours: float
    party_size: int
    model_config = ConfigDict(from_attributes=True)


class CommunicationPreferences(BaseModel):
    """Represents a guest's communication preferences."""
    email: bool = True
    sms: bool = True
    push_notifications: bool = True
    marketing_emails: bool = False
    model_config = ConfigDict(from_attributes=True)


class AccessibilityNeeds(BaseModel):
    """Represents a guest's accessibility requirements."""
    wheelchair_access: bool = False
    mobility_assistance: bool = False
    visual_assistance: bool = False
    hearing_assistance: bool = False
    dietary_restrictions: List[str] = Field(default_factory=list)
    special_accommodations: str = ""
    model_config = ConfigDict(from_attributes=True)


class ParkPreferences(BaseModel):
    """Represents a guest's park preferences."""
    favorite_attractions: List[str] = Field(default_factory=list)
    preferred_dining: List[str] = Field(default_factory=list)
    thrill_level: str = "moderate"  # "mild", "moderate", "extreme"
    age_group: str = "adult"  # "child", "teen", "adult", "senior"
    interests: List[str] = Field(default_factory=list)
    avoid_attractions: List[str] = Field(default_factory=list)
    model_config = ConfigDict(from_attributes=True)


class CurrentVisit(BaseModel):
    """Represents the guest's current visit information."""
    visit_date: str
    ticket_type: str
    party_size: int
    special_occasion: Optional[str] = None
    check_in_time: str
    current_location: Optional[str] = None
    fast_passes_used: int = 0
    fast_passes_remaining: int = 0
    model_config = ConfigDict(from_attributes=True)


class Guest(BaseModel):
    """Represents an amusement park guest."""
    
    account_number: str
    guest_id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    membership_start_date: str
    membership_type: str  # "Day Pass", "Season Pass", "VIP", "Group"
    years_as_member: int
    address: Address
    visit_history: List[Visit]
    loyalty_points: int
    communication_preferences: CommunicationPreferences
    accessibility_needs: AccessibilityNeeds
    park_preferences: ParkPreferences
    current_visit: Optional[CurrentVisit] = None
    emergency_contact: Dict[str, str] = Field(default_factory=dict)
    scheduled_reservations: Dict = Field(default_factory=dict)
    model_config = ConfigDict(from_attributes=True)

    def to_json(self) -> str:
        """Converts the Guest object to a JSON string."""
        return self.model_dump_json(indent=4)

    @staticmethod
    def get_guest(guest_id: str) -> Optional["Guest"]:
        """Retrieves a guest based on their ID."""
        # Mock data for demonstration - in real implementation would be database lookup
        return Guest(
            guest_id=guest_id,
            account_number="TP789123456",
            first_name="Maya",
            last_name="Chen",
            email="maya.chen@example.com",
            phone_number="+1-555-THRILL",
            membership_start_date="2023-04-15",
            membership_type="Season Pass",
            years_as_member=1,
            address=Address(
                street="456 Adventure Ave",
                city="Orlando",
                state="FL",
                zip="32819"
            ),
            visit_history=[
                Visit(
                    date="2024-07-04",
                    ticket_type="Season Pass",
                    attractions_visited=[
                        Attraction(
                            attraction_name="Thunder Mountain Express",
                            ride_count=3,
                            last_ride_time="14:30",
                            rating=5
                        ),
                        Attraction(
                            attraction_name="Splash Safari",
                            ride_count=2,
                            last_ride_time="16:45",
                            rating=4
                        )
                    ],
                    purchases=[
                        Purchase(
                            date="2024-07-04",
                            items=[
                                {"name": "Cotton Candy", "price": 8.99, "quantity": 1},
                                {"name": "Park T-Shirt", "price": 24.99, "quantity": 1}
                            ],
                            total_amount=33.98,
                            location="Main Street Sweets"
                        )
                    ],
                    total_spent=33.98,
                    visit_duration_hours=8.5,
                    party_size=3
                )
            ],
            loyalty_points=450,
            communication_preferences=CommunicationPreferences(
                email=True,
                sms=True,
                push_notifications=True,
                marketing_emails=True
            ),
            accessibility_needs=AccessibilityNeeds(
                wheelchair_access=False,
                dietary_restrictions=["vegetarian"],
                special_accommodations=""
            ),
            park_preferences=ParkPreferences(
                favorite_attractions=["Thunder Mountain Express", "Carousel Dreams"],
                preferred_dining=["Adventurer's Grill", "Sweet Treats Cafe"],
                thrill_level="moderate",
                age_group="adult",
                interests=["family rides", "shows", "dining"],
                avoid_attractions=["Extreme Drop Tower"]
            ),
            current_visit=CurrentVisit(
                visit_date="2024-12-15",
                ticket_type="Season Pass",
                party_size=3,
                special_occasion="Birthday celebration",
                check_in_time="09:30",
                current_location="Adventure Land",
                fast_passes_used=1,
                fast_passes_remaining=2
            ),
            emergency_contact={
                "name": "David Chen",
                "relationship": "Spouse",
                "phone": "+1-555-EMERGENCY"
            },
            scheduled_reservations={}
        ) 