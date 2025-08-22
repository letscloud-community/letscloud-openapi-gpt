# 🚀 LetsCloud Infrastructure Manager - AI Assistant

[![OpenAI GPT](https://img.shields.io/badge/OpenAI%20GPT-Compatible-brightgreen.svg)](https://platform.openai.com/)
[![LetsCloud](https://img.shields.io/badge/LetsCloud-Platform-red.svg)](https://www.letscloud.io)
[![Privacy](https://img.shields.io/badge/Privacy-Secure-blue.svg)](https://letscloud-community.github.io/letscloud-openapi-gpt/privacy-policy.html)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **📝 Note**: All documentation in this repository is in English.

The **LetsCloud Infrastructure Manager** is an AI assistant that helps you manage your cloud servers and infrastructure using simple, natural language commands. No technical knowledge required!

## 📋 What can you do?

With the **LetsCloud Infrastructure Manager**, you can:

- ✅ **Create and manage servers** with simple commands
- ✅ **Start, stop, and restart** your servers
- ✅ **Monitor server status** and performance
- ✅ **Manage SSH keys** for secure access
- ✅ **Create backups** (snapshots) of your servers
- ✅ **View account information** and costs
- ✅ **Get cost optimization** recommendations

## 🚀 Quick Start

1. **Get your API key** from your [LetsCloud dashboard](https://www.letscloud.io)
2. **Find the GPT** in the GPT Store
3. **Set up your API key** in the conversation
4. **Start managing your infrastructure!**

**Example:**
```
You: "Show me all my servers"
GPT: "Here are your servers: [list of your servers]"
```

## 🎯 Features

- ✅ **21 different actions** for complete infrastructure management
- ✅ **Natural language commands** - no technical knowledge needed
- ✅ **Secure API key authentication** - your data stays private
- ✅ **Real-time server management** - instant responses
- ✅ **Cost monitoring** - track your spending
- ✅ **Backup management** - protect your data

## 🔑 Authentication

To use the LetsCloud Infrastructure Manager, you need your **LetsCloud API key**:

1. **Get your API key** from your [LetsCloud dashboard](https://www.letscloud.io)
2. **Set it up** in the GPT conversation
3. **Start managing** your infrastructure!

**Your API key is:**
- ✅ **Private and secure** - never shared with others
- ✅ **Easy to manage** - can be revoked anytime
- ✅ **Encrypted** - all communications are secure

## 💬 What you can say

### Server Management

| What you want to do | What to say |
|-------------------|-------------|
| See all servers | *"List my servers"* |
| Create new server | *"Create a web server with Ubuntu"* |
| Check server status | *"What's the status of my server?"* |
| Start a server | *"Start my web server"* |
| Stop a server | *"Stop my database server"* |
| Restart server | *"Restart my application server"* |
| Delete server | *"Delete my old test server"* |

### SSH Key Management

| What you want to do | What to say |
|-------------------|-------------|
| See all SSH keys | *"Show me my SSH keys"* |
| Add new SSH key | *"Add SSH key for my laptop"* |
| Check SSH key | *"What SSH keys do I have?"* |
| Remove SSH key | *"Delete my old SSH key"* |

### Backups and Snapshots

| What you want to do | What to say |
|-------------------|-------------|
| Create backup | *"Backup my production server"* |
| See all backups | *"Show me my backups"* |
| Restore from backup | *"Restore my server from backup"* |
| Delete backup | *"Delete old backup"* |

### Account and Costs

| What you want to do | What to say |
|-------------------|-------------|
| Check balance | *"What's my account balance?"* |
| See costs | *"Show my monthly costs"* |
| Available plans | *"What server plans are available?"* |
| Server locations | *"Where can I create servers?"* |

## 📖 Documentation

**For detailed instructions, see:**
- **[User Guide](GPT_ACTIONS_SETUP_GUIDE.md)** - Complete guide for users
- **[Quick Start](QUICK_SETUP.md)** - Get started in 3 steps
- **[Privacy Policy](https://letscloud-community.github.io/letscloud-openapi-gpt/privacy-policy.html)** - How we protect your data

### Setting up GPT Actions

#### Step 1: Configure Basic GPT Information

**Name:**
```
LetsCloud Infrastructure Manager
```

**Description:**
```
A specialized GPT for managing cloud infrastructure on LetsCloud platform. Create, manage, and monitor servers, SSH keys, snapshots, and account resources using natural language commands.
```

**Instructions:**
```
You are a cloud infrastructure management assistant for LetsCloud platform. Help users manage their cloud resources through natural language commands. Create, start, stop servers, manage SSH keys, handle snapshots, provide plan information, and optimize costs. Always confirm destructive operations and prioritize user safety.
```

**Conversation Starters:**
- "Show me all my servers and their current status"
- "Create a new web server with Ubuntu 22.04"
- "Help me optimize my infrastructure costs"

**Capabilities:**
- ✅ **Web Search**: Enable
- ❌ **Canvas**: Disable
- ❌ **Image Generation**: Disable
- ✅ **Code Interpreter**: Enable

#### Privacy & Sharing Considerations

**For Private GPTs (Recommended):**
- No privacy policy required
- Use your own API key
- Full control over access

**For Public GPTs:**
- Privacy policy URL required
- Each user must provide their own API key
- Users need to configure authentication individually
- **Privacy Policy URL**: `https://letscloud-community.github.io/letscloud-openapi-gpt/privacy-policy.html`

#### Step 2: Import OpenAPI Specification
   
   **Option A: Direct URL Import (Recommended)**
   ```yaml
   # In your GPT Actions configuration, use this URL:
   https://raw.githubusercontent.com/letscloud-community/letscloud-openapi-gpt/main/openapi.yaml
   ```
   
   **Option B: Local File Import**
   - Download the `openapi.yaml` file from this repository
   - Upload it directly to your GPT Actions configuration
   - File path: `./openapi.yaml`
   
   **Option C: GitHub Repository Import**
   - Repository: `letscloud-community/letscloud-openapi-gpt`
   - Branch: `main`
   - File: `openapi.yaml`
   
   **Specification Features:**
   - ✅ Optimized for GPT Actions with clear operation IDs
   - ✅ 21 endpoints with descriptive names
   - ✅ Comprehensive parameter validation
   - ✅ Detailed error responses
   - ✅ Authentication scheme configured
   - ✅ Production-ready API endpoints

2. **Configure Authentication**:
   
   **API Key Setup:**
   ```yaml
   # Security scheme: ApiKeyAuth
   # Header name: Authorization
   # Value format: Bearer YOUR_API_KEY
   ```
   
   **Environment Variable:**
   ```bash
   LETSCLOUD_API_KEY=your_api_key_here
   ```
   
   **Get Your API Key:**
   1. Log in to your LetsCloud account at https://www.letscloud.io
   2. Go to API Settings in your dashboard
   3. Generate a new API key
   4. Copy the key and keep it secure

3. **Available Actions**:
   
   **Server Management (7 actions):**
   - `listServers` - List all servers
   - `createServer` - Create new server
   - `getServer` - Get server details
   - `deleteServer` - Delete server
   - `startServer` - Start server
   - `shutdownServer` - Stop server
   - `rebootServer` - Reboot server
   
   **SSH Key Management (4 actions):**
   - `listSSHKeys` - List SSH keys
   - `createSSHKey` - Add new SSH key
   - `getSSHKey` - Get SSH key details
   - `deleteSSHKey` - Remove SSH key
   
   **Snapshot Management (5 actions):**
   - `listSnapshots` - List server snapshots
   - `createSnapshot` - Create backup snapshot
   - `getSnapshot` - Get snapshot details
   - `deleteSnapshot` - Delete snapshot
   - `restoreSnapshot` - Restore from snapshot
   
   **Resource Discovery (4 actions):**
   - `listPlans` - Available server plans
   - `listImages` - Available OS images
   - `listLocations` - Available locations
   - `getAccountInfo` - Account information

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

### 🔧 Troubleshooting & Tips

**Common Issues:**

1. **Authentication Errors:**
   - Ensure your API key is valid and active
   - Check that the Authorization header format is correct: `Bearer YOUR_API_KEY`
   - Verify your API key has the necessary permissions

2. **Import Issues:**
   - If the direct URL doesn't work, try downloading the file locally
   - Ensure you're using the latest version from the main branch
   - Check that your GPT Actions platform supports OpenAPI 3.0

3. **Action Not Found:**
   - Verify the operation IDs match exactly (case-sensitive)
   - Check that all 21 actions are properly imported
   - Restart your GPT Actions configuration if needed

**Best Practices:**

- ✅ Test with simple actions first (like `listServers`)
- ✅ Use descriptive natural language commands
- ✅ Keep your API key secure and rotate regularly
- ✅ Monitor your API usage to avoid rate limits
- ✅ Use the latest version of the specification

## 🚀 Deployment Options

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Deploy%20Free-lightgrey.svg)](https://pages.github.com/)
[![Docker](https://img.shields.io/badge/Docker-Container%20Ready-blue.svg)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-Deploy%20Ready-orange.svg)](https://aws.amazon.com/)
[![GCP](https://img.shields.io/badge/GCP-Deploy%20Ready-blue.svg)](https://cloud.google.com/)
[![Azure](https://img.shields.io/badge/Azure-Deploy%20Ready-blue.svg)](https://azure.microsoft.com/)

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

## 🔧 Compatibility

[![OpenAI GPT](https://img.shields.io/badge/OpenAI%20GPT-Compatible-brightgreen.svg)](https://platform.openai.com/)
[![ChatGPT](https://img.shields.io/badge/ChatGPT-Integration-blue.svg)](https://chat.openai.com/)
[![Claude](https://img.shields.io/badge/Claude-Compatible-orange.svg)](https://claude.ai/)
[![Postman](https://img.shields.io/badge/Postman-Import-yellow.svg)](https://www.postman.com/)
[![Insomnia](https://img.shields.io/badge/Insomnia-Import-purple.svg)](https://insomnia.rest/)
[![Swagger UI](https://img.shields.io/badge/Swagger%20UI-Compatible-green.svg)](https://swagger.io/tools/swagger-ui/)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🤝 Community & Support

[![Issues](https://img.shields.io/badge/Issues-Welcome-brightgreen.svg)](https://github.com/letscloud-community/letscloud-openapi-gpt/issues)
[![Pull Requests](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](https://github.com/letscloud-community/letscloud-openapi-gpt/pulls)
[![Discussions](https://img.shields.io/badge/Discussions-Open-blue.svg)](https://github.com/letscloud-community/letscloud-openapi-gpt/discussions)
[![Contributing](https://img.shields.io/badge/Contributing-Guidelines-lightgrey.svg)](https://github.com/letscloud-community/letscloud-openapi-gpt/blob/main/CONTRIBUTING.md)

### Support Channels

For support, please contact:
- **Email**: support@letscloud.io
- **Website**: https://www.letscloud.io
- **Documentation**: https://developers.letscloud.io
- **GitHub Issues**: [Create an issue](https://github.com/letscloud-community/letscloud-openapi-gpt/issues)

---

**Note**: This OpenAPI specification is based on the LetsCloud Go library and uses the official API endpoint at [https://core.letscloud.io/api](https://core.letscloud.io/api). The specification may be updated as the API evolves. Always refer to the official documentation for the most current information.
