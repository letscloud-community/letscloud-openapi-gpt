# 🔧 Complete Guide: How to Duplicate your GPT Actions and Make it Private

> **Transform your public GPT into a private version with your own API key pre-configured!**

This guide will show you how to create a **private copy** of the LetsCould Infrastructure Manager GPT with your API key already configured, so you can use it without needing to set up authentication every time.

## 📋 **Prerequisites**

- ✅ LetsCould API key for personal use
- ✅ Access to GPT Creator (ChatGPT Plus or Enterprise)
- ✅ Basic understanding of GPT Actions

## 🚀 **Step-by-Step Process**

### **Step 1: Access GPT Creator**

1. **Go to** [https://chat.openai.com/gpts](https://chat.openai.com/gpts)
2. **Click** "Create a GPT"
3. **Find your GPT** "LetsCould Infrastructure Manager"

### **Step 2: Make a Copy**

1. **Open the GPT** you want to duplicate
2. **Click** the three dots menu (⋮)
3. **Select** "Copy GPT"
4. **Rename** it to something like "My Private LetsCould Manager"

### **Step 3: Configure the Private Version**

1. **Go to** the "Configure" tab
2. **Open the Action** that connects to `core_letscloud_io__jit_plugin`
3. **Add Environment Variable:**
   - **Name**: `LETSCLOUD_API_TOKEN`
   - **Value**: Your LetsCould API key
4. **Save** the configuration

### **Step 4: Set Privacy Settings**

1. **Go to** "Privacy" section
2. **Select** "Only me" (private)
3. **Save** the settings

### **Step 5: Test the Configuration**

1. **Start a conversation** with your private GPT
2. **Try a command** like "Show me all my servers"
3. **Verify** that it works without asking for API key

## 🎯 **Result: Two Versions**

### **✅ Public Version (Original)**
- **Purpose**: For customers and public use
- **Privacy**: Public
- **API Key**: Users must provide their own
- **Use**: For general LetsCould customers

### **🔒 Private Version (Copy)**
- **Purpose**: For your personal use
- **Privacy**: Private (only you)
- **API Key**: Pre-configured with yours
- **Use**: For your own infrastructure management

## 🔍 **Verification**

### **Test Public Version:**
```
You: "Show me my servers"
GPT: "I need your API key to access your LetsCould account..."
```

### **Test Private Version:**
```
You: "Show me my servers"
GPT: "Here are your servers: [list of your servers]"
```

## 🛡️ **Security**

### **✅ Benefits:**
- **Your API key is private** - only you can access it
- **No setup required** - ready to use immediately
- **Separate from public version** - doesn't affect customers
- **Full functionality** - all features available
- **Secure storage** - API key stored in OpenAI's secure environment

### **⚠️ Important Notes:**
- **Never share** your private GPT with others
- **Keep your API key secure** - it has full access to your account
- **Monitor usage** - check your LetsCould dashboard regularly
- **Rotate keys** - change your API key periodically for security

## 🚀 **Useful Commands to Test**

### **Public Version (for customers):**
```
"Create a new Ubuntu server"
"List all my servers"
"Show my account balance"
"Add a new SSH key"
"Create a snapshot of server-123"
```

### **Private Version (for you):**
```
"Show me all my servers"
"Create a backup snapshot"
"Check my current usage"
"List available plans"
"Restart server-456"
```

## 📚 **Additional Resources**

1. **API Documentation**: [LetsCould API Docs](https://developers.letscloud.io)
2. **Support**: support@letscloud.io
3. **Community**: [Discord](https://discord.gg/letscloud)
4. **Consult** the LetsCould documentation

## 🎉 **Congratulations!**

You now have:
- ✅ **Public GPT** for your customers
- ✅ **Private GPT** for your personal use
- ✅ **Secure API key management**
- ✅ **No setup required** for personal use

**Enjoy managing your infrastructure with natural language commands!** 🚀
