# Project Structure

This document provides an overview of the project structure and the purpose of each file in the LetsCloud API OpenAPI specification for GPT Actions.

## 📁 Root Directory

```
letscloud-openapi-gpt/
├── openapi.yaml                 # Main OpenAPI 3.0 specification
├── README.md                    # Project documentation and usage guide
├── LICENSE                      # MIT License
├── DEPLOYMENT.md               # Deployment and publishing guide
├── PROJECT_STRUCTURE.md        # This file - project structure overview
├── gpt-actions-config.yaml     # GPT Actions configuration examples
├── .gitignore                  # Git ignore rules
├── assets/                     # Static assets and images
│   └── LetsCloud_logo.png      # LetsCloud logo image
├── docs/                       # Web documentation
│   ├── index.html              # Main API documentation page
│   ├── gpt-actions.html        # GPT Actions documentation page
│   ├── openapi.yaml            # OpenAPI spec for web docs
│   ├── robots.txt              # SEO configuration
│   ├── sitemap.xml             # Site map for search engines
│   └── _config.yml             # Documentation configuration
└── examples/                   # Code examples and implementations
    ├── usage-examples.py       # Python client implementation
    └── requirements.txt        # Python dependencies
```

## 📄 File Descriptions

### Core Files

#### `openapi.yaml`
- **Purpose**: Main OpenAPI 3.0 specification file
- **Content**: Complete API definition with all endpoints, schemas, and examples
- **Usage**: Import directly into GPT Actions or use with API documentation tools
- **Key Features**:
  - 20+ API endpoints for cloud management
  - Comprehensive data models
  - Detailed error responses
  - Authentication configuration
  - GPT Actions optimized operation IDs

#### `README.md`
- **Purpose**: Main project documentation
- **Content**: 
  - Quick start guide
  - API endpoint overview
  - Authentication instructions
  - Usage examples
  - Integration guidelines
- **Target Audience**: Developers, DevOps engineers, GPT Actions users

#### `LICENSE`
- **Purpose**: MIT License for open source usage
- **Content**: Standard MIT license terms
- **Usage**: Allows commercial and non-commercial use with attribution

### Configuration Files

#### `gpt-actions-config.yaml`
- **Purpose**: Example configuration for GPT Actions integration
- **Content**:
  - Action definitions and categories
  - Parameter templates
  - Usage examples
  - Best practices
  - Security considerations
- **Usage**: Reference for setting up GPT Actions

#### `DEPLOYMENT.md`
- **Purpose**: Comprehensive deployment guide
- **Content**:
  - Multiple deployment options
  - Step-by-step instructions
  - Security considerations
  - Troubleshooting guide
  - Performance optimization tips
- **Target Audience**: System administrators, DevOps teams

### Assets Directory

#### `assets/LetsCloud_logo.png`
- **Purpose**: LetsCloud brand logo for web documentation
- **Usage**: Displayed in the footer of the API documentation pages
- **Format**: PNG image with transparent background
- **Size**: Optimized for web display

### Web Documentation Directory

#### `docs/index.html`
- **Purpose**: Main API documentation page with Swagger UI
- **Content**: 
  - Interactive API documentation
  - Swagger UI integration
  - Custom branding and styling
  - Navigation to other pages
- **Features**: 
  - Real-time API testing
  - Authentication setup
  - Request/response examples
  - Mobile responsive design

#### `docs/gpt-actions.html`
- **Purpose**: GPT Actions specific documentation page
- **Content**: 
  - GPT Actions integration guide
  - Configuration examples
  - Best practices
  - Troubleshooting tips

#### `docs/openapi.yaml`
- **Purpose**: OpenAPI specification for web documentation
- **Content**: Identical to root openapi.yaml for web access
- **Usage**: Served by web documentation pages

#### `docs/robots.txt`
- **Purpose**: SEO configuration for search engines
- **Content**: Crawling rules and sitemap reference

#### `docs/sitemap.xml`
- **Purpose**: XML sitemap for search engine indexing
- **Content**: List of all documentation pages

#### `docs/_config.yml`
- **Purpose**: Configuration file for documentation generation
- **Content**: Site settings and metadata

### Examples Directory

#### `examples/usage-examples.py`
- **Purpose**: Practical implementation examples
- **Content**:
  - Complete Python client class
  - All API methods implemented
  - Error handling examples
  - GPT Actions workflow examples
- **Usage**: Learning resource and starting point for custom implementations

#### `examples/requirements.txt`
- **Purpose**: Python dependencies for examples
- **Content**: Required packages for running the examples
- **Dependencies**:
  - `requests>=2.31.0` - HTTP client library
  - `typing-extensions>=4.0.0` - Type hints support

## 🏗️ Architecture Overview

### OpenAPI Specification Structure

