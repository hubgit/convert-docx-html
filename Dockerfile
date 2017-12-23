FROM python:2

#RUN apt-get update \
#    && apt-get install -y calibre pandoc pandoc-citeproc \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*

# flask
RUN pip install --no-cache-dir flask

# mammoth
RUN pip install --no-cache-dir mammoth

# pandoc
RUN curl --location 'https://github.com/jgm/pandoc/releases/download/2.0.5/pandoc-2.0.5-1-amd64.deb' \
         --output pandoc.deb \
    && dpkg -i pandoc.deb \
    && rm pandoc.deb

# calibre
RUN curl --location 'https://calibre-ebook.com/dist/linux64' \
         --output calibre.tar.xz \
    && mkdir /opt/calibre \
    && tar -xvf calibre.tar.xz --directory /opt/calibre \
    && rm calibre.tar.xz

# calibre dependencies
RUN apt-get update \
    && apt-get install -y libgl1-mesa-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# web
COPY app.py .

ENTRYPOINT ["python", "app.py"]
