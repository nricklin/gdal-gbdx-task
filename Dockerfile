FROM tdgp/gdal

RUN curl -O https://bootstrap.pypa.io/get-pip.py
RUN python /get-pip.py
RUN pip install glob2

ADD task.py /task.py

CMD python /task.py
