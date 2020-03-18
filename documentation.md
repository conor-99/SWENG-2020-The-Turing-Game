# The Turing Game: API Reference

## Conversations

### Start Conversation

Start a conversation with another user or the AI.

###### Endpoint:

`GET /api/conversation/start`

###### Parameters:

| Name | Type | Description |
| - | - | - |
| `auth` | `string` | The user's authentication token. |

###### Response:

```JSON
{
	"cid": 123
}
```

###### Example:

```cURL
curl -X GET localhost/api/conversation/start -u abcdef_12345
```

```JSON
{
	"cid": 123
}
```

### End Conversation

Submit your guess and finish the conversation. Supply the conversation ID in the URL.

###### Endpoint

`POST /api/conversation/end/:cid`

###### Parameters:

| Name | Type | Description |
| - | - | - |
| `auth` | `string` | The user's authentication token. |
| `guess` | `integer` | The user's guess (i.e. 0 for human or 1 for bot). |

###### Response:

None.

###### Example:

```cURL
curl -X POST localhost/api/conversation/flag/123 -u abcdef_12345 -d '"guess":1'
```

### Flag Conversation

Flag the other user in a conversation for inappropriate behaviour. Supply the conversation ID in the URL.

###### Endpoint

`GET /api/conversation/flag/:cid`

###### Parameters:

| Name | Type | Description |
| - | - | - |
| `auth` | `string` | The user's authentication token. |

###### Response:

None.

###### Example:

```cURL
curl -X GET localhost/api/conversation/flag/123 -u abcdef_12345
```

### Send Message

Send a message in a conversation. Supply the conversation ID in the URL.

###### Endpoint

`POST /api/conversation/send/:cid`

###### Parameters:

| Name | Type | Description |
| - | - | - |
| `auth` | `string` | The user's authentication token. |
| `text` | `string` | The message content. |

###### Response:

None.

###### Example:

```cURL
curl -X POST localhost/api/conversation/send/123 -u abcdef_12345 -d '"text":"Hello World!"'
```

### Receive Message

Get all of the messages from the other user in a conversation. Supply the conversation ID in the URL.

###### Endpoint

`GET /api/conversation/receive/:cid`

###### Parameters:

| Name | Type | Description |
| - | - | - |
| `auth` | `string` | The user's authentication token. |

###### Response:

```JSON
{
	"cid": 123,
    "messages": [
    	{
        	"id": 0,
            "text": "Hello World!",
            "timestamp": "2020-01-01 00:00:00"
        },
        ...
    ]
}
```

###### Example:

```cURL
curl -X GET localhost/api/conversation/receive/123 -u abcdef_12345'
```

```JSON
{
	"cid": 123,
    "messages": [
    	{
        	"id": 0,
            "text": "Hello World!",
            "timestamp": "2020-01-01 00:00:00"
        },
        {
        	"id": 1,
            "text": "How are you?",
            "timestamp": "2020-01-01 00:00:10"
        }
    ]
}
```

## Leaderboards

### Get Leaderboards

Get an object containing the highest scoring users.

###### Endpoint

`GET /api/leaderboards`

###### Parameters:

None.

###### Response:

```JSON
{
	"users": [
    	{
        	"rank": 0,
            "username": "user1",
            "score": 0.95
        },
        ...
    ]
}
```

###### Example:

```cURL
curl -X GET localhost/api/leaderboards
```

```JSON
{
	"users": [
    	{
        	"rank": 0,
            "username": "user1",
            "score": 0.95
        },
        {
        	"rank": 1,
            "username": "user2",
            "score": 0.80
        },
        {
        	"rank": 2,
            "username": "user3",
            "score": 0.79
        },
        {
        	"rank": 3,
            "username": "user4",
            "score": 0.52
        },
        {
        	"rank": 4,
            "username": "user5",
            "score": 0.00
        }
    ]
}
```

## Authentication

### Introduction
Firebase provides built-in method to authenticate users using Google Sign-In. It requires SHA1 fingerprint (should be there now) and generates UserID for a logged in user. 
UserID is persistent, i.e it is unique for a specific user and will be the same on each log in.
It will be used to associate data with a specific user.

### API

When user is logged in on front end, he should be assigned the session token.
This token will be used by back-end to verify the user and proceed with data transfer.
API should be set up like in the documentation below:
[Firebase token verification guide](https://firebase.google.com/docs/auth/admin/verify-id-tokens "Firebase documentation")
