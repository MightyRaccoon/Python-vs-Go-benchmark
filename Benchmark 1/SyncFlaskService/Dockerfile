FROM python

COPY . /DataFiller

WORKDIR /DataFiller

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

ARG ROWS_COUNT
ENV ROWS_COUNT=$ROWS_COUNT

CMD python3 data_fill.py --rows-count $ROWS_COUNT