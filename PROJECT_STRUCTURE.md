# Project Structure

This document provides an overview of the project structure and the purpose of each file in the LetsCould API OpenAPI specification for GPT Actions.

## 📁 Root Directory

```
letscould-openapi-gpt/
├── docs/
│   ├── openapi.yaml                    # Main OpenAPI 3.1 specification
│   ├── LETSCOULD_API_DOCUMENTATION.md  # Complete API documentation
│   ├── index.html                      # GitHub Pages main page
│   ├── privacy-policy.html             # Privacy policy page
│   ├── robots.txt                      # SEO configuration
│   ├── sitemap.xml                     # Site map for search engines
│   └── _config.yml                     # Jekyll configuration
├── README.md                           # Project documentation and usage guide
├── LICENSE                             # MIT License
├── PROJECT_STRUCTURE.md                # This file - project structure overview
├── gpt-actions-config.yaml             # GPT Actions configuration examples
├── GPT_CREATOR_INSTRUCTIONS.md         # Instructions for GPT creators
├── GPT_DUPLICATION_GUIDE.md            # Guide for duplicating GPTs
├── GPT_ACTIONS_SETUP_GUIDE.md          # Setup guide for GPT Actions
├── QUICK_SETUP.md                      # Quick setup instructions
├── API_KEY_SETUP_GUIDE.md              # API key configuration guide
├── KNOWLEDGE_FILES.md                  # Knowledge files documentation
├── .gitignore                          # Git ignore rules
├── docs/
│   ├── assets/                         # Static assets and images
│   │   └── LetsCloud_logo.png          # LetsCould logo image
├── examples/                           # Code examples and implementations
│   ├── usage-examples.py               # Python client implementation
│   └── requirements.txt                # Python dependencies
└── knowledge-examples/                 # Knowledge base examples
    └── letscloud-platform-guide.md     # Platform usage guide
```

## 📄 File Descriptions

### Core Files

#### `docs/openapi.yaml`
- **Purpose**: Main OpenAPI 3.1 specification file for LetsCould API
- **Content**: Complete API definition with all endpoints, schemas, and examples
- **Usage**: Import directly into GPT Actions or use with API documentation tools
- **Key Features**:
  - 20+ API endpoints for cloud management
  - Comprehensive data models
  - Detailed error responses
  - Authentication configuration
  - GPT Actions optimized operation IDs
  - Updated for LetsCould API v1.0.0

#### `docs/LETSCOULD_API_DOCUMENTATION.md`
- **Purpose**: Complete API documentation for LetsCould
- **Content**: 
  - Authentication methods
  - HTTP methods and status codes
  - Response formats
  - Rate limits
  - Endpoint examples
  - Best practices
- **Target Audience**: Developers, DevOps engineers, API users

### Web Documentation Files

#### `docs/index.html`
- **Purpose**: Main GitHub Pages website with interactive API documentation
- **Content**: 
  - Landing page with project overview
  - Interactive Swagger UI for API testing
  - Feature showcase and documentation links
  - Responsive design with modern UI
- **Features**: 
  - Real-time API testing interface
  - Bootstrap-based responsive design
  - SEO optimized with meta tags
  - Social media integration

#### `docs/privacy-policy.html`
- **Purpose**: Privacy policy page for legal compliance
- **Content**: 
  - Comprehensive privacy policy
  - GDPR and CCPA compliance information
  - Data handling practices
  - User rights and contact information
- **Usage**: Required for legal compliance and user trust

#### `docs/robots.txt`
- **Purpose**: SEO configuration for search engine crawlers
- **Content**: 
  - Crawling rules and permissions
  - Sitemap reference
  - Crawl delay settings
- **Usage**: Helps search engines index the site properly

#### `docs/sitemap.xml`
- **Purpose**: XML sitemap for search engine indexing
- **Content**: 
  - List of all important pages
  - Update frequency and priority settings
  - Last modification dates
- **Usage**: Improves search engine discoverability

#### `docs/_config.yml`
- **Purpose**: Jekyll configuration for GitHub Pages
- **Content**: 
  - Site metadata and settings
  - SEO configuration
  - Social media links
  - Build settings
- **Usage**: Controls how GitHub Pages builds and serves the site

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
- **Updated**: Now includes all LetsCould API endpoints



### GPT Integration Files

#### `GPT_CREATOR_INSTRUCTIONS.md`
- **Purpose**: Instructions for creating GPTs with LetsCould API
- **Content**: 
  - Step-by-step GPT creation guide
  - Configuration instructions
  - Best practices
  - Troubleshooting tips

