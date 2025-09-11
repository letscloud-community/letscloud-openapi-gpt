#!/usr/bin/env python3
"""
LetsCloud API Client Examples

This script demonstrates how to use the LetsCloud API through the proxy server
for managing cloud infrastructure programmatically.

Requirements:
- Python 3.7+
- requests library
- Valid LetsCloud API key

Usage:
    python usage-examples.py
"""

import requests
import json
import time
import uuid
from typing import Dict, Any, Optional

class LetsCloudClient:
    """Client for interacting with LetsCloud API through proxy server."""
    
    def __init__(self, proxy_url: str = "https://action.letscloud.io"):
        """
        Initialize the LetsCloud client.
        
        Args:
            proxy_url: URL of the proxy server
        """
        self.proxy_url = proxy_url
        self.user_id = str(uuid.uuid4())
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'LetsCloud-Python-Client/1.0'
        })
    
    def set_api_key(self, api_key: str) -> Dict[str, Any]:
        """
        Configure API key for authentication.
        
        Args:
            api_key: Your LetsCloud API key
            
        Returns:
            Response from the proxy server
        """
        url = f"{self.proxy_url}/set-apikey"
        payload = {
            "userId": self.user_id,
            "apiKey": api_key
        }
        
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    
    def _make_request(self, method: str, path: str, body: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Make a request to the LetsCloud API through the proxy.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            path: API endpoint path
            body: Request body for POST/PUT requests
            
        Returns:
            Response from the LetsCloud API
        """
        url = f"{self.proxy_url}/proxy"
        payload = {
            "userId": self.user_id,
            "path": path,
            "method": method
        }
        
        if body:
            payload["body"] = body
        
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    
    def list_instances(self) -> Dict[str, Any]:
        """List all instances."""
        return self._make_request("GET", "/v2/instances")
    
    def get_instance(self, instance_id: str) -> Dict[str, Any]:
        """Get details of a specific instance."""
        return self._make_request("GET", f"/v2/instances/{instance_id}")
    
    def create_instance(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new instance.
        
        Args:
            config: Instance configuration including:
                - location_slug: Location for the instance
                - plan_slug: Plan/size for the instance
                - hostname: Hostname for the instance
                - label: Display label
                - image_slug: OS image to use
                - password: Root password
        """
        return self._make_request("POST", "/v2/instances", config)
    
    def delete_instance(self, instance_id: str) -> Dict[str, Any]:
        """Delete an instance."""
        return self._make_request("DELETE", f"/v2/instances/{instance_id}")
    
    def power_on_instance(self, instance_id: str) -> Dict[str, Any]:
        """Power on an instance."""
        return self._make_request("POST", f"/v2/instances/{instance_id}/power-on")
    
    def power_off_instance(self, instance_id: str) -> Dict[str, Any]:
        """Power off an instance."""
        return self._make_request("POST", f"/v2/instances/{instance_id}/power-off")
    
    def reboot_instance(self, instance_id: str) -> Dict[str, Any]:
        """Reboot an instance."""
        return self._make_request("POST", f"/v2/instances/{instance_id}/reboot")
    
    def list_plans(self) -> Dict[str, Any]:
        """List available plans."""
        return self._make_request("GET", "/v2/plans")
    
    def list_images(self) -> Dict[str, Any]:
        """List available images."""
        return self._make_request("GET", "/v2/images")
    
    def list_locations(self) -> Dict[str, Any]:
        """List available locations."""
        return self._make_request("GET", "/v2/locations")
    
    def list_ssh_keys(self) -> Dict[str, Any]:
        """List SSH keys."""
        return self._make_request("GET", "/v2/ssh-keys")
    
    def create_ssh_key(self, title: str, public_key: str) -> Dict[str, Any]:
        """Create a new SSH key."""
        return self._make_request("POST", "/v2/ssh-keys", {
            "title": title,
            "key": public_key
        })
    
    def delete_ssh_key(self, key_id: int) -> Dict[str, Any]:
        """Delete an SSH key."""
        return self._make_request("DELETE", f"/v2/ssh-keys/{key_id}")
    
    def get_account_info(self) -> Dict[str, Any]:
        """Get account information."""
        return self._make_request("GET", "/v2/account")
    
    def check_api_key_status(self) -> Dict[str, Any]:
        """Check if API key is configured."""
        url = f"{self.proxy_url}/apikey-status"
        params = {"userId": self.user_id}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()


def main():
    """Main function demonstrating API usage."""
    
    # Initialize client
    client = LetsCloudClient()
    
    # You need to set your API key here
    API_KEY = "your-api-key-here"  # Replace with your actual API key
    
    print("🚀 LetsCloud API Client Examples")
    print("=" * 50)
    
    try:
        # Step 1: Configure API key
        print("\n1. Configuring API key...")
        result = client.set_api_key(API_KEY)
        print(f"✅ API key configured: {result}")
        
        # Step 2: Check API key status
        print("\n2. Checking API key status...")
        status = client.check_api_key_status()
        print(f"✅ API key status: {status}")
        
        # Step 3: Get account information
        print("\n3. Getting account information...")
        account_info = client.get_account_info()
        print(f"✅ Account info: {json.dumps(account_info, indent=2)}")
        
        # Step 4: List available resources
        print("\n4. Listing available resources...")
        
        # List locations
        locations = client.list_locations()
        print(f"📍 Available locations: {len(locations.get('data', []))}")
        
        # List plans
        plans = client.list_plans()
        print(f"💻 Available plans: {len(plans.get('data', []))}")
        
        # List images
        images = client.list_images()
        print(f"🖼️  Available images: {len(images.get('data', []))}")
        
        # Step 5: List existing instances
        print("\n5. Listing existing instances...")
        instances = client.list_instances()
        print(f"🖥️  Existing instances: {len(instances.get('data', []))}")
        
        for instance in instances.get('data', []):
            print(f"   - {instance.get('label', 'Unnamed')} ({instance.get('status', 'unknown')})")
        
        # Step 6: List SSH keys
        print("\n6. Listing SSH keys...")
        ssh_keys = client.list_ssh_keys()
        print(f"🔑 SSH keys: {len(ssh_keys.get('data', []))}")
        
        for key in ssh_keys.get('data', []):
            print(f"   - {key.get('title', 'Unnamed')}")
        
        # Example: Create a new instance (commented out to avoid charges)
        """
        print("\n7. Creating a new instance...")
        instance_config = {
            "location_slug": "us-east",
            "plan_slug": "2vcpu-4gb-30ssd",
            "hostname": "python-test-server",
            "label": "Python Test Server",
            "image_slug": "ubuntu-22.04",
            "password": "SecurePassword123!"
        }
        
        new_instance = client.create_instance(instance_config)
        print(f"✅ Instance created: {new_instance}")
        """
        
        print("\n🎉 All examples completed successfully!")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Request error: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")


def example_create_server():
    """Example of creating a server with specific configuration."""
    
    client = LetsCloudClient()
    API_KEY = "your-api-key-here"  # Replace with your actual API key
    
    try:
        # Configure API key
        client.set_api_key(API_KEY)
        
        # Create server configuration
        server_config = {
            "location_slug": "us-east",           # Location
            "plan_slug": "2vcpu-4gb-30ssd",      # Plan (2 vCPU, 4GB RAM, 30GB SSD)
            "hostname": "my-web-server",          # Hostname
            "label": "My Web Server",             # Display label
            "image_slug": "ubuntu-22.04",        # Ubuntu 22.04 LTS
            "password": "MySecurePassword123!"    # Root password
        }
        
        print("Creating server with configuration:")
        print(json.dumps(server_config, indent=2))
        
        # Create the instance
        result = client.create_instance(server_config)
        print(f"✅ Server created successfully: {result}")
        
        # Get the instance ID
        instance_id = result.get('data', {}).get('id')
        if instance_id:
            print(f"Instance ID: {instance_id}")
            
            # Wait a moment for the instance to be created
            print("Waiting for instance to be ready...")
            time.sleep(10)
            
            # Get instance details
            instance_details = client.get_instance(instance_id)
            print(f"Instance details: {json.dumps(instance_details, indent=2)}")
        
    except Exception as e:
        print(f"❌ Error creating server: {e}")


def example_manage_ssh_keys():
    """Example of managing SSH keys."""
    
    client = LetsCloudClient()
    API_KEY = "your-api-key-here"  # Replace with your actual API key
    
    try:
        # Configure API key
        client.set_api_key(API_KEY)
        
        # List existing SSH keys
        print("Existing SSH keys:")
        ssh_keys = client.list_ssh_keys()
        for key in ssh_keys.get('data', []):
            print(f"  - {key.get('title')} (ID: {key.get('id')})")
        
        # Example: Create a new SSH key (you would use your actual public key)
        """
        public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC..."  # Your actual public key
        new_key = client.create_ssh_key("My Laptop", public_key)
        print(f"✅ SSH key created: {new_key}")
        """
        
    except Exception as e:
        print(f"❌ Error managing SSH keys: {e}")


if __name__ == "__main__":
    # Run the main examples
    main()
    
    # Uncomment to run specific examples
    # example_create_server()
    # example_manage_ssh_keys()
