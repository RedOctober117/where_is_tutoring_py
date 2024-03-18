# start by pulling the python image
FROM python:3.8-alpine

RUN apk add git

RUN mkdir /app

# switch working directory
WORKDIR /app

RUN \
git init . && \
git remote add origin https://github.com/RedOctober117/where_is_tutoring_py.git && \
git fetch --depth 1 origin 7d1e38e && \
git checkout test

# RUN git clone --depth 1 https://github.com/RedOctober117/where_is_tutoring_py.git /app

RUN cat /app/wit/static/style.css

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["wit/main.py" ]