from django import dispatch


article_publish = dispatch.Signal(providing_args=["instance", ])
