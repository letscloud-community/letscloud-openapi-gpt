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

### 🔑 Setting Up Your API Key

After starting a conversation with the GPT, type:
```
I need to set up my API key: YOUR_API_TOKEN_HERE
```

**Example:**
```
You: "I need to set up my API key: your-token-here"
GPT: "✅ API key configured successfully! You can now manage your infrastructure."
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

## 🛠️ For Developers

*This section is for developers who want to create their own GPT or integrate with the API directly.*

### Technical Setup

**OpenAPI Specification URL:**
```
https://raw.githubusercontent.com/letscloud-community/letscloud-openapi-gpt/main/openapi.yaml
```

**Authentication:**
```yaml
Authentication Type: API Key
Header Name: api-token
Header Value Format: {api_token}
```
   
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
   # Header name: api-token
   # Value format: YOUR_API_TOKEN
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
   - Check that the api-token header format is correct: `YOUR_API_TOKEN`
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

## 🛠️ Troubleshooting

### Common Issues

**"Authentication failed"**
- Check if your API key is correct
- Make sure you included "Bearer" before your API key
- Try regenerating your API key in your LetsCloud dashboard

**"Server not found"**
- Make sure the server exists in your account
- Use "List my servers" to see all available servers

**"Action failed"**
- Check if your API key has the right permissions
- Try again - some actions may take a few moments
- Contact support if problems persist

### Getting Help

- **Support**: support@letscloud.io
- **Documentation**: [https://www.letscloud.io/docs](https://www.letscloud.io/docs)
- **Community**: [GitHub Repository](https://github.com/letscloud-community/letscloud-openapi-gpt)

## 🔗 Useful Links

- [LetsCloud Website](https://www.letscloud.io)
- [LetsCloud Documentation](https://www.letscloud.io/docs)
- [Privacy Policy](https://letscloud-community.github.io/letscloud-openapi-gpt/privacy-policy.html)

## 📞 Support

**Need help?**
- **Email**: support@letscloud.io
- **Website**: [https://www.letscloud.io](https://www.letscloud.io)
- **Documentation**: [https://www.letscloud.io/docs](https://www.letscloud.io/docs)

---

**Ready to get started?** 🚀

1. Get your API key from your [LetsCloud dashboard](https://www.letscloud.io)
2. Find the **LetsCloud Infrastructure Manager** in the GPT Store
3. Set up your API key and start managing your infrastructure with simple commands!

**Happy cloud managing!** ☁️
