FROM python:3.8
WORKDIR /WOG
ADD MainScores.py /
ADD Scores.txt /
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "/MainScores.py"]
