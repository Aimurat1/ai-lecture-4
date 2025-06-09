# AI Lecture 4 - Advanced AI Agent Systems

This project demonstrates two advanced AI agent patterns using Google's Agent Development Kit (ADK): a **Routing Pattern** for customer service and a **Parallel Processing Pattern** for travel planning. These implementations showcase different approaches to building intelligent, scalable multi-agent systems.

## 🎯 Learning Objectives

- Understand multi-agent system architectures
- Implement routing patterns for intelligent query classification
- Build parallel processing systems for concurrent task execution
- Integrate real-time web search with AI agents
- Apply Google ADK framework for agent development
- Compare performance optimization techniques across different patterns

## 📋 Project Overview

This educational project contains two distinct AI agent systems:

### 🎢 Customer Service Agent (Routing Pattern)
An intelligent customer service system for ThrillZone Adventure Park that uses the **routing pattern** to classify guest queries and direct them to specialized agents for expert assistance.

### ✈️ Travel Planning Agent (Parallel Processing Pattern) 
A comprehensive travel planning system that uses **parallel processing** to research multiple aspects of a trip simultaneously, then aggregates results into a unified travel plan.

## 🏗️ Project Structure

```
ai-lecture-4/
├── customer-service/          # Routing Pattern Implementation
│   ├── customer_service/      # Main customer service module
│   ├── tests/                 # Unit tests
│   ├── eval/                  # Evaluation scripts
│   ├── deployment/            # Deployment configurations
│   ├── demo_routing.py        # Routing pattern demo
│   └── README.md             # Detailed customer service docs
├── travel-planning/           # Parallel Processing Implementation
│   └── travel_planning/       # Main travel planning module
│       ├── specialists/       # Individual specialist agents
│       ├── entities/          # Data models and entities
│       ├── aggregation/       # Result aggregation logic
│       ├── agent.py          # Main agent coordination
│       └── demo_parallel_travel.py  # Parallel processing demo
├── main.py                   # Project entry point
├── pyproject.toml           # Project dependencies
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.13+**
- **Google ADK SDK**

### Installation

1. **Clone and navigate to the project:**
   ```bash
   git clone <repository-url>
   cd ai-lecture-4
   ```

2. **Install dependencies:**
   ```bash
   # Using uv (recommended)
   uv sync

4. **Configure environment variables:**
   ```bash
   export GOOGLE_API_KEY=YOUR_API_KEY
   ```

   API key can be obtained from https://aistudio.google.com/apikey

### Running the Systems

#### Customer Service Agent (Routing Pattern)
```bash
# CLI Mode
cd customer-service

# Web UI Mode  
adk web

```

#### Travel Planning Agent (Parallel Processing)
```bash
# Run Parallel Travel Planning Demo
cd travel-planning

adk web
```

## 🎯 System Architectures

### Customer Service Agent - Routing Pattern

The customer service system uses intelligent routing to connect guests with specialized agents:

```
Guest Query → Router Agent → Specialist Agent → Response
              (Classification)   (Domain Expert)
```

**Specialists:**
- 🎢 **Attraction Expert** - Ride wait times, reservations, recommendations
- 🍽️ **Dining Specialist** - Restaurant reservations, dietary accommodations  
- 🎫 **Ticket Manager** - Upgrades, discounts, group bookings
- 🏨 **Guest Services** - Lost & found, accessibility, general assistance
- 🎭 **Entertainment Coordinator** - Shows, events, character meet & greets
- 🚨 **Emergency Responder** - Medical assistance, safety incidents

**Benefits:**
- ⚡ Fast query classification with lightweight router
- 🎯 Specialized expertise for accurate responses
- 🔧 Modular design for easy maintenance
- 💰 Cost-efficient with right-sized models

### Travel Planning Agent - Parallel Processing Pattern

The travel planning system uses parallel execution for comprehensive trip research:

```
Travel Request → ParallelAgent → [5 Specialists] → TravelCoordinator → Unified Plan
                                 (Concurrent)      (Aggregation)
```

