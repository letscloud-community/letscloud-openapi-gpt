#!/bin/bash

# LetsCloud API Gateway Deployment Script
# This script sets up and deploys the Nginx API gateway with OpenAPI documentation

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
DOMAIN=${1:-"api-docs.yourdomain.com"}
ENVIRONMENT=${2:-"production"}
SSL_EMAIL=${3:-"admin@yourdomain.com"}

echo -e "${BLUE}🚀 LetsCloud API Gateway Deployment${NC}"
echo -e "${BLUE}================================${NC}"
echo ""

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   print_error "This script should not be run as root"
   exit 1
fi

# Check prerequisites
print_info "Checking prerequisites..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    print_error "Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

print_status "Prerequisites check passed"

# Create necessary directories
print_info "Creating directories..."
mkdir -p ssl logs grafana/dashboards grafana/datasources
print_status "Directories created"

# Generate SSL certificate for production
if [ "$ENVIRONMENT" = "production" ]; then
    print_info "Setting up SSL certificate for production..."
    
    # Check if certbot is available
    if command -v certbot &> /dev/null; then
        print_info "Using Let's Encrypt for SSL certificate..."
        # This would require additional setup with certbot
        print_warning "SSL certificate setup requires manual configuration with Let's Encrypt"
    else
        print_warning "Certbot not found. Using self-signed certificate for now."
        print_info "You can replace it later with a proper SSL certificate."
    fi
else
    print_info "Using self-signed certificate for development..."
fi

# Copy configuration files
print_info "Copying configuration files..."

# Copy the OpenAPI specification
if [ -f "../openapi.yaml" ]; then
    cp ../openapi.yaml .
    print_status "OpenAPI specification copied"
else
    print_error "OpenAPI specification not found at ../openapi.yaml"
    exit 1
fi

# Copy the Swagger UI HTML
if [ -f "../docs/index.html" ]; then
    cp ../docs/index.html .
    print_status "Swagger UI copied"
else
    print_error "Swagger UI not found at ../docs/index.html"
    exit 1
fi

# Create Prometheus configuration
cat > prometheus.yml << EOF
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'letscloud-api-gateway'
    static_configs:
      - targets: ['letscloud-api-gateway:8080']
    metrics_path: /status
    scrape_interval: 5s
EOF
print_status "Prometheus configuration created"

# Create Grafana datasource
mkdir -p grafana/datasources
cat > grafana/datasources/prometheus.yml << EOF
apiVersion: 1

datasources:
  - name: Prometheus
    type: prometheus
    access: proxy
    url: http://prometheus:9090
    isDefault: true
EOF
print_status "Grafana datasource configuration created"

# Create Grafana dashboard
mkdir -p grafana/dashboards
cat > grafana/dashboards/letscloud-api.yml << EOF
apiVersion: 1

providers:
  - name: 'LetsCloud API'
    orgId: 1
    folder: ''
    type: file
    disableDeletion: false
    updateIntervalSeconds: 10
    allowUiUpdates: true
    options:
      path: /etc/grafana/provisioning/dashboards
EOF
print_status "Grafana dashboard configuration created"

# Update domain in configuration
print_info "Updating domain configuration..."
sed -i "s/api-docs.yourdomain.com/$DOMAIN/g" nginx.conf
sed -i "s/api-docs.yourdomain.com/$DOMAIN/g" docker-compose.yml
print_status "Domain configuration updated"

# Build and start services
print_info "Building and starting services..."
docker-compose build
print_status "Services built"

docker-compose up -d
print_status "Services started"

# Wait for services to be ready
print_info "Waiting for services to be ready..."
sleep 10

# Check service health
print_info "Checking service health..."

# Check API Gateway
if curl -f http://localhost:8080/health > /dev/null 2>&1; then
    print_status "API Gateway is healthy"
else
    print_error "API Gateway health check failed"
    docker-compose logs letscloud-api-gateway
    exit 1
fi

# Check Redis (if enabled)
if docker-compose ps redis | grep -q "Up"; then
    if docker-compose exec redis redis-cli ping | grep -q "PONG"; then
        print_status "Redis is healthy"
    else
        print_warning "Redis health check failed"
    fi
fi

# Check Prometheus (if enabled)
if docker-compose ps prometheus | grep -q "Up"; then
    if curl -f http://localhost:9090/-/healthy > /dev/null 2>&1; then
        print_status "Prometheus is healthy"
    else
        print_warning "Prometheus health check failed"
    fi
fi

# Check Grafana (if enabled)
if docker-compose ps grafana | grep -q "Up"; then
    if curl -f http://localhost:3000/api/health > /dev/null 2>&1; then
        print_status "Grafana is healthy"
    else
        print_warning "Grafana health check failed"
    fi
fi

# Display deployment information
echo ""
echo -e "${GREEN}🎉 Deployment completed successfully!${NC}"
echo ""
echo -e "${BLUE}📋 Service Information:${NC}"
echo -e "  API Documentation: ${GREEN}http://$DOMAIN${NC}"
echo -e "  API Gateway: ${GREEN}http://localhost:8080${NC}"
echo -e "  Health Check: ${GREEN}http://localhost:8080/health${NC}"
echo ""

if docker-compose ps prometheus | grep -q "Up"; then
    echo -e "  Prometheus: ${GREEN}http://localhost:9090${NC}"
fi

if docker-compose ps grafana | grep -q "Up"; then
    echo -e "  Grafana: ${GREEN}http://localhost:3000${NC}"
    echo -e "    Username: ${YELLOW}admin${NC}"
    echo -e "    Password: ${YELLOW}admin${NC}"
fi

if docker-compose ps redis | grep -q "Up"; then
    echo -e "  Redis: ${GREEN}localhost:6379${NC}"
fi

echo ""
echo -e "${BLUE}🔧 Management Commands:${NC}"
echo -e "  View logs: ${YELLOW}docker-compose logs -f${NC}"
echo -e "  Stop services: ${YELLOW}docker-compose down${NC}"
echo -e "  Restart services: ${YELLOW}docker-compose restart${NC}"
echo -e "  Update services: ${YELLOW}docker-compose pull && docker-compose up -d${NC}"
echo ""

echo -e "${BLUE}🔒 Security Notes:${NC}"
echo -e "  - Change default passwords for Grafana"
echo -e "  - Configure proper SSL certificates for production"
echo -e "  - Set up firewall rules"
echo -e "  - Monitor logs for security issues"
echo ""

print_status "Deployment script completed"
