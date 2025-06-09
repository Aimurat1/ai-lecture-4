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

"""Guest query router implementation for ThrillZone Adventure Park."""

import logging
from typing import Dict, Any, Literal
from pydantic import BaseModel, Field
from google.adk import Agent
from google.adk.tools import ToolContext

from .park_routes_config import PARK_AGENT_ROUTES, DEFAULT_ROUTE
from ..config import Config

logger = logging.getLogger(__name__)
configs = Config()


class RouteSelection(BaseModel):
    """Schema for route selection response."""
    route: Literal[
        "attraction_expert",
        "dining_specialist", 
        "ticket_manager",
        "guest_services",
        "entertainment_coordinator",
        "emergency_responder"
    ]
    reason: str = Field(
        description="Short explanation why this route was selected for the guest query."
    )
    confidence: float = Field(
        description="Confidence level (0.0-1.0) in the route selection.",
        ge=0.0,
        le=1.0
    )


class GuestQueryRouter:
    """Router for directing guest queries to appropriate specialist agents."""
    
    def __init__(self):
        """Initialize the router with a lightweight model for fast classification."""
        self.router_agent = Agent(
            model=configs.agent_settings.router_model,
            name="thrillzone_query_router",
            instruction=self._get_router_instruction()
        )
    
    def _get_router_instruction(self) -> str:
        """Get the instruction prompt for the router agent."""
        return f"""
        You are a query classification agent for ThrillZone Adventure Park customer service.
        
        Your job is to analyze guest queries and select the most appropriate specialist agent to handle them.
        
        Available specialist agents and their capabilities:
        {self._format_routes_for_prompt()}
        
        Classification Guidelines:
        1. Analyze the guest's query for key topics, intent, and urgency
        2. Consider multiple aspects - a query might have secondary topics
        3. Choose the MOST RELEVANT specialist based on the primary intent
        4. For emergency or safety-related queries, ALWAYS route to emergency_responder
        5. When uncertain, route to guest_services as the general support agent
        6. Provide a confidence score: 0.9+ for clear matches, 0.7+ for likely matches, below 0.7 for uncertain
        
        Respond ONLY with a valid JSON object matching the RouteSelection schema.
        """
    
    def _format_routes_for_prompt(self) -> str:
        """Format the routes configuration for the prompt."""
        formatted = []
        for route_name, description in PARK_AGENT_ROUTES.items():
            formatted.append(f"**{route_name}**: {description.strip()}")
        return "\n\n".join(formatted)
    
    def route_query(self, guest_query: str, guest_context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Route a guest query to the appropriate specialist agent.
        
        Args:
            guest_query: The guest's question or request
            guest_context: Optional context about the guest (preferences, current visit, etc.)
            
        Returns:
            Dictionary containing route selection and metadata
        """
        try:
            # Prepare the routing prompt
            context_info = ""
            if guest_context:
                context_info = f"\n\nGuest Context: {guest_context}"
            
            routing_prompt = f"""
            Guest Query: "{guest_query}"{context_info}
            
            Select the best specialist agent to handle this query and provide your reasoning.
            """
            
            # Get route selection from router agent
            response = self.router_agent.run(routing_prompt)
            
            # Parse the response - assuming it returns JSON-like structure
            # In a real implementation, you'd use structured output or JSON parsing
            route_info = self._parse_route_response(response)
            
            logger.info(
                f"Routed query to {route_info['route']} "
                f"(confidence: {route_info.get('confidence', 'unknown')}): {route_info.get('reason', '')}"
            )
            
            return route_info
            
        except Exception as e:
            logger.error(f"Error during routing: {e}")
            # Fallback to default route
            return {
                "route": DEFAULT_ROUTE,
                "reason": "Routing failed, using default agent",
                "confidence": 0.5,
                "error": str(e)
            }
    
    def _parse_route_response(self, response: str) -> Dict[str, Any]:
        """
        Parse the router agent response into structured data.
        
        This is a simplified implementation - in production you'd want
        more robust JSON parsing or use structured output capabilities.
        """
        # For now, we'll use a simple heuristic-based approach
        # In a real implementation, you'd parse JSON or use structured output
        
        response_lower = response.lower()
        
        # Check for route keywords in the response
        best_route = DEFAULT_ROUTE
        confidence = 0.6
        reason = "Default routing"
        
        for route_name in PARK_AGENT_ROUTES.keys():
            if route_name.replace("_", " ") in response_lower:
                best_route = route_name
                confidence = 0.8
                reason = f"Matched {route_name} in response"
                break
        
        # Emergency detection
        emergency_keywords = ["emergency", "urgent", "medical", "safety", "help", "hurt"]
        if any(keyword in response_lower for keyword in emergency_keywords):
            best_route = "emergency_responder"
            confidence = 0.95
            reason = "Emergency keywords detected"
        
        return {
            "route": best_route,
            "reason": reason,
            "confidence": confidence,
            "full_response": response
        }
    
    def get_available_routes(self) -> Dict[str, str]:
        """Return available routes and their descriptions."""
        return PARK_AGENT_ROUTES.copy()


# Utility function for easy routing
def route_guest_query(query: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Convenience function to route a guest query.
    
    Args:
        query: Guest's question or request
        context: Optional guest context
        
    Returns:
        Routing result with selected agent and metadata
    """
    router = GuestQueryRouter()
    return router.route_query(query, context) 