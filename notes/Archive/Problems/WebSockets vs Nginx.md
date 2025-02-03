If you are using a nginx as a reverse proxy for a websocket and you want to support upgrading ws to wss, you are in trouble. Nginx will consume and `upgrade` value from the `Connection` header, as well as the value `Upgrade: websocket`. You will need to manually pass these values through, e.g.

```nginx
  location / {
	proxy_pass http://127.0.0.1:8001;
	proxy_set_header Connection $http_connection;
	proxy_set_header Upgrade $http_upgrade;
	proxy_pass_request_headers on; # this is the same as default values
	}
```

Some links discussing this:

- [https://stackoverflow.com/questions/65309160/client-is-not-using-the-websocket-protocol-upgrade-token-not-found-in-connec](https://stackoverflow.com/questions/65309160/client-is-not-using-the-websocket-protocol-upgrade-token-not-found-in-connec)
- [https://github.com/gorilla/websocket/issues/507/](https://github.com/gorilla/websocket/issues/507/)
- [http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass_request_headers](http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_pass_request_headers)
- [https://stackoverflow.com/questions/15193743/nginx-reverse-proxy-websockets](https://stackoverflow.com/questions/15193743/nginx-reverse-proxy-websockets)
