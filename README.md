# LetsCloud API - OpenAPI Specification for GPT Actions

This project provides a comprehensive OpenAPI 3.0 specification for the LetsCloud API, designed specifically for integration with GPT Actions. The specification covers all major cloud infrastructure management operations available through the [LetsCloud Go library](https://github.com/letscloud-community/letscloud-go).

## 📋 Overview

The LetsCloud API allows you to manage cloud infrastructure including:
- **Server Management**: Create, delete, start, stop, and reboot servers
- **SSH Key Management**: Add, list, and delete SSH keys
- **Snapshot Management**: Create, restore, and delete server snapshots
- **Resource Discovery**: List available plans, images, and locations
- **Account Information**: Get account details and billing information

## 🚀 Quick Start

### 1. Authentication

All API requests require authentication using your LetsCloud API key. You can provide the API key in two ways:

- **Header Authentication**: Include `Authorization: Bearer YOUR_API_KEY` in your requests
- **Environment Variable**: Set `LETSCLOUD_API_KEY=your_api_key` in your environment

### 2. Base URLs

- **Production**: `https://core.letscloud.io/api`
- **Staging**: `https://core.letscloud.io/api`

## 📚 API Endpoints

### Server Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/servers` | List all servers |
| `POST` | `/servers` | Create a new server |
| `GET` | `/servers/{server_id}` | Get server details |
| `DELETE` | `/servers/{server_id}` | Delete a server |
| `POST` | `/servers/{server_id}/start` | Start a server |
| `POST` | `/servers/{server_id}/stop` | Shutdown a server |
| `POST` | `/servers/{server_id}/reboot` | Reboot a server |

### SSH Key Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/ssh-keys` | List all SSH keys |
| `POST` | `/ssh-keys` | Create a new SSH key |
| `GET` | `/ssh-keys/{key_id}` | Get SSH key details |
| `DELETE` | `/ssh-keys/{key_id}` | Delete an SSH key |

### Snapshot Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/servers/{server_id}/snapshots` | List server snapshots |
| `POST` | `/servers/{server_id}/snapshots` | Create a server snapshot |
| `GET` | `/servers/{server_id}/snapshots/{snapshot_id}` | Get snapshot details |
| `DELETE` | `/servers/{server_id}/snapshots/{snapshot_id}` | Delete a snapshot |
| `POST` | `/servers/{server_id}/snapshots/{snapshot_id}/restore` | Restore server from snapshot |

### Resource Discovery

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/plans` | List available plans |
| `GET` | `/images` | List available images |
| `GET` | `/locations` | List available locations |

### Account Information

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/account` | Get account information |

## 🔧 GPT Actions Integration

### Setting up GPT Actions

1. **Import the OpenAPI Specification**:
   - Use the `openapi.yaml` file in this repository
   - The specification is optimized for GPT Actions with clear operation IDs and descriptions

2. **Configure Authentication**:
   - Set up your LetsCloud API key in your GPT Actions configuration
   - Use the `ApiKeyAuth` security scheme

3. **Available Actions**:
   - All endpoints are mapped to GPT Actions with descriptive names
   - Each action includes proper parameter validation and error handling

### Example GPT Actions Usage

```yaml
# Example GPT Actions configuration
actions:
  - name: list_servers
    description: "List all servers in your LetsCloud account"
    operation_id: listServers
    
  - name: create_server
    description: "Create a new server with specified configuration"
    operation_id: createServer
    
  - name: manage_ssh_keys
    description: "Manage SSH keys for server access"
    operation_id: listSSHKeys
```

## 📖 Examples

### Creating a Server

```bash
curl -X POST https://core.letscloud.io/api/servers \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "My Web Server",
    "plan_slug": "basic-1gb",
    "image_slug": "ubuntu-22-04",
    "location_slug": "nyc1",
    "hostname": "webserver-01"
  }'
```

### Listing Servers

```bash
curl -X GET https://core.letscloud.io/api/servers \
  -H "Authorization: Bearer YOUR_API_KEY"
```

### Creating an SSH Key

```bash
curl -X POST https://core.letscloud.io/api/ssh-keys \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Laptop Key",
    "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC..."
  }'
```

## 🔍 Data Models

### Server Object

```json
{
  "id": 123,
  "label": "My Web Server",
  "hostname": "webserver-01",
  "status": "running",
  "ip_address": "192.168.1.100",
  "private_ip": "10.0.0.100",
  "plan": {
    "slug": "basic-1gb",
    "name": "Basic 1GB",
    "ram": 1024,
    "cpu": 1,
    "disk": 25,
    "price": 5.00
  },
  "image": {
    "slug": "ubuntu-22-04",
    "name": "Ubuntu 22.04 LTS",
    "distribution": "Ubuntu",
    "version": "22.04"
  },
  "location": {
    "slug": "nyc1",
    "name": "New York",
    "country": "United States"
  },
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Error Response

```json
{
  "error": "Server not found",
  "code": "NOT_FOUND",
  "details": {
    "server_id": 123
  }
}
```

## 🛡️ Error Handling

The API uses standard HTTP status codes and returns detailed error messages:

- `400` - Bad Request (invalid parameters)
- `401` - Unauthorized (invalid API key)
- `404` - Not Found (resource doesn't exist)
- `409` - Conflict (resource state conflict)
- `422` - Validation Error (invalid request data)
- `500` - Internal Server Error

## 📊 Rate Limiting

API requests are rate limited to ensure fair usage. Implement appropriate retry logic with exponential backoff when encountering rate limit errors.

## 🔗 Related Resources

- [LetsCloud Go Library](https://github.com/letscloud-community/letscloud-go)
- [LetsCloud Website](https://www.letscloud.io)
- [API Documentation](https://developers.letscloud.io)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support, please contact:
- **Email**: support@letscloud.io
- **Website**: https://www.letscloud.io
- **Documentation**: https://developers.letscloud.io

---

**Note**: This OpenAPI specification is based on the LetsCloud Go library and uses the official API endpoint at [https://core.letscloud.io/api](https://core.letscloud.io/api). The specification may be updated as the API evolves. Always refer to the official documentation for the most current information.
