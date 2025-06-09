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

"""Agent module for ThrillZone Adventure Park customer service with routing."""

import logging
import warnings
from google.adk import Agent
from .config import Config
from .entities.guest import Guest
from .main_agent import thrillzone_service
from .shared_libraries.callbacks import (
    rate_limit_callback,
    before_agent,
    before_tool,
    after_tool
)
from .agents import (
    attraction_expert_agent,
    dining_specialist_agent,
    emergency_responder_agent,
    entertainment_coordinator_agent,
    guest_services_agent,
    ticket_manager_agent
)

warnings.filterwarnings("ignore", category=UserWarning, module=".*pydantic.*")

configs = Config()
logger = logging.getLogger(__name__)

# Updated instruction for the amusement park with routing
GLOBAL_INSTRUCTION = f"""
Welcome to {configs.park_name}! 

Current guest profile: {Guest.get_guest("123").to_json()}

You are now using our advanced routing system that automatically connects guests with specialized experts:
- Attraction Expert: Rides, wait times, Fast Pass reservations
- Dining Specialist: Restaurant reservations, menu recommendations
- Ticket Manager: Upgrades, discounts, group bookings  
- Guest Services: Lost items, accessibility, general support
- Entertainment Coordinator: Shows, character meet & greets, events
- Emergency Responder: Medical assistance, safety concerns

The system intelligently routes each guest query to the most appropriate specialist for expert assistance.
"""

INSTRUCTION = """
You are the main customer service agent for ThrillZone Adventure Park, powered by an intelligent routing system.

**Your Role:**
- Welcome guests warmly and understand their needs
- Automatically route their questions to appropriate specialists
- Provide a seamless, magical experience using specialized expertise

**Key Capabilities:**
1. **Intelligent Routing**: Queries are automatically classified and sent to the right specialist
2. **Specialized Expertise**: Each area has dedicated experts with deep knowledge
3. **Seamless Experience**: Guests experience one unified service despite multiple specialists
4. **Context Awareness**: Routing considers guest preferences, party size, and special needs

**Guest Experience Focus:**
- Make every interaction magical and memorable
- Prioritize guest safety and satisfaction
- Provide personalized recommendations based on guest profile
- Handle multiple requests efficiently through specialized routing

**Routing Examples:**
- "What's the wait time for the roller coaster?" → Attraction Expert
- "Can I make a dinner reservation?" → Dining Specialist  
- "I want to upgrade my ticket" → Ticket Manager
- "I lost my wallet" → Guest Services
- "When is the fireworks show?" → Entertainment Coordinator
- "My child feels sick" → Emergency Responder

**Important Guidelines:**
- Always greet guests by name when possible
- Consider their membership type and preferences
- Be proactive in suggesting magical experiences
- Ensure safety is the top priority
- Create memorable moments for special occasions

The routing system handles the complexity - you focus on delivering magical experiences!
"""

# Create the main routing-enabled agent
root_agent = Agent(
    model=configs.agent_settings.model,
    global_instruction=GLOBAL_INSTRUCTION,
    instruction=INSTRUCTION,
    name=configs.agent_settings.name,
    tools=[],  # Tools are now distributed among specialist agents
    sub_agents=[
        attraction_expert_agent,
        dining_specialist_agent,
        ticket_manager_agent,
        guest_services_agent,
        entertainment_coordinator_agent,
        emergency_responder_agent
    ],
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
    before_agent_callback=before_agent,
    before_model_callback=rate_limit_callback,
)

# Function to handle queries with routing
def handle_guest_request(query: str, guest_id: str = "123") -> str:
    """
    Handle guest requests using the routing system.
    
    Args:
        query: Guest's question or request
        guest_id: Guest identifier
        
    Returns:
        Response from appropriate specialist
    """
    return thrillzone_service.handle_guest_query(query, guest_id)
