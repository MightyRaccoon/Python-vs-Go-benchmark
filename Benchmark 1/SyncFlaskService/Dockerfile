FROM python

COPY . /SyncFlaskService

WORKDIR /SyncFlaskService

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

CMD python3 FlaskService.py