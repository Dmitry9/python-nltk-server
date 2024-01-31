FROM python:3.10.12
WORKDIR /app
RUN pip install flask nltk youtube_transcript_api --quiet
COPY ./src .
CMD python3 server.py
