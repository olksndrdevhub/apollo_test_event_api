# Easynetwork, social network API


## How to run:  
1. Clone this repository:  
`git clone https://github.com/olksndrdevhub/apollo_test_event_api.git`  


2. Activate your virtualvenv ("`conda activate <venv_name>`" or some other what you use)  

3. Navigate to project folder:  
`cd apollo_test_event_api/`

4. Install requirements:  
`pip install -r requirements.txt`

5. Make migrate:  
`python manage.py migrate`  

6. Create superuser:  
`python manage.py createsuperuser`

7. Run server:  
`python manage.py runserver`

<hr>

### For full testing this API you can user Postman(recommended) or httpie. Browsable API got some restrict couse to get access to endpoints you need get Token, so it is not recommended to test with a browser.

## Authentication:  

For Authentication you need to get Token. You need send POST request to `http://localhost:8000/api/v1/token/` endpoint with your username and password in request body:  
<pre>
{
    "username":"your_username",
    "password":"Your_password"
}
</pre>  
This will return your Token.  

<b>If you need to authentication in Postman go to Authorization tab(1), select Type as OAuth 2.0(2), paste your Token in field(3) and write '*Token*' at Header Prefix field(4).</b>  

![postman manual](readme_res/token_pic.png)

## Endpoints:  

`http://localhost:8000/` - Index view of project. Return link to Index API view.
<hr>

`http://localhost:8000/api/v1/` - Index endpoint of API. Return links to Events view and EventTypes view. 
<hr>

`http://localhost:8000/api/v1/events/` - Events endpoint. Allow to get list of events (GET method, require authentication) or create new event (POST method, require authentication).   

To create new Event just send POST request to this endpoint with `event_type`(ID), `info`(JSON), and `timestamp` in request body. (You must already have some EventTypes in your DB. To create it check bellow.)  
For example:
<pre>
{
    "event_type":2,
    "info":[
        {
            "price":1001010
        }
    ],
    "timestamp": "2021-02-16T15:26:59Z"
}
</pre>
<hr>

`http://localhost:8000/api/v1/events/<id>/` - Endpoint for Event with `id=event id`. Here you can get, update, delete event. Require authentication.  
Return selected event.
<hr>

`http://localhost:8000/api/v1/event-types/` - EventTypes endpoint. Allow to get list of event types (GET method, require authentication) or create new event type (POST method, require authentication).   

To create new EventType just send POST request to this endpoint with `name` in request body.  
For example:  
<pre>
{
    "name": "First Event"
}
</pre>
<hr>

`http://localhost:8000/api/v1/event-types/<id>/` - Endpoint for EventType with `id=event type id`. Here you can get, update, delete event type. Require authentication.  
Return selected event type.
<hr>


## Testing:

Project have 4 tests for POST request to `/api/v1/events/`  

To start tests run in command line: `python manage.py test`