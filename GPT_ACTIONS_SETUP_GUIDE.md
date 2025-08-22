# 🚀 Complete Guide: Configuring LetsCloud API in GPT Actions

## 📋 Overview

This guide details **exactly** how to configure the LetsCloud API in GPT Actions so you can manage your infrastructure using natural language.

## 🎯 Prerequisites

- ✅ [LetsCloud](https://www.letscloud.io) account
- ✅ [OpenAI](https://platform.openai.com) account with GPT Actions access
- ✅ LetsCloud API Key (we'll get this in step 1)

---

## 📝 Step 1: Get Your LetsCloud API Key

### 1.1 Access Your LetsCloud Account
1. Go to [https://www.letscloud.io](https://www.letscloud.io)
2. Log in to your account
3. Navigate to the **Dashboard**

### 1.2 Access API Settings
1. In the sidebar menu, look for **"API Settings"** or **"API Configuration"**
2. Click to access the API settings section

### 1.3 Generate a New API Key
1. Click **"Generate New API Key"** or **"Generate New Key"**
2. Give it a descriptive name (e.g., "GPT Actions Integration")
3. Copy the generated key and **store it securely**
4. ⚠️ **IMPORTANT**: The key will only be shown once!

**Example API Key:**
```
lc_1234567890abcdef1234567890abcdef12345678
```

---

## 🤖 Step 2: Access GPT Actions

### 2.1 Access OpenAI Platform
1. Go to [https://platform.openai.com](https://platform.openai.com)
2. Log in to your OpenAI account
3. Navigate to **"GPTs"** in the sidebar

### 2.2 Create or Edit a GPT
1. Click **"Create"** to create a new GPT
2. Or select an existing GPT and click **"Edit"**

### 2.3 Access Actions Configuration
1. In the GPT editor, click the **"Configure"** tab
2. Scroll down to find the **"Actions"** section
3. Click **"Add actions"** or **"Create new action"**

---

## 🔧 Step 3: Configure the Action

### 3.1 Import OpenAPI Specification

**Recommended Method (Direct URL):**
1. Select **"Import from URL"**
2. Paste this URL:
```
https://raw.githubusercontent.com/letscloud-community/letscloud-openapi-gpt/main/openapi.yaml
```
3. Click **"Import"**

**Alternative Method (File Upload):**
1. Download the `openapi.yaml` file from the repository
2. Select **"Upload file"**
3. Upload the downloaded file

### 3.2 Configure Authentication

After importing, you'll see an **"Authentication"** section:

1. **Authentication Type**: Select **"API Key"**
2. **Header Name**: Type `Authorization`
3. **Header Value Format**: Type `Bearer {api_key}`
4. **API Key**: Paste your LetsCloud key (without "Bearer")

**Complete Configuration:**
```yaml
Authentication Type: API Key
Header Name: Authorization
Header Value Format: Bearer {api_key}
API Key: lc_1234567890abcdef1234567890abcdef12345678
```

### 3.3 Verify Import

After configuration, you should see:

✅ **21 Actions available:**
- Server Management (7 actions)
- SSH Key Management (4 actions)  
- Snapshot Management (5 actions)
- Resource Discovery (4 actions)
- Account Information (1 action)

✅ **Base URL configured:**
- `https://core.letscloud.io/api`

✅ **Authentication configured:**
- ApiKeyAuth scheme active

---

## 🧪 Step 4: Test Configuration

### 4.1 Save and Publish
1. Click **"Save"** to save the configuration
2. Click **"Publish"** to publish the GPT

### 4.2 Test with Simple Commands

**Test 1: List Servers**
```
"List all my servers"
```

**Expected Response:**
```
I'll check your servers for you. Let me list all the servers in your LetsCloud account.

[Executing listServers action...]

Here are your servers:
- Server ID: 123, Label: "My Web Server", Status: running
- Server ID: 124, Label: "Database Server", Status: stopped
```

**Test 2: Check Available Plans**
```
"Show me available server plans"
```

**Expected Response:**
```
I'll show you the available server plans on LetsCloud.

[Executing listPlans action...]

Available plans:
- Basic 1GB: $5/month (1 CPU, 1GB RAM, 25GB SSD)
- Standard 2GB: $10/month (2 CPU, 2GB RAM, 50GB SSD)
- Premium 4GB: $20/month (4 CPU, 4GB RAM, 100GB SSD)
```

**Test 3: Account Information**
```
"Check my account information"
```

---

## 💬 Step 5: Use Advanced Commands

### 5.1 Server Creation
```
"Create a new web server with Ubuntu 22.04, 2GB RAM, in New York"
```

### 5.2 SSH Key Management
```
"Add a new SSH key for my laptop"
```

### 5.3 Backup and Snapshots
```
"Create a backup snapshot of my production server"
```

### 5.4 Monitoring
```
"Show me the status of all my servers"
```

---

## 🔧 Troubleshooting

### ❌ Error: "Authentication failed"

**Cause:** Invalid or malformed API Key

**Solution:**
1. Verify the API Key is correct
2. Make sure you didn't include "Bearer" in the API Key field
3. Test the key directly:
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" https://core.letscloud.io/api/servers
```

### ❌ Error: "Action not found"

**Cause:** OpenAPI specification not imported correctly

**Solution:**
1. Verify the URL is correct
2. Try uploading the local file
3. Check if 21 actions are available

### ❌ Error: "Network error"

**Cause:** Connectivity issue or API unavailable

**Solution:**
1. Check your internet connection
2. Test if letscloud.io is accessible
3. Wait a few minutes and try again

### ❌ Error: "Rate limit exceeded"

**Cause:** Too many requests in a short time

**Solution:**
1. Wait a few minutes
2. Reduce command frequency
3. Use more specific commands

---

## 📊 Monitoring and Logs

### Check OpenAI Logs
1. Go to [https://platform.openai.com/usage](https://platform.openai.com/usage)
2. Check Actions requests
3. Monitor errors and latency

### Check LetsCloud Logs
1. Access your LetsCloud dashboard
2. Go to "API Usage" or "Logs"
3. Check the requests made

---

## 🛡️ Security

### Best Practices
- ✅ **Never share** your API Key
- ✅ **Rotate** the key periodically
- ✅ **Monitor** API usage
- ✅ **Use HTTPS** always
- ✅ **Keep** the GPT private if needed

### Security Settings
```yaml
# Recommended settings
Privacy: Private (if applicable)
Sharing: Disabled (if applicable)
API Key: Rotate monthly
Monitoring: Enabled
```

---

## 🎯 Real Usage Examples

### Scenario 1: Individual Developer
```
"I need a server to test my Node.js application"
```

### Scenario 2: DevOps Engineer
```
"Set up the entire infrastructure for a staging environment"
```

### Scenario 3: Startup
```
"Optimize my infrastructure costs"
```

### Scenario 4: SysAdmin
```
"Backup all critical servers"
```

---

## 📞 Support

### Useful Resources
- [LetsCloud Documentation](https://www.letscloud.io/docs)
- [OpenAI Platform](https://platform.openai.com/docs)
- [Project Repository](https://github.com/letscloud-community/letscloud-openapi-gpt)

### Contact
- **LetsCloud Support**: support@letscloud.io
- **Issues**: [GitHub Issues](https://github.com/letscloud-community/letscloud-openapi-gpt/issues)

---

## ✅ Final Checklist

- [ ] LetsCloud API Key obtained
- [ ] GPT Actions configured
- [ ] OpenAPI specification imported
- [ ] Authentication configured
- [ ] Basic tests completed
- [ ] Advanced commands tested
- [ ] Security configured
- [ ] Monitoring active

**🎉 Congratulations! You can now manage your LetsCloud infrastructure using natural language!**
