FROM python:2

RUN pip install --no-cache-dir flask

RUN apt-get update \
    && apt-get install -y calibre-bin \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/

#RUN curl --location 'https://calibre-ebook.com/dist/linux64' \
#         --output calibre.tar.xz \
#    && tar -xvf calibre.tar.xz \
#    && rm calibre.tar.xz
#
#RUN ln -s /opt/calibre/ebook-convert /usr/bin/ebook-convert

COPY app.py .

ENTRYPOINT ["python", "app.py"]