#### `GPT_DUPLICATION_GUIDE.md`
- **Purpose**: Guide for duplicating and customizing GPTs
- **Content**:
  - Duplication process
  - Customization options
  - Configuration management

#### `GPT_ACTIONS_SETUP_GUIDE.md`
- **Purpose**: Detailed setup guide for GPT Actions
- **Content**:
  - Action configuration
  - Authentication setup
  - Testing procedures
  - Integration examples

#### `QUICK_SETUP.md`
- **Purpose**: Quick start guide for immediate setup
- **Content**:
  - Minimal setup steps
  - Essential configuration
  - Basic usage examples

#### `API_KEY_SETUP_GUIDE.md`
- **Purpose**: Guide for setting up API authentication
- **Content**:
  - API key generation
  - Security best practices
  - Environment configuration

#### `KNOWLEDGE_FILES.md`
- **Purpose**: Documentation for knowledge base integration
- **Content**:
  - Knowledge file structure
  - Integration guidelines
  - Best practices

### Assets Directory

#### `assets/LetsCloud_logo.png`
- **Purpose**: LetsCould brand logo for documentation
- **Usage**: Displayed in documentation and examples
- **Format**: PNG image with transparent background
- **Size**: Optimized for web display

### Examples Directory

#### `examples/usage-examples.py`
- **Purpose**: Python client implementation examples
- **Content**:
  - Complete API client class
  - Method implementations for all endpoints
  - Error handling examples
  - Usage patterns
- **Target Audience**: Python developers, API integrators

#### `examples/requirements.txt`
- **Purpose**: Python dependencies for examples
- **Content**: Required packages for running examples
- **Usage**: Install with `pip install -r requirements.txt`

### Knowledge Examples Directory

#### `knowledge-examples/letscloud-platform-guide.md`
- **Purpose**: Platform usage guide for knowledge base
- **Content**:
  - Platform overview
  - Feature descriptions
  - Usage examples
  - Best practices
- **Usage**: Can be used as knowledge base content for GPTs

## 🔄 Recent Changes

### Removed Files
The following files were removed to streamline the project:
- `docs/openapi_simple_backup.yaml` - Backup file no longer needed
- `docs/openapi_test.yaml` - Test specification file
- `docs/openapi_simple.yaml` - Simplified specification file
- `docs/openapi_full.yaml` - Redundant full specification

### Updated Files
- `docs/openapi.yaml` - Updated to LetsCould API v1.0.0
- `gpt-actions-config.yaml` - Updated with new endpoints and operation IDs
- `PROJECT_STRUCTURE.md` - This file updated to reflect current structure

## 🎯 Project Goals

1. **Provide a complete OpenAPI specification** for the LetsCould API
2. **Enable GPT Actions integration** with comprehensive configuration
3. **Offer clear documentation** for developers and users
4. **Maintain clean project structure** with only necessary files
5. **Support multiple deployment options** for different use cases

## 📚 Documentation Structure

The project documentation is organized into several categories:

### Core Documentation
- **API Specification**: `docs/openapi.yaml`
- **API Documentation**: `docs/LETSCOULD_API_DOCUMENTATION.md`
- **Project Overview**: `README.md`

### Setup Guides
- **Quick Setup**: `QUICK_SETUP.md`
- **GPT Actions Setup**: `GPT_ACTIONS_SETUP_GUIDE.md`
- **API Key Setup**: `API_KEY_SETUP_GUIDE.md`

### Integration Guides
- **GPT Creation**: `GPT_CREATOR_INSTRUCTIONS.md`
- **GPT Duplication**: `GPT_DUPLICATION_GUIDE.md`
- **Knowledge Files**: `KNOWLEDGE_FILES.md`

### Advanced Topics
- **Project Structure**: `PROJECT_STRUCTURE.md`

## 🚀 Getting Started

1. **Read the Quick Setup guide** (`QUICK_SETUP.md`)
2. **Configure your API key** (`API_KEY_SETUP_GUIDE.md`)
3. **Set up GPT Actions** (`GPT_ACTIONS_SETUP_GUIDE.md`)
4. **Explore the API documentation** (`docs/LETSCOULD_API_DOCUMENTATION.md`)
5. **Review examples** (`examples/usage-examples.py`)

## 🤝 Contributing

This project is open source and welcomes contributions. Please refer to the individual documentation files for specific guidelines and best practices.
