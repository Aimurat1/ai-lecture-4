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

"""Amusement park tools for ThrillZone Adventure Park customer service."""

import logging
import uuid
from datetime import datetime, timedelta
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


# ============= ATTRACTION EXPERT TOOLS =============

def get_ride_wait_times(attraction_name: str = None, park_section: str = None) -> Dict[str, Any]:
    """
    Get current wait times for attractions.
    
    Args:
        attraction_name: Specific attraction name (optional)
        park_section: Park area like "Adventure Land", "Fantasy Forest" (optional)
    
    Returns:
        Dictionary with wait time information
    """
    logger.info(f"Getting wait times for attraction: {attraction_name}, section: {park_section}")
    
    # Mock wait times data
    mock_wait_times = {
        "Thunder Mountain Express": {"wait_minutes": 45, "status": "open", "fast_pass_available": True},
        "Splash Safari": {"wait_minutes": 25, "status": "open", "fast_pass_available": True},
        "Carousel Dreams": {"wait_minutes": 5, "status": "open", "fast_pass_available": False},
        "Extreme Drop Tower": {"wait_minutes": 60, "status": "open", "fast_pass_available": True},
        "Family Fun Coaster": {"wait_minutes": 15, "status": "open", "fast_pass_available": False},
        "Haunted Mansion": {"wait_minutes": 30, "status": "temporary_closure", "fast_pass_available": False}
    }
    
    if attraction_name:
        if attraction_name in mock_wait_times:
            return {"attraction": attraction_name, **mock_wait_times[attraction_name]}
        else:
            return {"error": f"Attraction '{attraction_name}' not found"}
    
    return {"wait_times": mock_wait_times, "last_updated": "2024-12-15 14:30:00"}


def check_height_requirements(guest_age: str, attraction_name: str) -> Dict[str, Any]:
    """
    Check height requirements and age restrictions for attractions.
    
    Args:
        guest_age: Age group ("child", "teen", "adult") or specific age
        attraction_name: Name of the attraction
    
    Returns:
        Dictionary with requirement information and recommendations
    """
    logger.info(f"Checking height requirements for {guest_age} on {attraction_name}")
    
    height_requirements = {
        "Thunder Mountain Express": {"min_height_inches": 44, "max_age": None, "adult_supervision": "under_7"},
        "Splash Safari": {"min_height_inches": 40, "max_age": None, "adult_supervision": "under_8"},
        "Carousel Dreams": {"min_height_inches": None, "max_age": None, "adult_supervision": "under_3"},
        "Extreme Drop Tower": {"min_height_inches": 52, "max_age": None, "adult_supervision": "never"},
        "Family Fun Coaster": {"min_height_inches": 36, "max_age": None, "adult_supervision": "under_5"},
        "Haunted Mansion": {"min_height_inches": None, "max_age": None, "adult_supervision": "under_6"}
    }
    
    if attraction_name not in height_requirements:
        return {"error": f"Attraction '{attraction_name}' not found"}
    
    req = height_requirements[attraction_name]
    return {
        "attraction": attraction_name,
        "requirements": req,
        "suitable_for_age": guest_age,
        "recommendation": "Check height at entrance for exact measurement"
    }


def reserve_fast_pass(guest_id: str, attraction_name: str, time_slot: str) -> Dict[str, Any]:
    """
    Reserve a Fast Pass for an attraction.
    
    Args:
        guest_id: Guest identifier
        attraction_name: Name of the attraction
        time_slot: Preferred time slot (e.g., "14:00-15:00")
    
    Returns:
        Dictionary with reservation confirmation
    """
    logger.info(f"Reserving Fast Pass for guest {guest_id} on {attraction_name} at {time_slot}")
    
    reservation_id = f"FP{uuid.uuid4().hex[:8].upper()}"
    
    return {
        "status": "confirmed",
        "reservation_id": reservation_id,
        "attraction": attraction_name,
        "time_slot": time_slot,
        "guest_id": guest_id,
        "instructions": "Present this confirmation at the Fast Pass entrance during your time slot"
    }


