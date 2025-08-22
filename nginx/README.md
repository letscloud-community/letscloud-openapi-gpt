# Nginx API Gateway - LetsCloud API Documentation

This directory contains the configuration for a self-hosted API gateway using Nginx to serve the LetsCloud API documentation with OpenAPI/Swagger UI.

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Client        │    │   Nginx Gateway  │    │   LetsCloud API │
│   (Browser)     │───▶│   (Documentation)│───▶│   (core.letscloud.io) │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │   Monitoring     │
                       │   (Prometheus)   │
                       └──────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │   Visualization  │
                       │   (Grafana)      │
                       └──────────────────┘
```

## 📁 File Structure

```
nginx/
├── nginx.conf              # Nginx configuration
├── Dockerfile              # Docker image definition
├── docker-compose.yml      # Multi-service orchestration
├── deploy.sh               # Deployment script
├── README.md               # This file
├── ssl/                    # SSL certificates (created during deployment)
├── logs/                   # Nginx logs
└── grafana/                # Grafana configuration
    ├── dashboards/         # Dashboard definitions
    └── datasources/        # Data source configurations
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Domain name pointing to your server (for production)
- Ports 80, 443, 8080 available

### 1. Basic Deployment

```bash
# Clone the repository
git clone <repository-url>
cd letscloud-openapi-gpt-actions/nginx

# Make deployment script executable
chmod +x deploy.sh

# Deploy with default settings
./deploy.sh
```

### 2. Custom Domain Deployment

```bash
# Deploy with custom domain
./deploy.sh api-docs.yourdomain.com production admin@yourdomain.com
```

### 3. Development Deployment

```bash
# Deploy for development (no SSL, localhost)
./deploy.sh localhost development
```

## 🔧 Configuration

### Nginx Configuration (`nginx.conf`)

The Nginx configuration includes:

- **SSL/TLS Support**: Automatic HTTPS redirection
- **Rate Limiting**: API and documentation rate limiting
- **CORS Support**: Cross-origin resource sharing
- **Caching**: Static asset caching
- **Security Headers**: XSS protection, content type sniffing prevention
- **API Proxy**: Optional proxy to LetsCloud API
- **Health Checks**: Built-in health monitoring

### Key Features

```nginx
# Rate limiting
limit_req_zone $binary_remote_addr zone=api:10m rate=10r/s;
limit_req_zone $binary_remote_addr zone=docs:10m rate=30r/s;

# SSL configuration
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;

# Security headers
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
```

### Docker Compose Services

1. **letscloud-api-gateway**: Main Nginx service
2. **redis**: Caching layer (optional)
3. **prometheus**: Metrics collection (optional)
4. **grafana**: Metrics visualization (optional)

## 📊 Monitoring

### Prometheus Metrics

The gateway exposes metrics at `/status`:

- Request count
- Response times
- Error rates
- Active connections

### Grafana Dashboards

Pre-configured dashboards for:

- API usage patterns
- Response time trends
- Error rate monitoring
- Geographic distribution

### Health Checks

```bash
# Check API Gateway health
curl http://localhost:8080/health

# Check all services
docker-compose ps
```

## 🔒 Security

### SSL/TLS Configuration

For production, replace the self-signed certificate:

```bash
# Generate Let's Encrypt certificate
certbot certonly --standalone -d api-docs.yourdomain.com

# Copy certificates
cp /etc/letsencrypt/live/api-docs.yourdomain.com/fullchain.pem ssl/letscloud-api.crt
cp /etc/letsencrypt/live/api-docs.yourdomain.com/privkey.pem ssl/letscloud-api.key
```

### Security Headers

The configuration includes comprehensive security headers:

- **X-Frame-Options**: Prevent clickjacking
- **X-Content-Type-Options**: Prevent MIME type sniffing
- **X-XSS-Protection**: XSS protection
- **Strict-Transport-Security**: Force HTTPS
- **Content-Security-Policy**: Resource loading restrictions

### Rate Limiting

