#!/usr/bin/env python3
"""
LetsCloud API Usage Examples
This file contains practical examples of how to use the LetsCloud API
based on the OpenAPI specification for GPT Actions integration.
"""

import requests
import json
import os
from typing import Dict, List, Optional

class LetsCloudAPI:
    """LetsCloud API client based on the OpenAPI specification"""
    
    def __init__(self, api_key: str = None, base_url: str = "https://api.letscloud.io"):
        """
        Initialize the LetsCloud API client
        
        Args:
            api_key: Your LetsCloud API key. If not provided, will try to get from LETSCLOUD_API_KEY env var
            base_url: Base URL for the API (production or staging)
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key or os.getenv('LETSCLOUD_API_KEY')
        
        if not self.api_key:
            raise ValueError("API key is required. Provide it directly or set LETSCLOUD_API_KEY environment variable.")
        
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
    
    def _make_request(self, method: str, endpoint: str, data: Dict = None) -> Dict:
        """Make an HTTP request to the LetsCloud API"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json() if response.content else {}
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            raise



    # SSH Key Management Methods
    def store_or_generate_ssh_key(self, title: str, key: str = None) -> Dict:
        """Store your current SSH key or generate a new one"""
        data = {'title': title}
        if key:
            data['key'] = key
        return self._make_request('POST', '/sshkeys', data)
    
    def delete_ssh_key_by_slug(self, slug: str) -> Dict:
        """Delete an SSH key using its slug"""
        data = {'slug': slug, '_method': 'DELETE'}
        return self._make_request('DELETE', '/sshkeys', data)



    # Instance Management Methods
    def shutdown_instance(self, identifier: str) -> Dict:
        """Shutdown a running instance"""
        return self._make_request('POST', f'/instances/{identifier}/shutdown')
    
    def change_instance_plan(self, identifier: str, plan_slug: str) -> Dict:
        """Change the plan of an existing instance"""
        data = {
            '_method': 'PUT',
            'plan_slug': plan_slug
        }
        return self._make_request('POST', f'/instances/{identifier}/change-plan', data)

    # Resource Discovery Methods
    def list_plans(self) -> Dict:
        """List available plans"""
        return self._make_request('GET', '/plans')
    
    def list_images(self) -> Dict:
        """List available images"""
        return self._make_request('GET', '/images')
    
    def list_locations(self) -> Dict:
        """List available locations"""
        return self._make_request('GET', '/locations')
    
    def list_plans_by_location(self, location_slug: str) -> Dict:
        """List plans by location"""
        return self._make_request('GET', f'/locations/{location_slug}/plans')
    
    def list_images_by_location(self, location_slug: str) -> Dict:
        """List images by location"""
        return self._make_request('GET', f'/locations/{location_slug}/images')

    # Account Information Methods
    def get_account_info(self) -> Dict:
        """Get account information"""
        return self._make_request('GET', '/account')


def main():
    """Example usage of the LetsCloud API client"""
    
    # Initialize the API client
    # You can set your API key as an environment variable: export LETSCLOUD_API_KEY=your_key
    try:
        client = LetsCloudAPI()
        print("✅ Successfully initialized LetsCloud API client")
    except ValueError as e:
        print(f"❌ Error: {e}")
        return

    try:
        # Example 1: Get account information
        print("\n📋 Getting account information...")
        account = client.get_account_info()
        print(f"Account: {account.get('name', 'N/A')} ({account.get('email', 'N/A')})")
        print(f"Balance: ${account.get('balance', 0):.2f} {account.get('currency', 'USD')}")

        # Example 2: Discover available resources
        print("\n🔍 Discovering available resources...")
        
        plans = client.list_plans()
        print(f"Available plans: {len(plans.get('plans', []))}")
        
        images = client.list_images()
        print(f"Available images: {len(images.get('images', []))}")
        
        locations = client.list_locations()
        print(f"Available locations: {len(locations.get('locations', []))}")

        # Example 3: List plans by location
        print("\n📍 Listing plans by location...")
        location_plans = client.list_plans_by_location("MIA1")
        if location_plans.get('data'):
            location_data = location_plans['data'][0]
            print(f"Location: {location_data.get('city')}, {location_data.get('country')}")
            print(f"Available plans: {len(location_data.get('plans', []))}")

        # Example 4: List images by location
        print("\n🖼️  Listing images by location...")
        location_images = client.list_images_by_location("MIA2")
        print(f"Available images: {len(location_images.get('data', []))}")

        # Example 5: Store or generate SSH key (commented out for safety)
        """
        print("\n🔑 Storing SSH key...")
        new_key = client.store_or_generate_ssh_key(
            title="Example Key",
            key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC..."
        )
        print(f"Stored SSH key: {new_key.get('title')} (Slug: {new_key.get('slug')})")
        """

        print("\n✅ All examples completed successfully!")

    except Exception as e:
        print(f"❌ Error during API operations: {e}")


def gpt_actions_example():
    """Example of how GPT Actions would use the API"""
    
    # This is a conceptual example of how GPT Actions would interact with the API
    # based on the OpenAPI specification
    
    actions_workflow = [
        {
            "action": "listPlans",
            "description": "Get available server plans for cost optimization",
            "parameters": {}
        },
        {
            "action": "listImages",
            "description": "Find the best OS image for the use case",
            "parameters": {}
        },
        {
            "action": "listLocations",
            "description": "Get available server locations",
            "parameters": {}
        },
        {
            "action": "listPlansByLocation",
            "description": "Get plans available in a specific location",
            "parameters": {
                "location_slug": "MIA1"
            }
        },
        {
            "action": "listImagesByLocation",
            "description": "Get images available in a specific location",
            "parameters": {
                "location_slug": "MIA2"
            }
        },
        {
            "action": "storeOrGenerateSSHKey",
            "description": "Store or generate a new SSH key",
            "parameters": {
                "title": "My Project Key"
            }
        },
        {
            "action": "shutdownInstance",
            "description": "Shutdown a running instance",
            "parameters": {
                "identifier": "your-instance-identifier"
            }
        },
        {
            "action": "changeInstancePlan",
            "description": "Change instance plan for cost optimization",
            "parameters": {
                "identifier": "your-instance-identifier",
                "plan_slug": "1vcpu-2gb-20ssd"
            }
        }
    ]
    
    print("🤖 GPT Actions Workflow Example:")
    for i, action in enumerate(actions_workflow, 1):
        print(f"{i}. {action['action']}: {action['description']}")


if __name__ == "__main__":
    print("🚀 LetsCloud API Examples")
    print("=" * 50)
    
    # Run the main examples
    main()
    
    # Show GPT Actions workflow example
    gpt_actions_example()
