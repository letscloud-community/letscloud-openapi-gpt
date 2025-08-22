# ⚡ Quick Setup - LetsCloud API in GPT Actions

## 🎯 Executive Summary

**OpenAPI Specification URL:**
```
https://raw.githubusercontent.com/letscloud-community/letscloud-openapi-gpt/main/openapi.yaml
```

**Authentication Configuration:**
```yaml
Authentication Type: API Key
Header Name: Authorization
Header Value Format: Bearer {api_key}
API Key: [your_letscloud_key]
```

---

## 📋 Essential Steps (5 minutes)

### 1. Get API Key
- Go to: https://www.letscloud.io
- Dashboard → API Settings → Generate New API Key
- Copy the key (format: `lc_1234567890abcdef...`)

### 2. Configure GPT Actions
- Go to: https://platform.openai.com
- GPTs → Create/Edit → Configure → Actions
- Import from URL: paste the URL above

### 3. Configure Authentication
- Authentication Type: **API Key**
- Header Name: **Authorization**
- Header Value Format: **Bearer {api_key}**
- API Key: **paste your key** (without "Bearer")

### 4. Test
```
"List all my servers"
```

---

## 🔧 Complete Configuration

### OpenAPI Specification
```yaml
# URL for import
https://raw.githubusercontent.com/letscloud-community/letscloud-openapi-gpt/main/openapi.yaml

# API Base URL
https://core.letscloud.io/api

# Available actions: 21
- Server Management: 7 actions
- SSH Key Management: 4 actions
- Snapshot Management: 5 actions
- Resource Discovery: 4 actions
- Account Information: 1 action
```

### Authentication
```yaml
# Security scheme
security:
  - ApiKeyAuth: []

# Configuration in GPT Actions
Authentication Type: API Key
Header Name: Authorization
Header Value Format: Bearer {api_key}
API Key: lc_1234567890abcdef1234567890abcdef12345678
```

---

## 🧪 Quick Tests

### Basic Test
```
"Show me available server plans"
```

### Authentication Test
```
"List all my servers"
```

### Creation Test
```
"Create a test server with Ubuntu 22.04"
```

---

## ❌ Common Issues

| Problem | Solution |
|---------|----------|
| "Authentication failed" | Verify API Key is correct |
| "Action not found" | Reimport OpenAPI specification |
| "Network error" | Check connectivity to letscloud.io |
| "Rate limit exceeded" | Wait a few minutes |

---

## 📞 Quick Support

- **Complete Documentation**: [GPT_ACTIONS_SETUP_GUIDE.md](GPT_ACTIONS_SETUP_GUIDE.md)
- **LetsCloud Support**: support@letscloud.io
- **GitHub Issues**: [Report Issue](https://github.com/letscloud-community/letscloud-openapi-gpt/issues)

---

## ✅ Verification Checklist

- [ ] API Key obtained from LetsCloud
- [ ] OpenAPI specification imported
- [ ] Authentication configured
- [ ] Basic test working
- [ ] 21 actions available

**🎉 Setup complete! You can now manage your infrastructure with natural language.**
