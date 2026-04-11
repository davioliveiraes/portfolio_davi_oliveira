import multiprocessing

bind = "unix:/run/portfolio/gunicorn.sock"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
timeout = 120
accesslog = "/var/log/portfolio/access.log"
errorlog = "/var/log/portfolio/error.log"
loglevel = "info"
