# LetsCould API Documentation

## Overview

The LetsCould API allows you to manage your cloud resources programmatically. All requests must be made over HTTPS for encryption and security.

## Base URL

```
https://api.letscloud.io
```

## Versioning

- **Default version**: v1
- **Version header**: `application/vnd.letscloud.v1+json`

If no version is specified in the header, the default version (v1) will be used.

## Authentication

All API requests require authentication using an API token in the request headers.

### Header Format

```
api-token: your-token-here
```

## HTTP Methods

The API supports the following HTTP methods:

| Method | Usage |
|--------|-------|
| **GET** | For simple retrieval of information about your account and instances. The information you request will be returned as a JSON object. Any request using the GET method is read-only and will not affect any of the objects you are querying. |
| **POST** | To create a new object. The POST request includes all of the attributes necessary to create a new object. |
| **PUT** | To update the information about a resource in your account. It sets the state of the target using the provided values, regardless of their current values. |
| **DELETE** | To destroy a resource and remove it from your account and environment. This will remove the specified object if it is found. If it is not found, the operation will return a response indicating that the object was not found. |

## HTTP Status Codes

The API returns a maximum of 5 HTTP status codes divided into two groups:

### Successful Requests

| Status Code | Description |
|-------------|-------------|
| **200 OK** | Standard response for successful HTTP requests. The actual response will depend on the request method used. In a GET request, the response will contain an entity corresponding to the requested resource. In a POST request, the response will contain an entity describing or containing the result of the action. |

### Unsuccessful Requests

| Status Code | Description |
|-------------|-------------|
| **400 Bad Request** | The server cannot or will not process the request due to an apparent client error (e.g., malformed request syntax, size too large, invalid request message framing, or deceptive request routing). |
| **401 Unauthorized** | Specifically for use when authentication is required and has failed or has not yet been provided. |
| **500 Internal Server Error** | A generic error message, given when an unexpected condition was encountered and no more specific message is suitable. |
| **503 Service Unavailable** | The server is currently unavailable (because it is overloaded or down for maintenance). Generally, this is a temporary state. |

## Response Format

All API responses are returned in JSON format with two main properties: `success` and either `data` or `message`.

### Success Response Examples

```json
{
    "success": true,
    "data": { }
}
```

or

```json
{
    "success": true,
    "message": "string"
}
```

### Error Response Example

```json
{
    "success": false,
    "message": "string"
}
```

## Rate Limits

Rate limits determine how frequently you can call a particular endpoint. The current limits are:

- **Hourly limit**: 5,000 requests per hour
- **Daily limit**: 120,000 requests per day per API token

The rate can vary per resource, and the current rate limiting information is returned in the HTTP headers of your response. Check the response headers for the most recent rate limiting information.

## API Endpoints

### Snapshots

#### Get Snapshot Status

Get the current build status of a snapshot. To find out the slug, you can List All Snapshots.

**Endpoint:** `GET /snapshots/status/:image-slug`

**Headers:**
```
api-token: your-token-here
Accept: application/json
Content-Type: application/json
```

**Path Variables:**
- `image-slug`: The slug of the snapshot (required)

**Example Request:**
```bash
curl --location 'https://api.letscloud.io/snapshots/status/your-image-slug-here' \
--header 'api-token: your-token-here' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json'
```

**Response:**
This request doesn't return any response body.

#### Update Snapshot Label

Update the label of an existing snapshot.

**Endpoint:** `POST /snapshots/:image-slug`

**Headers:**
```
api-token: your-token-here
Content-Type: application/json
```

**Path Variables:**
- `image-slug`: The slug of the snapshot (required)

**Body (formdata):**
```
_method: PUT
label: Your new label
```

**Example Request:**
```bash
curl --location --request PUT 'https://api.letscloud.io/snapshots/your-snapshot-slug' \
--header 'api-token: your-token-here' \
--header 'Content-Type: application/json' \
--form 'label="Your new label"'
```

**Example Response:**
```json
{
  "success": true,
  "message": "Snapshot successfully updated"
}
```

#### Delete Snapshot

Delete a snapshot from your account. To find out the slug, you can List All Snapshots.

**Endpoint:** `POST /snapshots/:image-slug`

**Headers:**
```
api-token: your-token-here
Content-Type: application/json
```

**Path Variables:**
- `image-slug`: The slug of the snapshot (required)

**Body (formdata):**
```
_method: DELETE
```

**Example Request:**
```bash
curl --location --request DELETE 'https://api.letscloud.io/snapshots/your-snapshot-slug' \
--header 'api-token: your-token-here'
```

**Example Response:**
```json
{
  "success": true,
  "message": "Snapshot successfully deleted!"
}
```

### Instances

#### Shutdown Instance

Shutdown a running instance.

**Endpoint:** `POST /instances/:identifier/shutdown`

**Headers:**
```
api-token: your-token-here
```

**Path Variables:**
- `identifier`: The identifier of the instance (required)

**Example Request:**
```bash
curl --location --request POST 'https://api.letscloud.io/instances/your-identifier-here/shutdown' \
--header 'api-token: your-token-here'
```

**Response:**
This request doesn't return any response body.

#### Change Instance Plan

Change the plan of an existing instance.

**Endpoint:** `POST /instances/:identifier/change-plan`

**Headers:**
```
api-token: your-token-here
```

**Path Variables:**
- `identifier`: The identifier of the instance (required)

**Body (formdata):**
```
_method: PUT
plan_slug: 1vcpu-2gb-20ssd
```

