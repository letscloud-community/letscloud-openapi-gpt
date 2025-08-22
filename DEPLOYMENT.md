# Deployment Guide - LetsCloud API OpenAPI for GPT Actions

This guide provides step-by-step instructions for deploying and publishing the LetsCloud API OpenAPI specification for use with GPT Actions.

## 📋 Prerequisites

Before deploying, ensure you have:

- [ ] A LetsCloud account with API access
- [ ] Your LetsCloud API key
- [ ] Access to GPT Actions (OpenAI account with appropriate permissions)
- [ ] Basic understanding of OpenAPI specifications

## 🚀 Deployment Options

### Option 1: Direct GPT Actions Integration

#### Step 1: Prepare Your API Key

1. **Get your LetsCloud API key**:
   - Log into your LetsCloud account
   - Navigate to API settings
   - Generate a new API key or copy your existing one

2. **Set up environment variable** (recommended):
   ```bash
   export LETSCLOUD_API_KEY=your_api_key_here
   ```

#### Step 2: Configure GPT Actions

1. **Access GPT Actions**:
   - Go to your OpenAI account
   - Navigate to GPT Actions configuration
   - Click "Add Action"

2. **Import OpenAPI Specification**:
   - Use the `openapi.yaml` file from this repository
   - Upload or paste the specification content
   - GPT will automatically parse the endpoints

3. **Configure Authentication**:
   - Select "API Key" authentication type
   - Set header name: `api-token`
   - Set header value format: `{api_token}`
   - Provide your LetsCloud API key

4. **Test the Integration**:
   - Use the GPT Actions testing interface
   - Try a simple action like "list servers"
   - Verify the response format

### Option 2: Self-Hosted API Gateway

#### Step 1: Set Up API Gateway

1. **Choose a gateway solution**:
   - AWS API Gateway
   - Kong Gateway
   - Custom Node.js/Express server

2. **Deploy the gateway**:
   ```bash
   # Example with Express.js
   npm install express swagger-ui-express
   ```

3. **Configure CORS** (if needed):
   ```javascript
   app.use(cors({
     origin: ['https://chat.openai.com'],
     credentials: true
   }));
   ```

#### Step 2: Deploy to Cloud Platform

**AWS Lambda + API Gateway**:
```yaml
# serverless.yml
service: letscloud-api-gateway

provider:
  name: aws
  runtime: nodejs18.x
  region: us-east-1

functions:
  api:
    handler: handler.api
    events:
      - http:
          path: /{proxy+}
          method: ANY
          cors: true
```

**Docker Deployment**:
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

### Option 3: GitHub Pages + Swagger UI

#### Step 1: Set Up GitHub Pages

1. **Create a new repository** for hosting the OpenAPI spec
2. **Upload the files**:
   - `openapi.yaml`
   - `index.html` (Swagger UI)
   - `README.md`

3. **Enable GitHub Pages**:
   - Go to repository settings
   - Enable GitHub Pages
   - Select source branch

#### Step 2: Create Swagger UI Page

```html
<!DOCTYPE html>
<html>
<head>
    <title>LetsCloud API Documentation</title>
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@5.0.0/swagger-ui.css">
</head>
<body>
    <div id="swagger-ui"></div>
    <script src="https://unpkg.com/swagger-ui-dist@5.0.0/swagger-ui-bundle.js"></script>
    <script>
        window.onload = function() {
            SwaggerUIBundle({
                url: './openapi.yaml',
                dom_id: '#swagger-ui',
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIStandalonePreset
                ],
                layout: "StandaloneLayout"
            });
        };
    </script>
</body>
</html>
```

## 🔧 Configuration Details

### Environment Variables

```bash
# Required
LETSCLOUD_API_KEY=your_api_key_here

# Optional
LETSCLOUD_BASE_URL=https://core.letscloud.io/api
LETSCLOUD_ENVIRONMENT=production
```

### GPT Actions Configuration

