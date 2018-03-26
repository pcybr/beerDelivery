Start server in Docker - mod_wsgi-express start-server --reload-on-changes --working-directory /app/beerDelivery/beerDelivery/ /app/beerDelivery/beerDelivery/beerDelivery/wsgi.py &


For fixtures:
python manage.py dumpdata --exclude=contenttypes > db0.json