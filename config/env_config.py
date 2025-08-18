from environs import env

ENV_SECRET_KEY = env.str("SECRET_KEY")
ENV_DEBUG = env.bool("DEBUG")
ENV_ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
