# lambdacookie [![Build Status](https://travis-ci.org/Jawshua/aws-lambda-cookies.svg?branch=master)](https://travis-ci.org/Jawshua/aws-lambda-cookies)

Have you ever needed to set multiple cookies in a lambda response served through API Gateway? AWS doesn't natively support setting arrays as header values (which is an ongoing issue [here](https://forums.aws.amazon.com/thread.jspa?threadID=205782)), therefore we need to get creative with header naming to make it work. This library should make your life moderately easier by doing it for you.

# Installation

This package is available on [pypi](https://pypi.python.org/pypi/lambdacookie). Install using pip:
```
pip install lambdacookie
```

# Usage
This library is tested with a [Serverless](https://serverless.com/) deployment, but it should work with any Lambda function behind an API Gateway. Simply call `lambdacookie.headers` with a list of cookies and a dict of headers will be returned. The returned dict can be output directly from the handler.

A basic multi-cookie serving handler looks something like this:

```
import lambdacookie

def cookies_handler(event, context):
    cookie = http.cookies.SimpleCookie("tracking_you=intently")
    cookie["tracking_you"]["expires"] = 3600

    headers = lambdacookie.headers([
        'session_cookie=1',
        cookie
    ])
    headers["content-type"] = "text/html"

    return {
        "statusCode": 200,
        "body": "I'm totally tracking you right now",
        "headers": headers
    }
```

We can fire off a request to the the endpoint to confirm it's working:
```
# curl https://asdasdasd.execute-api.eu-central-1.amazonaws.com/dev/cookies -v

> GET /dev/cookies HTTP/2
> Host: asdasdasd.execute-api.eu-central-1.amazonaws.com
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/2 200
< content-type: text/html
...
< set-cookie: session_cookie=1
< set-cookie: tracking_you=intently; expires=Tue, 05 Dec 2017 15:49:38 GMT
<
I'm totally tracking you right now
```


If you're making use of [custom header mapping](http://docs.aws.amazon.com/apigateway/latest/developerguide/request-response-data-mappings.html) then you can specify a custom header name by passing it in the `header` kwarg to `lambdacookie.headers`.

# Related Links

- The header generation method was largely inspired by the [lamba-proxy-utils](https://www.npmjs.com/package/lambda-proxy-utils) and [binary-case](https://www.npmjs.com/package/binary-case) packages for NodeJS.
