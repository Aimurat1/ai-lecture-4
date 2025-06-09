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

"""Main orchestrator agent for ThrillZone Adventure Park with routing pattern."""

import logging
from typing import Dict, Any
from google.adk import Agent

from .config import Config
from .entities.guest import Guest
from .routing.guest_query_router import GuestQueryRouter

logger = logging.getLogger(__name__)
configs = Config()


class ThrillZoneParkService:
    """Main orchestrator for ThrillZone Adventure Park customer service using routing pattern."""
    
    def __init__(self):
        """Initialize the park service with router and specialist agents."""
        self.router = GuestQueryRouter()
        logger.info("ThrillZone Park Service initialized with routing pattern")
    
    def handle_guest_query(self, guest_query: str, guest_id: str = "123") -> str:
        """Process a guest query using the routing pattern."""
        try:
            # Get guest context for routing
            guest = Guest.get_guest(guest_id)
            guest_context = {
                "membership_type": guest.membership_type,
                "preferences": guest.park_preferences.model_dump(),
                "party_size": guest.current_visit.party_size if guest.current_visit else 1
            }
            
            # Route the query
            routing_result = self.router.route_query(guest_query, guest_context)
            selected_route = routing_result.get("route")
            
            logger.info(f"Query routed to {selected_route}")
            
            return f"Routing to {selected_route}: {routing_result.get('reason', '')}"
            
        except Exception as e:
            logger.error(f"Error handling guest query: {e}")
            return f"I apologize for any difficulties. How can I help you today?"


# Main service instance
thrillzone_service = ThrillZoneParkService() 