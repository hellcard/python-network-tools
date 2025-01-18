<h2 align="center">Python network tools</h2>
<h4 align="center">Basic networking tools</h4>

----

<h4 align="center">clients_and_server</h4>


![path]()

<h4 align="center">example use</h4>

<p align="center">tab-1</p>


```
python3 TCP-server.py <IP> <PORT>
--
python3 TCP-server.py 0.0.0.0 9998
```

<p align="center">tab-2</p>

```
python3 TCP-client.py <IP> <PORT>
---
python3 TCP-client.py 0.0.0.0 9998
```

<h4 align="center">results</h4>

<p align="center">tab-1</p>

```
 python3 TCP-server.py 0.0.0.0 9998

  [+] Listening: 0.0.0.0 : 9998
  [+] Accepted connection from: 127.0.0.1 : 59250
  [+] Recv: hello from TCP-client :)
```

<p align="center">tab-2</p>

```
python3 TCP-client.py 0.0.0.0 9998

  good
```

----