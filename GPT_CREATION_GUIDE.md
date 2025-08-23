# 🛠️ GPT Creation Guide - LetsCould Infrastructure Manager

## 📋 Overview

This guide will help you create a **private GPT** from scratch that integrates with the LetsCould API. This is an alternative to duplicating the existing GPT.

## 🎯 What You'll Create

A private GPT that can:
- 🖥️ **Manage servers** (create, start, stop, delete)
- 🔑 **Handle SSH keys** (add, list, remove)
- 📸 **Manage snapshots** (create, list, restore)
- 💰 **Check account info** (balance, costs)
- 📍 **Discover resources** (plans, images, locations)

## 🚀 Step-by-Step Setup

### Step 1: Get Your API Key

1. **Log in** to your [LetsCould Dashboard](https://my.letscloud.io)
2. **Go to Settings** → **API Keys**
3. **Generate a new API key**
4. **Copy the token** (keep it secure!)

### Step 2: Create a New GPT

1. **Open ChatGPT** and go to [GPT Builder](https://chat.openai.com/gpts)
2. **Click "Create a GPT"**
3. **Choose "Create"** (not "Configure")

### Step 3: Configure Your GPT

#### Basic Information
- **Name**: "LetsCould Infrastructure Manager"
- **Description**: "Your AI-powered cloud infrastructure management companion. Manage servers, SSH keys, snapshots, and resources with natural language commands."
- **Instructions**: Use the content from [GPT_CREATOR_INSTRUCTIONS.md](GPT_CREATOR_INSTRUCTIONS.md)

#### Privacy Settings
- **Set to "Private"** - Only you can access it
- **Enable "Actions"** - Required for API integration

### Step 4: Add API Configuration

#### Configure Actions
1. **Click "Add actions"**
2. **Choose "Import from URL"**
3. **Use this URL**: `https://raw.githubusercontent.com/letscloud-community/letscloud-openapi-gpt/main/docs/openapi.yaml`

#### Alternative: Manual Configuration
If the URL import doesn't work, manually configure:

1. **Click "Add actions"**
2. **Choose "Create new action"**
3. **Copy the configuration** from [gpt-actions-config.yaml](gpt-actions-config.yaml)

### Step 5: Configure API Authentication

#### Add API Key
1. **In the Actions section**, find "Authentication"
2. **Add your API key**:
   - **Type**: API Key
   - **Name**: `api-token`
   - **Value**: Your LetsCould API key

#### Test Connection
1. **Click "Test"** to verify the connection
2. **Try a simple command** like "Show my account information"

### Step 6: Finalize and Save

1. **Review all settings**
2. **Click "Save"**
3. **Your private GPT is ready!**

## 🔧 Configuration Files

### Required Files
- **OpenAPI Spec**: [docs/openapi.yaml](docs/openapi.yaml)
- **GPT Actions Config**: [gpt-actions-config.yaml](gpt-actions-config.yaml)
- **Creator Instructions**: [GPT_CREATOR_INSTRUCTIONS.md](GPT_CREATOR_INSTRUCTIONS.md)

### Optional Files
- **Documentation**: [docs/LETSCOULD_API_DOCUMENTATION.md](docs/LETSCOULD_API_DOCUMENTATION.md)
- **Examples**: [examples/usage-examples.py](examples/usage-examples.py)

## 🧪 Testing Your GPT

### Basic Commands to Test
```
"Show my account information"
"List available server plans"
"Show available locations"
```

### Advanced Commands
```
"Create a new server with Ubuntu 22.04"
"Add a new SSH key for my laptop"
"Create a backup of my server"
```

## 🔒 Security Best Practices

### API Key Security
- ✅ **Use private GPT** - Only you have access
- ✅ **Never share your API key** in conversations
- ✅ **Rotate keys regularly** - Generate new keys periodically
- ✅ **Monitor usage** - Check your API usage in LetsCould dashboard

### GPT Configuration
- ✅ **Keep it private** - Don't make it public
- ✅ **Regular updates** - Update configuration when API changes
- ✅ **Backup settings** - Save your configuration

## 🛠️ Troubleshooting

### Common Issues

**"Authentication failed"**
- Check if your API key is correctly configured
- Verify the API key format (no extra spaces)
- Try regenerating your API key

**"Actions not working"**
- Verify the OpenAPI spec URL is accessible
- Check if all required fields are configured
- Test the API endpoint directly

**"GPT not responding"**
- Check your internet connection
- Verify the LetsCould API is accessible
- Try restarting the conversation

### Getting Help
- **LetsCould Support**: support@letscloud.io
- **GitHub Issues**: [Repository Issues](https://github.com/letscloud-community/letscloud-openapi-gpt/issues)

## 🎉 Success!

Once configured, your private GPT will:
- 🔒 **Securely store** your API key
- 🚀 **Work immediately** without setup
- 🎯 **Provide full functionality** for managing your infrastructure
- 👤 **Be completely private** - only you can access it

**Happy cloud managing! 🚀**
