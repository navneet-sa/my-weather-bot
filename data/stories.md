## story_greeting
* greet
    - utter_greet
    
## story_farewell
* farewell
    - utter_farewell

## story_weather_check_1
* greet
    - utter_greet
* weather_check{"place": "hyderabad"}
    - slot{"place": "hyderabad"}
    - check_weather_info
    - slot{"place": "hyderabad"}
* thank_you
    - utter_accept_thanks
* farewell
    - utter_farewell
    
## story_weather_check_2
* greet
    - utter_greet
* weather_check
    - utter_ask_location
* weather_location
    - slot{"place": "hyderabad"}
    - check_weather_info
    - slot{"place": "hyderabad"}
* farewell
    - utter_farewell