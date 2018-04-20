docker build -t my-haproxy .
docker run -it --rm --name haproxy-syntax-check ntuz/my-haproxy haproxy -c -f /usr/local/etc/haproxy/haproxy.cfg