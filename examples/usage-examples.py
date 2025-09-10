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
    def list_instances(self) -> Dict:
        """List all your instances"""
        return self._make_request('GET', '/instances')
    
    def get_instance_details(self, identifier: str) -> Dict:
        """Get detailed information about a specific instance"""
        return self._make_request('GET', f'/instances/{identifier}')
    
    def create_instance(self, location_slug: str, plan_slug: str, hostname: str, 
                       label: str, image_slug: str, password: str, ssh_slug: List[str] = None) -> Dict:
        """Create a new instance with specified configuration"""
        data = {
            'location_slug': location_slug,
            'plan_slug': plan_slug,
            'hostname': hostname,
            'label': label,
            'image_slug': image_slug,
            'password': password
        }
        if ssh_slug:
            data['ssh_slug'] = ssh_slug
        return self._make_request('POST', '/instances', data)
    
    def delete_instance(self, identifier: str) -> Dict:
        """Delete an instance from your account"""
        return self._make_request('DELETE', f'/instances/{identifier}')
    
    def power_on_instance(self, identifier: str) -> Dict:
        """Turn on a specific instance"""
        return self._make_request('PUT', f'/instances/{identifier}/power-on')
    
    def power_off_instance(self, identifier: str) -> Dict:
        """Turn off a specific instance"""
        return self._make_request('PUT', f'/instances/{identifier}/power-off')
    
    def reboot_instance(self, identifier: str) -> Dict:
        """Reboot a specific instance"""
        return self._make_request('PUT', f'/instances/{identifier}/reboot')
    
    def reset_instance_password(self, identifier: str, password: str) -> Dict:
        """Change the root password of a specific instance"""
        data = {
            'password': password,
            '_method': 'PUT'
        }
        return self._make_request('POST', f'/instances/{identifier}/reset-password', data)
    
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
    def get_profile_info(self) -> Dict:
        """Get profile information"""
        return self._make_request('GET', '/profile')


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
        # Example 1: Get profile information
        print("\n📋 Getting profile information...")
        profile = client.get_profile_info()
        print(f"Profile: {profile.get('name', 'N/A')} ({profile.get('email', 'N/A')})")
        print(f"Balance: {profile.get('currency', '$')}{profile.get('balance', '0.00')}")

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
        if location_images.get('data'):
            print(f"Available images: {len(location_images['data'])}")
            for image in location_images['data'][:3]:  # Show first 3 images
                print(f"  - {image.get('distro')} ({image.get('os')})")

        # Example 5: Instance Management
        print("\n🖥️  Instance Management Examples...")
        
        # List all instances
        print("\n📋 Listing all instances...")
        instances = client.list_instances()
        if instances.get('data'):
            print(f"Found {len(instances['data'])} instances:")
            for instance in instances['data']:
                status = "🟢 Running" if instance.get('booted') else "🔴 Stopped"
                print(f"  - {instance.get('label', 'Unnamed')} ({instance.get('identifier')}) - {status}")
                print(f"    Plan: {instance.get('cpus')} vCPU, {instance.get('memory')}MB RAM, {instance.get('total_disk_size')}GB disk")
                print(f"    OS: {instance.get('template_label')} | Location: {instance.get('location', {}).get('city', 'Unknown')}")
        else:
            print("No instances found.")
        
        # Example 6: Create a new instance (commented out to avoid charges)
        print("\n🆕 Example: Creating a new instance (commented out to avoid charges)")
        print("# Uncomment the following lines to create a new instance:")
        print("# new_instance = client.create_instance(")
        print("#     location_slug='MIA1',")
        print("#     plan_slug='1vcpu-1gb-10ssd',")
        print("#     hostname='my-test-server',")
        print("#     label='Test Server',")
        print("#     image_slug='ubuntu-20-04-x64',")
        print("#     password='SecurePassword123!'")
        print("# )")
        print("# print(f'Instance creation result: {new_instance}')")
        
        # Example 7: Instance power management (commented out to avoid changes)
        print("\n⚡ Example: Instance power management (commented out to avoid changes)")
        print("# Uncomment the following lines to manage instance power state:")
        print("# if instances.get('data'):")
        print("#     instance_id = instances['data'][0]['identifier']")
        print("#     # Power on instance")
        print("#     power_on_result = client.power_on_instance(instance_id)")
        print("#     print(f'Power on result: {power_on_result}')")
        print("#     # Reboot instance")
        print("#     reboot_result = client.reboot_instance(instance_id)")
        print("#     print(f'Reboot result: {reboot_result}')")

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
