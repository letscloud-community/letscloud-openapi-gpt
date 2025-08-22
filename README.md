# 🚀 LetsCloud Infrastructure Manager - AI Assistant

> **Your AI-powered cloud infrastructure management companion**

Manage your LetsCloud servers, SSH keys, snapshots, and resources with natural language commands through ChatGPT.

## ✨ **Features**

- 🖥️ **Server Management**: Create, start, stop, reboot, and delete servers
- 🔑 **SSH Key Management**: Add, list, and remove SSH keys
- 📸 **Snapshot Operations**: Create and restore server snapshots
- 💰 **Account Management**: Check balance and account information
- 🔍 **Resource Monitoring**: List and manage all your resources
- 🛡️ **Secure Authentication**: API token-based security

## 🚀 **Quick Start**

### **For Users (Public Version)**

1. **Find the LetsCloud GPT** in the GPT Store
2. **Start a conversation** with the GPT
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

### **For Personal Use (Private Version)**

If you want to create a **private version** for personal use with your API key pre-configured:

1. **Follow our duplication guide**: [GPT Duplication Guide](GPT_DUPLICATION_GUIDE.md)
2. **Create a private copy** of the GPT
3. **Configure your API key** in the private version
4. **Use without setup** - your key is already configured!

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

### **Authentication Scheme**
- **Type**: API Key
- **Header Name**: `api-token`
- **Header Value Format**: `{api_token}`
- **Environment Variable**: `LETSCLOUD_API_TOKEN`

### **Getting Your API Token**

1. **Log in** to your [LetsCloud Dashboard](https://app.letscloud.io)
2. **Go to Settings** → API Keys
3. **Generate a new API key**
4. **Copy the token** (keep it secure!)

## 🛠️ **Troubleshooting**

### **Common Issues**

**"Authentication failed"**
- Check if your API key is correct
- Make sure you provide your API token without any prefix
- Try regenerating your API key in your LetsCloud dashboard

**"No servers found"**
- Verify your account has active servers
- Check if your API key has the correct permissions
- Ensure your servers are not in a suspended state

**"Error talking to connector"**
- Verify your internet connection
- Check if the LetsCloud API is accessible
- Try again in a few minutes

## 📚 **Useful Links**

- [LetsCloud Dashboard](https://app.letscloud.io)
- [LetsCloud Documentation](https://developers.letscloud.io)
- [API Reference](https://developers.letscloud.io/api)
- [Support Center](https://support.letscloud.io)

## 🆘 **Support**

Need help? We're here for you:

- **Documentation**: [developers.letscloud.io](https://developers.letscloud.io)
- **Community**: [Discord](https://discord.gg/letscloud)
- **Email**: support@letscloud.io

## 🔒 **Security & Privacy**

- **API tokens** are encrypted and secure
- **No data** is stored permanently
- **All communications** use HTTPS
- **Your privacy** is our priority

---

**Made with ❤️ by the LetsCloud Team**

*Transform your cloud infrastructure management with AI!*
