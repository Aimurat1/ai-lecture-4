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

"""Main agent for Travel Planning Parallel System using Google ADK ParallelAgent."""

import logging
import warnings
from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent, BaseAgent
from .config import Config
from .entities.travel_request import TravelRequest
from .specialists import (
    accommodation_specialist,
    attractions_specialist,
    dining_specialist,
    transportation_specialist,
    budget_specialist
)
from .aggregation import travel_coordinator

warnings.filterwarnings("ignore", category=UserWarning, module=".*pydantic.*")

configs = Config()
logger = logging.getLogger(__name__)

# Global instruction for the travel planning system
GLOBAL_INSTRUCTION = f"""
Welcome to the {configs.service_name}!

This system uses advanced parallel processing to provide comprehensive travel planning:
- 5 specialist agents research different aspects of your trip simultaneously
- Real-time web search provides current pricing and availability
- Expert coordination synthesizes all findings into a practical travel plan

Sample travel request: {TravelRequest.get_sample_request().to_json()}

The system efficiently handles complex travel planning through parallel specialist research and intelligent aggregation.
"""

# --- 1. Create ParallelAgent for Specialist Research ---
# This agent orchestrates concurrent execution of all 5 specialists
parallel_research_agent = ParallelAgent(
    name="ParallelTravelResearch",
    sub_agents=[
        accommodation_specialist,
        attractions_specialist,
        dining_specialist,
        transportation_specialist,
        budget_specialist
    ],
    description="Runs travel research specialists in parallel to gather comprehensive information"
)

# --- 2. Create SequentialAgent for Complete Workflow ---
# This coordinates: Parallel Research → Aggregation
travel_planning_pipeline = SequentialAgent(
    name="TravelPlanningPipeline",
    sub_agents=[
        parallel_research_agent,  # Run all specialists in parallel first
        travel_coordinator        # Then synthesize results into final plan
    ],
    description="Complete travel planning workflow: parallel research followed by expert coordination"
)

root_agent = LlmAgent(
    name="TravelPlanningRoot",
    model=configs.agent_settings.coordinator_model,
    global_instruction=GLOBAL_INSTRUCTION,
    instruction="""
You are the root agent for the travel planning system.
You will be given a travel request and you will need to coordinate the travel planning pipeline to provide a comprehensive travel plan.

If explicitly asked, you will also provide a travel plan, transfer to "TravelPlanningPipeline" agent
If not, answer user question directly

""",
    sub_agents=[
        travel_planning_pipeline,
    ],
    description="Root agent for travel planning system",
    output_key="travel_plan_root"
)

# --- 3. Main Root Agent ---
root_agent = root_agent

# Function to handle travel planning requests
def plan_travel(travel_request: str) -> str:
    """
    Handle travel planning requests using the parallel workflow.
    
    Args:
        travel_request: Travel planning request description
        
    Returns:
        Comprehensive travel plan from coordinated specialist research
    """
    logger.info(f"Processing travel planning request: {travel_request[:100]}...")
    
    # The root_agent (SequentialAgent) will:
    # 1. Execute ParallelAgent (all 5 specialists research simultaneously)
    # 2. Execute TravelCoordinator (synthesize all results)
    # 3. Return comprehensive travel plan
    
    return f"Travel planning request received: {travel_request}"


# Export the main agent for ADK
__all__ = ["root_agent", "plan_travel"] 