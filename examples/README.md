# LetsCloud API Python Examples

This directory contains Python examples for using the LetsCloud API through the proxy server.

## Files

- `usage-examples.py` - Complete client implementation with examples
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Get Your API Key

1. Go to [LetsCloud Dashboard](https://my.letscloud.io)
2. Navigate to **Settings** → **API Keys**
3. Generate a new API key
4. Copy the key (keep it secure!)

### 3. Configure the Examples

Edit `usage-examples.py` and replace `"your-api-key-here"` with your actual API key:

```python
API_KEY = "sk_live_your_actual_api_key_here"
```

### 4. Run the Examples

```bash
python usage-examples.py
```

## Available Examples

### Basic Usage

```python
from usage_examples import LetsCloudClient

# Initialize client
client = LetsCloudClient()

# Configure API key
client.set_api_key("your-api-key")

# List instances
instances = client.list_instances()
print(instances)
```

### Create a Server

```python
# Create server configuration
config = {
    "location_slug": "us-east",
    "plan_slug": "2vcpu-4gb-30ssd",
    "hostname": "my-server",
    "label": "My Server",
    "image_slug": "ubuntu-22.04",
    "password": "SecurePassword123!"
}

# Create the instance
result = client.create_instance(config)
print(f"Server created: {result}")
```

### Manage SSH Keys

```python
# List SSH keys
keys = client.list_ssh_keys()

# Create new SSH key
new_key = client.create_ssh_key(
    title="My Laptop",
    public_key="ssh-rsa AAAAB3NzaC1yc2E..."
)
```

### Power Management

```python
# Power on instance
client.power_on_instance("server-123")

# Power off instance
client.power_off_instance("server-123")

# Reboot instance
client.reboot_instance("server-123")
```

## API Methods

The `LetsCloudClient` class provides the following methods:

### Authentication
- `set_api_key(api_key)` - Configure API key
- `check_api_key_status()` - Check if API key is configured

### Instance Management
- `list_instances()` - List all instances
- `get_instance(instance_id)` - Get instance details
- `create_instance(config)` - Create new instance
- `delete_instance(instance_id)` - Delete instance
- `power_on_instance(instance_id)` - Power on instance
- `power_off_instance(instance_id)` - Power off instance
- `reboot_instance(instance_id)` - Reboot instance

### Resource Discovery
- `list_plans()` - List available plans
- `list_images()` - List available images
- `list_locations()` - List available locations

### SSH Key Management
- `list_ssh_keys()` - List SSH keys
- `create_ssh_key(title, public_key)` - Create SSH key
- `delete_ssh_key(key_id)` - Delete SSH key

### Account Information
- `get_account_info()` - Get account information

## Error Handling

The client includes proper error handling:

```python
try:
    instances = client.list_instances()
    print(instances)
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"Error: {e}")
```

## Security Notes

- **Never commit API keys** to version control
- **Use environment variables** for production deployments
- **Rotate API keys** regularly
- **Monitor usage** in your LetsCloud dashboard

## Environment Variables

For production use, consider using environment variables:

```python
import os

API_KEY = os.getenv('LETSCLOUD_API_TOKEN')
if not API_KEY:
    raise ValueError("LETSCLOUD_API_TOKEN environment variable is required")
```

## Support

- **Documentation**: [LetsCloud API Docs](https://developers.letscloud.io)
- **Support**: support@letscloud.io
- **GitHub**: [LetsCloud Community](https://github.com/letscloud-community/letscloud-openapi-gpt)
