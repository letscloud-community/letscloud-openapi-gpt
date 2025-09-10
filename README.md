# 🚀 LetsCloud API - ChatGPT Actions Integration

> **Complete OpenAPI specification and ChatGPT Actions integration for LetsCloud cloud infrastructure management**

Manage your LetsCloud instances, SSH keys, snapshots, and resources with natural language commands through ChatGPT Actions.

## ✨ **Features**

- 🖥️ **Instance Management**: List, create, delete, and manage cloud instances
- ⚡ **Power Control**: Start, stop, reboot, and shutdown instances
- 🔑 **SSH Key Management**: Add, list, and remove SSH keys
- 📸 **Snapshot Operations**: Create and manage instance snapshots
- 💰 **Account Management**: Check balance and account information
- 🔍 **Resource Discovery**: List available plans, images, and locations
- 🛡️ **Secure Authentication**: API token-based security

## 🚀 **Quick Start**

### **📋 ChatGPT Actions Configuration**

This project includes the required `ai-plugin.json` configuration files for ChatGPT Actions:

- **Root configuration**: `ai-plugin.json` - Main plugin configuration
- **Standard location**: `.well-known/ai-plugin.json` - Where ChatGPT automatically looks for plugin config

The configuration includes:
- ✅ Plugin metadata and descriptions
- ✅ Service HTTP authentication with API key authorization
- ✅ OpenAI verification tokens for ChatGPT Actions (replace with your token)
- ✅ OpenAPI specification reference
- ✅ Contact information and legal links

**⚠️ Important**: Before deploying, replace `"replace-with-your-verification-token"` in both `ai-plugin.json` files with your actual OpenAI verification token.

## 📁 **Repository Structure**

```
letscloud-openapi-gpt/
├── docs/
│   ├── openapi.yaml                    # Complete OpenAPI 3.1 specification
│   ├── LETSCOULD_API_DOCUMENTATION.md  # Comprehensive API documentation
│   ├── index.html                      # GitHub Pages documentation site
│   ├── privacy-policy.html             # Privacy policy
│   ├── robots.txt                      # SEO configuration
│   ├── sitemap.xml                     # Site map
│   ├── _config.yml                     # Jekyll configuration
│   └── assets/
│       └── LetsCloud_logo.png          # LetsCloud branding
├── examples/
│   ├── usage-examples.py               # Python client implementation
│   └── requirements.txt                # Python dependencies
├── .well-known/
│   └── ai-plugin.json                  # ChatGPT Actions configuration
├── ai-plugin.json                      # Main plugin configuration
├── gpt-actions-config.yaml             # GPT Actions configuration examples
├── verify-plugin-config.py             # Configuration validation script
├── README.md                           # This file
├── LICENSE                             # MIT License
└── Setup Guides:
    ├── GPT_CREATION_GUIDE.md           # How to create a new GPT
    ├── GPT_DUPLICATION_GUIDE.md        # How to duplicate existing GPT
    ├── GPT_ACTIONS_SETUP_GUIDE.md      # ChatGPT Actions setup
    ├── GITHUB_PAGES_SETUP.md           # GitHub Pages deployment guide
    └── QUICK_SETUP.md                  # Quick start guide
```

## 📚 **Documentation**