```
openapi.yaml
├── Info Section
│   ├── Title, description, version
│   ├── Contact information
│   └── License details
├── Servers
│   └── Production API
├── Security
│   └── API Key authentication
├── Paths
│   ├── /servers (GET, POST)
│   ├── /servers/{server_id} (GET, DELETE)
│   ├── /servers/{server_id}/start (POST)
│   ├── /servers/{server_id}/stop (POST)
│   ├── /servers/{server_id}/reboot (POST)
│   ├── /ssh-keys (GET, POST)
│   ├── /ssh-keys/{key_id} (GET, DELETE)
│   ├── /servers/{server_id}/snapshots (GET, POST)
│   ├── /servers/{server_id}/snapshots/{snapshot_id} (GET, DELETE)
│   ├── /servers/{server_id}/snapshots/{snapshot_id}/restore (POST)
│   ├── /plans (GET)
│   ├── /images (GET)
│   ├── /locations (GET)
│   └── /account (GET)
└── Components
    ├── Security Schemes
    ├── Schemas
    │   ├── Server
    │   ├── Plan
    │   ├── Image
    │   ├── Location
    │   ├── SSHKey
    │   ├── Snapshot
    │   ├── Account
    │   └── Error
    └── Responses
        ├── BadRequest
        ├── Unauthorized
        ├── NotFound
        ├── ValidationError
        └── InternalServerError
```

### API Endpoint Categories

#### 1. Server Management
- **Purpose**: Full lifecycle management of cloud servers
- **Endpoints**: 7 endpoints for CRUD operations and power management
- **Key Features**: Create, read, update, delete, start, stop, reboot

#### 2. SSH Key Management
- **Purpose**: Secure access management for servers
- **Endpoints**: 4 endpoints for key management
- **Key Features**: Add, list, view, delete SSH keys

#### 3. Snapshot Management
- **Purpose**: Backup and restore functionality
- **Endpoints**: 5 endpoints for snapshot operations
- **Key Features**: Create, list, view, delete, restore snapshots

#### 4. Resource Discovery
- **Purpose**: Information about available resources
- **Endpoints**: 3 endpoints for resource listing
- **Key Features**: Plans, images, locations discovery

#### 5. Account Information
- **Purpose**: Account and billing information
- **Endpoints**: 1 endpoint for account details
- **Key Features**: Balance, profile, billing information

## 🔧 Integration Points

### GPT Actions Integration

```
GPT Actions Configuration
├── Import openapi.yaml
├── Configure authentication
├── Set up environment variables
├── Test endpoints
└── Deploy to production
```

### Custom Client Integration

```
Custom Implementation
├── Use openapi.yaml as reference
├── Implement client library
├── Add error handling
├── Include authentication
└── Add monitoring/logging
```

### API Gateway Integration

```
API Gateway Setup
├── Load openapi.yaml
├── Configure routing
├── Set up authentication
├── Add rate limiting
└── Deploy to cloud platform
```

## 📊 Data Flow

### Request Flow
```
User Request → GPT Actions → LetsCloud API → Response → User
```

### Authentication Flow
```
API Key → Authorization Header → LetsCloud API → Validation → Response
```

### Error Handling Flow
```
Error → HTTP Status Code → Error Response → User Notification
```

## 🛡️ Security Model

### Authentication
- **Method**: API Key authentication
- **Header**: `Authorization: Bearer {api_key}`
- **Environment Variable**: `LETSCLOUD_API_KEY`

### Authorization
- **Scope**: Account-level access
- **Permissions**: Full account management
- **Rate Limiting**: Server-side enforcement

### Data Protection
- **Transport**: HTTPS/TLS encryption
- **Storage**: Secure API key management
- **Logging**: No sensitive data in logs

## 📈 Scalability Considerations

### API Design
- **Stateless**: Each request is independent
- **RESTful**: Standard HTTP methods and status codes
- **Pagination**: Support for large result sets
- **Caching**: Appropriate cache headers

### Performance
- **Response Time**: Optimized for real-time operations
- **Throughput**: Rate limiting for fair usage
- **Availability**: High availability infrastructure

## 🔄 Versioning Strategy

### API Versioning
- **Current Version**: 1.2.0
- **Backward Compatibility**: Maintained within major versions
- **Deprecation Policy**: Clear communication of changes
- **Migration Path**: Documented upgrade procedures

### Specification Updates
- **Semantic Versioning**: MAJOR.MINOR.PATCH
- **Change Log**: Documented in README
- **Breaking Changes**: Clearly marked and explained

## 🎯 Use Cases

### Primary Use Cases
1. **Server Provisioning**: Automated server creation and configuration
2. **Infrastructure Management**: Ongoing server maintenance and monitoring
3. **Backup Management**: Automated snapshot creation and restoration
4. **Access Control**: SSH key management for secure access
5. **Resource Planning**: Discovery of available plans and locations

### GPT Actions Use Cases
1. **Natural Language Commands**: "Create a web server with Ubuntu"
2. **Workflow Automation**: Multi-step infrastructure setup
3. **Monitoring and Alerts**: Status checking and notifications
4. **Cost Optimization**: Plan comparison and recommendations
5. **Disaster Recovery**: Automated backup and restore procedures

## 📚 Documentation Standards

### Code Comments
- **Language**: English (as per user preference)
- **Style**: Clear and descriptive
- **Examples**: Practical usage examples
- **Updates**: Maintained with code changes

### API Documentation
- **Format**: OpenAPI 3.0 specification
- **Examples**: Comprehensive request/response examples
- **Error Codes**: Detailed error descriptions
- **Authentication**: Clear setup instructions

---

This project structure provides a complete foundation for integrating LetsCloud API with GPT Actions, including comprehensive documentation, examples, and deployment guidance.
