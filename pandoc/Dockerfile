FROM python:2

RUN pip install --no-cache-dir flask

RUN apt-get update \
    && apt-get install -y pandoc pandoc-citeproc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/

#RUN curl --location $(curl 'https://api.github.com/repos/jgm/pandoc/releases/latest' | jq --raw-output 'first(.assets[] | select(.browser_download_url | endswith(".deb")) | .browser_download_url)') \
#         --output pandoc.deb \
#    && dpkg -i pandoc.deb \
#    && rm pandoc.deb

COPY app.py .

ENTRYPOINT ["python", "app.py"]
