FROM python:3.8

WORKDIR /app

COPY . /app/

RUN pip install -r /app/requirements.txt

ENV DATABASE_USERNAME=postgres
ENV DATABASE_PASSWORD=postgres
ENV DATABASE_HOST=localhost
ENV DATABASE_NAME=user_auth_db
ENV DATABASE_PORT=5432
ENV ACCESS_TOKEN_EXPIRE_TIME_MINUTES=15
ENV REFRESH_TOKEN_EXPIRE_TIME_HOURS=24
ENV JWT_ALGORITHM=HS384
ENV AUTH_JWT_HEADER_TYPE = Bearer
ENV AUTH_SECRET_KEY = 6e727d7e38a32358e9fae28eb0a882c8a1c3993ec627f910c24379106a9239c0
ENV authjwt_secret_key = 6e727d7e38a32358e9fae28eb0a882c8a1c3993ec627f910c24379106a9239c0
ENV TEST_DB_URL=sqlite:///./test.db


CMD [ "python", "/app/run.py"]

EXPOSE 8000