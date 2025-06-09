#!/usr/bin/env python3
"""
Demo script to showcase ThrillZone Adventure Park routing pattern.

This demonstrates how different guest queries are automatically routed 
to appropriate specialist agents using the routing pattern from Agent Recipes.
"""

import sys
import os

# Add the customer_service module to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'customer_service'))

from customer_service.main_agent import thrillzone_service
from customer_service.entities.guest import Guest

def demo_routing_pattern():
    """Demonstrate the routing pattern with various guest queries."""
    
    print("🎢 ThrillZone Adventure Park - Routing Pattern Demo 🎢")
    print("=" * 60)
    
    # Sample guest queries that should route to different specialists
    demo_queries = [
        {
            "query": "What's the wait time for Thunder Mountain Express?",
            "expected_route": "attraction_expert",
            "description": "Ride wait time query"
        },
        {
            "query": "Can I make a dinner reservation for 4 people at 6 PM?",
            "expected_route": "dining_specialist", 
            "description": "Restaurant reservation request"
        },
        {
            "query": "I want to upgrade my day pass to a VIP pass",
            "expected_route": "ticket_manager",
            "description": "Ticket upgrade request"
        },
        {
            "query": "I lost my wallet near the carousel",
            "expected_route": "guest_services",
            "description": "Lost item report"
        },
        {
            "query": "When is the fireworks show tonight?",
            "expected_route": "entertainment_coordinator",
            "description": "Entertainment schedule inquiry"
        },
        {
            "query": "My child is feeling sick and needs medical help",
            "expected_route": "emergency_responder",
            "description": "Medical emergency"
        },
        {
            "query": "Can you help me find vegetarian food options?",
            "expected_route": "dining_specialist",
            "description": "Dietary accommodation request"
        },
        {
            "query": "Is my 8-year-old tall enough for the roller coaster?",
            "expected_route": "attraction_expert",
            "description": "Height requirement check"
        }
    ]
    
    # Load guest context
    guest = Guest.get_guest("123")
    print(f"Guest: {guest.first_name} {guest.last_name}")
    print(f"Membership: {guest.membership_type}")
    print(f"Party Size: {guest.current_visit.party_size if guest.current_visit else 1}")
    print(f"Special Occasion: {guest.current_visit.special_occasion if guest.current_visit else 'None'}")
    print("-" * 60)
    
    # Test each query
    for i, demo in enumerate(demo_queries, 1):
        print(f"\n{i}. {demo['description']}")
        print(f"Query: \"{demo['query']}\"")
        print(f"Expected Route: {demo['expected_route']}")
        
        try:
            # Get routing result
            routing_result = thrillzone_service.router.route_query(
                demo['query'], 
                {
                    "membership_type": guest.membership_type,
                    "party_size": guest.current_visit.party_size if guest.current_visit else 1
                }
            )
            
            actual_route = routing_result.get('route')
            confidence = routing_result.get('confidence', 0)
            reason = routing_result.get('reason', '')
            
            print(f"Actual Route: {actual_route}")
            print(f"Confidence: {confidence:.2f}")
            print(f"Reason: {reason}")
            
            # Check if routing was correct
            if actual_route == demo['expected_route']:
                print("✅ Routing: CORRECT")
            else:
                print("❌ Routing: INCORRECT")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print("-" * 40)
    
    print("\n🎯 Routing Pattern Demo Complete!")
    print("\nThis demonstrates how the routing pattern automatically classifies")
    print("guest queries and directs them to the most appropriate specialist agent.")


if __name__ == "__main__":
    demo_routing_pattern() 