**Specialists (Running in Parallel):**
- 🏨 **Accommodation Specialist** + Google Search
- 🎯 **Attractions Specialist** + Google Search  
- 🍽️ **Dining Specialist** + Google Search
- 🚗 **Transportation Specialist** + Google Search
- 💰 **Budget Specialist** + Google Search

**Benefits:**
- 🚀 60-70% faster than sequential processing
- 🌐 Real-time web data for current pricing/availability
- 🎯 Comprehensive coverage with domain expertise
- ⚖️ Intelligent aggregation resolves conflicts

## 💡 Example Interactions

### Customer Service Routing Example

**Guest:** "Hi! My daughter wants to ride the big roller coaster, but I'm not sure if she's tall enough."

**System:** *Routes to Attraction Expert*

**Attraction Expert:** "I'd be happy to help! Thunder Mountain Express requires riders to be at least 44 inches tall. Would you like me to suggest family-friendly alternatives and help you reserve Fast Passes?"

### Travel Planning Parallel Example

**Request:** "Plan a 5-day family trip to Orlando, Florida for 4 people, $3,000 budget"

**Parallel Processing:**
- 🏨 Accommodation: Researches family hotels near theme parks
- 🎢 Attractions: Finds Disney World/Universal ticket deals  
- 🍽️ Dining: Locates character dining and vegetarian options
- 🚗 Transportation: Compares flights from departure city
- 💰 Budget: Analyzes costs and finds money-saving opportunities

**Result:** Comprehensive 5-day itinerary with coordinated recommendations

## 🛠️ Development

### Running Tests

```bash
# Customer Service Tests
cd customer-service
pytest tests/

# Evaluate Routing Accuracy  
pytest eval/
```

## 📚 Educational Value

### Key Concepts Demonstrated

1. **Multi-Agent Architectures**
   - Router-specialist pattern vs parallel execution
   - Agent coordination and communication
   - Specialized vs generalized intelligence

2. **Performance Optimization**
   - Model right-sizing for different tasks
   - Parallel vs sequential processing trade-offs
   - Real-time data integration challenges

3. **System Design Patterns**
   - Modular, scalable architecture
   - Separation of concerns
   - Error handling and fallback strategies

4. **Real-World Applications**
   - Customer service automation
   - Travel industry solutions
   - Enterprise AI system design

### Learning Outcomes

After working with this project, students will understand:
- How to design and implement multi-agent systems
- Trade-offs between different AI agent patterns
- Integration of AI agents with external data sources
- Performance considerations in agent system design
- Practical applications of advanced AI patterns

## 🔧 Configuration

### Customer Service Configuration
Located in `customer-service/customer_service/config.py`:
- Park theme and branding settings
- Router vs specialist model configurations
- Classification thresholds and fallback options

### Travel Planning Configuration  
Located in `travel-planning/travel_planning/config.py`:
- Specialist agent configurations
- Google Search integration settings
- Parallel processing parameters

## 📦 Dependencies

Key dependencies managed in `pyproject.toml`:
- **google-adk>=1.2.1** - Google Agent Development Kit
- **jsonschema>=4.24.0** - Data validation
- Additional dependencies for web search, async processing, and testing

## 🚀 Deployment

### Customer Service Deployment
```bash
cd customer-service
poetry build --format=wheel --output=deployment
cd deployment
python deploy.py
```

### Travel Planning Integration
The travel planning system can be integrated into larger applications or deployed as a standalone service using the Google ADK framework.

## 🤝 Contributing

This is an educational project. Students are encouraged to:
- Experiment with different agent configurations
- Add new specialist agents
- Implement additional AI patterns
- Optimize performance and accuracy
- Create new demo scenarios

## 📄 License

This project is created for educational purposes as part of AI Lecture 4 curriculum.

## 🔗 Additional Resources

- [Google ADK Documentation](https://github.com/google/adk)
- [Agent Design Patterns](https://www.agentrecipes.com/)
- [Multi-Agent Systems](https://en.wikipedia.org/wiki/Multi-agent_system)
- [Vertex AI Gemini](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini)

---

**Note:** This project demonstrates advanced AI agent patterns for educational purposes. Both systems showcase different approaches to building intelligent, scalable multi-agent systems using modern AI frameworks and real-time data integration.