**Example Request:**
```bash
curl --location 'https://api.letscloud.io/instances/Mq5VF63YAdCqXt4U/change-plan' \
--header 'api-token: your-token-here' \
--form '_method="PUT"' \
--form 'plan_slug="1vcpu-2gb-20ssd"'
```

**Response:**
This request doesn't return any response body.

### Resources by Location

#### List Plans by Location

Retrieve all available plans for a specific location in your desired currency.

**Endpoint:** `GET /locations/:location-slug/plans`

**Headers:**
```
api-token: your-token-here
```

**Path Variables:**
- `location-slug`: The slug of the location (required)

**Example Request:**
```bash
curl --location 'https://api.letscloud.io/locations/location-slug-here/plans' \
--header 'api-token: your-token-here'
```

**Example Response:**
```json
{
  "success": true,
  "data": [
    {
      "country": "United States",
      "city": "Miami",
      "slug": "MIA1",
      "plans": [
        {
          "currencycode": "USD",
          "shortcode": "$",
          "slug": "1vcpu-1gb-10ssd",
          "core": 1,
          "memory": 1024,
          "disk": 10,
          "bandwidth": 1000,
          "monthly_value": "5.00"
        },
        {
          "currencycode": "USD",
          "shortcode": "$",
          "slug": "1vcpu-2gb-20ssd",
          "core": 1,
          "memory": 2048,
          "disk": 20,
          "bandwidth": 1500,
          "monthly_value": "10.00"
        }
      ]
    }
  ]
}
```

#### List Images by Location

Retrieve all available images for a specific location.

**Endpoint:** `GET /locations/:location-slug/images`

**Headers:**
```
api-token: your-token-here
```

**Path Variables:**
- `location-slug`: The slug of the location (required)

**Example Request:**
```bash
curl --location 'https://api.letscloud.io/locations/location-slug-here/images' \
--header 'api-token: your-token-here'
```

**Example Response:**
```json
{
  "success": true,
  "data": [
    {
      "distro": "CentOS 6.9 x64",
      "os": "linux",
      "slug": "centos-69-x64"
    },
    {
      "distro": "Fedora 27 x64",
      "os": "linux",
      "slug": "fedora-27-x64"
    },
    {
      "distro": "FreeBSD 10.4 x64",
      "os": "freebsd",
      "slug": "freebsd-104-x64"
    }
  ]
}
```

### SSH Keys

#### Store or Generate SSH Key

Store your current SSH key or generate a new one. If you want to update or recreate a new SSH key, use the same title that will be updating the key.

**Important:** After creating a new key, the response will return both `public_key` and `private_key`. You must save the private key because it will not be stored and cannot be retrieved later.

**Endpoint:** `POST /sshkeys`

**Headers:**
```
api-token: your-token-here
Content-Type: application/json
```

**Body:**
```json
{
  "title": "your-title-here",
  "key": "your-key-here"
}
```

**Note:** If you want to generate a new key, send only the `title` and omit the `key` parameter.

**Example Request - Store Current SSH Key:**
```bash
curl --location 'https://api.letscloud.io/sshkeys' \
--header 'api-token: your-token-here' \
--header 'Content-Type: application/json' \
--data '{
  "title": "My Project 1",
  "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDR1FmANsdfdsMmMSKMSDMKDMSKDMSIODM=="
}'
```

**Example Request - Generate New SSH Key:**
```bash
curl --location 'https://api.letscloud.io/sshkeys' \
--header 'api-token: your-token-here' \
--header 'Content-Type: application/json' \
--data '{
  "title": "My New Key"
}'
```

**Example Response:**
```json
{
  "success": true,
  "data": {
    "title": "My Project 1",
    "slug": "my-project-1",
    "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDR1FmANsdfdsMmMSKMSDMKDMSKDMSIODM=="
  }
}
```

#### Delete SSH Key by Slug

Delete an SSH key from your account using its slug.

**Endpoint:** `DELETE /sshkeys`

**Headers:**
```
api-token: your-token-here
Content-Type: application/json
```

**Body:**
```json
{
  "slug": "your-sshkey-slug-here",
  "_method": "DELETE"
}
```

**Example Request:**
```bash
curl --location --request DELETE 'https://api.letscloud.io/sshkeys' \
--header 'api-token: your-token-here' \
--header 'Content-Type: application/json' \
--data '{
  "slug": "my-project-1"
}'
```

**Example Response:**
```json
{
  "success": true,
  "message": "SSH Key was successfully deleted!"
}
```

## Getting Started

1. **Obtain an API Token**: You'll need to generate an API token from your LetsCould dashboard.
2. **Set up Authentication**: Include your API token in the `api-token` header with all requests.
3. **Choose Your Version**: Specify the API version in the `Accept` header if you need a specific version.
4. **Make Requests**: Use the appropriate HTTP method and endpoint for your desired operation.

## Error Handling

Always check the `success` field in the response to determine if your request was successful. If `success` is `false`, the `message` field will contain details about what went wrong.

## Best Practices

1. **Always use HTTPS**: All requests must be made over HTTPS for security.
2. **Handle Rate Limits**: Monitor your request rate and implement appropriate backoff strategies.
3. **Check Response Status**: Always verify both HTTP status codes and the `success` field in responses.
4. **Use Proper Headers**: Include all required headers, especially the `api-token` for authentication.
5. **Version Your Requests**: Specify the API version in headers when needed for compatibility.

## Support

For additional support or questions about the API, please refer to the LetsCould documentation or contact their support team.
