# api
warehouse api


## Base URL:
All endpoints begin with `https://inventory-api-rmot.onrender.com`
NOTE: API Root is /api/
|  Method  |  Endpoint  |  Description |
| -------- | ---------- | ------------ |
|POST|[/auth/users/](#create-a-new-user)|Create a new user|
|POST|[/auth/token/login/](#login-user)|Login user|
|POST|[/auth/users/me/](#users-info)|User's info|
|GET| [auth/users/](#all_users)|List of all users|
|POST|[/auth/token/logout/](#logout-user)|Logout user|

## Create a new user
### Request
Required fields: username and password
Optional fields: email
```json
POST auth/users/
{
  "username": "Tim",
  "password": "Badpassword"
}
```
### Response
Response: If you receive the same info you provided, user creation was successful!
```json
201 Created
{
	"email": "",
	"username": "Tim",
	"id": 3
}

## Login user
### Request
Required fields: username, password
```json
POST auth/token/login/
{
    "username": "Tim",
    "password": "Badpassword"
}
```
### Response
```json
200 OK
{
	"auth_token": "da08cd6dc27e9ba32adab4d829ce55b9d7bcd05e"
}
```
NOTE: auth_token must be passed for all requests with the logged in user. It remains active till user is [logged out](#logout-user).

## User's info
Requirement: user must be logged in.
```json
GET /auth/users/me/
```
### Response
```json
200 OK
{
    "id": 4,
    "username": "Luke",
    "email": "",
}
```
## Logout user
### Request
Required fields: None
```json
POST /auth/token/logout/
```
### Response
```json
204 No Content
```