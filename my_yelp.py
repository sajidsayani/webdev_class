import requests

api_key="TZtNk0uDCSOKB1rUr1crScByluu0WVdy10Hfozbn7OAnWsAmkYc5Bdah0r_ggXH5SS3mobO_o2kl4ZB7wJMH07LA6uoKyOgEgYtdFBWzlbgPkM45z7CC44Yy62t_W3Yx"

url="https://api.yelp.com/v3/businesses/search"

my_headers ={
    "Authorization": "Bearer %s" % api_key
}

my_params = {
"term": "restaurants",
"location": "chicago",
"limit":3,
}

businesses_object = requests.get(url, headers=my_headers, params=my_params)

businesses_dict = businesses_object.text
print(businesses_dict)
