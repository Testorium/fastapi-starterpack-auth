FROM python:3.13-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY ./backend/requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./backend .

RUN chmod +x ./prestart.sh
RUN chmod +x ./run

ENTRYPOINT ["./prestart.sh"]
CMD ["./run"]