```yaml
# Example GPT Actions config
name: "LetsCloud Cloud Management"
description: "Manage cloud infrastructure on LetsCloud platform"

actions:
  - name: "list_servers"
    description: "List all servers in your account"
    operation_id: "listServers"
    
  - name: "create_server"
    description: "Create a new server"
    operation_id: "createServer"
    
  - name: "manage_ssh_keys"
    description: "Manage SSH keys"
    operation_id: "listSSHKeys"
```

## 🧪 Testing

### Local Testing

1. **Install dependencies**:
   ```bash
   cd examples
   pip install -r requirements.txt
   ```

2. **Run the test script**:
   ```bash
   python usage-examples.py
   ```

3. **Verify API responses**:
   - Check that all endpoints return expected data
   - Verify error handling works correctly
   - Test authentication with invalid keys

### GPT Actions Testing

1. **Test basic operations**:
   ```
   User: "List my servers"
   GPT: [Calls listServers action]
   ```

2. **Test complex workflows**:
   ```
   User: "Create a new web server with Ubuntu 22.04"
   GPT: [Calls listPlans, listImages, createServer actions]
   ```

3. **Test error scenarios**:
   - Invalid API key
   - Non-existent resources
   - Invalid parameters

## 🔒 Security Considerations

### API Key Management

1. **Secure storage**:
   - Use environment variables
   - Never commit API keys to version control
   - Rotate keys regularly

2. **Access control**:
   - Limit API key permissions
   - Monitor usage patterns
   - Set up alerts for unusual activity

### Rate Limiting

1. **Client-side implementation**:
   ```python
   import time
   from functools import wraps
   
   def rate_limit(calls_per_minute=60):
       def decorator(func):
           @wraps(func)
           def wrapper(*args, **kwargs):
               time.sleep(60 / calls_per_minute)
               return func(*args, **kwargs)
           return wrapper
       return decorator
   ```

2. **Server-side monitoring**:
   - Track API usage
   - Implement backoff strategies
   - Handle rate limit errors gracefully

## 📊 Monitoring and Analytics

### Set Up Monitoring

1. **API usage tracking**:
   ```python
   import logging
   
   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)
   
   def log_api_call(endpoint, status_code, response_time):
       logger.info(f"API Call: {endpoint} - {status_code} - {response_time}ms")
   ```

2. **Error tracking**:
   - Monitor failed requests
   - Track authentication errors
   - Alert on unusual patterns

### Analytics Dashboard

Consider setting up:
- Request volume over time
- Most used endpoints
- Error rates
- Response times
- User activity patterns

## 🚨 Troubleshooting

### Common Issues

1. **Authentication Errors**:
   - Verify API key is correct
   - Check key permissions
   - Ensure proper header format

2. **CORS Issues**:
   - Configure CORS headers
   - Allow OpenAI domains
   - Test with different browsers

3. **Rate Limiting**:
   - Implement exponential backoff
   - Monitor usage limits
   - Contact support if needed

### Debug Mode

Enable debug logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Support Resources

- [LetsCloud Documentation](https://developers.letscloud.io)
- [OpenAPI Specification Guide](https://swagger.io/docs/specification/)
- [GPT Actions Documentation](https://platform.openai.com/docs/actions)

## 📈 Performance Optimization

### Caching Strategy

1. **Resource discovery caching**:
   ```python
   import time
   from functools import lru_cache
   
   @lru_cache(maxsize=128)
   def get_plans():
       # Cache plans for 1 hour
       return client.list_plans()
   ```

2. **Response optimization**:
   - Compress responses
   - Use pagination
   - Implement conditional requests

### Load Balancing

For high-traffic deployments:
- Use multiple API endpoints
- Implement health checks
- Set up failover mechanisms

## 🔄 Updates and Maintenance

### Version Management

1. **API versioning**:
   - Use semantic versioning
   - Maintain backward compatibility
   - Document breaking changes

2. **Update schedule**:
   - Regular security updates
   - Feature additions
   - Bug fixes

### Backup Strategy

1. **Configuration backups**:
   - Version control for configs
   - Regular backups of API keys
   - Document all changes

2. **Disaster recovery**:
   - Multiple deployment regions
   - Automated failover
   - Recovery procedures

---

**Note**: This deployment guide is based on the current OpenAPI specification. Always refer to the latest LetsCloud documentation for the most up-to-date information.
