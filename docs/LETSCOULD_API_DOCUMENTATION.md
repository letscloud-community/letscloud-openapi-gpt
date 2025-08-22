# LetsCould API Documentation

## Overview

The LetsCould API allows you to manage your cloud resources programmatically. All requests must be made over HTTPS for encryption and security.

## Base URL

```
https://core.letscloud.io/api
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

Retrieve the current build status of a snapshot.

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
curl --location 'https://core.letscloud.io/api/snapshots/status/your-image-slug-here' \
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
curl --location --request PUT 'https://core.letscloud.io/api/snapshots/your-snapshot-slug' \
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

Delete a snapshot from your account.

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
curl --location --request DELETE 'https://core.letscloud.io/api/snapshots/your-snapshot-slug' \
--header 'api-token: your-token-here'
```

**Example Response:**
```json
{
  "success": true,
  "message": "Snapshot successfully deleted!"
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
