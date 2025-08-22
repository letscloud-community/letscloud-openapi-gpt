# Dockerfile for LetsCloud API Documentation Gateway
# This Dockerfile creates a self-hosted API gateway with Nginx and OpenAPI documentation

FROM nginx:alpine

# Install additional tools
RUN apk add --no-cache \
    curl \
    openssl \
    bash \
    && rm -rf /var/cache/apk/*

# Create necessary directories
RUN mkdir -p /var/www/letscloud-api-docs \
    && mkdir -p /etc/nginx/ssl \
    && mkdir -p /var/log/nginx

# Copy Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Copy static files (Swagger UI)
COPY ../docs/index.html /var/www/letscloud-api-docs/
COPY ../openapi.yaml /var/www/letscloud-api-docs/

# Create custom error pages
RUN echo '<!DOCTYPE html><html><head><title>404 - Page Not Found</title></head><body><h1>404 - Page Not Found</h1><p>The requested page could not be found.</p></body></html>' > /var/www/letscloud-api-docs/404.html

RUN echo '<!DOCTYPE html><html><head><title>500 - Server Error</title></head><body><h1>500 - Server Error</h1><p>An internal server error occurred.</p></body></html>' > /var/www/letscloud-api-docs/50x.html

# Set proper permissions
RUN chown -R nginx:nginx /var/www/letscloud-api-docs \
    && chmod -R 755 /var/www/letscloud-api-docs \
    && chown -R nginx:nginx /var/log/nginx

# Create SSL certificate (self-signed for development)
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/letscloud-api.key \
    -out /etc/nginx/ssl/letscloud-api.crt \
    -subj "/C=US/ST=State/L=City/O=Organization/CN=api-docs.yourdomain.com"

# Create health check script
RUN echo '#!/bin/bash\ncurl -f http://localhost:8080/health || exit 1' > /usr/local/bin/healthcheck \
    && chmod +x /usr/local/bin/healthcheck

# Expose ports
EXPOSE 80 443 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD /usr/local/bin/healthcheck

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
