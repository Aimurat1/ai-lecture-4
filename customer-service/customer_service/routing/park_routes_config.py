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

"""Park routes configuration for the amusement park customer service routing system."""

from typing import Dict

# Route definitions for the amusement park customer service agents
PARK_AGENT_ROUTES: Dict[str, str] = {
    "attraction_expert": """
    Best agent for all ride and attraction-related queries including:
    - Ride wait times, height requirements, accessibility features
    - Attraction recommendations based on guest preferences and thrill level
    - Fast pass reservations and availability
    - Ride closures, maintenance updates, and seasonal attractions
    - Questions about specific rides, shows, or entertainment venues
    """,
    
    "dining_specialist": """
    Best agent for all food and dining-related queries including:
    - Restaurant reservations and availability
    - Menu recommendations based on dietary restrictions and preferences
    - Food allergen information and special dietary accommodations
    - Mobile food ordering and delivery within the park
    - Dining package deals and character dining experiences
    """,
    
    "ticket_manager": """
    Best agent for all ticketing and admission-related queries including:
    - Ticket upgrades, add-ons, and package deals
    - Group bookings and corporate rates
    - Season pass renewals and member benefits
    - Promotional codes and discount applications
    - Payment processing and billing inquiries
    """,
    
    "guest_services": """
    Best agent for general support and guest assistance including:
    - Lost and found items, guest complaints and feedback
    - Accessibility services and special accommodation requests
    - General park information, directions, and facility locations
    - Guest profile updates and membership account management
    - Non-emergency assistance and general inquiries
    """,
    
    "entertainment_coordinator": """
    Best agent for shows, events, and entertainment-related queries including:
    - Show schedules, performance times, and venue information
    - Character meet and greet appointments and locations
    - Special events, parades, fireworks, and seasonal celebrations
    - Private party bookings and VIP experience packages
    - Entertainment venue reservations and seating arrangements
    """,
    
    "emergency_responder": """
    Best agent for safety, medical, and urgent assistance including:
    - Medical emergencies, first aid, and health-related incidents
    - Safety concerns, accident reports, and hazard notifications
    - Emergency evacuation procedures and safety protocols
    - Lost children, security incidents, and urgent guest assistance
    - Weather-related closures and emergency communications
    """
}

# Keywords and phrases that help identify which agent to route to
ROUTE_KEYWORDS = {
    "attraction_expert": [
        "ride", "attraction", "roller coaster", "wait time", "height requirement",
        "fast pass", "thrill", "scary", "fun", "exciting", "line", "queue",
        "closed", "open", "maintenance", "show times", "performance"
    ],
    
    "dining_specialist": [
        "food", "restaurant", "dining", "eat", "hungry", "menu", "reservation",
        "allergic", "vegetarian", "vegan", "gluten", "meal", "snack", "drink",
        "character dining", "breakfast", "lunch", "dinner"
    ],
    
    "ticket_manager": [
        "ticket", "pass", "upgrade", "admission", "price", "cost", "discount",
        "group", "season pass", "membership", "payment", "billing", "promo",
        "voucher", "refund", "purchase"
    ],
    
    "guest_services": [
        "lost", "found", "complaint", "feedback", "accessibility", "wheelchair",
        "help", "assistance", "information", "directions", "where is", "location",
        "restroom", "parking", "locker", "stroller"
    ],
    
    "entertainment_coordinator": [
        "show", "parade", "fireworks", "character", "meet", "greet", "event",
        "celebration", "birthday", "anniversary", "special occasion", "VIP",
        "private", "party", "schedule", "time"
    ],
    
    "emergency_responder": [
        "emergency", "medical", "hurt", "injured", "sick", "help", "urgent",
        "safety", "dangerous", "accident", "lost child", "security", "evacuation",
        "weather", "storm", "closed", "urgent"
    ]
}

# Fallback route when classification is uncertain
DEFAULT_ROUTE = "guest_services" 