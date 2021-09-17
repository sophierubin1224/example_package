# example.py

{% api-method method="get" host="" path="" %}
{% api-method-summary %}
add\_one\( \)
{% endapi-method-summary %}

{% api-method-description %}
The method add\_one\( \) takes any float and adds 1 to that number. 
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="num " type="number" required=true %}
any float 
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
output = input + 1
{% endapi-method-response-example-description %}

```

```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

```text
def add_one(number):
    return number + 1
```



