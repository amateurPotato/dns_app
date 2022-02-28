#  Simplified authoritative server for a network of applications

## System Architecture

[Architecture](IMAGES/architecture.png)

![Architecture](https://github.com/amateurPotato/dns_app/blob/main/IMAGES/architecture.png?raw=true)

## Steps to set up the environment

### Set-up authoritative server
```
cd AS
docker build -t ruchikau8/as:latest . 
docker network create dns_app_network
docker run --network dns_app_network --name ascontainer -p 53533:53533/udp -it ruchikau8/as:latest
```

### Set-up fibonacci server
```
cd FS
docker build -t ruchikau8/fs:latest . 
docker run --network dns_app_network --name fscontainer -p 9090:9090 -it ruchikau8/fs:latest
```

### Set-up user server
```
cd US
docker build -t ruchikau8/us:latest . 
docker network create dns_app_network
docker run --network dns_app_network --name uscontainer -p 8080:8080 -it ruchikau8/us:latest
```


