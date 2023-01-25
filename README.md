#  Inventory Api
This is an Inventory API that allows authenticated users to create, read update and destroy items and categories.  Users can also create shipments for items and see the remaining quantity of the item after it is shipped.  Users can view low stock items, search for items by product and search for category by title. A list of all shipments is available by item.  There is also a list of all shipments independent of items.


## Base URL:
All endpoints begin with `https://inventory-api-rmot.onrender.com`
NOTE: API Root is /api/
|  Method  |  Endpoint  |  Description |
| -------- | ---------- | ------------ |
|POST|  [/auth/users/](#create-a-new-user)|Create a new user|
|POST|  [/auth/token/login/](#login-user)|Login user|
|POST|  [/auth/users/me/](#users-info)|User's info|
|GET|   [/auth/users/](#all_users)|List of all users|
|POST|  [/auth/token/logout/](#logout-user)|Logout user|
|GET|   [/api/items/](#list-of-all-items)|List of all items|
|GET|   [/api/items/<pk>/](#details-of-one-item)|Detail of one item
|POST|  [/api/categories/<int:category_pk>/items/](#create-a-item)|Create a item
|DELETE|[/api/items/<int:item_pk>/](#delete-a-item)|Delete a item
|PATCH| [/api/items/<int:item_pk>/](#update-a-item)|Update a item
|GET|   [/api/categories](#list-of-all-categories)|List of all categories
|GET|   [/api/categories/<int:category_pk>/](#detail-of-one-category)|Details of one category
|POST|  [/api/categories/](#create-a-category)|Create a category
|PATCH| [/api/categories/<int:category_pk>/](#edit-a-category)|Edit a category
|DELETE|[/api/categories/<int:category_pk>/](#delete-a-category)|Delete a Category
|GET|   [/api/shipments/](#list-of-shipment)|List of shipments
|POST|  [/api/items/<int:item_pk>/shipments/](#add-a-shipment)|Add a shipment
|GET|   [/api/items/<int:item_pk>/shipments/](#list-of-shipments-by-item)|List of shipments by item
|GET|   [/api/lowstock/](#list-of-low-stock-items-with-quantity-below-100)|List of low stock items with quantity below 100
|GET|   [/api/items?search=<search-term>](#search-for-items-by-title)|Search for items by title
|GET|   [/api/categories?search=<search-term>](#search-for-items-by-category)|Search for items by category





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
```
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
## list of all items
Returns list of all items.
### Request
Required fields: 
```json
GET api/items/
```
### Response
```json
200 OK
[
	{
		"pk": 1,
		"product": "Brake Pads",
		"amount": 68,
		"category": "Car Parts"
	},
	{
		"pk": 2,
		"product": "Oil Filter",
		"amount": 2000,
		"category": "Car Parts"
	},
	{
		"pk": 3,
		"product": "Feul Pump",
		"amount": 1000,
		"category": "Car Parts"
	}
]
```
## details of one item
Returns detail of one item.
### Request
Required fields: None
```json
GET api/items/<int:item_pk>/
```
### Response
```json
200 OK  
{
	"pk": 11,
	"product": "Playstation 5",
	"manufacturer": "Sony",
	"date_received": "2023-01-25T17:21:22.978499Z",
	"amount": 200,
	"item_description": "Price: $499 (standard), $399 (Digital Edition)\r\nCPU: 3.5GHz, 8-core AMD Zen 2.\r\nGPU: 10.3 teraflop RDNA 2 GPU.\r\nRAM: 16GB GDDR6.\r\nStorage: Custom 825GB SSD.\r\nExpansion: NVMe M.2 SSD slot.\r\nDisc drive: 4K Blu-ray player.\r\nSize: 15.4 x 10.2 x 4.1 inches.",
	"category": "Electronics",
	"shipments": [
		{
			"pk": 21,
			"item": "Playstation 5",
			"quantity_shipped": 3,
			"date": "2023-01-25T18:56:38.137423Z",
			"attn": "Trent Rezner",
			"address_line_one": "2541 fake St.",
			"address_line_two": "Providence, RD 21654",
			"tracking_number": "RA385135335US"
		},
		{
			"pk": 22,
			"item": "Playstation 5",
			"quantity_shipped": 4,
			"date": "2023-01-25T18:59:44.638339Z",
			"attn": "Jake Head",
			"address_line_one": "6541 Fake St",
			"address_line_two": "Concord, NH 12354",
			"tracking_number": "RA351790685US"
		}
	]
}
```
## create a item
create a item.
### Request
Required fields: product, manufacturer, amount, item description 
```json
POST api/categories/<int:category_pk>/items/
{
	
	"product": "Tires",
	"manufacturer": "Michelin",
	"amount": 125,
	"item_description": "ALL-SEASON TIRES"
		
	}	
```
### Response
```json
201 Created
{
	"pk": 13,
	"product": "Tires",
	"manufacturer": "Michelin",
	"date_received": "2023-01-25T19:38:37.862085Z",
	"amount": 125,
	"item_description": "ALL-SEASON TIRES",
	"category": "Car Parts",
	"shipments": []
}
```


## delete a item
delete a item.
### Request
Required fields:None
```json
DELETE api/items/<int:item_pk>/

```
### Response
```json
204 No Content
```


## update a item
update a item.
### Request
Required fields: item pk
```json
PATCH api/items/<int:item_pk>/
{
	"manufacturer": "Goodyear"	
	}		
```
### Response
```json
200 OK
{
	"pk": 13,
	"product": "Tires",
	"manufacturer": "Goodyear",
	"date_received": "2023-01-25T19:38:37.862085Z",
	"amount": 125,
	"item_description": "ALL-SEASON TIRES",
	"category": "Car Parts",
	"shipments": []
}
```    


## list of all categories
list of all categories
### Request
Required fields:None
```json
GET api/categories
```
### Response
```json
200 OK
[
	{
		"pk": 1,
		"title": "Electronics",
		"items": [
			{
				"pk": 10,
				"product": "Iphone 14 Pro Max",
				"amount": 75,
				"category": "Electronics"
			},
			{
				"pk": 11,
				"product": "Playstation 5",
				"amount": 200,
				"category": "Electronics"
			},
			{
				"pk": 12,
				"product": "Xbox Series X",
				"amount": 800,
				"category": "Electronics"
			}
		]
	},
	{
		"pk": 2,
		"title": "Pets",
		"items": [
			{
				"pk": 7,
				"product": "Dog Food",
				"amount": 85,
				"category": "Pets"
			},
			{
				"pk": 8,
				"product": "Wet Cat Food",
				"amount": 560,
				"category": "Pets"
			},
			{
				"pk": 9,
				"product": "Tropical Flakes Fish Food",
				"amount": 425,
				"category": "Pets"
			}
		]
	}
]    
```


## Detail of one category
Detail of one category
### Request
Required fields:None

GET api/categories/<int:category_pk>/
### Response
```json

200 OK
{
	"pk": 3,
	"title": "Household Products",
	"items": [
		{
			"pk": 4,
			"product": "Laundry Detergent",
			"amount": 20,
			"category": "Household Products"
		},
		{
			"pk": 5,
			"product": "Disinfectant Wipes",
			"amount": 1000,
			"category": "Household Products"
		},
		{
			"pk": 6,
			"product": "Liquid All Purpose Cleaner",
			"amount": 1250,
			"category": "Household Products"
		}
	]
}
```


## Create a category
Create a category
### Request
POST api/categories/
Required fields: title
```json
{
	"title": "clothes"
}
```

### Response
```json
201 CREATED
{
	"pk": 5,
	"title": "clothes",
	"items": []
}
```
## Edit a Category
Edit a Category
### Request
PATCH api/categories/<int:category_pk>/
Required fields:
```json
{
	"title": "Cleaning Products"
}
```
### Response
```json
200 OK
{
	"pk": 3,
	"title": "Cleaning Products",
	"items": [
		{
			"pk": 4,
			"product": "Laundry Detergent",
			"amount": 20,
			"category": "Cleaning Products"
		},
		{
			"pk": 5,
			"product": "Disinfectant Wipes",
			"amount": 1000,
			"category": "Cleaning Products"
		},
		{
			"pk": 6,
			"product": "Liquid All Purpose Cleaner",
			"amount": 1250,
			"category": "Cleaning Products"
		}
	]
}
```
## Delete a category
Delete a Category
### Request
DELETE api/categories/<int:category_pk>/
Required fields:None

### Response
```json
204 NO CONTENT
```
## List of all shipments
List of shipments
### Request
GET api/shipments/
Required fields:None

### Response
```json
200 OK
[
	{
		"pk": 24,
		"item": "Xbox Series X",
		"quantity_shipped": 6,
		"date": "2023-01-25T19:02:59.327972Z",
		"attn": "Patton Oswalt",
		"address_line_one": "7649 Fake St",
		"address_line_two": "Lincoln, NB 65241",
		"tracking_number": "RA276867082US",
		"remaining_after_shipment": 794
	},
	{
		"pk": 23,
		"item": "Xbox Series X",
		"quantity_shipped": 5,
		"date": "2023-01-25T19:01:16.650891Z",
		"attn": "Rory Scovel",
		"address_line_one": "2134 Fake St",
		"address_line_two": "Bangor, MA 21471",
		"tracking_number": "RA231346603US",
		"remaining_after_shipment": 795
	},
	{
		"pk": 22,
		"item": "Playstation 5",
		"quantity_shipped": 4,
		"date": "2023-01-25T18:59:44.638339Z",
		"attn": "Jake Head",
		"address_line_one": "6541 Fake St",
		"address_line_two": "Concord, NH 12354",
		"tracking_number": "RA351790685US",
		"remaining_after_shipment": 196
	},
	{
		"pk": 21,
		"item": "Playstation 5",
		"quantity_shipped": 3,
		"date": "2023-01-25T18:56:38.137423Z",
		"attn": "Trent Rezner",
		"address_line_one": "2541 fake St.",
		"address_line_two": "Providence, RD 21654",
		"tracking_number": "RA385135335US",
		"remaining_after_shipment": 197
	},
	{
		"pk": 20,
		"item": "Iphone 14 Pro Max",
		"quantity_shipped": 21,
		"date": "2023-01-25T18:54:56.577642Z",
		"attn": "Alex Gray",
		"address_line_one": "2145 Fake St",
		"address_line_two": "Owensboro, KY",
		"tracking_number": "RA007714942US",
		"remaining_after_shipment": 54
	},
	{
		"pk": 19,
		"item": "Iphone 14 Pro Max",
		"quantity_shipped": 24,
		"date": "2023-01-25T18:53:17.353463Z",
		"attn": "Walter White",
		"address_line_one": "6451 Fake St.",
		"address_line_two": "Alexandria, TN 21474",
		"tracking_number": "RA831440525US",
		"remaining_after_shipment": 51
	}
]
```
## Add a shipment
Add a shipment
### Request
POST api/items/<int:item_pk>/shipments/
```json
{
		"quantity_shipped": 6,
		"attn": "Matt Braunger",
		"address_line_one": "8514 Fake St",
		"address_line_two": "Portland, OR 65241",
		"tracking_number": "RA804894270US"
}
```
### Response
```json
201 CREATED
   {
	"pk": 25,
	"item": "Laundry Detergent",
	"quantity_shipped": 6,
	"date": "2023-01-25T21:02:01.841200Z",
	"attn": "Matt Braunger",
	"address_line_one": "8514 Fake St",
	"address_line_two": "Portland, OR 65241",
	"tracking_number": "RA804894270US",
	"remaining_after_shipment": 14
}
``` 
### List of shipments by item
List of shipments by item
### Request
GET api/items/<int:item_pk>/shipments/
Required fields:None

### Response
```json
200 OK
[
	{
		"pk": 3,
		"item": "Oil Filter",
		"quantity_shipped": 55,
		"date": "2023-01-25T17:35:23.088529Z",
		"attn": "Ari Shaffir",
		"address_line_one": "1454 Fake St",
		"address_line_two": "New York, NY 65847",
		"tracking_number": "RH489547286CN",
		"remaining_after_shipment": 1945
	},
	{
		"pk": 4,
		"item": "Oil Filter",
		"quantity_shipped": 4,
		"date": "2023-01-25T17:37:06.641683Z",
		"attn": "Robert Kelly",
		"address_line_one": "7854 Fake St.",
		"address_line_two": "Los Angelos, CA 65478",
		"tracking_number": "RH962025418CN",
		"remaining_after_shipment": 1996
	}
]
```
## List of low stock items with quantity below 100
List of low stock items with quantity below 100
### Request
GET api/lowstock/
Required fields:None

### Response
```json
200 OK
[
	{
		"pk": 1,
		"product": "Brake Pads",
		"amount": 68,
		"category": "Car Parts"
	},
	{
		"pk": 4,
		"product": "Laundry Detergent",
		"amount": 20,
		"category": "Cleaning Products"
	},
	{
		"pk": 7,
		"product": "Dog Food",
		"amount": 85,
		"category": "Pets"
	},
	{
		"pk": 10,
		"product": "Iphone 14 Pro Max",
		"amount": 75,
		"category": "Electronics"
	}
]
```
## Search for items by title
Search for items by title
### Request
GET api/items?search=<search-term>
Required fields:None

### Response
```json
[
	{
		"pk": 10,
		"product": "Iphone 14 Pro Max",
		"amount": 75,
		"category": "Electronics"
	}
]
```
## Search for items by category
Search for items by category
### Request
Get api/categories?search=<search-term>
Required fields:None

### Response
```json
[
	{
		"pk": 1,
		"title": "Electronics",
		"items": [
			{
				"pk": 10,
				"product": "Iphone 14 Pro Max",
				"amount": 75,
				"category": "Electronics"
			},
			{
				"pk": 11,
				"product": "Playstation 5",
				"amount": 200,
				"category": "Electronics"
			},
			{
				"pk": 12,
				"product": "Xbox Series X",
				"amount": 800,
				"category": "Electronics"
			}
		]
	}
]
```











