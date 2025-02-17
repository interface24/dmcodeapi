# dmcodeapi
Simple Treepoam server app with api to generate a datamatrix code

Treepoem uses the ghostscript library and must be manually installed on the host using a package manager for the OS. 

## Linux
apt-get install ghostscript

## Mac
apt-get install ghostscript



# Docker
Use the Dockerfile and it will automatically start the server with the API.

# URL
```http://127.0.0.1:5000/datamatrix?data=Hallo%20Welt ```

# Problems
Due to gohstscript the response from the server can take at least 4s.
