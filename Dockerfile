FROM python:3.6

ADD ./requirements.txt /
RUN pip install -r /requirements.txt

ADD . /
WORKDIR /

# RUN pip install simple-tensorflow-serving
RUN python ./setup.py install

EXPOSE 8500

CMD ["simple_tensorflow_serving", "--port=8500"]
