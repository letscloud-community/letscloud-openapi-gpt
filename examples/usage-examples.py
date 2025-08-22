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
    
    def __init__(self, api_key: str = None, base_url: str = "https://core.letscloud.io/api"):
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

    # Server Management Methods
    def list_servers(self) -> Dict:
        """List all servers in your account"""
        return self._make_request('GET', '/servers')
    
    def create_server(self, label: str, plan_slug: str, image_slug: str, 
                     location_slug: str, hostname: str = None, 
                     password: str = None, ssh_keys: List[int] = None) -> Dict:
        """Create a new server"""
        data = {
            'label': label,
            'plan_slug': plan_slug,
            'image_slug': image_slug,
            'location_slug': location_slug
        }
        
        if hostname:
            data['hostname'] = hostname
        if password:
            data['password'] = password
        if ssh_keys:
            data['ssh_keys'] = ssh_keys
            
        return self._make_request('POST', '/servers', data)
    
    def get_server(self, server_id: int) -> Dict:
        """Get server details"""
        return self._make_request('GET', f'/servers/{server_id}')
    
    def delete_server(self, server_id: int) -> None:
        """Delete a server"""
        self._make_request('DELETE', f'/servers/{server_id}')
    
    def start_server(self, server_id: int) -> Dict:
        """Start a server"""
        return self._make_request('POST', f'/servers/{server_id}/start')
    
    def stop_server(self, server_id: int) -> Dict:
        """Stop a server"""
        return self._make_request('POST', f'/servers/{server_id}/stop')
    
    def reboot_server(self, server_id: int) -> Dict:
        """Reboot a server"""
        return self._make_request('POST', f'/servers/{server_id}/reboot')

    # SSH Key Management Methods
    def list_ssh_keys(self) -> Dict:
        """List all SSH keys"""
        return self._make_request('GET', '/ssh-keys')
    
    def create_ssh_key(self, title: str, key: str) -> Dict:
        """Create a new SSH key"""
        data = {'title': title, 'key': key}
        return self._make_request('POST', '/ssh-keys', data)
    
    def get_ssh_key(self, key_id: int) -> Dict:
        """Get SSH key details"""
        return self._make_request('GET', f'/ssh-keys/{key_id}')
    
    def delete_ssh_key(self, key_id: int) -> None:
        """Delete an SSH key"""
        self._make_request('DELETE', f'/ssh-keys/{key_id}')

    # Snapshot Management Methods
    def list_snapshots(self, server_id: int) -> Dict:
        """List server snapshots"""
        return self._make_request('GET', f'/servers/{server_id}/snapshots')
    
    def create_snapshot(self, server_id: int, label: str, description: str = None) -> Dict:
        """Create a server snapshot"""
        data = {'label': label}
        if description:
            data['description'] = description
        return self._make_request('POST', f'/servers/{server_id}/snapshots', data)
    
    def get_snapshot(self, server_id: int, snapshot_id: int) -> Dict:
        """Get snapshot details"""
        return self._make_request('GET', f'/servers/{server_id}/snapshots/{snapshot_id}')
    
    def delete_snapshot(self, server_id: int, snapshot_id: int) -> None:
        """Delete a snapshot"""
        self._make_request('DELETE', f'/servers/{server_id}/snapshots/{snapshot_id}')
    
    def restore_snapshot(self, server_id: int, snapshot_id: int) -> Dict:
        """Restore server from snapshot"""
        return self._make_request('POST', f'/servers/{server_id}/snapshots/{snapshot_id}/restore')

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

        # Example 3: List existing servers
        print("\n🖥️  Listing existing servers...")
        servers = client.list_servers()
        server_count = len(servers.get('servers', []))
        print(f"Found {server_count} server(s)")
        
        for server in servers.get('servers', []):
            print(f"  - {server.get('label', 'Unnamed')} (ID: {server.get('id')}) - {server.get('status', 'Unknown')}")

        # Example 4: List SSH keys
        print("\n🔑 Listing SSH keys...")
        ssh_keys = client.list_ssh_keys()
        key_count = len(ssh_keys.get('ssh_keys', []))
        print(f"Found {key_count} SSH key(s)")
        
        for key in ssh_keys.get('ssh_keys', []):
            print(f"  - {key.get('title', 'Untitled')} (ID: {key.get('id')})")

        # Example 5: Create a new SSH key (commented out for safety)
        """
        print("\n🔑 Creating a new SSH key...")
        new_key = client.create_ssh_key(
            title="Example Key",
            key="ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC..."
        )
        print(f"Created SSH key: {new_key.get('title')} (ID: {new_key.get('id')})")
        """

        # Example 6: Create a new server (commented out for safety)
        """
        print("\n🖥️  Creating a new server...")
        new_server = client.create_server(
            label="Example Server",
            plan_slug="basic-1gb",
            image_slug="ubuntu-22-04",
            location_slug="nyc1",
            hostname="example-server"
        )
        print(f"Created server: {new_server.get('label')} (ID: {new_server.get('id')})")
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
            "action": "listServers",
            "description": "Check existing servers before creating new ones",
            "parameters": {}
        },
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
            "action": "createServer",
            "description": "Create a new server with optimal configuration",
            "parameters": {
                "label": "AI-Powered Web Server",
                "plan_slug": "standard-2gb",
                "image_slug": "ubuntu-22-04",
                "location_slug": "nyc1",
                "hostname": "ai-webserver-01"
            }
        },
        {
            "action": "createSnapshot",
            "description": "Create a backup snapshot after server setup",
            "parameters": {
                "server_id": "{server_id_from_previous_action}",
                "label": "Initial setup backup",
                "description": "Backup created after initial server configuration"
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
