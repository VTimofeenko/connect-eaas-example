This is a slightly modified version of boilerplate Connect extension.

This extension implements a basic check on incoming purchase request and checks for the following requirements:

* The incoming request has to be for more than 1 item
* The quantity of items has to match

If any of the checks fail – the purchase request is failed.

Otherwise, the request is approved using a hardcoded template.

See [extension.py](connect_ext/extension.py) file for details on implementation.

## License

**Demo project** is licensed under the *Apache Software License 2.0* license.