def get_attraction_recommendations(guest_preferences: Dict[str, Any], party_composition: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get personalized attraction recommendations based on guest preferences.
    
    Args:
        guest_preferences: Dict with thrill_level, interests, avoid_attractions
        party_composition: Dict with ages, accessibility_needs, group_size
    
    Returns:
        Dictionary with recommended attractions
    """
    logger.info(f"Getting recommendations for preferences: {guest_preferences}")
    
    all_attractions = {
        "Thunder Mountain Express": {"thrill_level": "moderate", "type": "roller_coaster", "family_friendly": True},
        "Splash Safari": {"thrill_level": "mild", "type": "water_ride", "family_friendly": True},
        "Carousel Dreams": {"thrill_level": "mild", "type": "classic_ride", "family_friendly": True},
        "Extreme Drop Tower": {"thrill_level": "extreme", "type": "thrill_ride", "family_friendly": False},
        "Family Fun Coaster": {"thrill_level": "mild", "type": "roller_coaster", "family_friendly": True},
        "Haunted Mansion": {"thrill_level": "moderate", "type": "dark_ride", "family_friendly": True}
    }
    
    thrill_level = guest_preferences.get("thrill_level", "moderate")
    recommendations = []
    
    for attraction, details in all_attractions.items():
        if details["thrill_level"] == thrill_level or (thrill_level == "moderate" and details["thrill_level"] == "mild"):
            recommendations.append({
                "attraction": attraction,
                "match_reason": f"Matches {thrill_level} thrill preference",
                "details": details
            })
    
    return {
        "recommendations": recommendations[:5],  # Top 5
        "total_matches": len(recommendations)
    }


# ============= DINING SPECIALIST TOOLS =============

def check_restaurant_availability(restaurant_name: str, party_size: int, preferred_time: str,) -> Dict[str, Any]:
    """
    Check availability for restaurant reservations.
    
    Args:
        restaurant_name: Name of the restaurant
        party_size: Number of people in the party
        preferred_time: Preferred dining time
    
    Returns:
        Dictionary with availability information
    """
    logger.info(f"Checking availability for {restaurant_name}, party of {party_size} at {preferred_time}")
    
    restaurants = {
        "Adventurer's Grill": {"cuisine": "american", "capacity": 200, "reservations": True},
        "Sweet Treats Cafe": {"cuisine": "desserts", "capacity": 50, "reservations": False},
        "Pizza Planet": {"cuisine": "italian", "capacity": 100, "reservations": True},
        "Tropical Tiki Bar": {"cuisine": "hawaiian", "capacity": 80, "reservations": True},
        "Character Dining Hall": {"cuisine": "buffet", "capacity": 150, "reservations": True}
    }
    
    if restaurant_name not in restaurants:
        return {"error": f"Restaurant '{restaurant_name}' not found"}
    
    # Mock availability
    available_times = ["11:30", "12:00", "12:30", "13:00", "13:30", "17:30", "18:00", "18:30"]
    
    return {
        "restaurant": restaurant_name,
        "party_size": party_size,
        "available_times": available_times,
        "restaurant_info": restaurants[restaurant_name],
        "booking_required": restaurants[restaurant_name]["reservations"]
    }


def make_dining_reservation(guest_id: str, restaurant: str, time: str, party_size: int, special_requests: str = "") -> Dict[str, Any]:
    """
    Make a dining reservation for a guest.
    
    Args:
        guest_id: Guest identifier
        restaurant: Restaurant name
        time: Reservation time
        party_size: Number of people
        special_requests: Special dietary needs or requests
    
    Returns:
        Dictionary with reservation confirmation
    """
    logger.info(f"Making reservation for guest {guest_id} at {restaurant} for {party_size} people")
    
    reservation_id = f"RES{uuid.uuid4().hex[:8].upper()}"
    
    return {
        "status": "confirmed",
        "reservation_id": reservation_id,
        "restaurant": restaurant,
        "date": "2024-12-15",
        "time": time,
        "party_size": party_size,
        "special_requests": special_requests,
        "confirmation_sent": True
    }


def get_menu_recommendations(dietary_restrictions: List[str], cuisine_preference: str = None) -> Dict[str, Any]:
    """
    Get menu recommendations based on dietary restrictions.
    
    Args:
        dietary_restrictions: List of restrictions like ["vegetarian", "gluten-free"]
        cuisine_preference: Preferred cuisine type
    
    Returns:
        Dictionary with menu recommendations
    """
    logger.info(f"Getting menu recommendations for restrictions: {dietary_restrictions}")
    
    menu_items = {
        "Adventurer's Grill": {
            "vegetarian": ["Garden Veggie Burger", "Quinoa Power Bowl", "Margherita Flatbread"],
            "gluten_free": ["Grilled Salmon", "Caesar Salad (no croutons)", "Rice Bowl"],
            "vegan": ["Buddha Bowl", "Veggie Wrap", "Fruit Smoothie"]
        },
        "Pizza Planet": {
            "vegetarian": ["Veggie Supreme Pizza", "Caprese Salad", "Garlic Bread"],
            "gluten_free": ["Gluten-Free Margherita Pizza", "Italian Salad"],
            "vegan": ["Vegan Cheese Pizza", "Mediterranean Salad"]
        }
    }
    
    recommendations = []
    for restaurant, items in menu_items.items():
        for restriction in dietary_restrictions:
            restriction_key = restriction.replace("-", "_").lower()
            if restriction_key in items:
                recommendations.extend([
                    {"restaurant": restaurant, "item": item, "dietary_info": restriction}
                    for item in items[restriction_key]
                ])
    
    return {"recommendations": recommendations[:10]}


# ============= TICKET MANAGER TOOLS =============

def upgrade_ticket(guest_id: str, current_ticket: str, target_ticket: str) -> Dict[str, Any]:
    """
    Upgrade a guest's ticket type.
    
    Args:
        guest_id: Guest identifier
        current_ticket: Current ticket type
        target_ticket: Desired ticket type
    
    Returns:
        Dictionary with upgrade information
    """
    logger.info(f"Upgrading ticket for guest {guest_id} from {current_ticket} to {target_ticket}")
    
    ticket_prices = {
        "Day Pass": 89.99,
        "VIP Pass": 149.99,
        "Season Pass": 299.99,
        "Family Package": 319.99
    }
    
    if current_ticket not in ticket_prices or target_ticket not in ticket_prices:
        return {"error": "Invalid ticket type"}
    
    price_difference = ticket_prices[target_ticket] - ticket_prices[current_ticket]
    
    return {
        "upgrade_available": price_difference >= 0,
        "price_difference": price_difference,
        "new_ticket_type": target_ticket,
        "upgrade_id": f"UPG{uuid.uuid4().hex[:6].upper()}"
    }


def apply_promotional_discount(promo_code: str, guest_id: str) -> Dict[str, Any]:
    """
    Apply promotional discount code.
    
    Args:
        promo_code: Promotional code
        guest_id: Guest identifier
    
    Returns:
        Dictionary with discount application result
    """
    logger.info(f"Applying promo code {promo_code} for guest {guest_id}")
    
    valid_codes = {
        "BIRTHDAY20": {"discount_percent": 20, "description": "Birthday Special"},
        "FAMILY15": {"discount_percent": 15, "description": "Family Fun Discount"},
        "SEASON10": {"discount_percent": 10, "description": "Season Pass Holder Discount"}
    }
    
    if promo_code not in valid_codes:
        return {"status": "invalid", "message": "Promotional code not found"}
    
    discount_info = valid_codes[promo_code]
    return {
        "status": "applied",
        "discount_percent": discount_info["discount_percent"],
        "description": discount_info["description"],
        "promo_code": promo_code
    }


# ============= GUEST SERVICES TOOLS =============

def report_lost_item(description: str, last_seen_location: str, guest_contact: str) -> Dict[str, Any]:
    """
    Report a lost item.
    
    Args:
        description: Description of the lost item
        last_seen_location: Where item was last seen
        guest_contact: Guest contact information
    
    Returns:
        Dictionary with lost item report confirmation
    """
    logger.info(f"Lost item reported: {description} at {last_seen_location}")
    
    report_id = f"LOST{uuid.uuid4().hex[:8].upper()}"
    
    return {
        "report_id": report_id,
        "status": "reported",
        "description": description,
        "location": last_seen_location,
        "estimated_response_time": "2-4 hours",
        "contact_method": "SMS notification when found"
    }


def request_accessibility_services(guest_id: str, service_type: str, location: str) -> Dict[str, Any]:
    """
    Request accessibility services.
    
    Args:
        guest_id: Guest identifier
        service_type: Type of service needed
        location: Current location or where service is needed
    
    Returns:
        Dictionary with service request confirmation
    """
    logger.info(f"Accessibility service requested: {service_type} at {location}")
    
    service_id = f"ACC{uuid.uuid4().hex[:8].upper()}"
    
    return {
        "service_id": service_id,
        "service_type": service_type,
        "location": location,
        "estimated_arrival": "10-15 minutes",
        "contact_number": "+1-555-HELP-NOW"
    }


# ============= ENTERTAINMENT COORDINATOR TOOLS =============

def get_show_schedule(date: str, show_type: str = None) -> Dict[str, Any]:
    """
    Get show and entertainment schedule.
    
    Args:
        date: Date for schedule
        show_type: Type of show (optional)
    
    Returns:
        Dictionary with show schedule
    """
    logger.info(f"Getting show schedule for {date}, type: {show_type}")
    
    shows = {
        "Magical Parade": {"times": ["11:00", "15:00"], "location": "Main Street", "duration": "30 min"},
        "Fireworks Spectacular": {"times": ["20:00"], "location": "Central Plaza", "duration": "20 min"},
        "Character Meet & Greet": {"times": ["10:00", "12:00", "14:00", "16:00"], "location": "Fantasy Forest", "duration": "15 min"},
        "Acrobatic Show": {"times": ["13:00", "17:00"], "location": "Adventure Theater", "duration": "45 min"}
    }
    
    if show_type:
        filtered_shows = {k: v for k, v in shows.items() if show_type.lower() in k.lower()}
        return {"date": date, "shows": filtered_shows}
    
    return {"date": date, "shows": shows}


def schedule_character_meet_greet(guest_id: str, character: str, preferred_time: str) -> Dict[str, Any]:
    """
    Schedule a character meet and greet.
    
    Args:
        guest_id: Guest identifier
        character: Character name
        preferred_time: Preferred meeting time
    
    Returns:
        Dictionary with meet and greet confirmation
    """
    logger.info(f"Scheduling character meet for guest {guest_id} with {character}")
    
    meeting_id = f"CHAR{uuid.uuid4().hex[:8].upper()}"
    
    return {
        "meeting_id": meeting_id,
        "character": character,
        "scheduled_time": preferred_time,
        "location": "Character Meet Zone",
        "duration": "10 minutes",
        "special_instructions": "Arrive 5 minutes early"
    }


# ============= EMERGENCY RESPONDER TOOLS =============

def request_medical_assistance(location: str, emergency_type: str, guest_info: str) -> Dict[str, Any]:
    """
    Request medical assistance for emergencies.
    
    Args:
        location: Current location of the emergency
        emergency_type: Type of medical emergency
        guest_info: Information about the guest needing help
    
    Returns:
        Dictionary with emergency response information
    """
    logger.info(f"MEDICAL EMERGENCY: {emergency_type} at {location}")
    
    incident_id = f"MED{uuid.uuid4().hex[:8].upper()}"
    
    return {
        "incident_id": incident_id,
        "status": "emergency_response_dispatched",
        "location": location,
        "estimated_arrival": "3-5 minutes",
        "emergency_contact": "911 contacted if needed",
        "first_aid_location": "First Aid Station - Main Street"
    }


def report_safety_incident(location: str, incident_type: str, severity: str) -> Dict[str, Any]:
    """
    Report a safety incident.
    
    Args:
        location: Location of the incident
        incident_type: Type of safety incident
        severity: Severity level
    
    Returns:
        Dictionary with incident report confirmation
    """
    logger.info(f"SAFETY INCIDENT: {incident_type} at {location}, severity: {severity}")
    
    incident_id = f"SAFE{uuid.uuid4().hex[:8].upper()}"
    
    return {
        "incident_id": incident_id,
        "status": "reported",
        "location": location,
        "incident_type": incident_type,
        "severity": severity,
        "response_team_notified": True,
        "follow_up_required": severity in ["high", "critical"]
    } 