### **🌐 GitHub Pages Documentation**
This repository includes a complete GitHub Pages site with interactive API documentation:
- **Live Documentation**: [View the interactive API docs](https://letscloud-community.github.io/letscloud-openapi-gpt/)
- **Interactive Testing**: Test API endpoints directly in your browser
- **Complete Reference**: All endpoints, schemas, and examples
- **Repository**: [GitHub Repository](https://github.com/letscloud-community/letscloud-openapi-gpt)

### **🚀 Deploying GitHub Pages**
After publishing this repository to GitHub:
1. Go to **Repository Settings** → **Pages**
2. Select **Source**: Deploy from a branch
3. Choose **Branch**: `main` (or your default branch)
4. Select **Folder**: `/docs`
5. Click **Save**
6. The documentation will be available at: `https://letscloud-community.github.io/letscloud-openapi-gpt/`

**📖 Detailed Setup Guide**: See [GitHub Pages Setup Guide](GITHUB_PAGES_SETUP.md) for complete instructions and troubleshooting.

### **📖 Available Documentation**
- **[Complete API Documentation](docs/LETSCOULD_API_DOCUMENTATION.md)** - Comprehensive API reference
- **[OpenAPI Specification](docs/openapi.yaml)** - Machine-readable API specification
- **[Python Examples](examples/usage-examples.py)** - Complete Python client implementation
- **[Setup Guides](QUICK_SETUP.md)** - Quick start and detailed setup instructions

### **🔒 Secure Setup: Create Your Private GPT**

For the best and most secure experience, create your own private GPT:

#### **Option 1: Duplicate Existing GPT (Recommended)**
1. **Follow our step-by-step guide**: [GPT Duplication Guide](GPT_DUPLICATION_GUIDE.md)
2. **Create a private copy** of the existing GPT
3. **Configure your API key** securely in the private GPT settings
4. **Use immediately** - no setup required in conversations!

#### **Option 2: Create New Private GPT**
1. **Create a new GPT** in ChatGPT (GPT Builder)
2. **Configure it as private** in the settings
3. **Follow our creation guide**: [GPT Creation Guide](GPT_CREATION_GUIDE.md)
4. **Configure your API key** securely in the GPT settings
5. **Use immediately** - no setup required in conversations!

**✅ Benefits of Private Setup:**
- 🔒 **Secure**: Your API key is encrypted and protected
- 🚀 **Fast**: No setup required in conversations
- 🎯 **Complete**: All features available
- 👤 **Personal**: Only you have access
- 💰 **Free**: No additional costs

**⚠️ Security Note**: We strongly recommend using the private version for secure and convenient access to your infrastructure.

## 🎯 **What You Can Do**

### **Server Operations**
```
"Create a new Ubuntu server"
"Start my server-123"
"Stop all running servers"
"Reboot server-456"
"Delete server-789"
"Show me all my servers"
```

### **SSH Key Management**
```
"Add a new SSH key"
"List my SSH keys"
"Remove SSH key key-123"
```

### **Snapshot Operations**
```
"Create a snapshot of server-123"
"List snapshots for server-456"
"Restore server from snapshot snap-789"
```

### **Account Information**
```
"Show my account balance"
"Get my account information"
"Check my current usage"
```

## 🔧 **Authentication**

### **🔒 Secure Setup: Private GPT**

For secure and convenient access, create your own private GPT:

#### **Option 1: Duplicate Existing GPT (Recommended)**
1. **Follow our step-by-step guide**: [GPT Duplication Guide](GPT_DUPLICATION_GUIDE.md)
2. **Configure your API key** securely in the private GPT settings
3. **Your key is encrypted** and stored securely by OpenAI
4. **No need to share keys** in conversations

#### **Option 2: Create New Private GPT**
1. **Create a new GPT** in ChatGPT (GPT Builder)
2. **Configure it as private** in the settings
3. **Follow our creation guide**: [GPT Creation Guide](GPT_CREATION_GUIDE.md)
4. **Configure your API key** securely in the GPT settings
5. **Your key is encrypted** and stored securely by OpenAI

### **Getting Your API Token**

1. **Log in** to your [LetsCould Dashboard](https://my.letscloud.io)
2. **Go to Settings** → API Keys
3. **Generate a new API key**
4. **Copy the token** (keep it secure!)

### **Authentication Scheme**
- **Type**: API Key
- **Header Name**: `api-token`
- **Header Value Format**: `{api_token}`
- **Environment Variable**: `LETSCLOUD_API_TOKEN`

## 🛠️ **Troubleshooting**

### **Common Issues**

**"Authentication failed"**
- Check if your API key is correctly configured in the GPT settings
- Try regenerating your API key in your LetsCould dashboard
- Ensure you followed the [GPT Duplication Guide](GPT_DUPLICATION_GUIDE.md) correctly

**"No servers found"**
- Verify your account has active servers
- Check if your API key has the correct permissions
- Ensure your servers are not in a suspended state

**"Error talking to connector"**
- Verify your internet connection
- Check if the LetsCould API is accessible
- Try again in a few minutes

**"GPT not responding to commands"**
- Ensure your API key is properly configured in the GPT settings
- Try restarting the conversation
- Verify you're using the private version of the GPT

### **Recommended Solution**

For the best experience and to avoid most issues, **use the private version** of this GPT:
1. Follow the [GPT Duplication Guide](GPT_DUPLICATION_GUIDE.md)
2. Configure your API key once in the private GPT settings
3. Enjoy hassle-free infrastructure management

## 📚 **Useful Links**

- [LetsCould Dashboard](https://my.letscloud.io)
- [LetsCould Documentation](https://developers.letscloud.io)
- [API Reference](https://developers.letscloud.io/api)
- [Support Center](https://letscloud.io/help)

## 🆘 **Support**

Need help? We're here for you:

- **Documentation**: [developers.letscloud.io](https://developers.letscloud.io)

- **Email**: support@letscloud.io

## 🔒 **Security & Privacy**

- **API tokens** are encrypted and secure
- **No data** is stored permanently
- **All communications** use HTTPS
- **Your privacy** is our priority

---

**Made with ❤️ by the LetsCould Team**

*Transform your cloud infrastructure management with AI!*
