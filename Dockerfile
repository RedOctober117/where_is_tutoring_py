# start by pulling the python image
FROM python:3.8-alpine

RUN apk add git

# switch working directory
WORKDIR /app

RUN git clone https://github.com/RedOctober117/where_is_tutoring_py.git /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["wit/main.py" ]