```nginx
# API requests: 10 requests per second
limit_req zone=api burst=20 nodelay;

# Documentation: 30 requests per second
limit_req zone=docs burst=20 nodelay;
```

## 🛠️ Management

### Service Management

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f letscloud-api-gateway

# Restart services
docker-compose restart

# Update services
docker-compose pull && docker-compose up -d
```

### Configuration Updates

```bash
# Update Nginx configuration
docker-compose exec letscloud-api-gateway nginx -s reload

# Update OpenAPI specification
cp ../openapi.yaml . && docker-compose restart letscloud-api-gateway
```

### Backup and Recovery

```bash
# Backup configuration
tar -czf letscloud-api-backup-$(date +%Y%m%d).tar.gz \
    nginx.conf docker-compose.yml ssl/ grafana/

# Restore from backup
tar -xzf letscloud-api-backup-20240101.tar.gz
docker-compose up -d
```

## 📈 Performance

### Optimization Features

- **Gzip Compression**: Reduces bandwidth usage
- **Static Asset Caching**: Long-term caching for static files
- **Connection Pooling**: Efficient upstream connections
- **Buffer Optimization**: Optimized proxy buffering

### Performance Monitoring

```bash
# Check Nginx status
curl http://localhost:8080/status

# Monitor resource usage
docker stats letscloud-api-gateway

# Check response times
curl -w "@curl-format.txt" -o /dev/null -s http://localhost:8080/
```

## 🔍 Troubleshooting

### Common Issues

1. **SSL Certificate Errors**
   ```bash
   # Check certificate validity
   openssl x509 -in ssl/letscloud-api.crt -text -noout
   
   # Regenerate self-signed certificate
   docker-compose exec letscloud-api-gateway \
     openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
     -keyout /etc/nginx/ssl/letscloud-api.key \
     -out /etc/nginx/ssl/letscloud-api.crt
   ```

2. **Port Conflicts**
   ```bash
   # Check port usage
   netstat -tulpn | grep :80
   netstat -tulpn | grep :443
   
   # Modify ports in docker-compose.yml
   ports:
     - "8080:80"    # Use different external port
     - "8443:443"
   ```

3. **Permission Issues**
   ```bash
   # Fix file permissions
   sudo chown -R $USER:$USER ssl/ logs/
   chmod 600 ssl/*.key
   chmod 644 ssl/*.crt
   ```

### Log Analysis

```bash
# View Nginx access logs
docker-compose exec letscloud-api-gateway tail -f /var/log/nginx/access.log

# View Nginx error logs
docker-compose exec letscloud-api-gateway tail -f /var/log/nginx/error.log

# Analyze traffic patterns
docker-compose exec letscloud-api-gateway \
  awk '{print $1}' /var/log/nginx/access.log | sort | uniq -c | sort -nr
```

## 🌐 Integration

### GPT Actions Integration

The gateway can be used as a proxy for GPT Actions:

1. **Configure GPT Actions** to use your gateway URL
2. **Set up authentication** through the gateway
3. **Monitor usage** through Prometheus/Grafana

### API Proxy Mode

Enable API proxying by uncommenting the `/api/` location block in `nginx.conf`:

```nginx
location /api/ {
    proxy_pass https://letscloud_api;
    # ... proxy configuration
}
```

### Custom Domains

Update the domain configuration:

```bash
# Update domain in configuration files
sed -i 's/api-docs.yourdomain.com/your-actual-domain.com/g' nginx.conf
sed -i 's/api-docs.yourdomain.com/your-actual-domain.com/g' docker-compose.yml
```

## 📚 Additional Resources

- [Nginx Documentation](https://nginx.org/en/docs/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)

## 🤝 Support

For issues and questions:

1. Check the troubleshooting section above
2. Review the logs: `docker-compose logs -f`
3. Verify configuration: `docker-compose config`
4. Test connectivity: `curl -I http://localhost:8080/health`

---

**Note**: This configuration is optimized for production use. For development, consider using the development server block on port 8080.
