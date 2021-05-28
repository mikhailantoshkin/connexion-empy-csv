Start the server with 
```bash
python empty.py
```

Then call the endpoint with empty query parameter
```bash
curl 'http://localhost:9090/v1.0/foo?message='
```

It returns `"You send the message: ['']"`