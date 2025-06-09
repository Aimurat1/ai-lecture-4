# ThrillZone Adventure Park Customer Service Agent

This project implements an AI-powered customer service system for ThrillZone Adventure Park using an advanced **routing pattern** architecture. The system automatically classifies guest queries and directs them to specialized agents for expert assistance.

## Overview

The ThrillZone Adventure Park Customer Service System uses the routing pattern from [Agent Recipes](https://www.agentrecipes.com/routing) to provide seamless, specialized assistance across all park operations. Instead of a single monolithic agent, the system employs intelligent routing to connect guests with the most appropriate specialist for their needs.

## Agent Details

| Feature            | Description             |
| ------------------ | ----------------------- |
| _Interaction Type_ | Conversational with Intelligent Routing |
| _Complexity_       | Advanced Multi-Agent    |
| _Agent Type_       | Router + 6 Specialists  |
| _Components_       | Tools, Routing, Multi-Agent |
| _Vertical_         | Amusement Park          |

### Architecture: Routing Pattern

The system implements the routing pattern with these components:

#### **🎯 Router Agent**
- **Purpose**: Classifies guest queries and routes to appropriate specialists
- **Model**: Fast, lightweight model for quick classification
- **Intelligence**: Context-aware routing using guest preferences and visit information

#### **🎢 Specialist Agents**

1. **Attraction Expert**
   - Ride wait times, height requirements, Fast Pass reservations
   - Attraction recommendations based on thrill level and preferences
   - Operational updates and accessibility information

2. **Dining Specialist** 
   - Restaurant reservations and menu recommendations
   - Dietary accommodations (vegetarian, vegan, gluten-free, allergies)
   - Character dining and special culinary experiences

3. **Ticket Manager**
   - Ticket upgrades, promotional discounts, group bookings
   - Season pass benefits and membership management
   - Payment processing and billing support

4. **Guest Services**
   - Lost and found, accessibility services, complaints
   - General park information and facility locations
   - Guest profile management and general assistance

5. **Entertainment Coordinator**
   - Show schedules, character meet & greets, special events
   - VIP experiences and private party bookings
   - Seasonal celebrations and entertainment packages

6. **Emergency Responder**
   - Medical assistance and first aid coordination
   - Safety incidents and emergency protocols
   - Critical priority routing for urgent situations

### Key Features

- **🧠 Intelligent Query Routing**: Automatically classifies guest requests and routes to the most qualified specialist
- **🎯 Specialized Expertise**: Each agent has deep domain knowledge and specialized tools
- **⚡ Performance Optimized**: Fast routing for simple queries, specialized models for complex requests
- **🛡️ Safety First**: Emergency queries automatically prioritized and routed to safety specialists
- **🎨 Personalized Experience**: Routing considers guest preferences, membership type, and party composition
- **🔄 Seamless Handoffs**: Guests experience unified service despite multiple specialists
- **📊 Context Awareness**: Uses guest history, current visit, and preferences for smart routing

### Sample Routing Examples

| Guest Query | Routed To | Reasoning |
|-------------|-----------|-----------|
| "What's the wait time for Thunder Mountain?" | Attraction Expert | Ride-specific information |
| "Can I make a dinner reservation?" | Dining Specialist | Restaurant service request |
| "I want to upgrade my ticket" | Ticket Manager | Ticketing transaction |
| "I lost my wallet" | Guest Services | Lost item assistance |
| "When is the fireworks show?" | Entertainment Coordinator | Entertainment schedule |
| "My child feels sick" | Emergency Responder | Medical emergency |

## Setup and Installation

### Prerequisites

- Python 3.11+
- Poetry (for dependency management)
- Google ADK SDK (installed via Poetry)
- Google Cloud Project (for Vertex AI Gemini integration)

### Installation

1. **Prerequisites:**
   ```bash
   gcloud auth login
   gcloud services enable aiplatform.googleapis.com
   ```

2. **Clone and Install:**
   ```bash
   git clone https://github.com/google/adk-samples.git
   cd adk-samples/python/agents/customer-service
   poetry install
   poetry env activate
   ```

3. **Environment Configuration:**
   ```bash
   export GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_NAME_HERE
   export GOOGLE_GENAI_USE_VERTEXAI=1
   export GOOGLE_CLOUD_LOCATION=us-central1
   ```

## Running the Agent

### CLI Mode
```bash
adk run customer_service
```

### Web UI Mode
```bash
adk web
```

### Demo Routing Pattern
```bash
python demo_routing.py
```

### Example Interaction

**Guest**: "Hi! I'm here with my family for my daughter's birthday. She's 8 years old and wants to ride the big roller coaster, but I'm not sure if she's tall enough."

**System**: *Routes to Attraction Expert*

**Attraction Expert**: "Happy birthday to your daughter! I'd be happy to help check if she meets the height requirements for Thunder Mountain Express. For safety, riders need to be at least 44 inches tall. Would you like me to also suggest some great family-friendly alternatives if she's not quite tall enough yet? I can also help you reserve Fast Passes for the rides she can enjoy!"

**Guest**: "Great! Can we also get a birthday dinner reservation somewhere special?"

**System**: *Routes to Dining Specialist*  

**Dining Specialist**: "How wonderful - a birthday celebration! I'd love to help you make this extra special. Our Character Dining Hall offers birthday packages with character visits and a complimentary birthday cake. Would you like me to check availability for your party?"

## Architecture Benefits

### 🚀 Performance
- **Fast Classification**: Lightweight router for quick query analysis
- **Specialized Processing**: Appropriate model complexity for each domain
- **Parallel Capability**: Multiple specialists can handle different guests simultaneously

### 🎯 Accuracy  
- **Domain Expertise**: Each specialist has focused knowledge and tools
- **Context-Aware**: Routing considers guest profile and current situation
- **Continuous Learning**: Routing improves with guest interaction patterns

### 🔧 Maintainability
- **Modular Design**: Easy to update individual specialists without affecting others
- **Clear Separation**: Each agent has distinct responsibilities and tools
- **Scalable**: Simple to add new specialists or enhance existing ones

### 💰 Cost Efficiency
- **Right-Sized Models**: Use appropriate model complexity for each task
- **Efficient Routing**: Quick classification reduces overall processing time
- **Resource Optimization**: Specialized agents avoid over-engineering

## Configuration

Configuration settings in `customer_service/config.py`:
- **Park Theme**: ThrillZone Adventure Park branding
- **Model Settings**: Router vs. specialist model configurations  
- **Routing Parameters**: Classification thresholds and fallback options

## Testing & Evaluation

### Run Tests
```bash
pytest tests/
```

### Run Routing Demo
```bash
python demo_routing.py
```

### Evaluate Routing Accuracy
```bash
pytest eval/
```

## Deployment

### Build Package
```bash
poetry build --format=wheel --output=deployment
```

### Deploy to Agent Engine
```bash
cd deployment
python deploy.py
```

## Routing Pattern Implementation

This project demonstrates the **routing pattern** from [Agent Recipes](https://www.agentrecipes.com/routing):

1. **Query Classification**: Router agent analyzes guest input
2. **Specialist Selection**: Determines most appropriate expert
3. **Context Transfer**: Passes guest information to specialist
4. **Specialized Response**: Expert provides domain-specific assistance
5. **Unified Experience**: Guest receives seamless, expert service

The pattern enables **cost optimization**, **performance improvement**, and **specialized expertise** while maintaining a unified guest experience.

---

*Experience the magic of ThrillZone Adventure Park with AI-powered customer service that connects you with the right expert, every time!* 🎢✨